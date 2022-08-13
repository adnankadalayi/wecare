from django.contrib import admin
from . models import Accounts
from django.contrib.auth.admin import UserAdmin

#show fields in admin panel with links sorted by date
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name','username', 'last_login', 'is_activated', )
    list_display_links = ('email', 'first_name', 'last_name')
    list_editable = ('is_activated',)
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

#to hide the password and not editable
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#register in admin panel
admin.site.register(Accounts, AccountAdmin )


