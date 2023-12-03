#Importamos el modulo routers de rest_framework que nos permite crear el crud de nuestros datos 
from rest_framework import routers

from .api import ProjectViewSet

#ejecutamos el modulo routers 
#el modulo routers tiene el default router que es el que va a crear el crud 
#le decimos que eso lo guarde en una variable router
router = routers.DefaultRouter()
#usando este router vamos a registar
#le vamos a decir que el register va a estar basado en el conjunto de datos que vienen de de projectVewSet
# y le ponemos nombre a la ruta "project" 
router.register('api/projects', ProjectViewSet, 'projects')

#las rutas la genera el router pero igual tenemos que exportar un urlpatterns que va a generar las urls
#genera 4 urls una para post, otra para get, delete y put el urlpatters maneja esas peticiones 
urlpatterns = router.urls