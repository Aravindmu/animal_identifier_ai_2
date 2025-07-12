from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
from .tensorflow_model import predict_animal

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_instance = form.save()
            img_path = img_instance.image.path ##Getting Image Path "image.path" like "uploads/image.jpg"
            animal_name = predict_animal(img_path) ##predicting which animal is this.
            return render(request, 'identifier/result.html', {'animal': animal_name, 'image': img_instance})
    else:
        form = ImageUploadForm()
    
    return render(request, 'identifier/upload.html', {'form': form})
