#!/usr/local/bin/python3

# my id 135480774
import serviceVk
import requests
import json
import os

class AccountWithoutLogin():
	__service = serviceVk.ServiceVk()
	__info_of_account = None

	def set_account(self, id):
		self.__info_of_account = self.__service.request_info_of_account(id)
		return self.__info_of_account.get_user_info()

	def get_info_about_account(self):
		return self.__info_of_account

	def get_public_friends(self):
		friends_list = self.__service.requests_public_friend_list(self.__info_of_account["id"])
		return friends_list

	def save_data_in_json(self, data, file_name):
		with open(str(file_name) + ".json", "w") as json_file:
			json.dump(data, json_file)

	def get_banned_and_deleted_friends(self):
		banned_accounts  = []
		deleted_accounts = []
		friends_list = self.get_public_friends()
		for friend in friends_list:
			if "deactivated" in friend:
				friend["link"] = ("https://vk.com/id" + str(friend["id"]))
				if friend["deactivated"] == "deleted":
					deleted_accounts.append(friend)
				elif friend["deactivated"] == "banned":
					banned_accounts.append(friend)
		return { "banned": banned_accounts, "deleted" : deleted_accounts }

	def get_count_banned(self):
		return len(self.get_banned_and_deleted_friends()["banned"])
	
	def get_count_deleted(self):
		return len(self.get_banned_and_deleted_friends()["deleted"])
	
	def get_count_friends(self):
		return len(self.get_public_friends())