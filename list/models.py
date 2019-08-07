from django.db import models

# Create your models here.
class test(models.Model):
    name = models.CharField(max_length = 20)
    Email = models.CharField(max_length = 30)
    mobile_no = models.CharField(max_length = 30)

    def __str__(self):
        return self.name