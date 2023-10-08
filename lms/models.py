from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Well(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью', **NULLABLE)
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='урок', **NULLABLE,
                             related_name='lessons')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payments(models.Model):
    CASH = 'cash'
    TRANSFER = 'transfer'

    payment_method_choices = (
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    )

    users = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь',
        related_name='user'
    )
    well = models.ForeignKey(Well, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE, related_name='well')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, **NULLABLE, verbose_name='урок', related_name='lesson')
    date_payment = models.DateTimeField(auto_now=True, verbose_name='дата оплаты')
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=20, choices=payment_method_choices)

    def __str__(self):
        return f'{self.users} - {self.well if self.well else self.lesson} ({self.amount})'

    class Meta:
        verbose_name = 'оплата'
        verbose_name_plural = 'оплата'
