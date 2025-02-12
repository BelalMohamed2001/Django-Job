from django.db import models

# Create your models here.

'''
for 
1 db size
2 html
3 validation
'''
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):#table
    title = models.CharField(max_length=100)#colum
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
  
    def __str__(self):
        return self.title