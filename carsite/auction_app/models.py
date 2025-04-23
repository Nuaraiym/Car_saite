
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('seller','seller'),
        ('buyer','buyer')
    )
    role = models.CharField(choices=ROLE_CHOICES,max_length=100)
    phone_number = PhoneNumberField(null=True,blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.brand_name}'

class CarModel(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return f'{self.brand}, {self.car_model}'

class Car(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    year = models.CharField()
    FUEL_CHOICES = (
        ('бензин','бензин'),
        ('газ','газ'),
        ('дизель','дизель'),
        ('электро','электро'),
    )
    fuel_type = models.CharField(choices=FUEL_CHOICES,max_length=30)
    CAR_TYPE = (
            ('automat','automat'),
            ('mehanica','mehanica'),
        )
    transmission = models.CharField(choices=CAR_TYPE,max_length=32)
    mileage = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()
    images = models.ImageField(upload_to='images/')
    seller = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.car_model}'

class Auction(models.Model):
    car = models.OneToOneField(Car,on_delete=models.CASCADE,related_name='cars')
    start_price = models.PositiveIntegerField(default=0)
    min_price = models.SmallIntegerField(null=True,blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    STATUS_CHOICES = (
        ('активен','активен'),
        ('завершен','завершен'),
        ('отменен','отменен')
    )
    status = models.CharField(choices=STATUS_CHOICES,max_length=32)

    def __str__(self):
        return f'{self.status} {self.car} {self.start_price} {self.start_time}'


class Bid(models.Model):
    auction = models.ForeignKey(Auction,on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.auction} {self.buyer}'

class Feedback(models.Model):
    seller = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='seller')
    buyer = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='bayer')
    rating = models.IntegerField(choices=[(i, str(i))for i in range(1,6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.seller} {self.buyer}'




