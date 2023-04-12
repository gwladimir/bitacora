import sys
sys.path.append('./')

from config.wsgi import *
from bitacora.models import Tipo

# LISTAR

# query = Tipo.objects.all()
# print(query)

# INSERTAR

# t = Tipo()
# t.tipo = 'Prueba'
# t.save()

# EDITAR

# try:
#     t = Tipo.objects.get(pk=2)
    # print(t.tipo) #Verificar si estoy escogiendo el objeto solicitado
#     t.tipo = 'hello'
#     t.save()
# except Exception as e:
#     print(e)

# ELIMINAR

# t = Tipo.objects.get(pk=3)
# t.delete()


# LISTAR FILTER

# obj = Tipo.objects.filter(tipo__contains='h').count()
# print(obj)

# for i in Tipo.objects.filter(tipo__endswith='o'):
#     print(i)
