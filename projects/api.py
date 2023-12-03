#importamos la clase Project de models 
from .models import Project
#importamos el viewset y permissions
from rest_framework import viewsets, permissions
#importamos el serializer
from .serializers import ProjectSerializer

#creamos la clase projectviewset que hereda de modlViewSet
#dentro diremos que consutas se van a poder hacer 
class ProjectViewSet(viewsets.ModelViewSet):
    #.all consulta todos lo datos de una tabla 
    #queryset = conjunto de datos 
    queryset = Project.objects.all()
    #le decimos en una lista que solo tendra permitido hacer operaciones en estas consultas y al 
    #colocar .AllowAny cualquier cliente podra solicitar datos al servidor 
    permission_classes = [permissions.AllowAny]
    #le decimos partir de que serializer usara nuestros datos osea como lo va a convertir 
    serializer_class = ProjectSerializer
