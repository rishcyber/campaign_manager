from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Agent, Campaign, CampaignResult
from .serializers import AgentSerializer, CampaignSerializer, CampaignResultSerializer

# Agent Views
@api_view(['GET', 'POST'])
def agent_list(request):
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = AgentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def agent_detail(request, pk):
    try:
        agent = Agent.objects.get(pk=pk)
    except Agent.DoesNotExist:
        return Response({'error': 'Agent not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AgentSerializer(agent)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = AgentSerializer(agent, data=request.data, partial=True)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        agent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Campaign Views
@api_view(['GET', 'POST'])
def campaign_list(request):
    if request.method == 'GET':
        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def campaign_detail(request, pk):
    try:
        campaign = Campaign.objects.get(pk=pk)
    except Campaign.DoesNotExist:
        return Response({'error': 'Campaign not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CampaignSerializer(campaign)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CampaignSerializer(campaign, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        campaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CampaignResult Views
@api_view(['GET', 'POST'])
def campaign_result_list(request):
    if request.method == 'GET':
        results = CampaignResult.objects.all()
        serializer = CampaignResultSerializer(results, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        campaign_id = request.data.get('campaign') 
        try:
            campaign = Campaign.objects.get(id=campaign_id)
        except Campaign.DoesNotExist:
            return Response({'error': 'Campaign not found'}, status=status.HTTP_404_NOT_FOUND)
        result_name = f"{campaign.name} result"
        data = request.data.copy()
        data['name'] = result_name  
        serializer = CampaignResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def campaign_result_detail(request, pk):
    try:
        result = CampaignResult.objects.get(pk=pk)
    except CampaignResult.DoesNotExist:
        return Response({'error': 'CampaignResult not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CampaignResultSerializer(result)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        campaign_id = request.data.get('campaign') 
        try:
            campaign = Campaign.objects.get(id=campaign_id)
        except Campaign.DoesNotExist:
            return Response({'error': 'Campaign not found'}, status=status.HTTP_404_NOT_FOUND)
        result_name = f"{campaign.name} result"
        data = request.data.copy()
        data['name'] = result_name  
        serializer = CampaignResultSerializer(result, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
