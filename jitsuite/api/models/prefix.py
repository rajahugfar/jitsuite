from django.db import models

class Prefix(models.Model):
    prefix_id = models.AutoField(primary_key=True)
    prefix_detail = models.CharField(max_length=255)
    status = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.prefix_detail
    
    class Meta:
        verbose_name_plural = 'Prefix'
        db_table = 'Prefix'