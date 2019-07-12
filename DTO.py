

class AccountDTO:
    def __init__(self, account_vk):
        self.id = account_vk.id
        self.first_name = account_vk.first_name
        self.account_link = account_vk.account_link
        self.last_name = account_vk.last_name
        self.is_online = account_vk.is_online
        self.is_deactivated = account_vk.is_deactivated()
        self.last_seen = account_vk.last_seen
        self.days_offline = account_vk.get_days_offline()
        self.photo_link = account_vk.avatar_link

    def to_json(self):
        json_data = dict()
        json_data['id'] = self.id
        json_data['first_name'] = self.first_name
        json_data['link'] = self.account_link
        json_data['last_name'] = self.last_name
        json_data['is_online'] = self.is_online
        json_data['is_deactivated'] = self.is_deactivated
        json_data['days_offline'] = self.days_offline
        json_data['last_seen'] = self.last_seen
        json_data['avatar'] = self.photo_link #TODO Фильтрацию по пустым полям- грубо говоря фильтер если ключ пустой- нахуй из ДТО

        return json_data


class FriendsDTO:
    def __init__(self, friends_list):
        self.friends_list = friends_list # OBJECTS

    def to_json(self):
        friends_list_DTO = map(AccountDTO, self.friends_list)
        json_data = [item.to_json() for item in friends_list_DTO]
        return json_data
