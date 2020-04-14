from django.db import models


# Create your models here.
class curr(models.Model):
    pid = models.IntegerField(default=0)
    sid = models.IntegerField(default=0)

class Customer(models.Model):
    cust_id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    c_address = models.CharField(max_length=50, default='Not provided')
    number = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


class owner(models.Model):
    owner_id = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(max_length=30)
    number = models.CharField(max_length=10)
    DOB = models.DateField()
    gender = models.CharField(max_length=10)
    b_address = models.CharField(max_length=50, default='Not provided')
    first_name = models.CharField(max_length=30, default='not provided')
    second_name = models.CharField(max_length=30, default='not provided')


class property(models.Model):
    prop_id = models.IntegerField(primary_key=True)
    ptype = models.IntegerField()
    pname = models.CharField(max_length=50, default="None")
    pstatus = models.BooleanField(default='True')
    price = models.IntegerField()
    p_address = models.CharField(max_length=50)
    owner_id = models.CharField(max_length=50)
    floor = models.IntegerField()
    p_age = models.IntegerField()
    size = models.IntegerField()
    area = models.CharField(max_length=10, default="")
    image = models.ImageField(upload_to='', default="")


class sales(models.Model):
    cust_id = models.CharField(max_length=50)
    owner_id = models.CharField(max_length=50)
    prop_id = models.IntegerField()
    price = models.IntegerField()
    sid = models.IntegerField(primary_key=True)


class requirement(models.Model):
    cust_id = models.CharField(max_length=50)
    rid = models.IntegerField(primary_key=True)
    floor = models.IntegerField()
    p_age = models.IntegerField()
    size = models.IntegerField()
    area = models.CharField(max_length=10)
    ptype = models.IntegerField()
    price = models.IntegerField()
