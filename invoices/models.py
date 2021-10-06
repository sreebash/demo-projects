from django.db import models


class Invoice(models.Model):
    invoice_no = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    price = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    unpaid = models.BooleanField(default=False)
    due = models.CharField(max_length=200)

    def __str__(self):
        return self.invoice_no


