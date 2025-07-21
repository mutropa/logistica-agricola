from django.urls import path
from .views import RegistarView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .token import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# View personalizada para JWT
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

urlpatterns = [
    path('registo/', RegistarView.as_view(), name='registo'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
