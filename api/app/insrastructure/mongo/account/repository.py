from typing import List, Any

from domain.account.model import Account
from domain.account.repository import AccountRepository


class AccountRepositoryMongo(AccountRepository):
    __collection: Any

    def __init__(self, collection):
        self.__collection = collection

    async def save(self, account: Account):
        insert_data = self.__serialize_to_schema(account)
        _ = await self.__collection.insert_one(insert_data)
        return

    async def find_by_email(self, email: str):
        return await self.__collection.find_one({"email": email})

    async def save_all(self, account_list: List[Account]):
        insert_data_list = [self.__serialize_to_schema(account) for account in account_list]
        await self.__collection.insert_many(insert_data_list)
        return

    @staticmethod
    def __serialize_to_schema(account: Account) -> dict:
        return {
            "_id": account.id(),
            "email": account.mail_address(),
            "hashed_password": account.hashed_password()
        }
