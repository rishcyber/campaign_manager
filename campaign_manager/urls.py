from django.urls import path
from . import views

urlpatterns = [
    # Agent URLs
    path('agents/', views.agent_list, name='agent-list'),
    path('agents/<int:pk>/', views.agent_detail, name='agent-detail'),
    
    # Campaign URLs
    path('campaigns/', views.campaign_list, name='campaign-list'),
    path('campaigns/<int:pk>/', views.campaign_detail, name='campaign-detail'),
    
    # CampaignResult URLs
    path('campaign-results/', views.campaign_result_list, name='campaign-result-list'),
    path('campaign-results/<int:pk>/', views.campaign_result_detail, name='campaign-result-detail'),
]
