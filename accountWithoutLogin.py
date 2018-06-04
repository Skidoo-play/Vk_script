#!/usr/local/bin/python3

# my id 135480774
import serviceVk
import requests
import json
import os

class AccountWithoutLogin(object):
	__service = serviceVk.ServiseVk()
	__friends_list = []
	__info_of_user = None

	def auth_account(self, id):
		self.__info_of_user = self.__service.authoriz_account(id)
		return self.__info_of_user

	def get_info_about_user(self):
		return self.__info_of_user

	def get_public_friends(self):
		request_friends_of_user = self.__service.requests_public_friend_list()
		self.__friends_list = request_friends_of_user["response"]["items"]
		return self.__friends_list

	def save_data_in_json(self, data, file_name):
		with open(str(file_name) + ".json", "w") as json_file:
			json.dump(data, json_file)

	def get_banned_and_deleted_friends(self):
		banned_accounts  = []
		deleted_accounts = []
		for friend in self.__friends_list:
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
		return len(self.__friends_list)