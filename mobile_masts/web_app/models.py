from django.db import models
from django_pandas.managers import DataFrameManager

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_address_line_1 = models.CharField(max_length=100)
    property_address_line_2 = models.CharField(max_length=100, blank=True)
    property_address_line_3 = models.CharField(max_length=100, blank=True)
    property_address_line_4 = models.CharField(max_length=100)
    unit_name = models.CharField(max_length=100)
    tenant_name = models.CharField(max_length=100)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    lease_years = models.IntegerField()
    current_rent = models.DecimalField(max_digits=10, decimal_places=2)
    mast_table = DataFrameManager()
