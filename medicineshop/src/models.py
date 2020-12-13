from django.db import models

# Create your models here.
class Customer(models.Model):
    c_id = models.CharField(max_length=30,unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email


class Insurance(models.Model):
    c_id = models.CharField(max_length=30)
    ins_no = models.IntegerField(unique=True)
    company = models.CharField(max_length=30)
    type_ins = models.CharField(max_length=30)
    percent = models.IntegerField(unique=True)

    def __str__(self):
        return self.ins_no


class Order(models.Model):
    order_id = models.CharField(max_length=30,unique=True)
    c_id = models.CharField(max_length=30)
    ins_no = models.IntegerField()
    m_id=models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.order_id


class Medicine(models.Model):
    m_id=models.CharField(max_length=30,unique=True)
    quantity = models.IntegerField()
    m_type = models.CharField(max_length=30)
    price = models.IntegerField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return self.m_id


class Payment(models.Model):
    p_id=models.CharField(max_length=30,unique=True)
    order_id = models.CharField(max_length=30)
    cost = models.IntegerField()
    disc = models.IntegerField()
    

    def __str__(self):
        return self.p_id

class availability(models.Model):
    m_id=models.CharField(max_length=30,unique=True)
    options = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.m_id
