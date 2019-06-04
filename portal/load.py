import pandas as pd
from .models import Project				

def update_project_data():
    df = pd.read_csv("microbiome/microbiome.csv") #need to specify path of the data accordingly
    #print(df)
    for index, row in df.iterrows():
        #print(row)
        Project.objects.update_or_create(
        repository=row['REPOSITORY_ID'],
	assay_type=row['ASSAY_TYPE'],
	platform=row['PLATFORM'],
	country=row['COUNTRY'],
	disease=row['DISEASE'],
	body_site=row['BODY_SITE'],
	instrument=row['INSTRUMENT'],
	log=row['LON'],
	lat=row['LAT'],
	sample_type=row['SAMPLE_TYPE'],
	ethnicity=row['ETHNICITY'],
	urbanization=row['URBANIZATION'],
	region=row['REGION']
	    )
