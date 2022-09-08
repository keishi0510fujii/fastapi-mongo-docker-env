from decouple import config
from motor import motor_asyncio


class MongoSetup:
    __client: motor_asyncio.AsyncIOMotorClient

    def __init__(self):
        user: str = config("MONGO_USERNAME")
        password: str = config("MONGO_PASSWORD")
        host: str = config("MONGO_HOST")
        port: int = int(config("MONGO_PORT"))
        connection_str: str = f"mongodb://{user}:{password}@{host}:{port}/"
        self.__client = motor_asyncio.AsyncIOMotorClient(connection_str)

    def client(self) -> motor_asyncio.AsyncIOMotorClient:
        return self.__client
