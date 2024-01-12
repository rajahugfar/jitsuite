from django.db import models
from .divisions import Division  # Import the Unit model

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name
    
    class Meta:
        verbose_name_plural = 'Department'
        db_table = 'Department'