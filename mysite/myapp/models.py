from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# Create your models here.
class laptop(models.Model):
    lap_name=models.CharField(max_length=20,blank=True)
    class Meta:
        ordering=['lap_name']

    def __str__(self):
        return "%s " % (self.lap_name)

class employee(models.Model):
    firstname=models.CharField(max_length=20,blank=True)
    lastname=models.CharField(max_length=20,blank=True)
    lap=models.OneToOneField(laptop,on_delete=models.CASCADE)
    class Meta:
        ordering=['firstname']

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)

class company(models.Model):
    company_name=models.CharField(max_length=100,blank=True)
    emp=models.ForeignKey(employee,on_delete=models.CASCADE)
    class Meta:
        ordering =['company_name']

    def __str__(self):
        return "%s " % (self.company_name)


