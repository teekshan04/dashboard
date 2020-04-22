from django.contrib import admin
from django.urls import path
from . import views
appname= "dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    #path('', views.importer, name='importer')
   # path('', views.importer, name='importer'),
]