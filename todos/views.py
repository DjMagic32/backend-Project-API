from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers
# Create your views here.


class ListTodo (generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailTodo (generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

# En la parte superior, importamos vistas genéricas de Django REST Framework
# y nuestros archivos models.py y serializers.py.
# Recuerde de nuestro archivo todos/urls.py que tenemos dos rutas y, por lo tanto, dos vistas distintas.
# Usaremos ListAPIView para mostrar todos los todos y RetrieveAPIView para mostrar una única instancia de modelo.
# Los lectores astutos notarán que hay un poco de redundancia en el código aquí.
# Básicamente, repetimos queryset y serializer_class para cada vista, aunque la vista genérica extendida es diferente.
# Más adelante en el libro aprenderemos sobre conjuntos de vistas y enrutadores que abordan este problema y nos permiten crear las mismas vistas de API y URL con mucho menos código.
# ¡Pero por ahora hemos terminado! Nuestra API está lista para consumir.
# Como puede ver, la única diferencia real entre Django REST Framework y Django es que con Django REST Framework necesitamos agregar un archivo serializers.py y no necesitamos un archivo de plantillas.
# De lo contrario, los archivos urls.py y views.py actúan de manera similar.
