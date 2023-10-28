from django.http import JsonResponse
from mindsdb import Predictor

def predict_condition(request):
    if request.method == "POST":
        image = request.FILES['image']
        # Save the image temporarily or process it as required
        prediction = Predictor(name='skincare_predictor').predict(when={'image': image.path})
        condition = prediction[0]['condition']
        return JsonResponse({'condition': condition}, status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

