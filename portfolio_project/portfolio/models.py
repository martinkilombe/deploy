from django.db import models

# Create your models here.
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
