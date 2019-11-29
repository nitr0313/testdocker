from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['fullname', 'email', 'username',]
    class Meta:
        fieldsets = (
            (('User'), {'fields': ('username', 'email','is_staff', 'fullname')}),
            (('Permissions'), {'fields': ('is_active','is_staff')}),
        )

admin.site.register(CustomUser, CustomUserAdmin)