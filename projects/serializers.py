#nos permite importar un modelo especial de rest_framework
from rest_framework import serializers
#le decimos  que esta basado en eun modelo ya creado previamente 
#y da aqui django sabra que responer cuando se le haga una peticion put, get, delete 
from .models import Project
#para que django sepa que responer cuando

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        #añadimos la tupla para decirle los datos que van a ser consultados 
        #los capos ya los tenemos 
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #para que no se modifique la fecha de creacion que sea solo lectura
        read_only_fields = ('created_at', )

