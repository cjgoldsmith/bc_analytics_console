from django.contrib.auth.models import User
from rest_framework import serializers

from .models import BCCredentials, BCAccounts


class BCCredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BCCredentials
        fields = ('id', 'name', 'client_id', 'client_secret', )


class BCAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BCAccounts
        fields = ('id', 'name', 'pub_id', 'auth', 'token', )


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', )
