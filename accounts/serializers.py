from rest_framework import serializers
from .models import Account, MyAccountManager

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class MyAccountManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyAccountManager
        fields = '__all__'