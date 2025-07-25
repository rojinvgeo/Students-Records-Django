from django.db import models

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    GUARDIAN_CHOICES = [
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('other', 'Other'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    batch = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    address = models.TextField()
    guardian = models.CharField(max_length=6, choices=GUARDIAN_CHOICES)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} (ID: {self.student_id})"
