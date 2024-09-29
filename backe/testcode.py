# from django.urls import path
# from django.shortcuts import render
# # from .forms import ResumeUploadForm
# import pdfplumber
# import openai
api_key = "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"
# def extract_skills(resume_text,job_description):
#     # jd_text=" "
# # Function to generate response using OpenAI's GPT-4
#     def generate_response(prompt, api_key):
#         openai.api_key = api_key
    
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.7,
#                 max_tokens=150,
#             )
        
#         # Extract and return the text response from the API
#             return response['choices'][0]['message']['content']
    
#         except Exception as e:
#             return f"Error: {str(e)}"

#     if __name__ == "__main__":
#     # Ask for user input
#         user_input ="job description " + job_description + "find the skills required from it.."
        
#     # Generate and print the response
#     skills = generate_response(user_input, api_key)
#     # jd_text=response_text_jd
#     # print("\nGenerated Response: ")
#     # print(response_text_jd)
#     return skills
job_description="At a glance $25/hr Hybrid, based in New York, NY Work in person for part of the week, from the location Internship Full-time∙From June 9 to August 15 US work authorization required Open to candidates with OPT/CPT Summer 2025 Internship - Data Analyst Application Deadline: November 15, 2024 We encourage you to submit your application as soon as you can as internship applications are reviewed on a rolling basis. Internship Dates & Details: June 9, 2025 - August 15, 2025 (You must be available to work during this period) About our Organization: Dow Jones is a global provider of news and business information, delivering content to consumers and organizations around the world across multiple formats, including print, digital, mobile and live events. Dow Jones has produced unrivaled quality content for more than 130 years and today has one of the world's largest news-gathering operations globally. It is home to leading publications and products including the flagship Wall Street Journal, America's largest newspaper by paid circulation; Barron's, MarketWatch, Mansion Global, Financial News, Investor's Business Daily, Factiva, Dow Jones Risk & Compliance, Dow Jones Newswires, OPIS and Chemical Market Analytics. Dow Jones is a division of News Corp (Nasdaq: NWS, NWSA; ASX: NWS, NWSLV). About the Role: You will be a part of our Insights and Solutions teams. The Data Analyst intern will be an integral member of the Dow Jones Data Management team in either our New York City office. You will support projects of data insights, engineering, and transformation strategy, which in turn supports the larger strategic goals at Dow Jones. This role would support either the Consumer or Professional Information side of the business, which includes Factiva, Risk & Compliance, WSJ, Barron’s, MarketWatch and more; but may also include exposure to other areas of the business, such as advertising. This role is hybrid, based in our New York City office. You Will: Assist with customer-facing report deliveries, both existing and ad hoc requests Interpret trends from data and work closely with stakeholders to enable them to understand the dynamics behind the data Contribute to the development of daily, weekly, monthly, and quarterly dashboards and assist in building new dashboards using Adobe, Tableau, Google Analytics, or other approved data visualization tools leveraging our own internal data lakes Apply fundamental skills in quantitative analysis, data exploration, and the presentation of data to see beyond the numbers and understand how our users interact with our products Support the company’s use of state-of-the art technology end-to-end; from data pipelines, to analysis, models, algorithms and visualization You Have: Completed at least 2 years toward your Bachelor’s degree in a quantitative subject (Statistics, Engineering, Economics, etc.) Exposure to data analysis and problem solving with large amounts of diverse data Basic fluency in SQL, Python or knowledge of relational databases and methods for efficiently retrieving data Strong Microsoft Excel skills are required including advanced formulas and functions Effective verbal and written communication skills. Ability to communicate the results of analyses clearly and effectively Demonstrated curiosity to dive into available data and enjoy searching for patterns that could indicate new insights Exposure to cloud infrastructure, such as AWS/S3, is a plus Hands-on coding experience is a plus Reasonable accommodation: Dow Jones, Making Careers Newsworthy - We are an equal opportunity employer and all qualified applicants will receive consideration for employment without regard to race, color, religion, sex, sexual orientation, gender identity or expression, pregnancy, age, national origin, disability status, genetic information, protected veteran status, or any other characteristic protected by law. EEO/AA/M/F/Disabled/Vets. Dow Jones is committed to providing reasonable accommodation for qualified individuals with disabilities, in our job application and/or interview process. If you need assistance or accommodation in completing your application, due to a disability, email us at talentresourceteam@dowjones.com. Please put Reasonable Accommodation in the subject line and provide a brief description of the type of assistance you need. This inbox will not be monitored for application status updates. We recognize that attracting the best talent is key to our strategy and success as a company. As a result, we aim for flexibility in structuring competitive compensation offers to ensure we are able to attract the best candidates. The quoted salary range represents our good faith estimate as to what our ideal candidates are likely to expect, and we tailor our offers within the range based on the selected candidate's experience, industry knowledge, location, technical and communication skills, and other factors that may prove relevant during the interview process. Pay-for-performance is a key element in our strategy to attract, engage, and motivate talented people to do their best work. Similarly to salary, for bonus eligible roles, targets are set based on a variety of factors including competitive market practice. For benefits eligible roles, in addition to cash compensation, the company provides a comprehensive and highly competitive benefits package, with a variety of physical health, retirement and savings, caregiving, emotional wellbeing, transportation, and other benefits, including elective benefits employees may select to best fit the needs and personal situations of our diverse workforce.. Since 1882, Dow Jones has been finding new ways to bring information to the world’s top business entities. Beginning as a niche news agency in an obscure Wall Street basement, Dow Jones has grown to be a worldwide news and information powerhouse, with prestigious brands including The Wall Street Journal, Dow Jones Newswires, Factiva, Barron’s, MarketWatch and Financial News. This longevity and success is due to a relentless pursuit of accuracy, depth and innovation, enhanced by the wisdom of past experience and a solid grasp on the future ahead. More than its individual brands, Dow Jones is a modern gateway to intelligence, with innovative technology, advanced data feeds, integrated solutions, expert research, award-winning journalism and customizable apps and delivery systems to bring the information that matters most to customers, when and where they need it, every day."
resume_text="Nova Southeastern University, Davie FL  B.S. in Computer Science, Expected May 2010  Minors in Mathematics and Physics GPA: 3.75 Honors: Dean's List Relevant Courses:  Human-Computer Interaction, Artificial Inte lligence, 3D Animation, Logic Programming, Quantum Mechanics, Theory of Computati on, Machine Learning, Computer Graphics SKILLS / STRENGTHS  Programming languages: Perl, Java, C++, HTML, PHP, MySQL, Scheme, MatLab  Software: Microsoft Office, Adobe Photos hop and Dreamweaver, 3ds Max  Operating Systems: Windows (95, 98, 2000, XP , Vista), Mac OS, Linux  Professional: Self-motivated, creative thinker; deta il-oriented; excellent time management skills EXPERIENCE ABC Research, Boca Raton FL , May 2008 – Sept 2008 Collaborative User Experience Group Intern  Developed wikis, blogs, and so cial networks with a team of computer and social scientists  Contributed technical support to development of groundbreaking networking software to be showcased in forthcoming industry publication Library Application Services, NSU , Davie FL, May 2007 - Present Student Web Developer  Develop and maintain individualized websites for a range of divisions across the university  Assist in the technical administration of the campus intranet and calendar systems Computer Science Departments, NSU , Davie FL, Sept 2007 - May 2008 Teaching Assistant  Gave weekly lectures to students enrolled in advanced programming language course and introductory physics course  Explained complex concepts in small group setting; grade assignments and examinations  Held office hours for individual student discussion YMCA , Fort Lauderdale FL, Jan 2005 – August 2007 Computer teacher  Taught basic computer skills to teenage and elderly town residents ACTIVITIES  Tutored elementary school children in math and science Freelance Music Teacher , Fort Lauderdale FL, 2005 - Present  Give guitar and piano lessons to high school and college students  Prepare students for recitals and a ccompany them during performances"
# skillss=extract_skills(resume_text,job_description)
# print(skillss)


# def get_certifications(required_skills,resume_text):
#     def generate_response(prompt, api_key):
#         openai.api_key = api_key
    
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.7,
#                 max_tokens=150,
#             )
        
#         # Extract and return the text response from the API
#             return response['choices'][0]['message']['content']
    
#         except Exception as e:
#             return f"Error: {str(e)}"

#     if __name__ == "__main__":
#     # Ask for user input
#         user_input ="job description "+ required_skills + "resume" + resume_text + "find 3 courses that I am missing in my job resume and are required by the job description, give me the course name and link,don't print anything else.."
#     certifications = generate_response(user_input,api_key)
#     return certifications

# op=get_certifications(skillss,resume_text)
# print(op)


# def get_roadmap(certifis):
#     # Function to generate response using OpenAI's GPT-4
#     def generate_response(prompt, api_key):
#         openai.api_key = api_key
    
#         try:
#             response = openai.ChatCompletion.create(
#                 model="gpt-4",
#                 messages=[{"role": "user", "content": prompt}],
#                 temperature=0.7,
#                 max_tokens=550,
#             )
        
#         # Extract and return the text response from the API
#             return response['choices'][0]['message']['content']
    
#         except Exception as e:
#             return f"Error: {str(e)}"

#     if __name__ == "__main__":
#     # Ask for user input
#         user_input ="give me a roadmap to learn these courses" + certifis
    
#     # Generate and print the response
#     roadmap = generate_response(user_input, api_key)
  
#     return roadmap


# op2=get_roadmap(op)
# print(op2)

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
# from .forms import ResumeUploadForm
import pdfplumber
import openai
api_key = "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"

# Try to import PyPDF2 and docx, handle if they are not installed
# try:
#     import PyPDF2
# except ImportError:
#     PyPDF2 = None
#     print("PyPDF2 module is not installed.")

# try:
#     import docx
# except ImportError:
#     docx = None
#     print("python-docx module is not installed.")

# def extract_text_from_pdf(file):
#     if PyPDF2 is None:
#         return "PyPDF2 is not installed, cannot process PDF."
    
#     try:
#         pdf_reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page in pdf_reader.pages:
#             text += page.extract_text() + '\n'
#         return text.strip()
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return "Error reading PDF."

# def extract_text_from_pdf(file):
#     if PyPDF2 is None:
#         return "PyPDF2 is not installed, cannot process PDF."
    
#     try:
#         subheading="Education"
#         pdf_reader = PyPDF2.PdfReader(file)
#         text = ''
#         capturing = False  # Flag to indicate if we are capturing text

#         # Loop through all the pages in the PDF
#         for page in pdf_reader.pages:
#             page_text = page.extract_text()
#             if page_text:  # If text is present on the page
#                 for line in page_text.split('\n'):
#                     # Check if the current line contains the subheading
#                     if subheading.lower() in line.lower():
#                         capturing = True  # Start capturing text after the subheading
#                         continue
#                     if capturing:
#                         text += line + '\n'  # Capture all subsequent lines

#         # If no text was captured, it could mean the subheading wasn't found
#         return text.strip() if text else f"Subheading '{subheading}' not found."
    
#     except Exception as e:
#         print(f"Error extracting text from PDF: {e}")
#         return "Error reading PDF."

# def extract_text_from_word(file):
#     if docx is None:
#         return "python-docx is not installed, cannot process Word documents."
    
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

def extract_skills(job_description):
    # jd_text=" "
# Function to generate response using OpenAI's GPT-4
    print("start")
    def generate_response(prompt, api_key):
        openai.api_key = api_key
    
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150,
            )
        
        # Extract and return the text response from the API
            return response['choices'][0]['message']['content']
    
        except Exception as e:
            return f"Error: {str(e)}"

    if __name__ == "__main__":
    # Ask for user input
        user_input ="job description " + job_description + "find the skills required from it.."
        
    # Generate and print the response
        skills = generate_response(user_input, api_key)
    # jd_text=response_text_jd
    # print("\nGenerated Response: ")
    # print(response_text_jd)
        return skills
def get_certifications(required_skills,resume_text):
    def generate_response(prompt, api_key):
        openai.api_key = api_key
    
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=150,
            )
        
        # Extract and return the text response from the API
            return response['choices'][0]['message']['content']
    
        except Exception as e:
            return f"Error: {str(e)}"

    if __name__ == "__main__":
    # Ask for user input
        user_input ="job description "+ required_skills + "resume" + resume_text + " find 3 courses that I am missing in my job resume and are required by the job description, give me the course name and link,don't print anything else.."
        certifications = generate_response(user_input,api_key)
        return certifications

def get_roadmap(certifis):
    # Function to generate response using OpenAI's GPT-4
    def generate_response(prompt, api_key):
        openai.api_key = api_key
    
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=550,
            )
        
        # Extract and return the text response from the API
            return response['choices'][0]['message']['content']
    
        except Exception as e:
            return f"Error: {str(e)}"

    if __name__ == "__main__":
    # Ask for user input

        user_input ="give me a roadmap to learn these courses" + certifis
    
    # Generate and print the response
        roadmap = generate_response(user_input, api_key)
  
        return roadmap

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


####################################################################
def upload_resume_and_job_description():
    # if request.method == 'POST':
        # resume_file = request.FILES.get('resume_file')
        # job_description = request.POST.get('job_description')

        # resume_text = ''
        # if resume_file:
        #     if resume_file.name.endswith('.pdf'):
        #         resume_text = extract_text_from_pdf(resume_file)
        #     elif resume_file.name.endswith('.docx'):
        #         resume_text = extract_text_from_word(resume_file)
        #     else:
        #         resume_text = "Unsupported file format. Please upload a PDF or Word document."
        # else:
        #     resume_text = "No resume file uploaded."

    required_skills = ''
    required_skills = extract_skills(job_description)
    certifis=''
    certifis=get_certifications(required_skills,resume_text)
    roadmap=get_roadmap(certifis)
    #     return render(request, 'upload_resume_and_job_description.html', {
    #         'certifications': certifis,
    #         'roadmap': get_roadmap(certifis),  # Adjust job position as needed
    #         'resume_text': resume_text,
    #         'job_description': job_description,
    #     })

    # return render(request, 'upload_resume_and_job_description.html', {
    #     'form': ResumeUploadForm()
    # })

# urlpatterns = [
#     path('', upload_resume_and_job_description, name='upload_resume_and_job_description'),
# ]
    print(roadmap)
upload_resume_and_job_description()

