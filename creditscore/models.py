from django.core.validators import MinValueValidator
from django.db import models

class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    age = models.PositiveBigIntegerField()
    monthly_income = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)])
    black_listed = models.BooleanField(default=False)
    rfc = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, primary_key=True)
    zip = models.PositiveIntegerField(null=True)


class Application(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

