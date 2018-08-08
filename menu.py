#!/usr/local/bin/python3

import sys
import color
import account
import service_vk

service = service_vk.ServiceVk()
anon = None
auth = False
account = None

print(r""" _____________________________________
/ Welcom to my first programm!         \
\ (c)Mikhail Ulyakov (vk.com/shzfrnia) /
 -------------------------------------
 \
  \
   \ >()_
      (__)__ _""")


def done_message():
    print("****************")
    print(color.green(f"""\n DONE \n"""))
    print("****************")

def eror_input_message():
    print("****************")
    print(color.red(f"""\n INCORRECT INPUT \n"""))
    print("****************")

def please_set_user_message():
    print(color.red("\n***Pleasy, set user***\n"))

while True:
    print("Menu")
    print(f"""1) Set user
2) Show banned and deleted account in friends
3) Show who last was half year past
0) Exit
Currently account: {account}""")
    answer = input("Choose number of menu item: ")

    if (answer == "0"):
        break

    elif (answer == "1"):
        anon_id = input("Input vk id: https://vk.com/")
        try:
            service.check_id_on_exists(anon_id)
        except:
            print("****************")
            print(color.red(f"""Syrry, but account: """), end = "")
            print(color.colorize(color.BgColor.Null, color.Base.Underline, color.FgColor.Red, "vk.com/" + anon_id), end = " ")
            print(color.red("is not exists.\nPlease, try again"))
            print("****************")
            continue
        anon = service.request_info_of_account(anon_id)
        auth = True
        account = f'{color.cyan(anon.get_name())} ({anon.get_link()}).\n'
        done_message()

    elif (answer == "2"):
        if auth == False:
            please_set_user_message()
            continue
        ban_and_del_acc = anon.get_banned_and_deleted_friends()
        count_deleted = anon.get_count_deleted()
        count_banned = anon.get_count_banned()
        print("****************")
        print(f'All friends: ({anon.get_count_friends()}).')
        print("Your banned friends: ")
        for banned_account in ban_and_del_acc["banned"]:
            print(f'{banned_account.get_name()} ({banned_account.get_link()})')
        print(f'    Count: {"You havent banned accounts in friends" if (count_banned == 0) else {count_banned}}')
        print("Your deleted friends: ")
        for deleted_account in ban_and_del_acc["deleted"]:
            print(f'{deleted_account.get_name()} ({deleted_account.get_link()})')
        print(f'    Count: {"You havent deleted accounts in friends" if (count_deleted == 0) else {count_deleted}}')
        print("****************")
    
    elif (answer == "3"):
        if auth == False:
            please_set_user_message()
            continue
        print("****************")
        friends = anon.get_non_active_friends()
        friends = sorted(friends, key = lambda friend: friend.get_days_offline(), reverse = 1)
        count_friends = len(friends)
        for friend in friends:
            print(f'{friend.get_name()} \n  offline: {friend.get_days_offline()} days. ({friend.get_link()})')
        print(f'Count: {"Zero accounts" if (count_friends == 0) else {count_friends}}')
        print("****************")

    else:
        eror_input_message()
