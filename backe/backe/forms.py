# resume_hack/forms.py
from django import forms

class ResumeUploadForm(forms.Form):
    resume_file = forms.FileField(required=False, label="Upload Resume (PDF or Word)")
    job_description = forms.CharField(widget=forms.Textarea, required=True, label="Job Description")