import unittest

from domain.account.model import Account


class TestAccount(unittest.TestCase):
    __hoge_email = "hogehoge@example.com"
    __hoge_password = "hogeH0G="

    def test_id(self):
        entity = Account(self.__hoge_email, self.__hoge_password, self.__hoge_password)
        self.assertEqual(26, len(entity.id()))

    def test_mail_address(self):
        entity = Account(self.__hoge_email, self.__hoge_password, self.__hoge_password)
        self.assertEqual(self.__hoge_email, entity.mail_address())

    def test_hashed_password(self):
        entity = Account(self.__hoge_email, self.__hoge_password, self.__hoge_password)
        self.assertIn("sha", entity.hashed_password())


if __name__ == '__main__':
    unittest.main()
