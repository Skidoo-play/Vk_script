#!/usr/local/bin/python3

import os

import requests
from dotenv import load_dotenv

from parameters import Fields
from methods import Methods

load_dotenv()


class ServiceVk:
    __ACCESS_TOKEN = os.getenv("VK_ACCESS_TOKEN")
    __VK_API = "https://api.vk.com/method/"
    __API_VERSION = "5.80"
    __LANGUAGE = "en"
    fields = Fields()
    methods = Methods()

    @classmethod
    def request_info_of_account(cls, user_ids=[]):
        """return array of accounts"""
        params = {
            "user_ids": ','.join(user_ids),
            "fields": cls.fields.ONLINE
        }

        user_ids_json = cls.__request_json(cls.methods.USER_GET, params=params)
        return user_ids_json["response"]

    @staticmethod
    def check_id_on_exists(self, vk_account_ids):
        """return bool"""
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

    @classmethod
    def __request_json(cls, method, params):
        """return json data"""
        vk_method = cls.__VK_API + str(method)
        vk_access_token = "?access_token=" + cls.__ACCESS_TOKEN
        vk_api_v = "&v=" + cls.__API_VERSION
        vk_lang = "&lang=" + cls.__LANGUAGE
        req = requests.get(vk_method + vk_access_token +
                           vk_api_v + vk_lang, params)
        json_data = req.json()
        return json_data

    @classmethod
    def request_public_friend_list(cls, account_vk_id, fields=[]):
        """return json data accounts"""
        params = {
            "order": "name",
            "fields": ",".join(fields),
            "user_id": int(account_vk_id)
        }
        req = cls.__request_json("friends.get", params)
        response_accounts = req["response"]["items"]
        return response_accounts
