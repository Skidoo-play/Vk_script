#!/usr/local/bin/python3

# my id 135480774
import serviceVk
import requests
import json
import os
import datetime

class AccountWithoutLogin():
	__service = serviceVk.ServiceVk()
	__info_of_account = None

	def set_account(self, id):
		self.__info_of_account = self.__service.request_info_of_account(id)
		return self.__info_of_account.get_user_info()

	def get_info_about_account(self):
		return self.__info_of_account

	def get_public_friends(self):
		friends_list = self.__service.requests_public_friend_list(self.__info_of_account["id"], "online, last_seen")
		return friends_list

	def save_data_in_json(self, data, file_name):
		with open(str(file_name) + ".json", "w") as json_file:
			json.dump(data, json_file)

	def get_banned_and_deleted_friends(self):
		friends_list = self.get_public_friends()
		deleted_accounts = list(filter(lambda friend: ("deactivated" in friend) and (friend["deactivated"] == "deleted"), friends_list))
		banned_accounts =  list(filter(lambda friend: ("deactivated" in friend) and (friend["deactivated"] == "banned"), friends_list))
		return { "banned": banned_accounts, "deleted" : deleted_accounts }

	def get_non_active_friends(self):
		currently_date = datetime.datetime.now().date()
		non_active_accounts = []
		half_year = 365/2
		friends_list = self.get_public_friends()
		friends_list = filter(lambda friend: friend["online"] == 0 and "deactivated" not in friend, friends_list) #toss online users
		
		def add_info_count_not_active_days(user):
			nonlocal currently_date
			last_seen_of_account = datetime.datetime.fromtimestamp(user["last_seen"]["time"]).date()
			user["count_day_offline"] = (currently_date - last_seen_of_account).days
			return user

		non_active_accounts = map(add_info_count_not_active_days, friends_list)
		non_active_accounts = list(filter(lambda user: user["count_day_offline"] > half_year, non_active_accounts))
		return non_active_accounts
		
	def get_count_banned(self):
		return len(self.get_banned_and_deleted_friends()["banned"])
	
	def get_count_deleted(self):
		return len(self.get_banned_and_deleted_friends()["deleted"])
	
	def get_count_friends(self):
		return len(self.get_public_friends())