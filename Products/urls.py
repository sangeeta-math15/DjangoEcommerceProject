# YourApp/urls.py
from django.urls import path
from .views import update_records_db, get_fit_result

urlpatterns = [
    path('update_records_db/', update_records_db, name='update_records_db'),
    path('api/get_fit_results', get_fit_result, name='get_fit_result'),

]
