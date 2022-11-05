from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.decorators import display

from vacation_management_app.models import Account, VacationRequest


class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = "Accounts"


class CustomizedUserAdmin(UserAdmin):
    list_display = ('id', 'email', 'get_fullname', 'get_status', 'is_staff')
    list_display_links = ('id', 'email')
    inlines = (AccountInline, )

    @display(ordering='account__status', description='Status')
    def get_status(self, obj):
        return obj.account.status

    @display(ordering='account__fullname', description='Full Name')
    def get_fullname(self, obj):
        return obj.account.fullname


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_email', 'fullname', 'status',)
    list_display_links = ('id', 'fullname', 'get_email')
    search_fields = ('user__email', 'fullname')
    ordering = ('status', '-id')
    list_editable = ('status',)
    list_filter = (
        ('status', admin.AllValuesFieldListFilter),
    )

    @display(ordering='user__email', description='Email Address')
    def get_email(self, obj):
        return obj.user.email


class VacationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_email', 'get_fullname',
                    'start_date', 'finish_date', 'get_total_days', 'status',)
    list_display_links = ('id', 'get_email')
    list_filter = ('status',)
    search_fields = ('user__email', 'account__fullname')
    exclude = ('account',)
    list_editable = ('status',)

    @display(description="Total Days")
    def get_total_days(self, obj):
        days = int((obj.finish_date - obj.start_date).days)
        if days == 1:
            return str(days) + ' day'
        return str(days) + ' days'

    @display(ordering='user__email', description='Email Address')
    def get_email(self, obj):
        return obj.user.email

    @display(ordering='account__fullname', description='Full Name')
    def get_fullname(self, obj):
        return obj.account.fullname


admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(VacationRequest, VacationRequestAdmin)
