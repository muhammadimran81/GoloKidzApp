from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=120, unique=True)

class Meta:
    ordering = ['name']

def __str__(self):
    return self.name


SIZES = [
("NB", "Newborn"),
("3M", "3 Months"), ("6M", "6 Months"), ("9M", "9 Months"),
("12M", "12 Months"), ("18M", "18 Months"), ("24M", "24 Months"),
("2T", "2T"), ("3T", "3T"), ("4T", "4T"), ("5T", "5T"),
("6", "Age 6"), ("7", "Age 7"), ("8", "Age 8"), ("9", "Age 9"),
("10", "Age 10"), ("12", "Age 12"), ("14", "Age 14"),
]


GENDERS = [
("boys", "Boys"),
("girls", "Girls"),
]

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10, choices=GENDERS, default='unisex')
    size = models.CharField(max_length=10, choices=SIZES, blank=True)
    brand = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Meta:
    ordering = ['-created_at']


def __str__(self):
    return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
     ordering = ['-created_at']

def __str__(self):
     return f"{self.subject} by {self.name}"