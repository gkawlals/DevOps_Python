from django.db import models

class BoardTable(models.Model):
    board_title = models.CharField(max_length=200, null=False, blank=False)
    board_user = models.CharField(max_length=200, null=False)
    board_context = models.TextField(null=False)
    board_like_cnt = models.IntegerField(null=False)
    board_dt = models.DateField()
    board_up_dt = models.DateField()
    board_like = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.board_title
