from django.contrib import admin

# Register your models here.
from .models import Profile,pitchDeck

admin.site.register(Profile)

admin.site.register(pitchDeck)
