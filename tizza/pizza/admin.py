from django.contrib import admin
from .models import Pizzeria, Pizza, Likes, Profile

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Pizzeria)
admin.site.register(Likes)
admin.site.register(Profile)
