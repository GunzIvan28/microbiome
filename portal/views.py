from django.shortcuts import render, render_to_response
from django.db.models import Count
import pandas as pd
import numpy as np
from portal.models import Project

def  view_maps(request):
	all_records=Project.objects.all()
	return render(request, 'index.html', {'records': all_records})
