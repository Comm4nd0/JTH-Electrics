from django.db import models

# Create your models here.

class ContactDetail(models.Model):
    page_title = models.CharField(max_length=100, blank=True)
    header_image_1600x660 = models.ImageField(blank=True)
    sub_heading = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    landline = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)

    image_600x350 = models.ImageField(blank=True)
    image_700x458_homepage = models.ImageField(blank=True)

    form_heading = models.CharField(max_length=100, blank=True)
    send_button_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.page_title