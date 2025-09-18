from django.db import models
from django_jalali.db import models as jmodels
import jdatetime


class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    username = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    national_code = models.CharField(max_length=10)
    birthday_date = jmodels.jDateField()
    ceremony_datetime = jmodels.jDateTimeField()
    country = models.CharField(max_length=50, default='Iran')

    def get_first_and_last_name(self):
        first_name, last_name = self.full_name.split(" ")
        return {'first_name': first_name, 'last_name': last_name}

    def get_age(self):
        today = jdatetime.date.today()
        age = today.year - self.birthday_date.year
        if (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day):
            age -= 1
        return age

    def is_birthday(self):
        today = jdatetime.date.today()
        return (today.month, today.day) == (self.birthday_date.month, self.birthday_date.day)

    def __str__(self):
        return self.username
