from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from io import BufferedWriter, FileIO
import keras
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from capsnet.capsulenet import CapsNet


@csrf_exempt
def predict(request):
	"""
	Get a prediction on the image put image.
	"""
	if request.method == 'POST':
		# reset keras session
		keras.backend.clear_session()

		# get the image file
		img = request.FILES['predict_image']
		with BufferedWriter(FileIO('tmp.jpg', 'w')) as tmp_img:
			for chunk in img.chunks():
				tmp_img.write(chunk)

		# read file as black and white
		img = imread('./tmp.jpg')[:,:,:1] / 255.0
		img = np.expand_dims(img, axis=0)
		# make sure the image shape is right
		assert img.shape == (1, 28, 28, 1)

		# load model
		_, model, _ = CapsNet(input=(28, 28, 1), n_class=10, routings=3)
		model.load_weights('./capsnet/trained_model.h5')

		# predict
		predictions, _ = model.predict(img, batch_size=100)
		prediction = predictions[0]
		prediction_number = np.argmax(prediction)

		return JsonResponse({'prediction': np.asscalar(argmax)}, status=200)
