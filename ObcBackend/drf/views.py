from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, renderers
from rest_framework.views import APIView

from rest_framework import permissions
from rest_framework import serializers, generics
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse

from django_filters.rest_framework import DjangoFilterBackend

from Kategorie.models import Letter, Kategoria, Profil, Miasto
from drf.serializers import LetterSerializer, KategoriaSerializer, ProfilSerializer, MiastoSerializer
from drf.serializers import UserSerializer, GroupSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class LetterViewset(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
class KategoriaViewset(viewsets.ModelViewSet):
    queryset = Kategoria.objects.all()
    serializer_class = KategoriaSerializer
class MiastoViewset(viewsets.ModelViewSet):
    queryset = Miasto.objects.all()
    serializer_class = MiastoSerializer
class ProfilViewset(viewsets.ModelViewSet):
    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer

# class Kategoria(generics.ListAPIView):
#    queryset = Kategoria.objects.all()
#    serializer_class = KategoriaSerializer
#    filter_backends = [DjangoFilterBackend]
#    filterset_fields = ['parent']


class LetterView(generics.ListAPIView):
    queryset = Letter.objects.all()
    serializer_class = MiastoSerializer
def MiastoView(request, pk):
    miasto = Miasto.objects.filter(pk=pk)
    kategoria = Kategoria.objects.filter(miasto__in=miasto)
    serializer =KategoriaSerializer(kategoria)
    args = {
        'p' : miasto,
        'k' : kategoria,
    }
    return render (request, 'miasto_detail.html', args)



class MiastoApiView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def get (self, request, pk):
        miasto = get_object_or_404(Miasto, pk=pk)

        serializer_context = {
            'request': request,
        }
        serializer = MiastoSerializer(miasto, context=serializer_context)
        return Response({'p':serializer.data})

