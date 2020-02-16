from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .import models
class Custom_Admin(UserAdmin):
    list_display = ('username','email','is_staff','is_admin')
    search_fields = ('username','email')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(models.Custom_user,Custom_Admin)
# Register your models here.
