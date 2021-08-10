from django.urls import include, path
from rest_framework import routers
from drf.views import  LetterViewset, KategoriaViewset, MiastoViewset, LetterView, MiastoView, ProfilViewset, MiastoApiView
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register('litery', LetterViewset)
router.register('miasta', MiastoViewset)
router.register('kategorie', KategoriaViewset)
router.register('profile', ProfilViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('miasta/<int:pk>', MiastoView, name='miasto'),
    path('miasta/<int:pk>/api', MiastoApiView.as_view())




]


