from django.contrib import admin
from .models import keyboard, drum, guitar, violin

# Register your models here.
admin.site.register(keyboard)
admin.site.register(drum)
admin.site.register(guitar)
admin.site.register(violin)