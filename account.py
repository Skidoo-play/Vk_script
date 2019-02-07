#!/usr/local/bin/python3

import datetime

import service_vk


class Account:
    def __init__(self, account_id, first_name, last_name, online, last_seen, diactivated):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_seen = last_seen
        self.diactivated = diactivated
        self.online = online
        self.__service = service_vk.ServiceVk()

    @property
    def id(self):
        return self.account_id

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def account_link(self):
        return "https://vk.com/id" + str(self.account_id)

    def get_public_friends(self):
        friends_list = self.__service.request_public_friend_list(
            self.id, "online, last_seen")
        return friends_list

    def get_days_offline(self):
        if self.last_seen:
            date_of_last_seen = datetime.datetime.fromtimestamp(
                self.last_seen["time"]).date()
            days_offline = (datetime.datetime.now().date() -
                            date_of_last_seen).days
            return days_offline
        else:
            return self.last_seen

    def get_last_seen(self):
        """Last seen in python date"""
        if self.last_seen:
            date_of_last_seen = datetime.datetime.fromtimestamp(
                self.last_seen["time"]).date()
            return date_of_last_seen
        else:
            return self.last_seen

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
        half_year = int(365/2)
        friends_list = self.get_public_friends()
        offline_friends = filter(lambda friend: not friend.is_online(
        ) and not friend.is_deactivated(), friends_list)
        non_active_accounts = filter(
            lambda user: user.get_days_offline() > half_year, offline_friends)
        non_active_accounts = list(non_active_accounts)
        return non_active_accounts

    def is_deactivated(self):
        return self.diactivated

    def is_online(self):
        return True if self.online == 1 else False
