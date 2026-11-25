from django.db import models

# Create your models here.
class Skill(models.Model):

    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Base de données'),
        ('tools', 'Outils'),
        ('other', 'Autres'),
    ]

    name = models.CharField(
        max_length=100,
        unique=True
    )

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    level = models.PositiveIntegerField(
        default=50
    )

    icon = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

