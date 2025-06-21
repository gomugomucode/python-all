from django.db import models

class Contact(models.Model):  # Class names should be PascalCase by convention
    SUBJECT_CHOICES = [
        ('General Inquiry', 'General Inquiry'),
        ('Order Information', 'Order Information'),
        ('Catering Services', 'Catering Services'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    sub = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    msg = models.TextField()
    date = models.DateField(auto_now_add=True)  # Optional: auto set on create

    def __str__(self):
        return f"{self.name} - {self.sub}"
