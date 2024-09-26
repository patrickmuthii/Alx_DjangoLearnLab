from django.shortcuts import render # type: ignore
from rest_framework import viewsets # type: ignore
from .serializers import TaskSerializer, UserSerializer
from django.shortcuts import get_object_or_404 # type: ignore

# Create your views here.
