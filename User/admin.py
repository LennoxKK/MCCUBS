from django.contrib import admin
from .models import User
from .models import Profile,UserProfile,CustomUser,CustomUserManager

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserProfile)
admin.site.register(User)


class CustomUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomUser,CustomUserAdmin)

