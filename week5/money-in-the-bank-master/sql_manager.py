import sqlite3
import re
import hashlib
import datetime
from Client import Client

conn = sqlite3.connect("bank.db", detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                block_time TIMESTAMP,
                login_attempts INTEGER DEFAULT 0,
                email TEXT,
                reset_code TEXT DEFAULT '',
                tans_generated INTEGER DEFAULT 0)'''

    cursor.execute(create_query)


def create_tans_tabe():
    create_query = '''CREATE TABLE IF NOT EXISTS
        tan_codes(id INTEGER PRIMARY KEY AUTOINCREMENT,
                tan TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES clients(id))'''

    cursor.execute(create_query)


def get_tans_for_user(user_id):
    tans_list = []
    select_query = "SELECT tan FROM tan_codes WHERE user_id = ?"
    tans = cursor.execute(select_query, (user_id,))
    for row in tans:
        tans_list.append(row[0])

    return tans_list


def remove_used_tan(user_id, tan_code):
    delete_query = "DELETE FROM tan_codes WHERE user_id = ? AND tan = ?"
    cursor.execute(delete_query, (user_id, tan_code))
    conn.commit()


def record_new_tans(user_id, tan_codes):
    for tan in tan_codes:
        insert_sql = "INSERT INTO tan_codes(tan, user_id) VALUES (?, ?)"
        cursor.execute(insert_sql, (tan, user_id))

    conn.commit()


def are_tans_generated(user_id):
    select_query = "SELECT tans_generated FROM clients WHERE id = ? LIMIT 1"
    cursor.execute(select_query, (user_id,))
    generated = cursor.fetchone()
    return generated[0]


def tans_are_generated(user_id):
    are_generated = 1
    update_sql = "UPDATE clients SET tans_generated = ? WHERE id = ?"
    cursor.execute(update_sql, (are_generated, user_id))
    conn.commit()


def get_number_of_failed_logins(username):
    select_query = "SELECT login_attempts FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(select_query, (username,))
    number_failed = cursor.fetchone()
    return number_failed[0]


def update_number_of_failed_logins(login_attempts, username):
    update_sql = "UPDATE clients SET login_attempts = ? WHERE username = ?"
    cursor.execute(update_sql, (login_attempts, username))
    conn.commit()


def get_blocked_datetime(username):
    select_query = "SELECT block_time FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(select_query, (username,))
    block_time = cursor.fetchone()
    return block_time[0]


def update_failed_datetime(datetime_fail, username):
    update_sql = "UPDATE clients SET block_time = ? WHERE username = ?"
    cursor.execute(update_sql, (datetime_fail, username))
    conn.commit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def get_user_email(username):
    select_query = "SELECT email FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(select_query, (username,))
    email_fetch = cursor.fetchone()
    return email_fetch[0]


def update_reset_code(username, code):
    update_sql = "UPDATE clients SET reset_code = ? WHERE username = ?"
    cursor.execute(update_sql, (code, username))
    conn.commit()


def check_hash_code(username, hash_code):
    select_query = "SELECT reset_code FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(select_query, (username,))
    email_fetch = cursor.fetchone()
    code_from_db = email_fetch[0]
    if code_from_db == hash_code:
        return True
    return False


def update_password(username, new_password):
    update_sql = "UPDATE clients SET password = ? WHERE username = ?"
    cursor.execute(update_sql, (new_password, username))
    conn.commit()


def hash_password(password):
    hashed_password = hashlib.sha1(password.encode(encoding="utf-8"))
    return hashed_password.hexdigest()


def check_pass(username, password):
    username_in = username in password
    regex = '^(?=.{8,}$)(?=.*[!@#$%^&])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*'
    if re.match(regex, password) and not username_in:
        return True
    else:
        return False


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    default_datetime = datetime.datetime(1900, 1, 1, 0, 0, 0)
    insert_sql = "INSERT INTO clients(username, password, block_time, email) VALUES (?, ?, ?, ?)"
    cursor.execute(insert_sql, (username, password, default_datetime, email))
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message, email FROM clients WHERE username = ? AND password = ? LIMIT 1"

    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False


def update_amount(username, amount):
    update_sql = "UPDATE clients SET balance = ? WHERE username = ?"
    cursor.execute(update_sql, (amount, username))
    conn.commit()
