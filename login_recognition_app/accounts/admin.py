# Create super user allows us to create Admin accounts

from django.contrib import admin
from accounts.models import UserProfile

admin.site.register(UserProfile)