from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "date_of_birth",)

admin.site.register(Member, MemberAdmin)