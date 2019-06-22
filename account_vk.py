#!/usr/local/bin/python3

import datetime


class Account:
    def __init__(self, account_id, first_name, last_name, online, last_seen, deactivated):
        self.id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_seen = last_seen
        self.deactivated = deactivated
        self.online = online

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def account_link(self):
        return "https://vk.com/id" + str(self.id)

    @property
    def is_online(self):
        return self.online == 1

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

    def is_deactivated(self):
        return self.deactivated

    def __repr__(self):
        return self.first_name + " " + self.last_name
