#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
# https://api.vk.com/method/users.get?user_id=210700286&v=5.52
# my id 135480774
import requests
import json

class account_without_login:
	def __init__(self, id):
		self.user_id = str(id)
		self.ACCESS_TOKEN = "a15ebe88a15ebe88a15ebe8871a13fc578aa15ea15ebe88fa546557fbb1e4cc820c017d"
		self.VK_API = "https://api.vk.com/method/"
		self.ACCOUNT_LINK = "https://vk.com/id"
		self.frineds_list = []
		self.banned_users = []
		self.info_of_user = None

		while (not self.check_id(self.user_id)):
			self.user_id = input("trooll heyv, input real ID!: ")

	def check_id(self, id):
		parametrs = {"user_id": self.user_id,
	     		 	 "access_token": self.ACCESS_TOKEN,
	     		 	 "v": "5.52"}
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
		parametrs = {"user_id": self.user_id,
					 "access_token": self.ACCESS_TOKEN,
					 "order": "name",
					 "fields": "online, photo_50",
					 "v": "5.52"}

		req = requests.get(self.VK_API + "friends.get", params = parametrs)

		with open("all friends.json", "w") as json_file:
			json_data = req.json()
			json.dump(json_data, json_file)
			self.frineds_list = json_data["response"]["items"]

	def get_banned_user(self):
		print("Your deleted friends: ")
		for _ in self.frineds_list:
			if _["photo_50"] == "https://vk.com/images/deactivated_50.png":
				_["link"] = (self.ACCOUNT_LINK + str(_["id"]))
				self.banned_users.append(_)

	def print_banned_friend(self):
		for _ in self.banned_users:
			print(f'{_["first_name"]} {_["last_name"]} ({_["link"]})')
		print(f'Count: {"You havent deleted friends" if ((len(self.banned_users)) == 0) else {len(self.banned_users)}}')

# 183230376
Anon = account_without_login(input("Input your vk id: "))
Anon.print_info_about_user()
Anon.friends_get()
Anon.get_banned_user()
Anon.print_banned_friend()