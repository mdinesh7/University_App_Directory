# from rest_framework import generics
# from .models import App_info
# from .serializers import AppInfoSerializer
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters

# class AppInfoList(generics.ListAPIView):
#     queryset = App_info.objects.all()
#     serializer_class = AppInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_field = ['name']

# class AppInfoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = App_info.objects.all()
#     serializer_class = AppInfoSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_field = ['name']

