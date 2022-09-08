import unittest
from time import time
from typing import List, Any

from domain.account.model import Account
from domain.account.repository import AccountRepository
from insrastructure.mongo.account.repository import AccountRepositoryMongo
from insrastructure.mongo.setup import MongoSetup


class TestAccountRepository(unittest.IsolatedAsyncioTestCase):
    __hoge_email = "hogehoge@example.com"
    __hoge_password = "hogeH0g="
    __fuga_email = "fugafuga@example.com"
    __fuga_password = "fuga2G@"
    __collection: Any
    __repository: AccountRepository

    async def asyncSetUp(self) -> None:
        db_client = MongoSetup().client()
        db = db_client.test_authentication
        self.__collection = db.account
        await self.__collection.create_index("email", unique=True)
        self.__repository = AccountRepositoryMongo(self.__collection)

    async def asyncTearDown(self) -> None:
        await self.__collection.drop()

    async def test_save(self):
        model: Account = Account(self.__hoge_email, self.__hoge_password, self.__hoge_password)
        await self.__repository.save(model)

        inserted_data = await self.__repository.find_by_email(self.__hoge_email)

        self.assertEqual(model.mail_address(), inserted_data['email'])

    async def test_save_all(self):
        model_list: List[Account] = [
            Account(
                self.__hoge_email + f"{i}",
                self.__hoge_password + f"{i}",
                self.__hoge_password + f"{i}"
            ) for i in
            range(25)]
        self.time_begin = time()
        _ = await self.__repository.save_all(model_list)

        inserted_data = await self.__repository.find_by_email(self.__hoge_email + "0")

        self.assertEqual(self.__hoge_email + "0", inserted_data['email'])


if __name__ == '__main__':
    unittest.main()
