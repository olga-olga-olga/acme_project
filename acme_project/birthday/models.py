from django.db import models
from django.urls import reverse

from .validators import real_age


class Birthday(models.Model):
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField(
        'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
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
        return self.last_name, self.first_name
    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})
    
