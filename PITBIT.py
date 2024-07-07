
### parse_resume.py
```python
import openai
import json
import os
import sys

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_resume(resume_text):
    prompt = f"""
    Please parse the following resume content into JSON format. The JSON should include sections for personal information, education, work experience, skills, and any other relevant categories.

    Resume:
    ---
    {resume_text}
    ---

    JSON format:
    {{
        "personal_information": {{
            "name": "",
            "address": "",
            "phone": "",
            "email": ""
        }},
        "education": [
            {{
                "degree": "",
                "institution": "",
                "graduation_year": ""
            }}
        ],
        "work_experience": [
            {{
                "job_title": "",
                "company": "",
                "start_date": "",
                "end_date": "",
                "responsibilities": ""
            }}
        ],
        "skills": [
            ""
        ],
        "certifications": [
            {{
                "name": "",
                "issuer": "",
                "issue_date": ""
            }}
        ],
        "projects": [
            {{
                "name": "",
                "description": "",
                "technologies": []
            }}
        ]
    }}
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1500
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_resume.py path/to/your_resume.txt")
        sys.exit(1)

    resume_path = sys.argv[1]

    with open(resume_path, 'r') as file:
        resume_text = file.read()

    parsed_resume = parse_resume(resume_text)

    with open('parsed_resume.json', 'w') as json_file:
        json_file.write(parsed_resume)

    print("Parsed resume saved to parsed_resume.json")
