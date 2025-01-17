from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from .validators import real_age


User = get_user_model()


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
    )
    author = models.ForeignKey(
        User, verbose_name='Автор записи', on_delete=models.CASCADE, null=True
    )
    birthday = models.DateField('Дата рождения', validators=(real_age,))
    image = models.ImageField('Фото', upload_to='birthdays_images', blank=True)

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constraint',
            ),
        )
        verbose_name = 'день рождения'
        verbose_name_plural = 'Дни рождения'

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})
