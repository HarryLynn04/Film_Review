from django.contrib import admin
from Film_Review.models import UserProfile

# Register your models here.
from Film_Review.models import Film

admin.site.register(Film)
admin.site.register(UserProfile)

