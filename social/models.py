from django.contrib.auth import get_user_model
from django.db import models


SOCIAL_NETWORK_CHOICES = [
        ('VK', 'VK'),
        ('Telegram', 'Telegram'),
        ('YouTube', 'YouTube'),
        ('Twitter', 'Twitter'),
        ('Instagram', 'Instagram'),
        ('Facebook', 'Facebook'),
        ('GitHub', 'GitHub'),
    ]


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', choices=SOCIAL_NETWORK_CHOICES)
    link = models.CharField(max_length=255, verbose_name='Ссылка')
    user = models.ForeignKey(get_user_model(), related_name='social_networks', 
                             on_delete=models.CASCADE, verbose_name='Владелец')
    date_create = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name

