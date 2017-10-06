from django.contrib import admin

from .models import Monedas
from .models import Paridades

admin.site.register(Monedas)
admin.site.register(Paridades)
