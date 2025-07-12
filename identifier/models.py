from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):    ##a human-readable representation of the object when it’s printed or displayed in the Django admin panel.
        return self.image.name
