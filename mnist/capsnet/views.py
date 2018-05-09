from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from capsnet.models import InputImage
from capsnet.serializers import InputImageSerializer

# Create your views here.
