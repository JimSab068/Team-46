# # 
# # resume_hack/urls.py
# from django.urls import path
# from django.shortcuts import render
# from .forms import ResumeUploadForm
# import PyPDF2
# import docx

# def extract_text_from_pdf(file):
#     try:
#         pdf_reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in pdf_reader.pages:
#             text += page.extract_text() + '\n'
#         return text.strip()
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return "Error reading PDF."

# def extract_text_from_word(file):
#     try:
#         doc = docx.Document(file)
#         text = ''
#         for paragraph in doc.paragraphs:
#             text += paragraph.text + '\n'
#         return text.strip()
#     except Exception as e:
#         print(f"Error extracting text from Word document: {e}")
#         return "Error reading Word document."

# def extract_skills(job_description):
#     # Example skill extraction logic; you can customize this
#     skills = ['Python', 'Django', 'Data Analysis', 'Machine Learning']  # Placeholder for skills
#     return skills

# def get_certifications(required_skills):
#     certifications = []
#     if 'Python' in required_skills:
#         certifications.append('Python for Everybody')
#     if 'Django' in required_skills:
#         certifications.append('Django for Beginners')
#     # Add more logic for other skills
#     return certifications

# def get_roadmap(position):
#     # Example roadmap structure
#     roadmap = {
#         'Data Scientist': [
#             'Learn Python',
#             'Master Statistics',
#             'Understand Machine Learning',
#             'Work on Data Projects'
#         ]
#     }
#     return roadmap.get(position, [])

# def upload_resume_and_job_description(request):
#     if request.method == 'POST':
#         resume_file = request.FILES.get('resume_file')
#         job_description = request.POST.get('job_description')

#         resume_text = ''
#         if resume_file:
#             if resume_file.name.endswith('.pdf'):
#                 resume_text = extract_text_from_pdf(resume_file)
#             elif resume_file.name.endswith('.docx'):
#                 resume_text = extract_text_from_word(resume_file)
#             else:
#                 resume_text = "Unsupported file format. Please upload a PDF or Word document."
#         else:
#             resume_text = "No resume file uploaded."

#         required_skills = []
#         if job_description:
#             required_skills = extract_skills(job_description)

#         return render(request, 'upload_resume_and_job_description.html', {
#             'certifications': get_certifications(required_skills),
#             'roadmap': get_roadmap('Data Scientist'),  # Adjust job position as needed
#             'resume_text': resume_text,
#             'job_description': job_description,
#         })

#     return render(request, 'upload_resume_and_job_description.html', {
#         'form': ResumeUploadForm()
#     })

# urlpatterns = [
#     path('', upload_resume_and_job_description, name='upload_resume_and_job_description'),
# ]

# resume_hack/urls.py
from django.urls import path
from django.shortcuts import render
from .forms import ResumeUploadForm
import pdfplumber
import openai as op
api_key = r'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'



# Try to import PyPDF2 and docx, handle if they are not installed
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None
    print("PyPDF2 module is not installed.")

# try:
#     import docx
# except ImportError:
#     docx = None
#     print("python-docx module is not installed.")

def extract_text_from_pdf(file):
    if PyPDF2 is None:
        return "PyPDF2 is not installed, cannot process PDF."
    
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text() + '\n'
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return "Error reading PDF."



#################################################

# Load your OpenAI API key from environment variable


def extract_skills(job_description):
    user_input = f"job description {job_description}, find the skills required from it."
    return generate_response(user_input,0.4,350)

def get_certifications(required_skills, resume_text):
    user_input = f"job description {required_skills}, resume {resume_text},  find courses that I am missing in my job resume and are required by the job description, give me the course name and link,don't print anything else.."
    return generate_response(user_input,0.7,550)
def get_roadmap(certifis):
    user_input = f"give me a roadmap to learn these courses" + certifis
    return generate_response(user_input,0.7,550)
def generate_response(prompt,temp=0.7,max_t=150):
    op.api_key = api_key
    try:
        response = op.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=max_t,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"




####################################################################
def upload_resume_and_job_description(request):
    if request.method == 'POST':
        resume_file = request.FILES.get('resume_file')
        job_description = request.POST.get('job_description')

        resume_text = ''
        if resume_file:
            if resume_file.name.endswith('.pdf'):
                resume_text = extract_text_from_pdf(resume_file)
            # elif resume_file.name.endswith('.docx'):
            #     resume_text = extract_text_from_word(resume_file)
            else:
                resume_text = "Unsupported file format. Please upload a PDF or Word document."
        else:
            resume_text = "No resume file uploaded."

        # required_skills = ''

        if job_description:
            required_skills = extract_skills(job_description)
            print(required_skills)
        # certifis=''
        certifis=get_certifications(required_skills,resume_text)
        # roadmap=''
        roadmap= get_roadmap(certifis)
        return render(request, 'upload_resume_and_job_description.html', {
            'certifications': certifis,
            'roadmap': roadmap,  # Adjust job position as needed
            'resume_text': resume_text,
            'job_description': job_description,
        })

    return render(request, 'upload_resume_and_job_description.html', {
        'form': ResumeUploadForm()
    })

urlpatterns = [
    path('', upload_resume_and_job_description, name='upload_resume_and_job_description'),
]


