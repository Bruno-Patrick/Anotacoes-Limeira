from Responsavel import Responsavel

dd = Responsavel('Bruno')

for attributes in dd.__slots__:
    print(attributes[1::],"\n")
    print(dd.__getattribute__(attributes))