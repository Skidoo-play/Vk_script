#!/usr/local/bin/python3
import accountWithoutLogin

def main():
    # Anon = AccountWithoutLogin(input("Input your vk id: "))
    Anon = accountWithoutLogin.AccountWithoutLogin(135480774)
    Anon.print_info_about_user()
    Anon.friends_get()
    print(f'\nYou have ({Anon.get_count_friends()}) friends')
    print("-------------------------------")
    Anon.get_banned_and_deleted_friends()
    print("Your banned friends: ")
    Anon.print_banned_friends()
    print(f'    Count: {"You havent banned friends" if (Anon.get_count_banned() == 0) else {Anon.get_count_banned()}}')
    print("Your deleted friends: ")
    Anon.print_deleted_friends()
    print(f'    Count: {"You havent deleted friends" if (Anon.get_count_deleted() == 0) else {Anon.get_count_deleted()}}')

if __name__ == '__main__':
    main()