from django.db import models
from .branches import Branch  # Import the Branch model

class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.division_name
    
    class Meta:
        verbose_name_plural = 'Division'
        db_table = 'Division'