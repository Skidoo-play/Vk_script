#!/usr/local/bin/python3

class User():
    __info_of_user = None

    def set_user(self, info_of_user):
         self.__info_of_user = info_of_user

#TODO ADD CONTAINS
    
    def __setitem__(self, key, value):
        self.__info_of_user[key] = value
    
    def get_user_info(self):
        return self.__info_of_user
    
    def __getitem__(self, key):
        if key in self.__info_of_user:
            return str(self.__info_of_user[key])
        else:
            raise IOError(f"""User hasn't atribyte: {key}""")