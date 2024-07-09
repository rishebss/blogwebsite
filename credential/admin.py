from django.contrib import admin
from .models import Cad, Interior
from . models import Lux
from . models import Luxmodel





# Register your models here.
admin.site.register(Cad)
admin.site.register(Lux)
admin.site.register(Luxmodel)
admin.site.register(Interior)



