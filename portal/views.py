from django.shortcuts import render, render_to_response
from django.db.models import Count
import pandas as pd
import numpy as np
from portal.models import Project

def  view_maps(request):
	all_records=Project.objects.all()
	return render(request, 'index.html', {'records': all_records})

def make_pie_and_barcharts(request):
	df = pd.DataFrame(list(Project.objects.all().values('platform', 'country', 'disease')))
	l=df['country']
	f=pd.Series(l).value_counts()

	xdata=['Gut', 'Skin', 'Saliva', 'Vagina', 'Lung', 'Mouth']#
	ydata1=[20,34,56,34,54,67]#f.values
	ydata2=[10,24,46,24,44,57]#f.values
	ydata3=[30,44,56,44,64,77]#f.values

	extra_serie1 = {"tooltip": {"y_start": "", "y_end": " cal"}}
	
	chartdata = {
	'x': xdata, 
	'name1': 'Samples', 'y1': ydata1, 'extra1': extra_serie1,
	'name2': 'Metagenomes',  'y2':ydata2, 'extra1': extra_serie1,
	'name3': 'Amplicons',  'y3':ydata3, 'extra1': extra_serie1,
	}
	charttype = "multiBarChart"
	chartcontainer="multibarchart_container"

	chartdata1 = {
	'x': xdata, 
	'name1': 'Samples', 'y': ydata1, 'extra1': extra_serie1}
	charttype1="pieChart"
	chartcontainer1='piechart_container'

	chartdata2 = {
	'x': xdata, 
	'name1': 'Samples', 'y1': ydata1, 'extra1': extra_serie1,
	'name2': 'Metagenomes',  'y2':ydata2, 'extra1': extra_serie1,
	'name3': 'Amplicons',  'y3':ydata3, 'extra1': extra_serie1,
	}
	charttype2="lineWithFocusChart"
	chartcontainer2="linewithfocuschart_container"

	data = {
	'charttype': charttype,
	'chartdata': chartdata,
	'chartcontainer': chartcontainer,
	'charttype1': charttype1,
	'chartdata1': chartdata1,
	'chartcontainer1': chartcontainer1,
	'charttype2': charttype2,
	'chartdata2': chartdata2,
	'chartcontainer2': chartcontainer2,
	'extra': {
    	'x_is_date': False,
        'x_axis_format': '',
        'tag_script_js': True,
        'jquery_on_ready': False,
        'reduceXTicks': False
    }
	}
	#print(data)
	return render_to_response('charts.html', data)


def make_charts(request):
	l=Project.objects.values('sample_type', 'assay_type').annotate(type_count=Count('sample_type'))
	df=pd.DataFrame(list(l))

	xdata_assay=df['assay_type']
	xdata_platform=df['platform']
	xdata_type=df['sample_type']

	ydata = df['type_count']
	extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}

	chartdata = {
	'y': ydata, 
	'name1': 'Assay', 'x1': xdata_assay, 'extra1': extra_serie,
	'name2': 'Platform',  'x2':xdata_platform, 'extra2': extra_serie,
	'name3': 'Type',  'x3':xdata_type, 'extra3': extra_serie,
	}
	charttype = "multiBarChart"
	chartcontainer="multibarchart_container"

	chartdata1 = {
	'x': xdata_type, 
	'name1': 'Samples', 'y': ydata, 'extra': extra_serie}
	charttype1="pieChart"
	chartcontainer1='piechart_container'


	data = {
	'charttype': charttype,
	'chartdata': chartdata,
	'chartcontainer': chartcontainer,
	'charttype1': charttype1,
	'chartdata1': chartdata1,
	'chartcontainer1': chartcontainer1,
	'extra': {
		'x_is_date': False,
		'x_axis_format': '',
		'tag_script_js': True,
		'jquery_on_ready': False,
		'reduceXTicks': False
    }
	}
	#print(data)
	return render_to_response('charts.html', data)