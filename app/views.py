from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from app.models import Student
from app.serializer import StudentSerializer
# Create your views here.
class Data_List(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request):
        return self.list(request)
class Data_create(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self,request):
        return self.create(request)
class Data_Retrive(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,**kwars):
        return self.retrieve(request,**kwars)
class Data_update(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self,request,**kwarg):
        return self.update(request,**kwarg)
class Data_delete(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self,request,**kwars):
        return self.destroy(request,**kwars)
