from domain.account.model import Account
from domain.account.repository import AccountRepository


class MockAccountRepositoryNormal(AccountRepository):

    async def save(self, account: Account):
        return
