import datetime
from platform import release
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField("el nombre de la persona",max_length=20)
    last_name = models.CharField("el apellido de la persona",max_length=20)
    cars = models.ManyToManyField('Car',verbose_name="Los carro del usuario")
    
    def __str__(self):
        return self.first_name
    
STATUS_CHOICE = (
    ('R','Reviewed'),
    ('N','Not Reviewed'),
    ('E','Error'),
    ('A','Accepted')
)

class WebSite(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    release_date = models.DateField()
    status = models.CharField(choices=STATUS_CHOICE,max_length=1)
    rating = models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE) 
    
    def was_released_last_week(self):
        if self.release_date < datetime.date.today() :
            return "Released before last week"
        else:
            return "Released last week"
        
    @property
    def get_full_name(self):
        return f"Este es el nombre completo del sitio web: {self.name}"
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/websites/{self.url}"
    
    def save(self,*args,**kwargs):
        print("Guardando")
        super().save(*args,**kwargs)
    
class Car(models.Model):
    name = models.CharField(max_length=40,primary_key=True)