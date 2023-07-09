"""
(c) All rights reserved. ECOLE POLYTECHNIQUE FEDERALE DE LAUSANNE, Switzerland, VPSI, 2023
"""

from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    def username(self, userprofile):
        return userprofile.user.username

    def email(self, userprofile):
        return userprofile.user.email

    def first_name(self, userprofile):
        return userprofile.user.first_name

    def last_name(self, userprofile):
        return userprofile.user.last_name


admin.site.register(UserProfile, UserProfileAdmin)
