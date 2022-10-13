import bcrypt

class Login:

    __slots__ = ["_isLogged", "_userActive","_user"]
    def __init__(self):
        self._isLogged = False
        self._userActive = True
        self._user = None



    @property
    def isLogged(self):
        return self._isLogged
    @property
    def userActive(self):
        return self._userActive
    @property
    def user(self):
        return self._user
    @property
    def getUserId(self):
        return self._user.id

    def set_user(self, value):
        self._user = value

    def logout(self):
        self._isLogged = False
    def login(self):
        self._isLogged = True

    def encript(self,key):

        if not key:
            raise Exception("key cannot be empty!")

        try:
            bytes = key.encode('utf-8')
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(bytes, salt)
        except Exception as err:
            print(err)

    def bytes(self, key):
        bytes = key.encode('utf-8')
        return bytes

    def isKeyTrue(self, key, hash):

        if not key:
            raise Exception("key cannot be empty!")
        if not hash:
            raise Exception("hash cannot be empty!")
        bytes = key.encode('utf-8')
        return bcrypt.checkpw(bytes, hash)