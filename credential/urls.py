from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static
app_name='credential'

urlpatterns = [
   path('',views.index,name='index'),
   path('account/',views.account,name='account'),
   path('/dashboard',views.dashboard,name='dashboard'),
   path('delete/<int:taskid>/',views.delete,name='delete'),
   path('main/',views.main,name='main'),
   path('updatemain', views.updatemain, name='updatemain'),
   path('editmain/<int:id>/', views.editmain, name='editmain'),
   path('uploadlead/',views.uploadlead,name='uploadlead'),
   path('editlead/',views.editlead,name='editlead'),
   path('deletelead/<int:luxid>/', views.deletelead, name='deletelead'),
   path('updatelead/<int:lexid>/', views.updatelead, name='updatelead'),
   path('viewinterior/', views.viewinterior, name='viewinterior'),
   path('uploadinterior/', views.uploadinterior, name='uploadinterior'),
   path('editinterior/', views.editinterior, name='editinterior'),
   path('deleteinterior/<int:interid>/', views.deleteinterior, name='deleteinterior'),
   path('about/',views.about,name='about'),
   path('demo/',views.demo,name='demo')


              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)