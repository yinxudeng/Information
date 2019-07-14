from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.exceptions import ValidationError

from django.utils import timezone

def age_limiter(value):
	if value > 150 or value < 0:
		raise ValidationError(
			("The person's age needs to be from 0 to 150."),
			params = {'value': value},
		)

# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 30)
	age = models.IntegerField(validators=[age_limiter])
	city = models.CharField(max_length = 30)
	province = models.CharField(max_length = 30)
	phone = models.CharField(max_length = 11, unique = True)
	timestamp_added = models.DateTimeField(auto_now_add = True)
	timestamp_lastupdated = models.DateTimeField(auto_now = True)
	objects = models.Manager()
	def __str__(self):
		return "%s, %d, %s (%s, %s)" % (self.name, self.age, self.phone, self.city, self.province)