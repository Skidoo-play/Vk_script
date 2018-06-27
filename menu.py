#!/usr/local/bin/python3

import serviceVk
import accountWithoutLogin
import sys

anon = accountWithoutLogin.AccountWithoutLogin()
service = serviceVk.ServiceVk()
auth = False
account = None
print(r""" _____________________________________
/ Welcom to my first program!          \
\ (c)Mikhail Ulyakov (vk.com/shzfrnia) /
 -------------------------------------
 \
  \
   \ >()_
      (__)__ _""")


def done_message():
    print("****************")
    print(f"""\n DONE \n""")
    print("****************")

def eror_input_message():
    print("****************")
    print(f"""\n INCORRECT INPUT \n""")
    print("****************")

while True:
    print("Menu")
    print(f"""1) Set user
2) Show banned and deleted account in friends
3) Show who last was half year past
0) Exit
Currently account: {account}""")
    answer = input("Choose number of menu item: ")
    if answer == "0":
        break

    elif answer == "1":
        anon_id = input("Input vk id: https://vk.com/")
        try:
            service.check_id_on_exists(anon_id)
        except:
            print("****************")
            print(f"""Syrry, but account {"vk.com/" + anon_id} is not exists.\nPlease, try again""")
            print("****************")
            continue
        anon.set_account(anon_id)
        account = anon.get_info_about_account()
        auth = True
        account = (f'{account["first_name"]} {account["last_name"]} ({account["link"]}).\n')
        done_message()

    elif (answer == "2"):
        if auth == False:
            print("\n***Pleasy, set user***\n")
            continue
        ban_and_del_acc = anon.get_banned_and_deleted_friends()
        count_deleted = anon.get_count_deleted()
        count_banned = anon.get_count_banned()
        print("****************")
        print(f'All friends: ({anon.get_count_friends()}).')
        print("Your banned friends: ")
        for banned_account in ban_and_del_acc["banned"]:
            print(f'{banned_account["first_name"]} {banned_account["last_name"]} ({banned_account["link"]})')
        print(f'    Count: {"You havent banned accounts in friends" if (count_banned == 0) else {count_banned}}')
        print("Your deleted friends: ")
        for deleted_account in ban_and_del_acc["deleted"]:
            print(f'{deleted_account["first_name"]} {deleted_account["last_name"]} ({deleted_account["link"]})')
        print(f'    Count: {"You havent deleted accounts in friends" if (count_deleted == 0) else {count_deleted}}')
        print("****************")
    
    elif (answer == "3"):
        if auth == False:
            print("\n***Pleasy, set user***\n")
            continue
        print("****************")
        friends = anon.get_non_active_friends()
        count_friends = len(friends)
        for friend in friends:
            print(f'{friend["first_name"]} {friend["last_name"]} \n  offline: {friend["count_day_offline"]} days. ({friend["link"]})')
        print(f'Count: {"Zero accounts" if (count_friends == 0) else {count_friends}}')
        print("****************")

    else:
        eror_input_message()