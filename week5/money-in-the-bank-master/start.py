import sql_manager
import getpass
import uuid
import datetime
import menu_functions


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    datetime_fail = datetime.datetime(1900, 1, 1, 0, 0, 0)

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            hashed_pass = sql_manager.hash_password(password)
            email = input("Enter your email: ")
            if sql_manager.check_pass(username, password):
                sql_manager.register(username, hashed_pass, email)
                print("Registration Successfull")
            else:
                print("Registration failed")

        elif command == 'login':
            username = input("Enter your username: ")
            failed_logins = sql_manager.get_number_of_failed_logins(username)
            blocked_datetime = sql_manager.get_blocked_datetime(username)
            difference = menu_functions.current_time() - blocked_datetime
            if str(difference) < "0:05:00":
                print("Please try again later.")
                failed_logins = 0
                sql_manager.update_number_of_failed_logins(failed_logins, username)
            else:
                if failed_logins < 5:
                    password = getpass.getpass("Enter your password: ")
                    password = sql_manager.hash_password(password)
                    logged_user = sql_manager.login(username, password)

                    if logged_user:
                        failed_logins = 0
                        sql_manager.update_number_of_failed_logins(failed_logins, username)
                        logged_menu(logged_user)
                    else:
                        print("Login failed")
                        failed_logins += 1
                        sql_manager.update_number_of_failed_logins(failed_logins, username)
                else:
                    datetime_fail = menu_functions.current_time()
                    sql_manager.update_failed_datetime(datetime_fail, username)
                    print("You can not login for the next 5 minutes.")

        elif 'send-reset-password' in command:
            username = command.split(" ")[1]
            user_email = sql_manager.get_user_email(username)
            if user_email is not None:
                unique_random = str(uuid.uuid4())
                sql_manager.update_reset_code(username, unique_random)
                menu_functions.send_email(user_email, unique_random)
            else:
                print("Wrong username or bad input!")

        elif 'send-reset-password' not in command and "reset-password" in command:
            username = command.split(" ")[1]
            hash_code = input("Enter the hash code we sent you: ")
            if sql_manager.check_hash_code(username, hash_code):
                new_password = getpass.getpass("Enter your password: ")
                new_hashed_pass = sql_manager.hash_password(new_password)
                sql_manager.update_password(username, new_hashed_pass)
                print("Password was reset successfully.")
            else:
                print("The hash code you entered is invalid.")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            username = logged_user.get_username()
            hashed_new_pass = sql_manager.hash_password(new_pass)
            if sql_manager.check_pass(username, new_pass):
                sql_manager.change_pass(hashed_new_pass, logged_user)
                print("Change Successfull")
            else:
                print("Change failed")

        elif command == 'get-tan':
            user_id = logged_user.get_id()
            password = getpass.getpass("Enter your password: ")
            password = sql_manager.hash_password(password)
            username = logged_user.get_username()
            logged_user = sql_manager.login(username, password)

            if logged_user:
                are_tans_generated = sql_manager.are_tans_generated(user_id)
                if are_tans_generated == 0:
                    menu_functions.tan_record_operations(logged_user)
                    sql_manager.tans_are_generated(user_id)
                else:
                    tans_list = sql_manager.get_tans_for_user(user_id)
                    print("You have {} remaining TAN codes to use.".format(len(tans_list)))
                    if len(tans_list) == 0:
                        menu_functions.tan_record_operations(logged_user)
            else:
                print("Wrong password.")
                main_menu()

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'deposit':
            amount = int(input("Enter amount: "))
            tan_code = input("Enter TAN code: ")
            user_id = logged_user.get_id()
            tans_list = sql_manager.get_tans_for_user(user_id)
            if tan_code in tans_list:
                logged_user = menu_functions.update_deposit_amount(logged_user, amount)
                sql_manager.remove_used_tan(user_id, tan_code)
            else:
                print("Invalid TAN code.")

        elif command == 'withdraw':
            amount = int(input("Enter amount: "))
            balance = logged_user.get_balance()
            if amount > balance:
                print("You do not have that amount of money in your account.")
            else:
                amount = -amount
                logged_user = menu_functions.update_deposit_amount(logged_user, amount)

        elif command == 'display-balance':
            balance = logged_user.get_balance()
            print("Your balance is: {}".format(balance))

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    sql_manager.create_clients_table()
    sql_manager.create_tans_tabe()
    main_menu()

if __name__ == '__main__':
    main()
