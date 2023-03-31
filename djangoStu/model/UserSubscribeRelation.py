from django.db import models


class UserSubscribeRelation(models.Model):
    subscriber = models.IntegerField()
    subscribed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_subscribe_relation'