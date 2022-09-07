from django.contrib.auth.models import User
from django.db import models
from django.forms import forms, ModelForm
from django.utils.safestring import mark_safe


# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=50, blank=False)
    symbol = models.CharField(max_length=50, blank=False)
    link = models.CharField(max_length=250, blank=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.CharField(max_length=50, blank=False)
    Percentage = models.CharField(max_length=10, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=50, blank=False)
    instName = models.CharField(max_length=250, blank=True, null=True)
    start = models.DateField()
    end = models.DateField()
    detail = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class userprofile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    posts = models.CharField(max_length=350, blank=True, null=True)
    summary = models.TextField()

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="30" height="30" />'.format(self.image.url))
        return ""


class Category(models.Model):
    title = models.CharField(blank=False, null=False, max_length=30)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=30)
    image = models.ImageField(upload_to='images/portfolios', blank=True, null=True)
    link = models.CharField(max_length=250, blank=True, null=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    detail = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="30" height="30" />'.format(self.image.url))
        return ""


class Images(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    title = models.CharField(blank=True, null=True, max_length=30)
    image = models.ImageField(upload_to='images/gallery', blank=True, null=True)

    @property
    def image_tags(self):
        if self.image:
            return mark_safe('<img src="{}" width="30" height="30" />'.format(self.image.url))
        return ""


class About(models.Model):
    title = models.CharField(blank=False, null=False, max_length=250)
    birthday = models.DateField()
    website = models.CharField(blank=False, null=False, max_length=30)
    image = models.ImageField(upload_to='images/profile', blank=True, null=True)
    phone = models.CharField(blank=False, null=False, max_length=30)
    city = models.CharField(blank=False, null=False, max_length=30)
    degree = models.CharField(blank=False, null=False, max_length=30)
    email = models.CharField(blank=False, null=False, max_length=30)
    Freelancer = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    @property
    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" width="30" height="30" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(blank=False, null=False, max_length=250)
    location = models.CharField(blank=False, null=False, max_length=250)
    start = models.DateField(null=True, blank=True)
    end = models.DateField()
    detail = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class ContactMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
