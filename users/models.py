from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        #parent classes save method
        super(Profile, self).save(*args, **kwargs)

        #grab image of the current instance that it saved
        img = Image.open(self.img.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # resizing to 300x300
            img.thumbnail(output_size)
            #saving it to the same path overwrite the original image
            img.save(self.img.path)