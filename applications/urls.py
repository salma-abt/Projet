from django.urls import path
from . import views

urlpatterns = [
    path('apply/job_offer/<int:offer_id>/', views.apply_for_job_offer, name='apply_for_job_offer'),
    path('apply/job_request/<int:request_id>/', views.apply_for_job_request, name='apply_for_job_request'),
    path('job_offer/<int:offer_id>/', views.job_offer_detail, name='job_offer_detail'),
    path('job_request/<int:request_id>/', views.job_request_detail, name='job_request_detail'),
]
