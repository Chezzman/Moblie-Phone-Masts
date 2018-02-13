from django.http import HttpResponse
from django.shortcuts import render
from .models import Property
import pandas as pd
import numpy as np

data_csv = "D:\MAIN\CODE\Mobile_Phone_Masts_Data\Moblie-Phone-Masts\mobile_masts\mobile_phone_masts.csv"
#  def index(request):
    # all_property = Property.objects.all()
#      return render(request, 'stats/index.html', {'all_property': all_property})


#needs to be intergrated with the forms page, model, and csv(hopefully just model and csv)
#def create(request):
    #create_property = Property.objects.get()
    #data = pd.to_csv(path_or_buf="data_csv")
    #if correct data get pushed here change to csv and push to datase
    #return render(request, 'stats/create.html')

# needs template/endpoint ITS CALLED TABLE_FIVE
def create(request):
    df = pd.read_csv(data_csv).head(5).to_html(classes=['table'])
    template = 'stats/table_five.html'
    return render(request, template, {'df': df})

def table(request):
    df = pd.read_csv(data_csv)
    template = 'stats/index.html'
    html = df.sort_values(by='Current Rent', ascending=True).to_html(classes=['table'])
    return render(request, template, {'html' : html})

# needs template/endpoint/test parse
# def date_list(request):
#     prng = pd.read_csv(data_csv).period_range(start='1999-06-01', end='2007-08-31', freq='M').to_html(classes=['table'])
#     template = 'stats/date_list.html'
#     return render(request, template, )

#needs
def total_rent(request):
    df = pd.read_csv(data_csv)
    df.loc['Total Rent'] = pd.Series(df['Current Rent'].sum(), index=['Current Rent'])
    total = df.to_html(classes=['table'])
    template = 'stats/total_rent.html'
    return render(request, template, {'total' : total})
