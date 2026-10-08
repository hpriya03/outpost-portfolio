"""Every fact about Hari Priya, written once.

build.py and panels.py fill these into the artboard: the sidebar, the contact
panel, the bulletin board, the projects terminal, the skills archive, the studio
wall and the resume panel. Change something here, run python3 gen/build.py, and
nothing else holds a second copy.

Values starting /_blob/<id> are files in static/_blob/, named <id>.<ext>.
"""

# ---- who ----
NAME = "HARI PRIYA"
ROLE = "Software Engineer"
EMAIL = "itsharipriya8919@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/haripriya-pb/"
#: where the site is published; used for search engines and link previews
SITE_URL = "https://hpriya03.github.io/outpost-portfolio/"
#: set to "" to hide every GitHub button on the site
GITHUB_URL = "https://github.com/hpriya03"
#: the contact forms send through Web3Forms (web3forms.com) to EMAIL. This key is
#: meant to be public: it can only send messages to that inbox.
WEB3FORMS_KEY = "fa79334f-4c5b-452a-85da-909fd9d1e80e"
#: what Ping says at each place, in the world and on the phone view
PING_LINES = {
    "home": "Hi, I'm Ping! I'll be your guide around Hari Priya's outpost. Come on, let's dive in and explore!",
    "room": "Have a look around. There's plenty to explore.",
    "skills": "The shelf where Hari Priya keeps every skill. I dust it. I do not read it.",
    "projects": "Hari Priya's projects live in here. Still warm, still running.",
    "experience": "Hari Priya's journey so far, pinned up one note at a time.",
    "art": "This is the art wall. Hari Priya made all of it. I mostly supervised.",
    "contact": "Want to reach Hari Priya? Post it here. I handle deliveries personally.",
}
#: the line before Ping on the phone view: why there is a penguin here at all
PING_INTRO = "This portfolio is also a little underwater world you can explore."
#: what Ping says on the phone view where it differs from the world
PING_PHONE = {
    "hello": "Hi, I'm Ping! I look after this place. Want to explore the world with me, or take the quick tour right here?",
    "art": "When Hari Priya isn't building software, she's sketching and painting. Every piece here is hers. I mostly supervised.",
}
#: the availability line under the phone intro: the highlighted part, then the rest.
#: set AVAILABILITY to "" to hide the line
AVAILABILITY = "Open to new opportunities."
AVAILABILITY_MORE = "Let\u2019s build something great together!"
#: the short introduction on the phone view
INTRO = ("Hi \U0001F44B I'm a software engineer with 4+ years of experience building secure, scalable "
         "backend systems across healthcare, e-pharmacy and enterprise. I enjoy solving problems, "
         "debugging, experimenting, and exploring new things.")

# ---- the resume panel ----
#: the resume PDF, served by DOWNLOAD PDF
RESUME_PDF_BLOB = "/_blob/7fe732e1d0bb48f1f3f13a6611639ee3"
#: out/resume-page-N.png, the same PDF's pages as images (gen/resume_pages.js)
RESUME_PAGES = [
    "/_blob/4c393a6ebc471c6c6e614ac6ce62e427",
    "/_blob/66e1eb830f58de504e69d4e622db5651",
]

# ---- the cavern panels ----
#: the experience timeline, newest first. "skills" show with the bullets when a
#: role is opened; list only what was used in that role.
EXPERIENCE = [{'title': 'SOFTWARE DEVELOPMENT ENGINEER',
  'where': 'Tata 1mg · Bangalore',
  'dates': 'Oct 2022 to Jun 2025',
  'card': '#fdf8ec',
  'pin': '#dc2626',
  'skills': ['Ruby on Rails', 'PostgreSQL', 'AWS', 'SQS FIFO', 'Redis', 'Apache Kafka', 'Sidekiq',
             'Karafka', 'AWS DMS & MSK', 'RSpec'],
  'bullets': ["Built and maintained backend services for ODIN, Tata 1mg's in-house warehouse management "
              'platform, covering inventory, orders and purchasing across warehouses and retail stores',
              'Cut high-traffic API response times by 75% by optimising ActiveRecord queries and removing '
              'unnecessary database calls',
              "Processed each vendor's updates in order with AWS SQS FIFO queues and Redis-tracked retries, "
              'lifting inventory reconciliation accuracy 25%+ across 50+ vendors',
              'Automated purchase-order processing by connecting ODIN to finance (FAS) and SAP over REST, '
              '500+ B2B orders a month, with Sidekiq and Kafka keeping other services in sync',
              'Audit-logging pipeline on AWS DMS, MSK and Karafka recording every database change (what, '
              'who and when) across multiple tables in one central history',
              'Automated the Re-GRN (goods return) workflow with bulk SQL inserts: 40%+ less manual effort, '
              '15+ minutes saved per return',
              'Picker-to-Packer handover automation saving ₹6 lakh/month (~£4,600); contributed to the SKU '
              'barcoding rollout, saving ₹20 lakh (~£15,500) in manpower',
              'Resolved 15+ production incidents a month with Sentry, New Relic and Kibana; mentored 3+ '
              'junior engineers']},
 {'title': 'SOFTWARE ENGINEER',
  'where': 'Tata Digital Health · Bangalore',
  'dates': 'Jul 2021 to Oct 2022',
  'card': '#e6f1fb',
  'pin': '#2563eb',
  'skills': ['Java', 'Spring Boot', 'Spring Data JPA', 'Hibernate', 'MySQL', 'REST APIs', 'Single Sign-On'],
  'bullets': ['Backend REST APIs in Java, Spring Boot and Spring Data JPA/Hibernate with MySQL for a '
              'telemedicine platform running 1,000+ consultations a day, including digital prescriptions',
              'Clinical Decision Support (CDSS) features: demographic-based symptom prompts and doctor '
              'matching across 4+ languages, cutting consultation setup time by 15%',
              'Integrated Single Sign-On and appointment-reminder push notifications, and contributed to the '
              'paid e-consultation cart-to-order and payment flow']},
 {'title': 'SOFTWARE ENGINEERING INTERN',
  'where': 'Cognizant · India',
  'dates': 'Feb 2021 to Jun 2021',
  'card': '#fdeef3',
  'pin': '#dc2626',
  'skills': ['Java', 'Spring Boot', 'MVC', 'JUnit', 'Mockito', 'TDD'],
  'bullets': ['Built a full-stack application end to end: a Java and Spring Boot backend with a layered MVC '
              'design, applying OOP, SOLID and TDD with JUnit and Mockito',
              'Led a 4-member team through Agile/Scrum sprints and earned a return offer as Programmer '
              'Analyst Trainee']}]

#: the green card at the bottom of the board
EDUCATION_CARD = {'card': '#e8f7ea',
 'pin': '#16a34a',
 'title': 'EDUCATION',
 'org': ''}
EDUCATION = [{'degree': 'MSc Advanced Computer Science',
  'where': 'University of Manchester',
  'place': 'Manchester, UK',
  'dates': 'Sep 2025 to Sep 2026',
  'note': 'Global Future Scholarship'},
 {'degree': 'BTech Information Technology',
  'where': 'Sona College of Technology',
  'place': 'Tamil Nadu, India',
  'dates': 'Aug 2017 to Apr 2021',
  'note': 'CGPA 8.92 / 10'}]

#: the terminal in the projects hub
PROJECTS = [{'num': '01',
  'slug': 'nutrivision',
  'name': 'NUTRIVISION',
  'tag': 'MSc project',
  'desc': 'Fine-tuned BLIP-2 (Flan-T5-XL) for automated dietary assessment using LoRA, benchmarked across five '
          'tasks on the Nutrition5K dataset.',
  'desc2': 'Added a zero-cost inference-time pipeline that improved dietary reasoning with no extra '
           'training or parameters.',
  'stack': ['PyTorch', 'Hugging Face PEFT', 'BLIP-2', 'LoRA', 'Gradio']},
 {'num': '02',
  'slug': 'health-monitor',
  'name': 'HEALTHCARE MONITORING',
  'tag': 'Published · IJPRSE',
  'desc': "Full-stack app predicting a patient's health-risk level from biometrics: age, BMI, blood "
          'pressure, pulse and temperature.',
  'desc2': 'Decision Tree classifier with Pandas/NumPy preprocessing, served behind a Bootstrap interface '
           'for real-time classification.',
  'stack': ['Python', 'Flask', 'scikit-learn', 'Pandas']},
 {'num': '03',
  'slug': 'sentiment-lens',
  'name': 'SENTIMENT ANALYSIS',
  'tag': 'AFINN & WordNet',
  'desc': 'Python desktop app (Tkinter) fetching live tweets through the Twitter API (Tweepy) and '
          'classifying them positive, negative or neutral with the AFINN and WordNet/SentiWordNet lexicons.',
  'desc2': 'NLTK preprocessing (tokenisation, POS tagging, lemmatisation and stemming), with the sentiment '
           'distribution visualised as a pie chart in Matplotlib.',
  'stack': ['Python', 'Tkinter', 'Tweepy', 'NLTK', 'Matplotlib']},
 {'num': '04',
  'slug': 'healdroid',
  'name': 'HEALDROID',
  'tag': 'IoT Health Monitoring',
  'desc': 'IoT system using Arduino/ESP8266 to stream biometric data (heart rate, body temperature) to the '
          'ThingSpeak cloud over WiFi.',
  'desc2': 'Android mobile app in Java for real-time remote patient monitoring through the ThingSpeak API '
           'and JSON.',
  'stack': ['Arduino', 'ESP8266', 'ThingSpeak', 'Java', 'Android']}]

#: the skills archive panel: one shelf per group, one book per skill.
#: every book on a shelf shares the shelf's colour, so colour means group.
SKILL_SHELVES = [
    ("LANGUAGES", "#9f2b2b", ["Ruby", "Java", "Python", "SQL", "JavaScript"]),
    ("FRAMEWORKS", "#1e4f8a", ["Ruby on Rails", "Spring Boot", "Spring MVC", "Spring Data JPA", "Hibernate", "Flask"]),
    ("DATA & MESSAGING", "#2f6b3f", ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Apache Kafka", "SNS / SQS", "Sidekiq", "Karafka"]),
    ("ARCHITECTURE", "#8a5a12", ["Microservices", "Event-driven", "Distributed systems", "REST APIs", "MVC", "SOLID"]),
    ("CLOUD & DEVOPS", "#1f6b6b", ["AWS", "Docker", "Kubernetes", "Jenkins", "CI/CD", "Linux", "Bash"]),
    ("TESTING", "#6b3fa0", ["JUnit", "RSpec", "Mockito", "TDD"]),
    ("ML & AI", "#8a2f5e", ["PyTorch", "Hugging Face", "LLMs & VLMs", "PEFT / LoRA", "RAG", "FAISS / pgvector", "scikit-learn", "Pandas", "NumPy"]),
]
#: the line under the last shelf
SKILL_EXTRAS = ["Sentry", "New Relic", "Kibana", "CloudWatch", "Postman", "Swagger", "Git", "Bitbucket", "Jira", "Confluence",
                "Agile & Scrum", "NLTK", "Matplotlib"]

#: spines on the bookshelf
SKILL_BOOKS = ['RUBY',
 'RAILS',
 'JAVA',
 'SPRING',
 'PYTHON',
 'KAFKA',
 'REDIS',
 'SQL',
 'AWS',
 'DOCKER',
 'K8S',
 'TORCH',
 'LINUX',
 'GIT',
 'REST',
 'TDD']

#: the studio wall. alt text describes each piece for anyone using a screen reader.
#: "thumb" is a small copy (360px WebP) for the phone page; see README.
#: how many pieces the phone Studio shows, from the top of this list (even numbers fill the grid)
STUDIO_PHONE_COUNT = 8
ARTWORKS = [
    {"blob": "/_blob/8dfeba9369e2654443af72428647b461", "thumb": "/_blob/15c54d618fa70838180e6d33966d7358",
     "alt": "Profile of a girl in a ribbed beanie and scarf, ink and pencil"},
    {"blob": "/_blob/7115d2fdb7fceaaa9b9a22e98b719f94", "thumb": "/_blob/25ebea399987a979702e40a8a9ffbe5d",
     "alt": "A pug resting its head, graphite"},
    {"blob": "/_blob/d1b099a003622ad9dccdd2227f59f0e8", "thumb": "/_blob/823e73248d37097275892ea5f43a17d4",
     "alt": "Study of a neck and collarbone, graphite"},
    {"blob": "/_blob/cd799374d79c52c6b97c58ecf61efe7a", "thumb": "/_blob/cbac19ef1ff3f4327c1f0d317b321688",
     "alt": "Portrait of a woman looking to one side, graphite"},
    {"blob": "/_blob/1ba8a0057014a2a677da5d85e5df0775", "thumb": "/_blob/c9de59caf3356debc5b390a514c18916",
     "alt": "Baby Groot, ballpoint pen"},
    {"blob": "/_blob/f380847db4e0dcbb98d90a901d2aa3d3", "thumb": "/_blob/3d3c635f3f1163fe5301c01eabcea28b",
     "alt": "Sun and moon in facing triangles, watercolour"},
    {"blob": "/_blob/67a33b0efd81125a2d56326bd232a0bc", "thumb": "/_blob/77e79a72f01a60b7b95869b559380fcf",
     "alt": "Four face studies on one sketchbook page, pencil"},
    {"blob": "/_blob/ee5745887b8fae37ecd557113ecb8e19", "thumb": "/_blob/f3657c9fd471a52b56f5f006a862dffa",
     "alt": "Portrait with hair falling across the face, graphite"},
    {"blob": "/_blob/436c6c596e8e0ad7e8c4198c81331372", "thumb": "/_blob/70a02eafa8988484f8aabc03eeb59837",
     "alt": "A bird on a street lamp beneath a swirling sky, after Van Gogh, graphite"},
]
