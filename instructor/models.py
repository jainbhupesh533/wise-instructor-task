# models.py

from django.contrib.auth.models import User
from django.db import models


class Instructor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# Add any other relevant fields for the instructor


class CheckInOut(models.Model):
	CHECK_IN = 'IN'
	CHECK_OUT = 'OUT'
	CHECK_TYPE_CHOICES = [
		(CHECK_IN, 'Check In'),
		(CHECK_OUT, 'Check Out'),
	]

	instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='check_ins_outs')
	check_time = models.DateTimeField()
	check_type = models.CharField(max_length=3, choices=CHECK_TYPE_CHOICES)

	def __str__(self):
		return f"{self.instructor.user.username} - {self.check_type} - {self.check_time}"