from django.contrib import admin

from appchat.models import User, FeedBack


# Register your models here.
admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'email', 'username', 'date_joined']
#     list_filter = ['first_name', 'username', 'email', 'last_name']
#     list_editable = ['email']
#     prepopulated_fields = {'first_name': ('last_name',)}
#     date_hierarchy = 'date_joined'


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_filter = ['name', 'email']
    list_editable = ['email']
