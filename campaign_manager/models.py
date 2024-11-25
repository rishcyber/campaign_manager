from django.utils import timezone
from django.db import models

from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=100)
    voice_id = models.CharField(max_length=100, unique=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Campaign(models.Model):
    CAMPAIGN_TYPES = [
        ('Inbound', 'Inbound'),
        ('Outbound', 'Outbound'),
    ]

    STATUS_CHOICES = [
        ('Running', 'Running'),
        ('Paused', 'Paused'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=CAMPAIGN_TYPES)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name="campaigns")

    def __str__(self):
        return self.name


class CampaignResult(models.Model):
    name = models.CharField(max_length=255)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="results")
    phone = models.CharField(max_length=20)
    cost = models.FloatField()
    outcome = models.CharField(max_length=255)
    call_duration = models.FloatField()
    recording = models.URLField()
    summary = models.TextField()
    transcription = models.TextField()

    def __str__(self):
        return self.name
