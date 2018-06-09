#!/usr/local/bin/python3

class User():
    __info_of_user = None

    def set_user(self, info_of_user):
         self.__info_of_user = info_of_user["response"][0]

    def add_info(self, key, value):
        if key not in self.__info_of_user:
            self.__info_of_user[key] = value
        else:
            raise IOError("You cannot change info this functuoin")
    
    def __setitem__(self, key, value):
        if key in self.__info_of_user:
            self.__info_of_user[key] = value
        else:
            raise IOError("You cannot change information which not exists")
    
    def get_user_info(self):
        return self.__info_of_user
    
    def __getitem__(self, key):
        if key in self.__info_of_user:
            return str(self.__info_of_user[key])
        else:
            raise IOError(f"""User hasn't atribyte: {key}""")