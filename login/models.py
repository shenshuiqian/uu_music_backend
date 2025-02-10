from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    date_joined = models.DateField(auto_now_add=True,null=True)
    class Meta:
        db_table = 'user_info'
    def find(self,name):
        user=User.objects.get(username=name)
        return user


