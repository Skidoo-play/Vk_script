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
		print(f'Ok your account is: {self.info_of_user["first_name"]} {self.info_of_user["last_name"]} ({self.info_of_user["link"]})')
		return
	
	def friends_get(self):
		self.count_banned_users = 0
		self.count_deleted_users = 0
		parametrs = {"user_id": self.user_id,
					 "access_token": self.ACCESS_TOKEN,
					 "order": "name",
					 "fields": "online, photo_50",
					 "v": self.API_VERSION}

		req = requests.get(self.VK_API + "friends.get", params = parametrs)

		with open("all friends.json", "w") as json_file:
			json_data = req.json()
			json.dump(json_data, json_file)
			self.friends_list = json_data["response"]["items"]

	def get_banned_and_deleted_user(self):
		for friend in self.friends_list:
			if "deactivated" in friend:
				friend["link"] = (self.ACCOUNT_LINK + str(friend["id"]))
				if friend["deactivated"] == "banned":
					self.banned_users.append(friend)
					self.count_banned_users += 1
				elif friend["deactivated"] == "deleted":
					self.banned_users.append(friend)
					self.count_deleted_users += 1

	def print_banned_friends(self):
		for banned_user in self.banned_users:
			print(f'{banned_user["first_name"]} {banned_user["last_name"]} ({banned_user["link"]})')
		print(f'Count: {"You havent banned friends" if (((self.count_banned_users)) == 0) else {len(self.banned_users)}}')

	def print_deleted_friends(self):
		for deleted_user in self.deleted_users:
			print(f'{deleted_user["first_name"]} {deleted_user["last_name"]} ({deleted_user["link"]})')
		print(f'Count: {"You havent deleted friends" if ((len(self.count_deleted_users)) == 0) else {len(self.deleted_users)}}')

# Anon = AccountWithoutLogin(input("Input your vk id: "))
Anon = AccountWithoutLogin(135480774)
Anon.print_info_about_user()
Anon.friends_get()
Anon.get_banned_and_deleted_user()
print("Your banned friends: ")
Anon.print_banned_friends()
print("Your deleted friends: ")
Anon.print_deleted_friends()
