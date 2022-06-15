from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
import tensorflow as tf
import time
# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def model_classification(request):
    img=request.FILES['img']
    model=tf.keras.models.load_model('recycle.h5')
    labels = ['can', 'glass', 'paper', 'pet', 'plastic', 'vinyl']
    img_tensor = tf.image.decode_image(img.read())
    img_resized = tf.image.resize(img_tensor, [160, 160])
    img_final = tf.expand_dims(img_resized, 0)

    y_probs = model.predict(img_final[:,:,:,:3])
    y_label = y_probs.argmax(axis=-1)

    label = labels[y_label[0]]
    percentage = format(y_probs.max() * 100, '.1f')
    data={"label":label,"percentage":percentage}
    return JsonResponse(data)
