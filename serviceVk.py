#!/usr/local/bin/python3

import os
import requests
import json

class ServiseVk(object):
    __ACCESS_TOKEN = os.environ["VK_ACCESS_TOKEN"]
    __VK_API = "https://api.vk.com/method/"
    __ACCOUNT_LINK = "https://vk.com/id"
    __API_VERSION = "5.52"
    __info_of_account = {}
    
    def authoriz_account(self, vk_account_id):
        if self.__check_id_on_exists(vk_account_id) == True:
            request_info_of_account = self.__request_json("users.get", vk_account_id)
            self.__info_of_account = request_info_of_account["response"][0]
            self.__info_of_account["link"] = (self.__ACCOUNT_LINK + vk_account_id)
            return self.__info_of_account
        else:
            raise IOError(self.__check_id_on_exists(vk_account_id))

    def __check_id_on_exists(self, vk_account_id):
        request_info_of_user = self.__request_json("users.get", vk_account_id)
        if len(request_info_of_user["response"]) == 0:
            return "Sorry but account isn't excists"
        elif "error" in request_info_of_user:
            return request_info_of_user["error"]["error_msg"]
        elif "deactivated" in request_info_of_user["response"][0]:
            return "Try again this account is: " + request_info_of_user["response"][0]["deactivated"]
        return True

    def __request_json(self, method, vk_account_id, parametrs = {}):
        req = requests.get(self.__VK_API + str(method) + "?access_token=" + self.__ACCESS_TOKEN + "&user_id=" + str(vk_account_id) + "&v=" + self.__API_VERSION, params=parametrs)
        json_data = req.json()
        return json_data
    
    def requests_public_friend_list(self):
        parametrs = {"order": "name", "fields": "online"}
        req = self.__request_json("friends.get", self.__info_of_account["id"], parametrs)
        return req
    