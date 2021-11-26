from django.contrib import admin
from board.models import BoardTable
# Register your models here.

class boardView(admin.ModelAdmin):
    list_display=('id','board_title','board_user','board_up_dt','board_context','board_dt','board_like_cnt','board_like')

admin.site.register(BoardTable, boardView);  