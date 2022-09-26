from Connection import Connection
from Responsavel import Responsavel

db = Connection()
r = Responsavel('Bruno')

obj = db.object_reader(r)
db.print_generator(obj)