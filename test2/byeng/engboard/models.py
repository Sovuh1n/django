from django.db import models
from django.core import validators
class Bb1(models.Model):
    class Kinds(models.TextChoices):
        BUY = 'b', 'Куплю'
        SELL = 's', 'Продам'
        EXCHANGE = 'c', 'Обменяю'
        RENT = 'r'
        __empty__ = 'Выберите тип публикации'

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-published']

class Apprentice(models.Model):
    name = models.CharField(max_length=24, verbose_name='Имя', validators=[validators.MinLengthValidator(2)],
                            error_messages={'invalid': 'Нахуй пшёл'})
    sName = models.CharField(max_length=24, verbose_name='Фамилия', db_index=True, validators=[validators.MinLengthValidator(2)],
                             error_messages={'invalid': 'Нахуй пшёл'})
    pNumber = models.CharField(max_length=24, verbose_name='Номер телефона', db_index=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлен')
    email = models.EmailField(verbose_name='Электронная почта', null=True, validators=[validators.EmailValidator()])
    lvl = models.CharField(max_length=24, verbose_name='Уровень языка', null=True)
    active = models.BooleanField(verbose_name='Активен', null=True)
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.PROTECT, verbose_name='Учитель')

    class Meta:
        verbose_name_plural = 'Ученики'
        verbose_name = 'Ученик'
        ordering = ['name']

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/engboard/%s/" % self.pk

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']

class Teacher(models.Model):
    name = models.CharField(max_length=24, verbose_name='Имя', validators=[validators.MinLengthValidator(2)],
                            error_messages={'invalid': 'Нахуй пшёл'})
    sName = models.CharField(max_length=24, verbose_name='Фамилия', db_index=True, validators=[validators.MinLengthValidator(2)],
                             error_messages={'invalid': 'Нахуй пшёл'})
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Добавлен')
    email = models.EmailField(verbose_name='Электронная почта', validators=[validators.EmailValidator()])
    pNumber = models.CharField(max_length=24, verbose_name='Номер телефона')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/engboard/%s/" % self.pk

    class Meta:
        verbose_name_plural = 'Учителя'
        verbose_name = 'Учитель'
        ordering = ['name']