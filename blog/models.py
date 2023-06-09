from django.db import models


LEVEL_CHOICES = [
    ('1','1'),#нормально
    ('2','2'),#не опасный
    ('3','3'),#умеренный
    ('4','4'),#опасный
    ('5','5'),#очень опасный
]


class ComentModel(models.Model):
    title = models.CharField(max_length=100,verbose_name='Заголовок')
    message = models.ForeignKey('MessageModel',on_delete=models.CASCADE,verbose_name='Сообщение')
    # user = models.ForeignKey('User',on_delete=)
    description = models.TextField(verbose_name='Описание')
    datetime = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True,verbose_name='is like or dislike')


class MessageModel(models.Model):

    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to ='media/%Y/%m/%d',verbose_name='Изображение')
    category = models.ForeignKey('CategoryModel',on_delete = models.CASCADE ,verbose_name='Категория')
    created_at = models.DateField(auto_now=True,verbose_name='Дата заявки')
    is_renovated = models.BooleanField(default=False,verbose_name='Отремонтирован')   #Отремонтирована или нет
    choices = models.CharField(
        max_length=1,
        choices = LEVEL_CHOICES,
        default = '1',
        verbose_name='Уровень угрозы'        
        )
    quantity = models.IntegerField(verbose_name='количество')#    ???????

    def __str__(self) -> str:
        return self.description

class CategoryModel(models.Model):
    name = models.CharField(max_length=100,verbose_name='наименовоание')
    slug = models.SlugField(max_length=100,verbose_name='Slug')