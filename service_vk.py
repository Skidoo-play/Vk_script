#!/usr/local/bin/python3

import os

import requests
from dotenv import load_dotenv

import account

load_dotenv()


class ServiceVk:
    __ACCESS_TOKEN = os.getenv("VK_ACCESS_TOKEN")
    __VK_API = "https://api.vk.com/method/"
    __API_VERSION = "5.80"
    __LANGUAGE = "ru"

    def request_info_of_account(self, vk_account_id):
        account_info = self.__request_json("users.get", params={"user_ids": vk_account_id,
                                                                "fields": "online"})["response"][0]
        vk_account = self.__deserealize_account(account_info)
        return vk_account

    def __deserealize_account(self, profile):
        return account.Account(profile.get("id"),
                               profile.get("first_name"),
                               profile.get("last_name"),
                               profile.get("online"),
                               profile.get("last_seen"),
                               profile.get("deactivated"))


    def check_id_on_exists(self, vk_account_ids):
        info_of_user = self.__request_json(
            "users.get", params={"user_ids": vk_account_ids})
        if "error" in info_of_user:
            raise Exception(info_of_user["error"]["error_msg"])
        elif not info_of_user["response"]:
            raise Exception("Sorry but account isn't exists")
        elif "deactivated" in info_of_user["response"][0]:
            raise Exception("Try again this account is: " +
                            info_of_user["response"][0]["deactivated"])
        return True

    def __request_json(self, method, params):
        vk_method = self.__VK_API + str(method)
        vk_access_token = "?access_token=" + self.__ACCESS_TOKEN
        vk_api_v = "&v=" + self.__API_VERSION
        vk_lang = "&lang=" + self.__LANGUAGE
        req = requests.get(vk_method + vk_access_token +
                           vk_api_v + vk_lang, params)
        json_data = req.json()
        return json_data

    def request_public_friend_list(self, vk_account_id, fields="online"):
        parametrs = {"order": "name",
                     "fields": fields,
                     "user_id": vk_account_id}
        req = self.__request_json("friends.get", parametrs)
        response_accounts = req["response"]["items"]

        friends_list = list(map(self.__deserealize_account, response_accounts))
        return friends_list
