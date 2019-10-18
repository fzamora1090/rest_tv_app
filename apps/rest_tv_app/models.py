from django.db import models
from datetime import datetime
# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):

        errors = {}
        # matched_show = Show.objects.filter(title=)
        if len(postData['title']) < 2 or Show.objects.filter(title=postData['title']):
           errors['title'] = "Title name should be unique and longer than 2 characters"


        if len(postData['network']) < 3:
           errors['network'] = "Network name should be longer than 3 characters"

        

        if len(postData['description'])  > 0 and len(postData['description']) < 10:
            errors['description'] = "Description should be longer than 10 characters"
        
        if datetime > datetime.now:
            errors['date'] = "Release date must be in the past"
        # if len(postData['description']) < 1:
        #    return errors
            

        return errors


class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    
    date = models.DateField(auto_now=False, auto_now_add=False)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()



