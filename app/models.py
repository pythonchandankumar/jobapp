from django.db import models
from django.contrib.auth.models import User



class Job(models.Model):
    title=models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description=models.CharField(max_length=500)
    created_at = models.DateField(auto_now=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    end_date=models.DateField()

    def __str__(self) -> str:
        return self.title

