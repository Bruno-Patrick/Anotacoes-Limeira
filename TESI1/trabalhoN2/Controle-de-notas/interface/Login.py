import bcrypt

class Login:

    __slots__ = ["_isLogged", "_userActive"]
    def __init__(self):
        self._isLogged = False
        self._userActive = True

    def encript(key):

        if not key:
            raise Exception("key can't not be empty!")

        try:
            bytes = key.encode('utf-8')
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(bytes, salt)
        except Exception as err:
            print(err)

    def isKeyTrue(key, hash):

        if not key:
            raise Exception("key can't not be empty!")
        if not hash:
            raise Exception("hash can't not be empty!")

        bytes = key.encode('utf-8')
        return bcrypt.checkpw(bytes, hash)