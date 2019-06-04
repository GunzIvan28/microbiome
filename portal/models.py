from django.db import models
#from django.contrib.gis.db import models
#from django.contrib.gis.db import models as geomodels


class Project(models.Model):
    repository = models.CharField(max_length=200)
    assay_type=models.CharField(max_length=200)
    platform=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    disease=models.CharField(max_length=200)
    body_site=models.CharField(max_length=200)
    instrument=models.CharField(max_length=200)
    log=models.DecimalField(max_digits=9, decimal_places=6)
    lat=models.DecimalField(max_digits=9, decimal_places=6)
    sample_type=models.CharField(max_length=200)
    ethnicity=models.CharField(max_length=200)
    urbanization=models.CharField(max_length=200)
    region=models.CharField(max_length=200)
    target_amplicon=models.CharField(max_length=200)