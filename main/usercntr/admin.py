from django.contrib import admin
from usercntr.models import UserTable
# Register your models here.

class usercntrView(admin.ModelAdmin):
    list_display=('id','user_id','user_name','user_pwd','user_like')

admin.site.register(UserTable,usercntrView);