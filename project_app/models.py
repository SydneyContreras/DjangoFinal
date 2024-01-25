from django.db import models

# Create your models here.

class appointments(models.Model):
	first_name = models.CharField(max_length=200)
	last_name  = models.CharField(max_length=200)
	email = models.EmailField(max_length=100,blank=True)
	appointment_title = models.CharField(max_length=40)
	appointment_description = models.TextField()
	time_field = models.TimeField(blank=True, null=True)
	date_field = models.DateField(blank=True, null=True)
	phone = models.CharField(max_length=14)


	def __str__(self):
		return self.appointment_title


