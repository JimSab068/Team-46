# resume_hack/urls.py
from django.urls import path
from django.shortcuts import render
from .forms import ResumeUploadForm
import requests
from bs4 import BeautifulSoup
import PyPDF2
import docx

def extract_text_from_pdf(file):
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() + '\n'
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return "Error reading PDF."

def extract_text_from_word(file):
    try:
        doc = docx.Document(file)
        text = ''
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from Word document: {e}")
        return "Error reading Word document."

def fetch_job_description(job_url):
    try:
        response = requests.get(job_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        job_description_div = soup.find('div', class_='job-description')
        if job_description_div:
            return job_description_div.get_text(separator='\n').strip()
        else:
            print("Job description div not found. Please check the class name.")
            return "Job description not found."
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return "Could not fetch the job description."

def extract_skills(job_description):
    # Example skill extraction logic; you can customize this based on your needs
    skills = ['Python', 'Django', 'Data Analysis', 'Machine Learning']  # Placeholder for skills
    return skills

def get_certifications(required_skills):
    certifications = []
    if 'Python' in required_skills:
        certifications.append('Python for Everybody')
    if 'Django' in required_skills:
        certifications.append('Django for Beginners')
    # Add more logic for other skills
    return certifications

def get_roadmap(position):
    # Example roadmap structure; you can expand this as needed
    roadmap = {
        'Data Scientist': [
            'Learn Python',
            'Master Statistics',
            'Understand Machine Learning',
            'Work on Data Projects'
        ]
    }
    return roadmap.get(position, [])

def upload_resume_and_job_description(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        job_url = request.POST.get('job_url')

        resume_text = ''
        if resume_file:
            if resume_file.name.endswith('.pdf'):
                resume_text = extract_text_from_pdf(resume_file)
            elif resume_file.name.endswith('.docx'):
                resume_text = extract_text_from_word(resume_file)
            else:
                resume_text = "Unsupported file format. Please upload a PDF or Word document."
        else:
            resume_text = "No resume file uploaded."

        job_description = ""
        required_skills = []
        if job_url:
            job_description = fetch_job_description(job_url)
            required_skills = extract_skills(job_description)

        return render(request, 'upload_resume_and_job_description.html', {
            'certifications': get_certifications(required_skills),
            'roadmap': get_roadmap('Data Scientist'),  # Adjust job position as needed
            'resume_text': resume_text,
            'job_description': job_description,
        })

    return render(request, 'upload_resume_and_job_description.html', {
        'form': ResumeUploadForm()
    })

urlpatterns = [
    path('', upload_resume_and_job_description, name='upload_resume_and_job_description'),
]
