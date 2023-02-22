from django.db import models

# Create your models here.
class common(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=20)

    class Meta:
        abstract=True
   

class Signup(common):
    name=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.name

class Login(common):

    def __str__(self):
        return self.email   

        #class based views

