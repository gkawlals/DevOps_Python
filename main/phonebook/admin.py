from django.contrib import admin
from phonebook.models import PhoneBook

# Register your models here.
class PhoneBookView(admin.ModelAdmin):
    list_display=('id',"이름","전화번호", '이메일', '생년월일','작성자')

admin.site.register(PhoneBook,PhoneBookView);


