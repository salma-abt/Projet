from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .filters import *
from .models import *


def offredemploi(request):
    if request.user.is_authenticated:
        try:
            filtered_offres = OffreDEmploiFilter(request.GET,queryset=OffreDEmploi.objects.all().order_by('-date_publication_present'))
        
            offres = filtered_offres.qs  

            if not offres.exists():
                offres = {}
            return render(request, 'offredemploi.html', {'offres' : offres})
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'offredemploi.html', {})
    else:
        messages.info(request, 'You dont have permission to access the home page log in first!')
        return redirect(reverse('login'))


def base(request):
    if request.user.is_authenticated:
        try:
            filtered_demandes = DemandeDEmploiFilter(request.GET, queryset=DemandeDEmploi.objects.all().order_by('-date_soumission'))
            demandes = filtered_demandes.qs  

            if not demandes.exists():
                demandes = {}

            for demande in demandes:
                demande.posseder_data = Posseder.objects.filter(candidat=demande.user)
            return render(request, 'base.html', {'demandes': demandes})
        except ValidationError as e:
            messages.error(request, str(e))
            return render(request, 'base.html', {})
    else:
        messages.info(request, 'You dont have permission to access the home page log in first!')
        return redirect(reverse('login'))

