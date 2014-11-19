import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.create_tans_tabe()
        hashed_pass = sql_manager.hash_password("HelloWorld1!")
        sql_manager.register('Tester', hashed_pass, 'tester@example.com')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_hash_password(self):
        password = "HelloWorld1!"
        self.assertEqual(sql_manager.hash_password(password), "5dd7302470de0113da4315435eb6c98c511d5325")

    def test_register(self):
        sql_manager.register('Dinko', 'HelloWorld1!', 'dinko@example.com')

        sql_manager.cursor.execute('SELECT Count(*)  FROM clients WHERE username = (?) AND password = (?)', ('Dinko', 'HelloWorld1!'))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], 1)

    def test_login(self):
        password = sql_manager.hash_password('HelloWorld1!')
        logged_user = sql_manager.login('Tester', password)
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_injection(self):
        logged_user = sql_manager.login('\' OR 1 = 1 --', 'HelloWorld1!')
        self.assertFalse(logged_user)

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', '123567')
        self.assertFalse(logged_user)

    def test_change_message(self):
        password = sql_manager.hash_password('HelloWorld1!')
        logged_user = sql_manager.login('Tester', password)
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        password = sql_manager.hash_password('HelloWorld1!')
        logged_user = sql_manager.login('Tester', password)
        new_password = "12345HW!"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_get_tans_for_user(self):
        password = sql_manager.hash_password('HelloWorld1!')
        logged_user = sql_manager.login('Tester', password)
        user_id = logged_user.get_id()
        tan_list = sql_manager.get_tans_for_user(user_id)
        self.assertListEqual(tan_list, [])


if __name__ == '__main__':
    unittest.main()
