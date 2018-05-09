from django.conf.urls import url
from capsnet import views

urlpatterns = [
	url(r'^capsnet/predict/$', views.predict),
]
