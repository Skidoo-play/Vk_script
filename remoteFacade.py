from accountMapper import AccountMapper
from assemblers import AccountAssembler, FriendsAssembler

class AccountFacade:

    @staticmethod
    def __get_account(user_ids):
        """Return account object"""
        return AccountMapper.get_user(user_ids)

    @staticmethod
    def __serealize_account(account_object):
        return AccountAssembler.serealize(account_object)

    @staticmethod
    def get_account(user_ids):
        """"Return accountDTO object"""
        account_vk = AccountFacade.__get_account(user_ids)
        account_vk_JSON = AccountFacade.__serealize_account(account_vk)
        return account_vk_JSON

    @staticmethod
    def get_friends(user_ids):
        account_vk = AccountFacade.__get_account(user_ids)
        friends_list = AccountMapper.get_public_friends(account_vk)
        friends_list_JSON = FriendsAssembler.serealize(friends_list)
        return friends_list_JSON