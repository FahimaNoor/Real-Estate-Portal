from django.contrib import admin
from django.contrib.auth.models import User

# Admin can access User Model
admin.register(User)
