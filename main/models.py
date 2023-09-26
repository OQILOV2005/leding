from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Speakers(models.Model):
    image = models.ImageField(upload_to='Speakers')
    name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Event',null=True,blank=True)

    def __str__(self):
        return self.name


class Venue(models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    text = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='Venue')


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Hotel')

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    image = models.ImageField(upload_to='Sponsor')


class Faq(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Ticet(models.Model):
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
