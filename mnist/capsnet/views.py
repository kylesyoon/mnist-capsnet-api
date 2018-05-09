from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from capsnet.models import InputImage
from capsnet.serializers import InputImageSerializer

@csrf_exempt
def predict(request):
	"""
	Get a prediction on the image put image.
	"""
	if request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = InputImageSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			serializer.data['prediction'] = 9
			return JsonResponse(serializer.data, status=201)
		else:
			return JsonResponse(serializer.data, status=400)

@csrf_exempt
def test(request):
	return JsonResponse({'foo': 'bar'}, status=201)
