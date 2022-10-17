class Usuario:

    __slots__ = ["_id","_hash","_username","_professor"]
    def __init__(self, hash, username, professor = None):
        self._id = None
        self._hash = hash
        self._username = username
        self._professor = professor

    @property
    def id(self):
        return self._id
    @property
    def hash(self):
        return self._hash
    @property
    def username(self):
        return self._username
    @property
    def professor(self):
        return self._professor

    @id.setter
    def id(self, value):
        self._id = value
    @hash.setter
    def hash(self, value):
        self._hash = value
    @username.setter
    def username(self, value):
        self._username = value
    @professor.setter
    def professor(self, value):
        self._professor = value