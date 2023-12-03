from django.db import models

# Create your models here.
#con esta clase podemos crear una tabla en la base de datos que este conectada a django
class Project(models.Model):
    #debemos decir el tipo de dato de cada uno 
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.TextField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)