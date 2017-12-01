from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('course_detail', args=(self.id,))

class Section(models.Model):
    pass
