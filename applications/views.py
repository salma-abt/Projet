from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from offre_demande.models import OffreDEmploi, DemandeDEmploi, Posseder, Diplome
from .models import JobApplicationRecruter, JobApplicationCandidat
from .forms import JobApplicationRecruterForm, JobApplicationCandidatForm
from AUTH_APP.models import Recruteur, Candidat
from django.http import HttpResponse
from django.contrib import messages


@login_required
def apply_for_job_request(request, request_id):
    try:
        job_request = DemandeDEmploi.objects.get(id_demande=request_id)
    except DemandeDEmploi.DoesNotExist:
        return HttpResponse('Job request does not exist.')

    try:
        recruiter = Recruteur.objects.get(user=request.user)
    except Recruteur.DoesNotExist:
        return HttpResponse('Recruteur matching query does not exist.')

    if JobApplicationRecruter.objects.filter(applicant=recruiter, job_request=job_request).exists():
        messages.error(request, 'You have already applied for this job request.')
        return redirect('job_request_detail', request_id=request_id)

    if request.method == 'POST':
        form = JobApplicationRecruterForm(request.POST, recruiter=recruiter, job_request=job_request)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = recruiter
            application.job_request = job_request
            application.save()
            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('job_request_detail', request_id=request_id)
    else:
        form = JobApplicationRecruterForm(recruiter=recruiter, job_request=job_request)

    return render(request, 'applications/apply_for_job_request.html', {'form': form, 'job_request': job_request})

@login_required
def apply_for_job_offer(request, offer_id):
    try:
        job_offer = OffreDEmploi.objects.get(id_offre=offer_id)
    except OffreDEmploi.DoesNotExist:
        return HttpResponse('Job offer does not exist.')

    try:
        candidate = Candidat.objects.get(user=request.user)
    except Candidat.DoesNotExist:
        return HttpResponse('Candidat matching query does not exist.')

    if JobApplicationCandidat.objects.filter(applicant=candidate, job_offer=job_offer).exists():
        messages.error(request, 'You have already applied for this job offer.')
        return redirect('job_offer_detail', offer_id=offer_id)

    if request.method == 'POST':
        form = JobApplicationCandidatForm(request.POST, candidate=candidate, job_offer=job_offer)
        if form.is_valid():
            application = form.save(commit=False)
            application.applicant = candidate
            application.job_offer = job_offer
            application.save()
            messages.success(request, 'Your application has been submitted successfully.')
            return redirect('job_offer_detail', offer_id=offer_id)
    else:
        form = JobApplicationCandidatForm(candidate=candidate, job_offer=job_offer)

    return render(request, 'applications/apply_for_job_offer.html', {'form': form, 'job_offer': job_offer})


def job_offer_detail(request, offer_id):
    try:
        job_offer = OffreDEmploi.objects.get(id_offre=offer_id)
    except OffreDEmploi.DoesNotExist:
        return HttpResponse('Job offer does not exist.')
    
    return render(request, 'applications/job_offer_detail.html', {'job_offer': job_offer})


def job_request_detail(request, request_id):
    try:
        job_request = DemandeDEmploi.objects.get(id_demande=request_id)
    except DemandeDEmploi.DoesNotExist:
        return HttpResponse('Job request does not exist.')
    
    return render(request, 'applications/job_request_detail.html', {'job_request': job_request})
