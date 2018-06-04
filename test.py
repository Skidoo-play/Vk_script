#!/usr/local/bin/python3

import accountWithoutLogin
import sys

# 135480774
def main():
    Anon = accountWithoutLogin.AccountWithoutLogin()
    if len(sys.argv) <= 1:
        Anon.auth_account(input("Input your vk id: "))
    else:
        Anon.auth_account(sys.argv[1])
    Anon.get_info_about_user()
    Anon.get_public_friends()
    info_of_anon = Anon.get_info_about_user()
    print(f'Ok your account is: {info_of_anon["first_name"]} {info_of_anon["last_name"]} ({info_of_anon["link"]})')
    print(f'You have ({Anon.get_count_friends()}) friends')
    print("-------------------------------")
    ban_and_del_acc = Anon.get_banned_and_deleted_friends()
    ban_acc = ban_and_del_acc["banned"]
    del_acc = ban_and_del_acc["deleted"]
    print("Your banned friends: ")
    for banned_account in ban_acc:
        print(f'{banned_account["first_name"]} {banned_account["last_name"]} ({banned_account["link"]})')
    print(f'    Count: {"You havent banned accounts in friends" if (Anon.get_count_banned() == 0) else {Anon.get_count_banned()}}')
    print("Your deleted friends: ")
    for deleted_account in del_acc:
        print(f'{deleted_account["first_name"]} {deleted_account["last_name"]} ({deleted_account["link"]})')
    print(f'    Count: {"You havent deleted accounts in friends" if (Anon.get_count_deleted() == 0) else {Anon.get_count_deleted()}}')





if __name__ == '__main__':
    main()