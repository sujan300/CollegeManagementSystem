from django.db import models
from accounts.models import Account

# Create your models here.
class TeacherAccount(models.Model):
    gender  = models.CharField(max_length=10)
    user    = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 