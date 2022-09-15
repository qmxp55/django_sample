from django.db import models


class CAR(models.Model):
    model_name = models.CharField(max_length=264, unique=True)
    model_year = models.IntegerField()
    mileage = models.IntegerField()


class CUSTOMER(models.Model):
    name = models.CharField(max_length=264)
    middle = models.CharField(max_length=264)
    last = models.CharField(max_length=264)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=264, unique=True)


class BOOKINGS(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.IntegerField()
    customer = models.ForeignKey(CUSTOMER, on_delete=models.CASCADE)
    car = models.ForeignKey(CAR, on_delete=models.CASCADE)
