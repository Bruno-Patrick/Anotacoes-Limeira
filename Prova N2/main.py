from produto import *
from farmacia import Farmacia

RecolFarma = Farmacia()

Dipirona = Generico(101002,'Dipirona',4.50,'12/07/2023')
Amitriptilina = Referencia(101003, 'Amitriptilina',31.95,'12/07/2024')
Doralgina = Similar(101004, 'Doralgina',4.00,'19/03/2023')
Aminoxidil = Beleza(101005, 'Aminoxidil',4.00,'13/12/2022')
Sabonete = Beleza(101006, 'Sabonete',2.50,'13/12/2023')

RecolFarma.cadastrar_produtos(Dipirona)
RecolFarma.cadastrar_produtos(Amitriptilina)
RecolFarma.cadastrar_produtos(Doralgina)
RecolFarma.cadastrar_produtos(Aminoxidil)
RecolFarma.cadastrar_produtos(Sabonete)

Dipirona.comprar(1)
Amitriptilina.comprar(60)
Doralgina.comprar(6)
Dipirona.comprar(9)
Sabonete.comprar(3)
Sabonete.comprar(10)
Sabonete.comprar(4.25)
RecolFarma.imprimir()
RecolFarma.situacao_monetaria()