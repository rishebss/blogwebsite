from django.urls import path
from . import views
app_name='cadapp'

urlpatterns = [
    path('complete/',views.complete,name='complete'),
    path('addcomplete/',views.addcomplete,name='addcomplete'),
    path('addincomplete/',views.addincomplete,name='addincomplete'),
    path('incomplete/', views.incomplete, name='incomplete'),
    path('viewcomplete/',views.viewcomplete,name='viewcomplete'),
    path('deletecomplete/<int:completeid>/',views.deletecomplete,name='deletecomplete'),
    path('viewincomplete/',views.viewincomplete,name='viewincomplete'),
    path('deleteincomplete/<int:incompleteid>/',views.deleteincomplete,name='deleteincomplete'),
    path('updatecomplete/<int:id>/',views.updatecomplete,name='updatecomplete'),
    path('updateincomplete/<int:id>/', views.updateincomplete, name='updateincomplete'),



]