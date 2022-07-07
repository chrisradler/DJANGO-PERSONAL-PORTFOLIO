from django.db import models
#this class was to create the project folder on the admin page
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    
    def __str__(self):
        return self.title

