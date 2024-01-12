from django.db import models

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=255)
    position_level = models.IntegerField()
    status = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position_name
    
    class Meta:
        verbose_name_plural = 'Position'
        db_table = 'Position'