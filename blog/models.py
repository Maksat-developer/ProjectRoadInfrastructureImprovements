from django.db import models


LEVEL_CHOICES = (
    ('1','нормально')
    ('2','не опасный')
    ('3','умеренный')
    ('4','опасный')
    ('5','очень опасный')
)


class MessageModel(models.Model):

    description = models.TextField(max_length=250,verbose_name='Описание')
    image = models.ImageField(upload_to ='media/%Y/%m/%d',verbose_name='Изображение')
    category = models.ForeignKey('Category',max_length=100,on_delete = models.CASCADE ,verbose_name='Категория')
    created_at = models.DateField(auto_now=True,verbose_name='Дата заявки')
    is_renovated = models.BooleanField(default=False,verbose_name='Отремонтирован')   #Отремонтирована или нет
    choices = models.CharField(
        max_length=5,
        choices = LEVEL_CHOICES,
         default = '1'        
        )
    quantity = models.IntegerField(verbose_name='')#    ??????
    