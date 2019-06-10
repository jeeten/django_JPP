from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class elasticIndex(models.Model):
        author = models.ForeignKey(User,on_delet=models.CASCADE,related_name = "elasticsearch")
        createdDate = models.DateField(default=timezone.now) 
        title = models.CharField(max_length=200)
        text = models.TextFiedl(max_length=1000)