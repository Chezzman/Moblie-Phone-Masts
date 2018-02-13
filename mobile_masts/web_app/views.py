from django.http import HttpResponse
from django.shortcuts import render
from .models import Property
import pandas as pd
import numpy as np


#  def index(request):
    # all_property = Property.objects.all()
#      return render(request, 'stats/index.html', {'all_property': all_property})
#
# def create(request):
#     return render(request, 'stats/create.html', {'data_table': data_table})

def table(request):
    #qs = Property.mast_table.all()
    df = pd.read_csv("D:\MAIN\CODE\Mobile_Phone_Masts_Data\Moblie-Phone-Masts\mobile_masts\mobile_phone_masts.csv")
    template = 'stats/index.html'
    #
    html = df.to_html()
    # ascending_rent = df.sort_values(by='Current Rent')    #html = df.to_html()
    # context = {
    #     'html': html,
    #     'ascending_rent': ascending_rent
     #}

    return render(request, template, {'html' : html})


# Parses the dataframe into an HTML element with 3 Bootstrap classes assigned.
# html = df.to_html(classes=["table-bordered", "table-striped", "table-hover"])
