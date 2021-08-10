from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
# from django.core.urlresolvers import reverse


# Create your models here.

class Letter (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Litery'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('litera', args=[str(self.slug)])

class Miasto(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Nazwa')
    slug = models.SlugField()
    litera = models.ForeignKey(Letter, on_delete=models.DO_NOTHING, related_name="children")

    class Meta:
        verbose_name_plural = 'Miasta'

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('miasto', args=[str(self.pk)])


class Kategoria(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nazwa')
    slug = models.SlugField()
    miasto = models.ForeignKey(Miasto, on_delete=models.DO_NOTHING, related_name="children")
    class Meta:
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('kategoria', args=[str(self.slug)])

class Profil(models.Model):
    title = models.CharField(max_length=255, verbose_name='Pseudonim')
    kategoria = models.ForeignKey(Kategoria, on_delete=models.DO_NOTHING, related_name="children")
    # parent = models.ForeignKey('self', null=True, blank=True, related_name='Children', on_delete=models.CASCADE, verbose_name='Miasto')
    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profil', args=[str(self.id)])


