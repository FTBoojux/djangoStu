from django.db import models


class UserReportInfo(models.Model):
    uri_id = models.AutoField(primary_key=True)
    ru_id = models.IntegerField()
    uid = models.IntegerField()
    reason = models.CharField(max_length=200)
    report_at = models.CharField(max_length=20)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_report_info'