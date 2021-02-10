from django.db import models
from all_users.models import User
from product.models import Product 

# Create your models here.
class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
    )
    supplier = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="supplier")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name="buyer")
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    units = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name
