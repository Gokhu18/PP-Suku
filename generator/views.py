from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import user
from .forms import userForm
from .serializers import UserSerializer
from django.contrib.auth.mixins import LoginRequiredMixin# Create your views here.

class UserAPI(viewsets.ModelViewSet):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,)

def index(request):
    return render(request, 'generator/index.html')

def user_new(request):
    form=userForm
    return render(request, 'generator/index.html', {'form': form})