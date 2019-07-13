from account_vk import Account
from DTO import AccountDTO, FriendsDTO


class AccountAssembler:
    @classmethod
    def deserialize(cls, json_of_account):
        """Deserialize json to account object"""
        params = {
            "account_id": json_of_account.get("id"),
            "first_name": json_of_account.get('first_name'),
            "last_name": json_of_account.get('last_name'),
            "online": json_of_account.get('online'),
            "last_seen": json_of_account.get('last_seen'),
            "deactivated": json_of_account.get('deactivated'),
            "ava_link": cls.__get_ava_link(json_of_account)
        }
        return Account(**params)

    @staticmethod
    def __get_ava_link(json_of_account):
        avatar_keys = frozenset(['photo_50', 'photo_100', 'photo_200_orig'])
        for _ in json_of_account.keys():
            if _ in avatar_keys:
                return json_of_account.get(_)
        return None


    @staticmethod
    def serialize(account_vk):
        """Serialize account object to JSON string"""
        return AccountDTO(account_vk).to_json()


class FriendsAssembler:
    @staticmethod
    def deserialize(json_friends_list):
        friend_list = list(map(AccountAssembler.deserialize, json_friends_list))
        return friend_list

    @staticmethod
    def serealize(friends_list):
        return FriendsDTO(friends_list).to_json()
