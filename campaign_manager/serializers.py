from rest_framework import serializers
from .models import Agent, Campaign, CampaignResult

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):
    agent_name = serializers.CharField(source='agent.name', read_only=True)

    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignResultSerializer(serializers.ModelSerializer):
    campaign_name = serializers.CharField(source='campaign.name', read_only=True)

    class Meta:
        model = CampaignResult
        fields = '__all__'
