from django.db import models

# Create your models here.
class StudentAPI(models.Model):
    name= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    roll= models.IntegerField()
    gender= models.CharField(max_length=100, choices= 
                               
                               [('Male', 'M'),
                               ('Female', 'F')
                             ]
                             
                             )
    
    def __str__(self):
        return self.name