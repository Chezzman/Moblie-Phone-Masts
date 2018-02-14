from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Property
from .form import property_form
import pandas as pd
import numpy as np

data_csv = "D:\MAIN\CODE\Mobile_Phone_Masts_Data\Moblie-Phone-Masts\mobile_masts\mobile_phone_masts.csv"

def table(request):
    df = pd.read_csv(data_csv)
    template = 'stats/index.html'
    html = df.sort_values(by='Current Rent', ascending=True).to_html(classes=['table'])
    return render(request, template, {'html' : html})

#needs to be intergrated with the forms page, model, and csv(hopefully just model and csv)
def create(request):
    template = 'stats/create.html'
    if request.method == 'POST':
        form = property_form(request.POST)
        if form.is_valid():
            text = form.cleaned_data['property_form']
            form.save()#to_csv(data_csv)
            return redirect('stats:index')
        create_property = {'form':form, 'text':text}
    else:
        return HttpResponseNotFound('<h2>Data not save, please try again or make sure all information is correct</h2>')
    return render(request, template, create_property)


    #
    # form = property_form(request.POST)
    # if form.is_valid():
    #     post = form.save(commit=False)
    #     post.save()
    #     text - form.cleaned_data['post']
    #     form = property_form()
    #     return redirect('stats:index')
    # create_property = {'form':form, 'text':text}
    # return render(request, template, create_property)

    # data = pd.to_csv(path_or_buf="data_csv")
    # if correct data get pushed here change to csv and push to datase
    #return render(request, 'stats/create.html')

#needs a toggle
def table_five(request):
    top_five = pd.read_csv(data_csv).head(5).to_html(classes=['table'])
    template = 'stats/table_five.html'
    return render(request, template, {'top_five': top_five})

def date_list(request):
    df = pd.read_csv(data_csv)
    df = pd.Series(df['Lease Start Date'])
    df = pd.period_range(start='1999-06-01', end='2007-08-31', freq='M')
    # date_table = df.to_html(classes=['table'])

    template = 'stats/date_list.html'
    return render(request, template, {'df' : df})


def total_rent(request):
    df = pd.read_csv(data_csv)
    df.loc['Total Rent'] = pd.Series(df['Current Rent'].sum(), index=['Current Rent'])
    total = df.to_html(classes=['table'])
    template = 'stats/total_rent.html'
    return render(request, template, {'total' : total})

#DICTIONARY
