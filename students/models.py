from django.db import models
from accounts.models import Account

# Create your models here.

class StudentBatch(models.Model):
    batch_date = models.DateTimeField(auto_now_add=True)



class StudentAccount(models.Model):
    gender                  = models.CharField(max_length=10)
    date_of_birth           = models.DateField(blank=True,null=True)
    user                    = models.ForeignKey(Account, on_delete=models.CASCADE)
    semister                = models.IntegerField(default=False)
    date_joined             = models.DateField(auto_now_add=True)

    def get_date_of_birth(self):
        return str(self.date_of_birth)