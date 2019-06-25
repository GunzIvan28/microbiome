from django.shortcuts import render, render_to_response
from django.db.models import Count
import pandas as pd
import numpy as np
from portal.models import Project

def  view_maps(request):
	records=Project.objects.all()
	return render(request, 'index.html', {'records': records})

def dashboard_charts(request):
	all_records=Project.objects.all()

	site_pie_dict = [{'name': item['body_site'], 'y': item['type_count'] } for item in all_records.values('body_site').annotate(type_count=Count('body_site')) ]

	platform_pie_dict = [{'name': item['platform'], 'y': item['type_count'] } for item in all_records.values('platform').annotate(type_count=Count('sample_type')) ]
	
	assay_type=pd.DataFrame(list(all_records.values('assay_type').annotate(type_count=Count('sample_type'))))
	xdata_assay=list(assay_type['assay_type'])
	ydata_assay=list(assay_type['type_count'])

	disease=pd.DataFrame(list(all_records.values('disease').annotate(type_count=Count('disease'))))
	xdata_disease=list(disease['disease'])
	ydata_disease=list(disease['type_count'])

	context={'xdata_assay': xdata_assay, 
		'ydata_assay': ydata_assay,
		'xdata_disease': xdata_disease, 
		'ydata_disease': ydata_disease, 
		'platform_pie_dict': platform_pie_dict, 
		'site_pie_dict': site_pie_dict, 
		'all_records': all_records};
		
	return render(request, 'dashboard.html', context=context)