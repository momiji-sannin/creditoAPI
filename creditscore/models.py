from django.core.validators import MinValueValidator
from django.db import models
from uuid import uuid4

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
    id = models.UUIDField(primary_key=True, default=uuid4)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    score = models.PositiveIntegerField(default=300)
    created_at = models.DateTimeField(auto_now_add=True)


class Document(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='documents')

    def __str__(self):
        return self.name