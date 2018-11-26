from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator

class OrderForm(models.Model):
    flavor = models.CharField(max_length=200)
    product_id = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    total_cost = models.IntegerField(default=0)
    current_date = models.DateTimeField('current date',auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def was_ordered_recently(self):
        return self.current_date >= timezone.now() - datetime.timedelta


class Choice(models.Model):
    question = models.ForeignKey(OrderForm, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=25)
    last_Name = models.CharField(max_length=25)
    street_Address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, validators=[RegexValidator('.{2}$')])
    zip_Code = models.CharField(max_length=5, validators=[RegexValidator('^\d{5}$')])

    def __str__(self):
        return '%s %s %s' % (str(self.customer_id).zfill(6), self.first_Name, self.last_Name)

#货物信息表
class ProductForm(models.Model):
    #产品号我建议使用Char类型
    product_id=models.CharField(max_length=50)
    #单价
    price=models.FloatField(default=0.0)
    #剩余数量
    numbers=models.IntegerField(default=0)
    #产品名称
    pname=models.CharField(max_length=20)
    #产地
    parea=models.CharField(max_length=20)