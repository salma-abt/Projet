from django.db import models
from django.contrib.auth.models import User
from offre_demande.models import OffreDEmploi, DemandeDEmploi
from AUTH_APP.models import Recruteur, Candidat

class JobApplicationRecruter(models.Model):
    applicant = models.ForeignKey(Recruteur, on_delete=models.CASCADE)
    job_request = models.ForeignKey(DemandeDEmploi, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job_request')

    def __str__(self):
        return f"Application by {self.applicant.user.username} for {self.job_request.title}"

class JobApplicationCandidat(models.Model):
    applicant = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    job_offer = models.ForeignKey(OffreDEmploi, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('applicant', 'job_offer')

    def __str__(self):
        return f"Application by {self.applicant.user.username} for {self.job_offer.titre_poste}"
