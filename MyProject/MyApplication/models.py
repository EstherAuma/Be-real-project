
'''
-A model is a description of physical database table ie
-A model is a table.
-Relational database is adatabase that stores data in a tabular format.
-A database is a collection oftables.
'''
#we are accessing django user model.
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
#shows the current time of yoour system.
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.


# class UserProfile(AbstractUser):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(blank=True)

#     def __str__(self): 
#         return self.username
#         db_table = 'spare_users'
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
    

#Here the table is called Category.
class Category(models.Model):
    #accepts both
    name = models.CharField(max_length = 50,null = False, blank = False)
   #This function classifies how it will be referred to by other classes.
    def __str__(self):
        return self.name
    
class Product(models.Model):
    #referencing the category of the product
    #showing the relationship
    Category_name = models.ForeignKey(Category, on_delete = models.CASCADE, null = False, blank = False)
    #When we delete any category, it will go with all its products.

    item_name = models.CharField(max_length = 50,null = False,blank = False)
    #reserved for date of arrival field
    country_of_origin =models.CharField(max_length = 50,null = False,blank = False) 
    total_quantity= models.IntegerField(default = 0, null=False, blank = False, validators=[MinValueValidator(1)])
    issued_quantity = models.IntegerField(default = 0, null=False, blank = False)
    recieved_quantity = models.IntegerField(default = 0, null = False, blank = False)
    unit_price = models.IntegerField(default = 0, null = False, blank = False)


    def __str__(self):
        return self.item_name
    

class Sale(models.Model):
    #on_delete should only be used on a foreign key.
    item = models.ForeignKey(Product, on_delete =models.CASCADE, null=False,blank=False)
    quantity = models.IntegerField(default =0, null=False,blank=False)
    amount_recieved = models.IntegerField(default =0, null=False, blank=False)
    issued_to = models.CharField(max_length=50, null=False, blank=False)
    unit_price = models.IntegerField(default =0, null=False, blank=False)
    branch_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=50, null=False, blank=False)

    def get_total(self):
        total = self.quantity*self.item.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() - self.amount_recieved
        #abs is absolute value
        return abs(int(change))
    
    def __str__(self):
        return self.item.item_name

