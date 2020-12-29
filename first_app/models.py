from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=(60),null=False)
    email = models.CharField(max_length=(60),null=False,unique=True)
    password = models.CharField(max_length=(60),null=False)
class Products(models.Model):
    name = models.CharField(max_length=60,null=False)
    price = models.EmailField(max_length=60,null=False)
    added_date = models.DateTimeField(auto_now_add=True,null=False)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'media')
    description = models.TextField()
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    class Meta:
        verbose_name='product'
        verbose_name_plural='products'
        def __str__(self):
            return self.name
