from django import forms
from .models import JobApplicationRecruter, JobApplicationCandidat
from AUTH_APP.models import Candidat, Recruteur
from offre_demande.models import Competence, Diplome, Posseder

class JobApplicationRecruterForm(forms.ModelForm):
    # Informations relativent au recruteur
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    num_telephone = forms.CharField(max_length=50)
    email = forms.EmailField()
    secteur_activite = forms.CharField(max_length=100)

    # Informations relatives à la demande d'emploi
    job_request_title = forms.CharField(max_length=100, required=False, disabled=True)
    job_request_description = forms.CharField(widget=forms.Textarea, required=False, disabled=True)
    job_request_competences = forms.CharField(widget=forms.Textarea, required=False, disabled=True)
    job_request_niveaux = forms.CharField(widget=forms.Textarea, required=False, disabled=True)

    def __init__(self, *args, **kwargs):
        recruiter = kwargs.pop('recruiter', None)
        job_request = kwargs.pop('job_request', None)
        super(JobApplicationRecruterForm, self).__init__(*args, **kwargs)
        if recruiter:
            self.fields['name'].initial = recruiter.nom_recruteur
            self.fields['email'].initial = recruiter.email
            self.fields['address'].initial = recruiter.address
            self.fields['num_telephone'].initial = recruiter.num_telephone
            self.fields['secteur_activite'].initial = recruiter.secteur_activite
        if job_request:
            self.fields['job_request_title'].initial = job_request.description
            self.fields['job_request_description'].initial = job_request.description

            # Retrieve competencies and proficiency levels
            competences = Posseder.objects.filter(candidat=job_request.user)
            competences_str = ", ".join([comp.id_competence.nom_competence for comp in competences])
            niveaux_str = ", ".join([comp.niveau_metrise for comp in competences])
            self.fields['job_request_competences'].initial = competences_str
            self.fields['job_request_niveaux'].initial = niveaux_str
    class Meta:
        model = JobApplicationRecruter
        fields = ['cover_letter']

class JobApplicationCandidatForm(forms.ModelForm):
    # Informations relativent au candidat
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    num_telephone = forms.CharField(max_length=50)
    email = forms.EmailField()

    # Informations relatives à l'offre d'emploi
    job_title = forms.CharField(max_length=100, required=False, disabled=True)
    job_description = forms.CharField(widget=forms.Textarea, required=False, disabled=True)
    job_competence = forms.CharField(max_length=100, required=False, disabled=True)
    job_salary = forms.CharField(max_length=100, required=False, disabled=True)
    job_publication_date = forms.CharField(max_length=100, required=False, disabled=True)
    job_application_deadline = forms.CharField(max_length=100, required=False, disabled=True)

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop('candidate', None)
        job_offer = kwargs.pop('job_offer', None)
        super(JobApplicationCandidatForm, self).__init__(*args, **kwargs)
        if candidate:
            self.fields['first_name'].initial = candidate.prenom
            self.fields['last_name'].initial = candidate.nom
            self.fields['email'].initial = candidate.email
            self.fields['address'].initial = candidate.address
            self.fields['num_telephone'].initial = candidate.num_telephone
        if job_offer:
            self.fields['job_title'].initial = job_offer.titre_poste
            self.fields['job_description'].initial = job_offer.description
            self.fields['job_competence'].initial = job_offer.competence
            self.fields['job_salary'].initial = job_offer.salaire_propose
            self.fields['job_publication_date'].initial = job_offer.date_publication_present
            self.fields['job_application_deadline'].initial = job_offer.date_limite_candidature


    class Meta:
        model = JobApplicationCandidat
        fields = ['cover_letter']

    