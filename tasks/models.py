from django.contrib.auth.models import User
from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class Task(models.Model):
    class Priority(DjangoChoices):
        high = ChoiceItem(0, 'Высокий')
        medium = ChoiceItem(1, 'Средний')
        low = ChoiceItem(2, 'Низкий')

    class Status(DjangoChoices):
        todo = ChoiceItem(0, 'План')
        in_progress = ChoiceItem(0, 'В процессе')
        done = ChoiceItem(0, 'Готово')

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    priority = models.PositiveSmallIntegerField(choices=Priority.choices, verbose_name='Приоритет')
    estimation = models.DurationField(verbose_name='Планируемое время')
    spent_time = models.DurationField(verbose_name='Затраченное время', default='00:00:00')
    status = models.PositiveSmallIntegerField(choices=Status.choices, verbose_name='Статус', default=Status.todo)
    user = models.ForeignKey(User, models.PROTECT, verbose_name='Создатель')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
