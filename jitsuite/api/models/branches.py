from django.db import models
from .company import Company  # Import the Company model
from .unit import Unit  # Import the Unit model

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.branch_name
    
    class Meta:
        verbose_name_plural = 'Branch'
        db_table = 'Branch'
    
