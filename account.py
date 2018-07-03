#!/usr/local/bin/python3

import datetime
import serviceVk

class Account:
    def __init__(self, profile):
        self.__online      = profile["online"]
        self.__first_name  = profile["first_name"]
        self.__second_name = profile["last_name"]
        self.__id          = profile["id"]
        self.__last_seen   = profile["last_seen"]["time"] if "last_seen"in profile else None
        self.__dectivated  = profile["deactivated"] if "deactivated" in profile else False
        self.__count_days_offline = None
        self.__link        = "https://vk.com/" + str(profile["id"])
        self.__service     = serviceVk.ServiceVk()

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__first_name + " " + self.__second_name
    
    def get_link(self):
        return self.__link
    
    def get_public_friends(self):
        friends_list = self.__service.requests_public_friend_list(self.get_id(), "online, last_seen")
        return friends_list
    
    def add_count_days_offline(self, days):
        self.__count_days_offline = days

    def get_days_offline(self):
        return self.__count_days_offline

    def __get_last_seen(self):
        return self.__last_seen
    
    def get_count_banned(self):
        return len(self.get_banned_and_deleted_friends()["banned"])
	
    def get_count_deleted(self):
        return len(self.get_banned_and_deleted_friends()["deleted"])
	
    def get_count_friends(self):
        return len(self.get_public_friends())
    
    def get_banned_and_deleted_friends(self):
        friends_list = self.get_public_friends()
        deleted_accounts = list(filter(lambda friend: (friend.is_deactivated() == "deleted"), friends_list))
        banned_accounts =  list(filter(lambda friend: (friend.is_deactivated() == "banned"), friends_list))
        return { "banned": banned_accounts, "deleted" : deleted_accounts }

    def get_non_active_friends(self):
        currently_date = datetime.datetime.now().date()
        non_active_accounts = []
        half_year = 365/2
        friends_list = self.get_public_friends()
        friends_list = filter(lambda friend: (not friend.is_online()) and  (not friend.is_deactivated()), friends_list)

        def add_info_count_not_active_days(account):
            nonlocal currently_date
            last_seen_of_account = datetime.datetime.fromtimestamp(account.__get_last_seen()).date()
            days_offline = (currently_date - last_seen_of_account).days
            account.add_count_days_offline(days_offline)
            return account

        non_active_accounts = map(add_info_count_not_active_days, friends_list)
        non_active_accounts = list(filter(lambda user: user.get_days_offline() > half_year, non_active_accounts))
        return non_active_accounts

    def is_deactivated(self):
        return self.__dectivated

    def is_online(self):
        return True if self.__online == 1 else False