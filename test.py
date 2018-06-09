#!/usr/local/bin/python3
import serviceVk
import accountWithoutLogin
import sys

# 135480774
def main():
    service = serviceVk.ServiceVk()
    anon = accountWithoutLogin.AccountWithoutLogin()
    if len(sys.argv) <= 1:
        anon_id = input("Input your vk id: ")
        service.check_id_on_exists(anon_id)
        anon.set_account(anon_id)
    else:
        service.check_id_on_exists(sys.argv[1])
        anon.set_account(sys.argv[1])
    anon.get_info_about_account()
    info_of_anon = anon.get_info_about_account()
    print(f'Ok your account is: {info_of_anon["first_name"]} {info_of_anon["last_name"]} ({info_of_anon["link"]})')
    print(f'You have ({anon.get_count_friends()}) friends')
    print("-------------------------------")
    ban_and_del_acc = anon.get_banned_and_deleted_friends()
    ban_acc = ban_and_del_acc["banned"]
    del_acc = ban_and_del_acc["deleted"]
    print("Your banned friends: ")
    for banned_account in ban_acc:
        print(f'{banned_account["first_name"]} {banned_account["last_name"]} ({banned_account["link"]})')
    print(f'    Count: {"You havent banned accounts in friends" if (anon.get_count_banned() == 0) else {anon.get_count_banned()}}')
    print("Your deleted friends: ")
    for deleted_account in del_acc:
        print(f'{deleted_account["first_name"]} {deleted_account["last_name"]} ({deleted_account["link"]})')
    print(f'    Count: {"You havent deleted accounts in friends" if (anon.get_count_deleted() == 0) else {anon.get_count_deleted()}}')


if __name__ == '__main__':
    main()