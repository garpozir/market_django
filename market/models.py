from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.db import models
from random import randint

class mahsool(models.Model):
    name=models.CharField(max_length=100,verbose_name='نام محصول را وارد کنید')
    info=models.TextField(verbose_name='توضیحات محصول را اینجا بنویسید',max_length=2000)
    rnd_code=randint(10000,99999)
    code=models.PositiveIntegerField(verbose_name='کد محصول توسط سیستم تعیین می شود',default=str(rnd_code),primary_key=True, validators=[MaxValueValidator(99999),MinValueValidator(10000)])
    amount=models.PositiveIntegerField(verbose_name='قیمت محصول را به تومان وارد کنید', validators=[MaxValueValidator(999999999),MinValueValidator(0)])
    img=models.ImageField(verbose_name='تصویر محصول را انتخاب کنید',upload_to ='uploads/')
    data=models.DateTimeField(verbose_name='تاریخ و ساعت زمان ثبت محصول')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='چه کسی این کار را انجام می دهد')
    def __str__(self):
        return "{}-{}".format(self.name,self.code)
