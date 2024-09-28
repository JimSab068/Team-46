# resume_hack/forms.py
from django import forms

class ResumeUploadForm(forms.Form):
    resume_file = forms.FileField(label='Upload Resume (PDF or Word)')
    job_url = forms.URLField(label='Job URL', required=True)
