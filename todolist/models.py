from django.db import models
import random

alpha = 'abcdefghijklmnopqrstuvwxyz0123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZ.@%()!#$^&*_+=-?<>,[];: '
signs = '0248AbCd1EfGhIjK3lMnOp5QrStUv7WxYzaBc9DeFghiJkLmN6oPqRsTuVwXyZabcdEFGHijKLmnOPqrSTuvWXy'
# Create your models here.

class tasks(models.Model):
    title = models.CharField(default='',blank=True,max_length=250)
    description = models.TextField(default='',null=True)
    deadline = models.DateField(blank = True , default = '2020-05-20')
    complete = models.CharField(max_length=1, default='N')
    identity = models.CharField(max_length=200,default='234',blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.identity = hash(self.title)
        super(tasks,self).save()

def hash(title):
    r=''
    for w in title:
        r += signs[alpha.index(w)]
    return r