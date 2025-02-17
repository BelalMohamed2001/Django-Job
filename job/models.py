from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

'''
for 
1 db size
2 html
3 validation
'''

'''
relations indjango
1-one to many (user-posts) forign key 
2-many to many(user-groups) same
3-one to one (user-profile)same
'''
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename,extension=filename.split(".") #%s/%s mean folder and last %s file if %s.%s maen only one file
    return "jobs/%s.%s"%(instance.id,extension)

    

class Job(models.Model):#table
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)#colum
    job_type = models.CharField(max_length=15 , choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1) 
    category=models.ForeignKey('Category',on_delete=models.CASCADE)# if category delete all job in this category deleted
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Job,self).save(*args,**kwargs)#override
    


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    webiste = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name