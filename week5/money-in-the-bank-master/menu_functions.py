import smtplib
import datetime
import sql_manager
import uuid
from Client import Client


def current_time():
    now = datetime.datetime.now()
    return datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)


def send_email(receiver, content):
    sender = "money-in-the-bank@test.com"

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    try:
        smtp.login(sender, 'email_password')
    except SMTPAuthenticationError:
        print('Wrong auth')

    smtp.sendmail(sender, receiver, content)
    smtp.quit()


def update_deposit_amount(logged_user, amount):
    new_amount = logged_user.get_balance() + amount
    username = logged_user.get_username()
    sql_manager.update_amount(username, new_amount)
    id = logged_user.get_id()
    message = logged_user.get_message()
    email = logged_user.get_email()
    logged_user = Client(id, username, new_amount, message, email)
    return logged_user


def generate_tans():
    tans_number = 10
    generated_tans = []
    for i in range(tans_number):
        tan = str(uuid.uuid4())
        tan = tan.replace("-", "")
        generated_tans.append(tan)

    return generated_tans


def send_tans(user_email, tans):
    email_content = "\n".join(tans)
    send_email(user_email, email_content)


def tan_record_operations(logged_user):
    tans = generate_tans()
    user_id = logged_user.get_id()
    sql_manager.record_new_tans(user_id, tans)
    user_email = logged_user.get_email()
    send_tans(user_email, tans)
