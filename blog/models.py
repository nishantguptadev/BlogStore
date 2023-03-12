from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=122)
    title= models.CharField(max_length=122)
    body= models.CharField(max_length=1000000)
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    image=models.ImageField(upload_to="blog/images", null=True, blank= True, default='')

    
    # def __str__(self): # this one works only for single 
        # return (self.name, self.title) #doesn't work for both, only one

    # def __str__(self): # this work for both
        # template = '{0.name}\n-----------\n{0.title}'
        # return template.format(self)
    # def __str__(self): #work for both
        # return f'{self.name}--------- {self.title}'