from django.db import models


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=30)
    choices = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]
    status = models.CharField(choices=choices, max_length=20)
    due = models.PositiveBigIntegerField(max_length=200)

    def __str__(self):
        return self.invoice_no
