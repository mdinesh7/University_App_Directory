from rest_framework import serializers
from .models import App_info

class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = App_info
        fields = ['name','desc','category','is_free','logo_url']
