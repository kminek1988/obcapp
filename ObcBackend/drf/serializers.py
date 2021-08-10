import rest_framework
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.reverse import reverse

from Kategorie.models import Letter, Kategoria, Profil, Miasto

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ProfilSerializer(serializers.HyperlinkedModelSerializer):
    kategoria_id = serializers.PrimaryKeyRelatedField(queryset=Kategoria.objects.all(), source='id')

    class Meta:
        model = Kategoria
        fields = ('id', 'title',  'kategoria_id', 'url')
        my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)


class KategoriaSerializer(serializers.HyperlinkedModelSerializer):
    miasto_id = serializers.PrimaryKeyRelatedField(queryset=Miasto.objects.all(), source='miasto')
    children = ProfilSerializer(many=True, read_only=True)
    class Meta:
        model = Kategoria
        fields = ('id', 'title',  'miasto_id', 'url', 'children')
        my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
class MiastoSerializer(serializers.HyperlinkedModelSerializer):
    litera_id = serializers.PrimaryKeyRelatedField(queryset=Letter.objects.all(), source='litera')
    children = KategoriaSerializer(many=True, read_only=True)
    class Meta:
        model = Miasto
        fields = ('id', 'title', 'url', 'litera_id', 'children')
        my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)
class LetterSerializer(serializers.HyperlinkedModelSerializer):
    children = MiastoSerializer(many=True, read_only=True)
    class Meta:
        model = Letter
        fields = ('id', 'url', 'title', 'children')
        my_absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)


