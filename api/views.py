from django.shortcuts import render
from api.serializers import studentserializer
from .models import student
from rest_framework.generics import ListAPIView
from .mypage import MyPageNumberPagfination

# Create your views here.

class studentlist(ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentserializer
    pagination_class=MyPageNumberPagfination
