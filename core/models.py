from django.db import models

# Create your models here.
class Profile(models.Model):

    full_name = models.CharField(max_length=150)

    title = models.CharField(max_length=150)

    bio = models.TextField()

    email = models.EmailField()

    photo = models.ImageField(
        upload_to='profile/',
        blank=True,
        null=True
    )

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    location = models.CharField(
        max_length=150,
        blank=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"
        
class SocialLink(models.Model):

    platform = models.CharField(
        max_length=100
    )

    url = models.URLField()

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.platform

