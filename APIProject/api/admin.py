from django.contrib import admin

# Register your models here.
from django.contrib import admin
from api.models import Dog, Breed

admin.site.register(Dog)
admin.site.register(Breed)