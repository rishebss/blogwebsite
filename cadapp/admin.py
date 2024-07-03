from django.contrib import admin
from . models import Complete
from .models import Incomplete
# Register your models here.
admin.site.register(Complete)
admin.site.register(Incomplete)