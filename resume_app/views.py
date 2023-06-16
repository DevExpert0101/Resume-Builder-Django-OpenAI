from django.shortcuts import render, redirect
import json
import openai

openai.api_key = "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"
messages = []

def complete_content(content):
    # Retrieve the values of the dynamically generated work experience fields
    work_experience_values = {}
    edu_experience_values = {}
    name, title, summary, skills = "", "", "", ""

    # print(request.POST.items())
    # for key, value in request.POST.items():
        # print(key, '--', value)
    for key, value in content:
        if key.startswith('workTitle') or key.startswith('workCompany') or key.startswith('workDate') or key.startswith('workDescription'):
            field_name, field_index = key.split('_', 1)  # Split the key into name and index
            if field_index not in work_experience_values:
                work_experience_values[field_index] = {}  # Create a dictionary for the index if it doesn't exist
            work_experience_values[field_index][field_name] = value
        
        if key.startswith('eduDegree') or key.startswith('eduSchool') or key.startswith('eduDate') or key.startswith('eduDescription'):
            field_name, field_index = key.split('_', 1)  # Split the key into name and index
            if field_index not in edu_experience_values:
                edu_experience_values[field_index] = {}  # Create a dictionary for the index if it doesn't exist
            edu_experience_values[field_index][field_name] = value
        
        if key.startswith('name'):
            name = value
        if key.startswith('title'):
            title = value
        if key.startswith('address'):
            address = value
        if key.startswith('email'):
            email = value
        if key.startswith('github'):
            github = value
        if key.startswith('linkedin'):
            linkedin = value
        if key.startswith('phone'):
            phone = value
        if key.startswith('summary'):
            summary = value
        if key.startswith('skills'):
            skills = value

        
    
    # Process the values and generate the resume
    
    # Pass the processed values to the template
    context = {
        'name': name,
        'title': title,
        'address': address,
        'email': email,
        'github': github,
        'linkedin': linkedin,
        'phone': phone,
        'summary': summary,
        'skills': skills,
        'work_experience_values': work_experience_values,
        'edu_experience_values': edu_experience_values,
        # Add other processed values as needed
    }

    message = json.dumps(context)
    messages.append({"role": "system", "content": message})
    messages.append({"role": "user", "content": """
                Please generate professional resume contents with above information.
                It should be the professional format.
                Please modify all of contents with state-of-the-art techs and methodologies.
                Add more information to summary and work experience.
                Answer should contain Name, Address, Gmail, Linkedin, Summary, Experience, Skills, Projects and Education parts and also JSON format like this:
                {
                    "name" : "Paht",
                    "title" : "Senior ML engineer", 
                    "summary": "Passionate about building websites with AI features.",
                    "workExperience":[ 
                        {
                            "dates": "05/2012 - 12/2020",
                            "company": "XOOJ",
                            "title": "Machine Learning Engineer",
                            "description": ["Expertized in establishing MLOps pipeline for projects and ML algorithms including regression, classification, clustering.", 
                                "Skillfully experienced with various types of ML algorithms, fine-tuning of hyperparameters, weight optimization.",
                                "Professionally experienced with AWS Lambda, Sagemaker, Kinesis, Firehose, Glue, Athena, EKS, EMR, Redshift, CodeBuild, CodeCommit and led as a technical advisor.",
                                "Experienced with Generative AI including ChatGPT, GPT4, Stable Diffusion, Midjourney and TTS, STT."]
                        },
                        {
                            "dates": "01/2021 - 12/2022",
                            "company": "Microsoft",
                            "title": "Senior Machine Learning Engineer",
                            "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
                                "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
                                "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
                        },
                        {
                            "dates": "01/2021 - 12/2022",
                            "company": "Microsoft",
                            "title": "Senior Machine Learning Engineer",
                            "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
                                "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
                                "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
                        }
                    ]
                    ,
                    "contactInfo": 
                        {
                            "address": "abc street",
                            "email": "john@gmail.com",
                            "github": "github.com/devexpert0101",
                            "linkedin": "linkedin.com/in/Paht",
                            "phone": "+12316512245"
                        }
                    ,
                    "education": [
                        {
                            "dates": "04/2010 - 06/2014",
                            "school": "University of Pennsylvania",
                            "degree": "Bachelor's Degree of Computer Science",
                            "description": ""
                        }
                    ]
                    ,
                    "skills" : ["Python", "C++" ,"C#", "HTML", "CSS", "Java", "JavaScript"]
                    }
        """})
    
    chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo', messages=messages
        )

    reply = chat.choices[0].message.content


    jsondata = json.loads(reply)


    tmpdata = {
                    "name" : "Paht",
                    "title" : "Senior ML engineer", 
                    "summary": "Passionate about building websites with AI features.",
                    "workExperience":[ 
                        {
                            "dates": "05/2012 - 12/2020",
                            "company": "XOOJ",
                            "title": "Machine Learning Engineer",
                            "description": ["Expertized in establishing MLOps pipeline for projects and ML algorithms including regression, classification, clustering.", 
                                "Skillfully experienced with various types of ML algorithms, fine-tuning of hyperparameters, weight optimization.",
                                "Professionally experienced with AWS Lambda, Sagemaker, Kinesis, Firehose, Glue, Athena, EKS, EMR, Redshift, CodeBuild, CodeCommit and led as a technical advisor.",
                                "Experienced with Generative AI including ChatGPT, GPT4, Stable Diffusion, Midjourney and TTS, STT."]
                        },
                        {
                            "dates": "01/2021 - 12/2022",
                            "company": "Microsoft",
                            "title": "Senior Machine Learning Engineer",
                            "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
                                "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
                                "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
                        },
                        {
                            "dates": "01/2021 - 12/2022",
                            "company": "Microsoft",
                            "title": "Senior Machine Learning Engineer",
                            "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
                                "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
                                "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
                        }
                    ]
                    ,
                    "contactInfo": 
                        {
                            "address": "abc street",
                            "email": "john@gmail.com",
                            "github": "github.com/devexpert0101",
                            "linkedin": "linkedin.com/in/Paht",
                            "phone": "+12316512245"
                        }
                    ,
                    "education": [
                        {
                            "dates": "04/2010 - 06/2014",
                            "school": "University of Pennsylvania",
                            "degree": "Bachelor's Degree of Computer Science",
                            "description": ""
                        }
                    ]
                    ,
                    "skills" : ["Python", "C++" ,"C#", "HTML", "CSS", "Java", "JavaScript"]
                    }

    return tmpdata

def index(request):
    return render(request, 'resume_app/index.html')

def generate_resume1(request):
    if request.method == 'POST':

        # print(request.body.decode('utf-8'))
        jsondata = complete_content(request.POST.items())
        # # Retrieve the values of the dynamically generated work experience fields
        # work_experience_values = {}
        # edu_experience_values = {}
        # name, title, summary, skills = "", "", "", ""

        # # print(request.POST.items())
        # # for key, value in request.POST.items():
        #     # print(key, '--', value)
        # for key, value in request.POST.items():
        #     if key.startswith('workTitle') or key.startswith('workCompany') or key.startswith('workDate') or key.startswith('workDescription'):
        #         field_name, field_index = key.split('_', 1)  # Split the key into name and index
        #         if field_index not in work_experience_values:
        #             work_experience_values[field_index] = {}  # Create a dictionary for the index if it doesn't exist
        #         work_experience_values[field_index][field_name] = value
            
        #     if key.startswith('eduDegree') or key.startswith('eduSchool') or key.startswith('eduDate') or key.startswith('eduDescription'):
        #         field_name, field_index = key.split('_', 1)  # Split the key into name and index
        #         if field_index not in edu_experience_values:
        #             edu_experience_values[field_index] = {}  # Create a dictionary for the index if it doesn't exist
        #         edu_experience_values[field_index][field_name] = value
            
        #     if key.startswith('name'):
        #         name = value
        #     if key.startswith('title'):
        #         title = value
        #     if key.startswith('address'):
        #         address = value
        #     if key.startswith('email'):
        #         email = value
        #     if key.startswith('github'):
        #         github = value
        #     if key.startswith('linkedin'):
        #         linkedin = value
        #     if key.startswith('phone'):
        #         phone = value
        #     if key.startswith('summary'):
        #         summary = value
        #     if key.startswith('skills'):
        #         skills = value

            
        
        # # Process the values and generate the resume
        
        # # Pass the processed values to the template
        # context = {
        #     'name': name,
        #     'title': title,
        #     'address': address,
        #     'email': email,
        #     'github': github,
        #     'linkedin': linkedin,
        #     'phone': phone,
        #     'summary': summary,
        #     'skills': skills,
        #     'work_experience_values': work_experience_values,
        #     'edu_experience_values': edu_experience_values,
        #     # Add other processed values as needed
        # }

        # message = json.dumps(context)
        # messages.append({"role": "system", "content": message})
        # messages.append({"role": "user", "content": """
        #             Please generate professional resume contents with above information.
        #             It should be the professional format.
        #             Please modify all of contents with state-of-the-art techs and methodologies.
        #             Add more information to summary and work experience.
        #             Answer should contain Name, Address, Gmail, Linkedin, Summary, Experience, Skills, Projects and Education parts and also JSON format like this:
        #             {
        #                 "name" : "Paht",
        #                 "title" : "Senior ML engineer", 
        #                 "summary": "Passionate about building websites with AI features.",
        #                 "workExperience":[ 
        #                     {
        #                         "dates": "05/2012 - 12/2020",
        #                         "company": "XOOJ",
        #                         "title": "Machine Learning Engineer",
        #                         "description": ["Expertized in establishing MLOps pipeline for projects and ML algorithms including regression, classification, clustering.", 
        #                             "Skillfully experienced with various types of ML algorithms, fine-tuning of hyperparameters, weight optimization.",
        #                             "Professionally experienced with AWS Lambda, Sagemaker, Kinesis, Firehose, Glue, Athena, EKS, EMR, Redshift, CodeBuild, CodeCommit and led as a technical advisor.",
        #                             "Experienced with Generative AI including ChatGPT, GPT4, Stable Diffusion, Midjourney and TTS, STT."]
        #                     },
        #                     {
        #                         "dates": "01/2021 - 12/2022",
        #                         "company": "Microsoft",
        #                         "title": "Senior Machine Learning Engineer",
        #                         "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
        #                             "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
        #                             "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
        #                     },
        #                     {
        #                         "dates": "01/2021 - 12/2022",
        #                         "company": "Microsoft",
        #                         "title": "Senior Machine Learning Engineer",
        #                         "description": ["Implemented Cloud based 10+ Machine Learning projects with the combination of coding, relational database, MySQL, Oracle, Computer Science, NLP and data-driven projects such as AI Poster, CRM and Recommendation System. ",
        #                             "Fully experienced with several data formats and over 4 ETL, ELT tools. ",
        #                             "Completed 10+ Deep Learning based computer vision, NLP projects using frameworks such as Tensorflow, PyTorch, Yolo Model and successfully deployed 5+ large-scale production AI solutions."]
        #                     }
        #                 ]
        #                 ,
        #                 "contactInfo": 
        #                     {
        #                         "address": "abc street",
        #                         "email": "john@gmail.com",
        #                         "github": "github.com/devexpert0101",
        #                         "linkedin": "linkedin.com/in/Paht",
        #                         "phone": "+12316512245"
        #                     }
        #                 ,
        #                 "education": [
        #                     {
        #                         "dates": "04/2010 - 06/2014",
        #                         "school": "University of Pennsylvania",
        #                         "degree": "Bachelor's Degree of Computer Science",
        #                         "description": ""
        #                     }
        #                 ]
        #                 ,
        #                 "skills" : ["Python", "C++" ,"C#", "HTML", "CSS", "Java", "JavaScript"]
        #                 }
        #     """})
        
        # chat = openai.ChatCompletion.create(
        #         model='gpt-3.5-turbo', messages=messages
        #     )

        # reply = chat.choices[0].message.content


        # jsondata = json.loads(reply)
        
        # Render the resume template with the processed values
        return render(request, 'resume_app/resume1.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume2(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume2.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume3(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume3.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume4(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume4.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume5(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume5.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume6(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume6.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume7(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume7.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume8(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume8.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume9(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume9.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume10(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume10.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume11(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume11.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume12(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume12.html', jsondata)
    else:
        return redirect('resume_app:index')
    
def generate_resume13(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume13.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume14(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume14.html', jsondata)
    else:
        return redirect('resume_app:index')

def generate_resume15(request):
    if request.method == "POST":
        content = request.POST.items()
        jsondata = complete_content(content)
        return render(request, 'resume_app/resume15.html', jsondata)
    else:
        return redirect('resume_app:index')