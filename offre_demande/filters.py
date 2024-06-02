from django.core.exceptions import ValidationError
import django_filters # type: ignore
from .models import *

class OffreDEmploiFilter(django_filters.FilterSet):
    titre_poste = django_filters.CharFilter(method='validate_titre_poste')
    competence = django_filters.CharFilter(method='validate_competence')
    salaire_propose = django_filters.NumberFilter(method='validate_salaire_propose')

    class Meta:
        model = OffreDEmploi
        fields = ['titre_poste', 'competence', 'salaire_propose']

    def validate_titre_poste(self, queryset, name, value):
        if not value.replace(' ', '').isalpha():  # Allow spaces in title
            raise ValidationError("Post title must only contain letters.")
        return queryset.filter(titre_poste__icontains=value).distinct()

    def validate_competence(self, queryset, name, value):
        if not value.replace(' ', '').isalpha():  # Allow spaces in competence
            raise ValidationError("Skill must only contain letters.")
        return queryset.filter(competence__icontains=value).distinct()

    def validate_salaire_propose(self, queryset, name, value):
        if value <= 0:
            raise ValidationError("Salary must be a positive number.")
        
        return queryset.filter(**{name: value})
    
class DemandeDEmploiFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(method='filter_by_description')
    niveau_metrise = django_filters.CharFilter(method='filter_by_niveau_metrise')
    id_competence = django_filters.CharFilter(method='filter_by_competence')

    class Meta:
        model = DemandeDEmploi
        fields = ['description', 'id_competence', 'niveau_metrise']

    def filter_by_competence(self, queryset, name, value):
        if not value.isalpha():
            raise ValidationError("Skill must only contain letters.")
        return queryset.filter(user__posseder__id_competence__nom_competence__icontains=value).distinct()
        
    def filter_by_description(self, queryset, name, value):
        if not value.replace(' ', '').isalpha():  # Allow spaces in description
            raise ValidationError("Post title must only contain letters.")
        return queryset.filter(description__icontains=value).distinct()
    
        