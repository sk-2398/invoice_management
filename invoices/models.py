from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)
