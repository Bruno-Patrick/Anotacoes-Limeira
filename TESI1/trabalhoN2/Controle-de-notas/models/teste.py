from Login import Login

login = Login()
senha = '12345'
a = login.encript(senha)
b = login.encript(senha)
c = login.encript(senha)
print(a)
print(b)
print(c)

print(login.isKeyTrue(senha,a))
print(login.isKeyTrue(senha,b))
print(login.isKeyTrue(senha,c))