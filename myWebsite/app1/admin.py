from django.contrib import admin
from .models import UserDataModel, SessionModel

# Register your models here.

admin.site.register(UserDataModel)
admin.site.register(SessionModel)