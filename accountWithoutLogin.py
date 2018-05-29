#!/usr/local/bin/python3

# my id 135480774
import requests
import json
import os

class AccountWithoutLogin:
	def __init__(self, id):
		self.user_id = str(id)
		self.ACCESS_TOKEN = os.environ["VK_ACCESS_TOKEN"]
		self.VK_API = "https://api.vk.com/method/"
		self.ACCOUNT_LINK = "https://vk.com/id"
		self.API_VERSION = "5.52"
		self.friends_list = []
		self.count_public_friends = 0
		self.banned_users = []
		self.count_banned_users = 0
		self.deleted_users =[]
		self.count_deleted_users = 0
		self.info_of_user = None

		while (not self.check_id(self.user_id)):
			self.user_id = input("trooll heyv, input real ID!: ")

	def check_id(self, id):
		parametrs = {"user_id": self.user_id,
					 "access_token": self.ACCESS_TOKEN,
					 "v": self.API_VERSION}
		req = requests.get(self.VK_API + "users.get", params = parametrs)
		info_of_user = req.json()
		if "error" in info_of_user:
			return False
		self.info_of_user = info_of_user["response"][0]
		self.info_of_user["link"] = (self.ACCOUNT_LINK + self.user_id)
		return True

	def print_info_about_user(self):
		print(f'Ok your account is: {self.info_of_user["first_name"]} {self.info_of_user["last_name"]} ({self.info_of_user["link"]})', end = "")
		return
	
	def refresh_lists_banned_and_deleted_users(self):
		self.count_banned_users = 0
		self.count_deleted_users = 0
		self.banned_users = []
		self.deleted_users = []

	def friends_get(self):
		self.refresh_lists_banned_and_deleted_users()
		parametrs = {"user_id": self.user_id,
					 "access_token": self.ACCESS_TOKEN,
					 "order": "name",
					 "fields": "online, photo_50",
					 "v": self.API_VERSION}

		req_friends_of_user = requests.get(self.VK_API + "friends.get", params = parametrs)
		json_data = req_friends_of_user.json()

		self.save_data_in_json(json_data,"All friends")
		self.count_public_friends = json_data["response"]["count"]
		self.friends_list = json_data["response"]["items"]

	def save_data_in_json(self, data, file_name):
		with open(str(file_name) + ".json", "w") as json_file:
			json.dump(data, json_file)

	def get_banned_and_deleted_friends(self):
		for friend in self.friends_list:
			if "deactivated" in friend:
				friend["link"] = (self.ACCOUNT_LINK + str(friend["id"]))
				if friend["deactivated"] == "deleted":
					self.deleted_users.append(friend)
					self.count_deleted_users += 1
				elif friend["deactivated"] == "banned":
					self.banned_users.append(friend)
					self.count_banned_users += 1

	def print_banned_friends(self):
		for banned_user in self.banned_users:
			print(f'{banned_user["first_name"]} {banned_user["last_name"]} ({banned_user["link"]})')
	
	def print_deleted_friends(self):
		for deleted_user in self.deleted_users:
			print(f'{deleted_user["first_name"]} {deleted_user["last_name"]} ({deleted_user["link"]})')

	def get_count_banned(self):
		return self.count_banned_users
	
	def get_count_deleted(self):
		return self.count_deleted_users
	
	def get_count_friends(self):
		return self.count_public_friends