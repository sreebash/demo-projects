from django.db import models


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=30, unique=True)
    choices = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    status = models.CharField(choices=choices, max_length=20)
    due = models.PositiveBigIntegerField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_no
