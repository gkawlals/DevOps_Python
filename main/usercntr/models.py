from django.db import models


class UserTable(models.Model):
    user_id = models.CharField(max_length=200, null=False)
    user_name = models.CharField(max_length=200)
    user_pwd = models.CharField(max_length=200, null=False)
    user_like = models.CharField(max_length=200)
    user_like_borad = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id

