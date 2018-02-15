from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Property
from .form import Property_Form
import pandas as pd
import numpy as np

data_csv = "D:\MAIN\CODE\Mobile_Phone_Masts_Data\Moblie-Phone-Masts\mobile_masts\mobile_phone_masts.csv"

def table(request):
    df = pd.read_csv(data_csv).replace(np.nan, '', regex=True)
    template = 'stats/index.html'
    html = df.sort_values(by='Current Rent', ascending=True).to_html(classes=['table'], index=False)
    return render(request, template, {'html' : html})

#needs to be intergrated with the csv
def create(request):
    template = 'stats/create.html'
    if request.method == 'POST':
        form = Property_Form(request.POST)
        if form.is_valid():
            text = form.cleaned_data['property_form']#this is not being registered
            form = df.to_csv(file_name, encoding='utf-8', index=False)
            form.save()#to_csv(data_csv)
            return redirect('stats:index')

    else:
         form = Property_Form
    return render(request, template, {'form':form})

#needs a toggle
def table_five(request):
    top_five = pd.read_csv(data_csv).replace(np.nan, '', regex=True).head(5).to_html(classes=['table'], index=False)
    template = 'stats/table_five.html'
    return render(request, template, {'top_five': top_five})

def date_list(request):
    df = pd.read_csv(data_csv).replace(np.nan, '', regex=True)
    df = df.loc['1999-06-01' : '2007-08-31']
    #df = pd.Series(df['Lease Start Date'])
    #df = pd.period_range(start='1999-06-01', end='2007-08-31', freq='M')
    df = df.to_html(classes=['table'], index=False)

    template = 'stats/date_list.html'
    return render(request, template, {'df' : df})


def total_rent(request):
    df = pd.read_csv(data_csv)
    df.loc['Total Rent'] = pd.Series(df['Current Rent'].sum(), index=['Current Rent'])
    total = df.replace(np.nan, '', regex=True).to_html(classes=['table'], index=False)
    template = 'stats/total_rent.html'
    return render(request, template, {'total' : total})

#DICTIONARY
def dictionary(request):
    df = pd.read_csv(data_csv)
    df = pd.pivot_table(df,index=["Tenant Name", "Property Name"])
    #df = df.loc['Everything Everywhere', ' Hutchinson', 'O2', 'Vodafone', 'Cornerstone', 'Arqiva']
    table = df.replace(np.nan, '', regex=True).to_html(classes=['table'])
    template = 'stats/dictionary.html'
    return render(request, template, {'table' : table})
