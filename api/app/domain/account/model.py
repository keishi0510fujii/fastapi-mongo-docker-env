import ulid
from passlib.hash import pbkdf2_sha256


class Account:
    __id: str
    __email: str
    __hashed_password: str

    def __init__(self, email: str, password: str, password_confirmation: str):
        if password != password_confirmation:
            raise Exception("password_confirmation is not same value password")
        self.__id = ulid.new().str
        self.__email = email
        self.__hashed_password = pbkdf2_sha256.hash(password)

    def id(self):
        return self.__id

    def mail_address(self):
        return self.__email

    def hashed_password(self):
        return self.__hashed_password
