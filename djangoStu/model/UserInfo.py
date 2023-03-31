from dataclasses import dataclass
from django.db import models
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class UserInfo(models.Model):
    uid: int = models.AutoField(primary_key=True)
    username: str = models.CharField(unique=True, max_length=20)
    password: str = models.CharField(max_length=100)
    avator: str = models.CharField(max_length=100, blank=True, null=True, default='')
    subscribeds: int = models.IntegerField(blank=True, null=True, default=0)
    subscribers: int = models.IntegerField(blank=True, null=True, default=0)
    is_advanced: int = models.IntegerField(blank=True, null=True, default=0)
    status: int = models.IntegerField(blank=True, null=True, default=0)
    is_del: int = models.IntegerField(blank=True, null=True, default=0)
    created_at: str = models.CharField(max_length=20, blank=True, null=True, default='')
    salt: str = models.CharField(max_length=45, default='')
    email: str = models.CharField(max_length=30, default='')

    class Meta:
        managed = False
        db_table = 'user_info'
