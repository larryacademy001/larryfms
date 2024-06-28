"""
Database Model

Description:
Specify the database table and fields for tracking income
transactions
"""

from django.conf import settings
from django.db import models
from django.shortcuts import reverse

import uuid
import django_filters


# Create your models here.
class ASHPenserIncome(models.Model):
    """
    Setup Income Transaction Model

    Description:
    Sets up database model for recording incomes
    """

    class Meta:
        verbose_name_plural = "IncomesData"
        db_table = "income_transactions"
        ordering = ("income_date", "category", "payer", "payment_method",)

    income_data = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ashpenser_data = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    income_date = models.DateTimeField(max_length=8)
    category = models.CharField(max_length=100, null=True, blank=True)
    payer = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of this object"""

        return f"{self.income_date} - {self.amount}"
    
    def get_absolute_url(self):
        return reverse("apm_incomes:income_detail", kwargs={"pk": self.pk})
    

class ASHPenserIncomeFilter(django_filters.FilterSet):
    """Provide filter capability for Income Data"""

    class Meta:
        model = ASHPenserIncome
        fields = ["income_date", "category", "payment_method", "payer", "amount"]