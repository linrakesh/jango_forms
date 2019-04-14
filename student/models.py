from django.db import models
from django.urls import reverse
from django.template.defaultfilters import mark_safe

# Create your models here.
class candidate(models.Model):
    GENDER = (
                ('M','Male'),
                ('F','Female')
            )
    SECTION = (
                ('A' ,'I'),
                ('B','II'),
                ('C', 'III'),
                ('D','IV')
            )

    admno   = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    dob   = models.DateField()
    gender  = models.CharField(max_length=6, choices = GENDER)
    phone   = models.CharField(max_length=10)
    std  =  models.CharField(max_length= 1, choices = SECTION)
    section = models.CharField(max_length=15)
    photo   = models.ImageField()
    active = models.BooleanField()

    class Meta:
        ordering = ['admno']
        verbose_name = "candidate"
        verbose_name_plural = "candidates"
      

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student-detail", kwargs={"pk": self.pk})
