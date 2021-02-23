from .accountMapper import AccountMapper
from .assemblers import AccountAssembler, FriendsAssembler


class AccountFacade:  # TODO добавить метод для проверки существования аккаунта
    @classmethod
    def __get_account(cls, user_ids):
        """Return account object"""
        return AccountMapper.get_user(user_ids)

    @classmethod
    def __serealize_account(cls, account_object):
        """Return JSON string of account"""
        return AccountAssembler.serialize(account_object)

    @classmethod
    def get_account(cls, user_ids):
        """"Return JSON STRING"""
        return cls.__serealize_account(cls.__get_account(user_ids))

    @classmethod
    def get_friends(cls, user_ids):
        """Return JSON string"""
        friends_list = AccountMapper.get_public_friends(
            cls.__get_account(user_ids)
        )
        return FriendsAssembler.serealize(friends_list)

    @classmethod
    def get_banned_friends(cls, user_ids):
        """Return JSON string"""
        banned_friends = AccountMapper.get_banned_friends(
            cls.__get_account(user_ids)
        )
        return FriendsAssembler.serealize(banned_friends)

    @classmethod
    def get_deleted_friends(cls, user_ids):
        """Return JSON string"""
        deleted_friends = AccountMapper.get_deleted_friends(
            cls.__get_account(user_ids)
        )
        return FriendsAssembler.serealize(deleted_friends)

    @classmethod
    def get_abandoned_friends(cls, user_ids, days_offline):
        """Return JSON string"""
        abandoned_friends = AccountMapper.get_non_active_friends(
            cls.__get_account(user_ids),
            days_offline=days_offline
        )
        return FriendsAssembler.serealize(abandoned_friends)
