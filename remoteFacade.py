from accountMapper import AccountMapper
from assemblers import AccountAssembler, FriendsAssembler


class AccountFacade: #TODO добавить метод для проверки существования аккаунта
    @staticmethod
    def __get_account(user_ids):
        """Return account object"""
        return AccountMapper.get_user(user_ids)

    @staticmethod
    def __serealize_account(account_object):
        """Return JSON string of account"""
        return AccountAssembler.serialize(account_object)

    @staticmethod
    def get_account(user_ids):
        """"Return JSON STRING"""
        account_vk = AccountFacade.__get_account(user_ids)
        account_vk_JSON = AccountFacade.__serealize_account(account_vk)
        return account_vk_JSON

    @staticmethod
    def get_friends(user_ids):
        """Return JSON string"""
        account_vk = AccountFacade.__get_account(user_ids)
        friends_list = AccountMapper.get_public_friends(account_vk)
        friends_list_JSON = FriendsAssembler.serealize(friends_list)
        return friends_list_JSON

    @staticmethod
    def get_banned_friends(user_ids):
        """Return JSON string"""
        account_vk = AccountFacade.__get_account(user_ids)
        banned_friends = AccountMapper.get_banned_friends(account_vk)
        banned_friends_JSON = FriendsAssembler.serealize(banned_friends)
        return banned_friends_JSON

    @staticmethod
    def get_deleted_friends(user_ids):
        """Return JSON string"""
        account_vk = AccountFacade.__get_account(user_ids)
        deleted_friends = AccountMapper.get_deleted_friends(account_vk)
        deleted_friends_JSON = FriendsAssembler.serealize(deleted_friends)
        return deleted_friends_JSON

    @staticmethod
    def get_abandoned_friends(user_ids):
        """Return JSON string"""
        account_vk = AccountFacade.__get_account(user_ids)
        abandoned_friends = AccountMapper.get_offline_friends(account_vk)
        abandoned_friends_JSON = FriendsAssembler.serealize(abandoned_friends)
        return abandoned_friends_JSON