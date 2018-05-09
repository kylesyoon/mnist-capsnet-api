from rest_framework import serializers
from capsnet.models import InputImage


class InputImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = InputImage
		fields = ('id', 'input_image', 'prediction')
	