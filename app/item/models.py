from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    nameOfCat=models.CharField(max_length=255)
    

    class Meta:
        verbose_name_plural='Categories'
        ordering=['nameOfCat']
        
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name=models.CharField(max_length=255)
    # category=models.ForeignKey(Category,name='nameOfCat',blank=True,on_delete=models.CASCADE,null=True)
    image=models.ImageField(upload_to='images',null=True,blank=True)
    descriptions=models.TextField(blank=True)
    created_by=models.ForeignKey(User,name='User Name',blank=True,on_delete=models.CASCADE)
    def __str__(self):
       return self.name
    class Meta:
         ordering=['name']

             