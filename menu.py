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

    if answer == "0":
        break

    elif answer == "1":
        anon_id = input("Input vk id: https://vk.com/")
        try:
            service.check_id_on_exists(anon_id)
        except:
            print("****************")
            print(color.red(f"""Syrry, but account: """), end="")
            print(color.colorize(color.BgColor.Null, color.Base.Underline,
                                 color.FgColor.Red, "vk.com/" + anon_id), end=" ")
            print(color.red("is not exists.\nPlease, try again"))
            print("****************")
            continue
        anon = service.request_info_of_account(anon_id)
        auth = True
        account = f'{color.cyan(anon.full_name)} ({anon.full_name}).\n'
        done_message()

    elif answer == "2":
        if auth == False:
            please_set_user_message()
            continue
        ban_and_del_acc = anon.get_banned_and_deleted_friends()
        count_friends = len(anon.get_public_friends())
        count_deleted = len(ban_and_del_acc["banned"])
        count_banned = len(ban_and_del_acc["deleted"])
        print("****************")
        print(f'All friends: ({count_friends}).')
        print(f"Your banned friends: ({count_banned}). ")
        for banned_account in ban_and_del_acc["banned"]:
            print(f'{banned_account.full_name} ({banned_account.account_link})')
        print(f"Your deleted friends: ({count_deleted}). ")
        for deleted_account in ban_and_del_acc["deleted"]:
            print(f'{deleted_account.full_name} ({deleted_account.account_link})')
        print("****************")

    elif answer == "3":
        if auth == False:
            please_set_user_message()
            continue
        print("****************")
        non_active_friends = anon.get_non_active_friends()
        non_active_friends = sorted(
            non_active_friends, key=lambda friend: friend.get_days_offline(), reverse=1)
        count_non_active_friends = len(non_active_friends)
        print(
            f"Your non active friends friends: ({count_non_active_friends}). ")
        for friend in non_active_friends:
            print(
                f'{friend.full_name} \n  offline: {friend.get_days_offline()} days. ({friend.account_link})')
        print("****************")

    else:
        eror_input_message()
