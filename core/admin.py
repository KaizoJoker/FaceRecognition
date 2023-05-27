from django.contrib import admin
from .models import *
from .views import lecturer

admin.site.register(Profile)
admin.site.register(Lecturer)
admin.site.register(LastFace)