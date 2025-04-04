# Julian Secures **2nd Place out of 40+** in SMU's Research & Innovation Week Undergraduate Research Convention 

### Research Fair Blog - https://www.smu.edu/moody/events/research-and-innovation-week/undergraduate-poster-session

On April 1st, Julian won **2nd Place overall out of 40+ presenters** at the Annual SMU Research & Innovation Week Undergraduate Poster Session, winning a $200 Dollar Cash Prize. He was the **youngest on Podium, being a freshman** and was one of the only 3 freshmen to compete. Students presented their Mentor-Led research at the convention, with 20 judges rating every contestant’s poster. 

<img width="610" alt="image" src="https://github.com/user-attachments/assets/bc87b752-0fb8-4abf-8bc4-f76840e12d01" />


## Julian presented his & Dr.McGee's AI LLM Research & his created Poster: “From Prompts to Patterns: Exploring AI Responses with Text Analytics.” Faculty mentor: Monnie McGee, Statistics and Data Science”. 


Julian has worked throughout the year on this Research Project as an **Paid AI & Data Science Research Assistant** which will soon be **published in a journal**, and **Julian will be co-authored**. His research with Dr. McGee, “From Prompts to Patterns: Exploring AI Responses with Text Analytics” aims to uncover socioeconomic inequality in AI Access for Student Learning by comparing several free and paid LLMs/AI’s (OpenAI, Grok, Claude & Gemini) response accuracy and conciseness when being asked to compute Statistics/Math Exam questions. (Refer to Poster at bottom for more details).

## LLM Web App Research Implementation
### Julian stood out to judges by creating and implementing an LLM Statistics Comparator Web App on his Poster in a QR Code that leveraged Python, Flask, and React to use API Keys to compare LLMs on one Landing Page. Web App may or may not run globally due to the expiration of the API Keys (Cost of Web servicing) since the website cost was funded by the school for a temporary period.
**Click on Image or link below to watch the demo:**



[![Watch the video](https://img.youtube.com/vi/2gq0KdhBIhg/0.jpg)](https://www.youtube.com/watch?v=2gq0KdhBIhg)

https://www.youtube.com/watch?v=2gq0KdhBIhg




## Technologies Used in Statistics Comparator Web App:
### Frontend
React – Interactive UI for selecting questions and comparing LLM responses.

Axios – For making HTTP requests to the Flask backend.

CSS / Bootstrap – Custom and responsive styling.

Vercel – Hosting platform for frontend deployment.

### Backend
Flask – Python web framework serving the API endpoints.

Flask-CORS – Handling cross-origin requests between frontend and backend.

Python requests – Used to call external LLM APIs (Grok, Claude, Gemini).

dotenv – Securely loads API keys from environment variables.

Railway – Hosting platform for backend deployment.

### LLM Integrations
OpenAI (GPT-3.5 Turbo) – Prompted via the OpenAI Python SDK.

Anthropic Claude – Prompted via Claude API with HTTP requests.

xAI Grok – Integrated through the Grok API.

Google Gemini – Connected using the google.generativeai Python library.

Technologies Used in Research:

## Technologies Used in Research
### Programming & Libraries
Python – Core scripting language for automation and model evaluation.

R – Used for question reformatting and statistical preprocessing.

ellmer - LLM R Package

TidyVerse - R TidyVerse Package 

Microsoft Excel

dotenv – Secure management of API keys and environment variables.

requests – HTTP client for calling Claude, Grok, and Gemini APIs.

openai – Official SDK for OpenAI GPT integration.

pandas / numpy – Data manipulation and result analysis.

matplotlib / seaborn – Visualization of performance statistics.

### High-Performance Computing (HPC)
**SMU ManeFrame II (M3)** & **Nvidia Superpod** – HPC cluster used for batch processing of prompts.

SLURM – Job scheduler for parallel task execution.

Bash / Shell – Used to automate HPC job submissions and logging.

### LLM APIs
OpenAI GPT (gpt-3.5 / gpt-4)

Anthropic Claude-3 Sonnet

xAI Grok 2

Google Gemini 1.5 Flash
(All integrated using respective APIs or SDKs


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Backend (Flask API)

#### Dependencies
Make sure you have Python 3.9+ and `pip` installed.

#### Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

#### Install requirements
```bash
pip install -r requirements.txt
```

#### Set up environment variables
Create a `.env` file in the backend directory with your API keys:
```
OPENAI_API_KEY=your-openai-key
GOOGLE_API_KEY=your-google-api-key
ANTHROPIC_API_KEY=your-claude-key
XAI_API_KEY=your-grok-key
```

#### Run the Flask server
```bash
python app.py
```
Your backend will run locally at `http://localhost:5000`.

---

###  3. Frontend (React)

#### Install dependencies
```bash
cd frontend
npm install
```

#### Configure API endpoint
In `App.js`, make sure your backend URL is correct:
```js
axios.get("http://localhost:5000/api/questions")
```

####  Run the React app
```bash
npm start
```
The frontend will be served at `http://localhost:3000`.

---

### 4. Deployment

#### Frontend (Vercel)
1. Push your frontend code to GitHub.
2. Go to [vercel.com](https://vercel.com) and import your repo.
3. Deploy it as a static React app (Vercel auto-detects React).
4. Update API URLs in your React app to point to the Railway backend.

#### Backend (Railway)
1. Push your Flask backend to a separate GitHub repo or subdirectory.
2. Go to [railway.app](https://railway.app) and create a new Python project.
3. Add your API keys as environment variables in Railway.
4. Railway will deploy your Flask app and provide a public URL — copy that and update the React `axios` calls to use this endpoint.


