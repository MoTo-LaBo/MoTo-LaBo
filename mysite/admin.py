from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mysite.models import User

# ここで UserAdmin を継承


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email',
                'password',
            )
        }),
        (None, {
            'fields': (
                'is_active',
                'is_admin',
            )
        })
    )

    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()


# 標準でグループが表示されるので、それを表示しないように(unregister)指示. import Group
admin.site.unregister(Group)
# admin に対して登録(register)しますよ。 mysite models.py で作成した User も
admin.site.register(User, CustomUserAdmin)
