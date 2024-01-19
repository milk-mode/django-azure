from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.TextField()
    
    def __str__(self) -> str:
        return f"First name: {self.first_name} Last name:{self.last_name}"
