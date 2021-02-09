from django.db import models

# Create your models here.
class Product(models.Model):
    product_status = (
        ('N',"New"),
        ('T',"Trending"),
        ('X','Excel'),
        )
    category_type = (
        ("Men","Men"),
        ("Women","Women"),
        ("Electronic","Electronic"),
        )

    color = (
        ("RED","RED"),
        ("White","White"),
        ("Yellow","Yellow"),
        ("Black","Black"),
        ("Blue","Blue"),
        )

    Size = (
        ('S',"Small"),
        ('M',"Medium"),
        ("L","Large"),
        )

    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=10,choices=category_type,null=True, blank=True)
    subCategory = models.CharField(max_length=50,null=True, blank=True)
    status = models.CharField(max_length=1,choices= product_status,null=True, blank=True)
    description = models.TextField(null=True,blank = True)
    pcolor = models.CharField(max_length=10,choices=color,blank=True)
    psize = models.CharField(max_length=10,choices=Size,blank=True)
    create_ts = models.DateTimeField(auto_now_add=True)
    pimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.name
