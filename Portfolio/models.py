from django.db import models

# Create your models here.
class GalleryItem(models.Model):
    PROJECT_TYPES = [
        ('dashboard', 'Dashboard'),
        ('webapp', 'Web App'),
        ('website', 'Website'),
        ('mobile', 'Mobile'),
    ]

    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)
    image = models.ImageField(upload_to='portfolio/')
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.project_name
    
    
class Testimonial(models.Model):
    author_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonial_images/')
    quote = models.TextField()

    def __str__(self):
        return self.author_name
    
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    tarih = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    