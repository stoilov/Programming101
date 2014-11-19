import sys
import unittest

sys.path.append("..")

import sql_manager

from menu_functions import current_time
from menu_functions import update_deposit_amount
from menu_functions import generate_tans


class FunctionsTest(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        hashed_pass = sql_manager.hash_password("HelloWorld1!")
        sql_manager.register('Tester', hashed_pass, 'tester@example.com')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')


    def test_current_time(self):
        now = current_time()
        self.assertEqual(current_time(), now)

    def test_update_deposit_amount(self):
        password = sql_manager.hash_password('HelloWorld1!')
        logged_user = sql_manager.login('Tester', password)
        deposit = 5000
        logged_user = update_deposit_amount(logged_user, deposit)
        self.assertEqual(logged_user.get_balance(), deposit)

    def test_generate_tans(self):
        tans = generate_tans()
        number_of_tans = len(tans)
        self.assertEqual(number_of_tans, 10)


if __name__ == '__main__':
    unittest.main()
