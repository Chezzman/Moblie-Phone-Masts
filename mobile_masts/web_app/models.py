from django.db import models

#Making a class for Mobile masts Property data from the CSV, to potentiall add data downt the line
class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_address_line_1 = models.CharField(max_length=50)
    property_address_line_2 = models.CharField(max_length=50)
    property_address_line_3 = models.CharField(max_length=50)
    property_address_line_4 = models.CharField(max_length=50)
    unit_name = models.CharField(max_length=50)
    tenant_name = models.CharField(max_length=50)
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    lease_years = models.IntegerField()
    current_rent = models.IntegerField()
