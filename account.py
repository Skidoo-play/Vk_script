#!/usr/local/bin/python3

import datetime

import service_vk


class Account:
    def __init__(self, profile):
        self.__profile = profile
        self.__service = service_vk.ServiceVk()
        if "last_seen" in profile:
            last_seen_of_acccount = profile["last_seen"]["time"]
            self.__date_of_last_seen = datetime.datetime.fromtimestamp(
                last_seen_of_acccount).date()
            self.__days_offline = (
                datetime.datetime.now().date() - self.__date_of_last_seen).days
        else:
            self.__days_offline = None
            self.__date_of_last_seen = None

    @property
    def id(self):
        return self.__profile["id"]

    @property
    def full_name(self):
        return self.__profile["first_name"] + " " + self.__profile["last_name"]

    @property
    def account_link(self):
        return "https://vk.com/id" + str(self.__profile["id"])

    def get_public_friends(self):
        friends_list = self.__service.request_public_friend_list(
            self.id, "online, last_seen")
        return friends_list

    def get_days_offline(self):
        return self.__days_offline

    @property
    def last_seen(self):
        return self.__date_of_last_seen

    def get_deleted_friends(self):
        friends_list = self.get_public_friends()
        deleted_accounts = list(
            filter(lambda friend: friend.is_deactivated() == "deleted", friends_list))
        return deleted_accounts

    def get_banned_friends(self):
        friends_list = self.get_public_friends()
        banned_accounts = list(
            filter(lambda friend: friend.is_deactivated() == "deleted", friends_list))
        return banned_accounts

    def get_non_active_friends(self):
        half_year = 365/2
        friends_list = self.get_public_friends()
        offline_friends = filter(lambda friend: not friend.is_online(
        ) and not friend.is_deactivated(), friends_list)
        non_active_accounts = filter(
            lambda user: user.get_days_offline() > half_year, offline_friends)
        non_active_accounts = list(non_active_accounts)
        return non_active_accounts

    def is_deactivated(self):
        return self.__profile["deactivated"] if "deactivated" in self.__profile else False

    def is_online(self):
        return True if self.__profile["online"] == 1 else False
