from typing import Any, Callable
from Login import Login

login = Login()
senha = '12345'
a = login.encript(senha)
# b = login.encript(senha)
# c = login.encript(senha)
a = str(a)
a = a.encode('utf-8')

def confirmar(n1,n2,command: str | Callable[[], Any]):...

# print(b)
# print(c)

print(login.isKeyTrue(senha,a))
# print(login.isKeyTrue(senha,b))
# print(login.isKeyTrue(senha,c))