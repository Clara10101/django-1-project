from django.contrib import admin
from pracownicy.models import Pracownicy, Zespoly, Etaty

# Register your models here.
admin.site.register(Pracownicy)
admin.site.register(Zespoly)
admin.site.register(Etaty)