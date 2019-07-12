from service_vk import ServiceVk
from assemblers import AccountAssembler, FriendsAssembler


class AccountMapper:
    @staticmethod
    def get_user(user_ids):
        """Return account object"""
        json = ServiceVk.request_info_of_account([user_ids])[0]
        return AccountAssembler.deserialize(json)

    @staticmethod
    def get_public_friends(account_vk):
        """Return accounts list"""
        json_friends_list = ServiceVk.request_public_friend_list(account_vk.id,
                                                                 [ServiceVk.fields.ONLINE,
                                                                  ServiceVk.fields.LAST_SEEN])
        return FriendsAssembler.deserialize(json_friends_list)

    @staticmethod
    def get_deleted_friends(account_vk):
        friends_list = AccountMapper.get_public_friends(account_vk)
        deleted_accounts = list(
            filter(lambda friend: friend.is_deactivatedrequest_public_friend_list() == "deleted", friends_list)
        )
        return deleted_accounts

    @staticmethod
    def get_banned_friends(account_vk):
        friends_list = AccountMapper.get_public_friends(account_vk)
        banned_accounts = list(
            filter(lambda friend: friend.is_deactivated() == "banned", friends_list)
        )
        return banned_accounts

    @staticmethod
    def get_offline_friends(account_vk):
        friends_list = AccountMapper.get_public_friends(account_vk)
        offline_friends = list(
            filter(lambda friend: not friend.is_online, friends_list)
        )
        return offline_friends

    @staticmethod
    def get_non_active_friends(account_vk, days_offline=365/2):
        offline_friends = AccountMapper.get_offline_friends(account_vk)
        offline_and_not_deactivated_friends = filter(
            lambda friend: not friend.is_deactivated(), offline_friends
        )
        non_active_friends = filter(
            lambda friend: friend.get_days_offline() > days_offline, offline_and_not_deactivated_friends
        )
        return list(non_active_friends)
