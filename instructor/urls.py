# urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateInstructorAPIView, CheckInAPIView, CheckOutAPIView, MonthlyReportAPIView

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('create', CreateInstructorAPIView.as_view(), name='create_instructor'),
    path('checkin', CheckInAPIView.as_view(), name='checkin'),
    path('checkout', CheckOutAPIView.as_view(), name='checkout'),
    path('monthly-report', MonthlyReportAPIView.as_view(), name='monthly_report'),
]