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
		friends_list = list(filter(lambda friend: friend["online"] != 1, friends_list)) #toss online users
		friends_list = list(filter(lambda friend: "deactivated" not in friend, friends_list)) #toss deactivate users
		friends_list = list(filter(lambda friend: datetime.datetime.fromtimestamp(friend["last_seen"]["time"]).date() != currently_date, friends_list)) #toss who was online today
		for friend in friends_list:
			last_seen_of_account = datetime.datetime.fromtimestamp(friend["last_seen"]["time"]).date()
			how_long_days_user_not_online = (currently_date - last_seen_of_account).days
			if how_long_days_user_not_online > half_year:
				friend["count_day_offline"] = how_long_days_user_not_online
				non_active_accounts.append(friend)
		return non_active_accounts
		
	def get_count_banned(self):
		return len(self.get_banned_and_deleted_friends()["banned"])
	
	def get_count_deleted(self):
		return len(self.get_banned_and_deleted_friends()["deleted"])
	
	def get_count_friends(self):
		return len(self.get_public_friends())