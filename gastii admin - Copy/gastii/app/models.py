from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField

class BannarImage(models.Model):
    title = models.CharField(max_length=150)
    short_discriptions = models.TextField(max_length=250)
    image= models.ImageField(upload_to='bannarimage/')

    class Meta:
        ordering = ['-id',]


    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=150)
    discriptions= RichTextField()
    

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
    
class AboutImage(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='aboutus')
    image = models.ImageField(upload_to='aboutimage/')
    def __str__(self):
        return self.image.name


class MenuCategories(models.Model):
    tags = models.CharField(max_length=150, null=True, blank=True)
    categori_name = models.CharField(max_length=150)
    icon= models.ImageField(upload_to='menuimage/')
    ctg_slug = AutoSlugField(populate_from ='categori_name', unique=True, default=None)

    def __str__(self):
        return self.categori_name
    
class Menu(models.Model):
    categori = models.ForeignKey(MenuCategories,on_delete=models.CASCADE ,related_name='categories')
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='menuimage/')
    short_discriptions =RichTextField(max_length=150)
    item_slug = AutoSlugField(populate_from ='name', unique=True, default=None)

    class Meta:
        ordering= ['id',]

    def __str__(self):
        return self.name
    



class Testimonial(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='testimonialimage/')
    discriptions = models.TextField(max_length=250)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.name
    

class Services(models.Model):
    service_name = models.CharField(max_length=150)
    icon = models.ImageField(upload_to='serviceimage/')
    discriptions= RichTextField(max_length=150)

    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.service_name


class ContactDetails(models.Model):
    location = models.CharField(max_length=150)
    phoneNo = models.PositiveIntegerField()
    email = models.EmailField()
    facebookUrl = models.URLField(null=True, blank=True)
    instagramUrl = models.URLField(null=True, blank=True)
    youtubeUrl = models.URLField(null=True, blank=True)
    twiterUrl = models.URLField(null=True, blank=True)
    openingHours= models.TextField()

    class Meta:
        ordering = ['-id',]


class CustomerQuery(models.Model):
    fullname = models.CharField(max_length=150)
    subject= models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()


    class Meta:
        ordering =['-id',]

    def __str__(self):
        return self.fullname


class WhyChooseUs(models.Model):
    videoTitle = models.TextField()
    videoUrl= models.URLField()

    class Meta:
        ordering = ['-id',]
