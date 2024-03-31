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
    

class UserProfile(models.Model):
    user=models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    is_employer=models.BooleanField(default=False)

User.userprofile=property(lambda u:UserProfile.objects.get_or_create(user=u)[0])


class Application(models.Model):
    job=models.ForeignKey(Job, on_delete=models.CASCADE)
    content=models.TextField()
    experience=models.TextField()

    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

