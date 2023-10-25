import os
from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework import generics
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .serializers import AppInfoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import App_info
# from .api_views import AppInfoList,AppInfoDetail


# Create your views here.
def index(request):

    appinfo = AppInfoList.as_view()(request).data
    appinfo = list(reversed(appinfo))

    return render(request, "index.html", {'appinfs':appinfo})

def create(request):

    mydata=App_info.objects.all()
    if(mydata!=''):
        return render(request, 'appdata.html',{'data':mydata})
    else:

        return render(request,'appdata.html')

def add(request):

    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        category = request.POST['category']
        is_free = request.POST.get('is_free', 'false') == 'true'
        uploaded_logo = request.FILES.get('logo_url')
        if uploaded_logo:
            fs = FileSystemStorage()
            filename = fs.save(uploaded_logo.name, uploaded_logo)
            logo_url = fs.url(filename).lstrip('/')
        else:
            logo_url = 'Canvas.jpeg' 
        
        obj = App_info()
        obj.name = name
        obj.desc = desc
        obj.category = category
        obj.is_free = is_free
        obj.logo_url = logo_url    
        obj.save()
        mydata=App_info.objects.all()
        return redirect(create)
    
    return render(request,'appdata.html')

def update(request, id):
    mydata=App_info.objects.get(id=id)    
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        category = request.POST['category']
        is_free = request.POST.get('is_free', 'false') == 'true'
        print(is_free)
        uploaded_logo = request.FILES.get('logo_url')
        if uploaded_logo:
            fs = FileSystemStorage()
            filename = fs.save(uploaded_logo.name, uploaded_logo)
            logo_url = fs.url(filename).lstrip('/')
        else:
            logo_url = 'Canvas.jpeg' 

        mydata.name=name
        mydata.desc=desc
        mydata.category=category
        mydata.is_free=is_free
        mydata.logo_url=logo_url
        mydata.save()
        return redirect('create')
    
    return render(request, 'update.html', {'data':mydata})

def delete(request, id):
    mydata=App_info.objects.get(id=id)
    mydata.delete()
    return redirect('create')

def search(request):
    sample = AppInfoList.as_view()(request).data
    
    return render(request, 'search.html', {'data':sample})

class AppInfoList(generics.ListAPIView):
    # queryset = App_info.objects.all()
    # serializer_class = AppInfoSerializer
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filterset_fields = ['category', 'is_free']
    # search_fields = ['name'] 
    queryset = App_info.objects.all()
    serializer_class = AppInfoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'is_free']
    search_fields = ['name', 'category']

    def get_queryset(self):
        queryset = super().get_queryset()
        name_search = self.request.query_params.get('name', None)
        if name_search:
            queryset = queryset.filter(name__icontains=name_search)
        return queryset
   

class AppInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = App_info.objects.all()
    serializer_class = AppInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_field = ['name']

    

