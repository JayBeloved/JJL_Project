from django.db import models
from django.contrib.auth.models import User

class PitchDeck(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pitch = models.TextField(max_length=7000)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True,  null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clicks = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('health', 'Healthcare'),
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('retail', 'Retail'),
        ('manufacturing', 'Manufacturing'),
        ('real_estate', 'Real Estate'),
        ('transportation', 'Transportation'),
        ('energy', 'Energy'),
        ('agriculture', 'Agriculture'),
        ('hospitality', 'Hospitality'),
        ('construction', 'Construction'),
        ('legal', 'Legal'),
        ('marketing', 'Marketing'),
        ('media', 'Media'),
        ('non_profit', 'Non-Profit'),
        ('sports', 'Sports'),
        ('telecommunications', 'Telecommunications'),
        ('utilities', 'Utilities'),
        ('other', 'Other'),
    ]
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, blank=True)

    def __str__(self):
        return f"{self.user.username}'s PitchDeck"