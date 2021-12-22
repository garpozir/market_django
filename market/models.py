from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.db import models
from random import randint
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
def random_string():
    return str(randint(10000, 99999))
class mahsool(models.Model):
    name=models.CharField(max_length=100,verbose_name='نام محصول را وارد کنید')
    info=models.TextField(verbose_name='توضیحات محصول را اینجا بنویسید',max_length=2000)
    code=models.CharField(verbose_name='کد محصول توسط سیستم تعیین می شود',default = random_string,primary_key=True, max_length=5)
    amount=models.PositiveIntegerField(verbose_name='قیمت محصول را به تومان وارد کنید', validators=[MaxValueValidator(999999999),MinValueValidator(0)])
    number=models.PositiveIntegerField(verbose_name='تعداد محصول', validators=[MaxValueValidator(999),MinValueValidator(0)])
    ofer=models.PositiveIntegerField(verbose_name='درصد تخفیف',default=str(0), validators=[MaxValueValidator(99),MinValueValidator(0)])
    img=models.ImageField(verbose_name='تصویر محصول را انتخاب کنید',upload_to ='home/')
    data=models.DateTimeField(verbose_name='تاریخ و ساعت زمان ثبت محصول')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name='چه کسی این کار را انجام می دهد')
    def __str__(self):
        return "{}-{}".format(self.name,self.code)

@receiver(pre_delete, sender=mahsool)
def mymodel_delete(sender, instance, **kwargs):
    instance.img.delete(False)
