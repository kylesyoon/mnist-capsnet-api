from django.db import models


class InputImage(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	input_image = models.ImageField()
	prediction = models.CharField(max_length=1, blank=True)
