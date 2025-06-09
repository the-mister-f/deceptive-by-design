# 🕵️‍♂️ Deceptive by Design: Assessing the Impact of UX Dark Patterns on Engagement and Trust in Digital Products

This repository accompanies the bachelor thesis:  
**"Deceptive by Design: Assessing the Impact of UX Dark Patterns on Engagement and Trust in Digital Products"**  
by **Firas Najar** (submitted April 11, 2025). It contains the experimental materials, prototypes, and scripts used to evaluate how UX dark patterns influence user behavior and perceived trust.<br><br>



## 📘 Overview

In today’s world of digital product design, data plays a critical role in shaping how user interfaces are developed. Instead of focusing on usability and creating userfriendly interfaces, companies are shifting towards manipulative designs that influence user behavior in ways that benefit the business. This often leads to users spending more money, sharing more personal data, or making unintended decisions. These tactics, known as dark patterns, take advantage of cognitive biases in an attempt to boost short-term engagement at the expense of the user’s autonomy. This thesis conducts an extensive literature review to trace the origins of dark patterns, their taxonomies, and their effects on engagement and trust.

To investigate these effects further, **a controlled online experiment** was carried out using a prototype of a nutrition-tracking app. Participants were randomly assigned to one of three interface versions:

- ✅ **Control Group** – Transparent, user-friendly UX
- ⚠️ **Mild Group** – Subtle dark patterns
- ❌ **Extreme Group** – Aggressive dark patterns

Key findings include:
- Dark patterns **significantly increased engagement** (e.g., more sign-ups and data sharing)
- **Trust decreased**, especially in emotionally and transactionally sensitive areas
- **Digitally literate users were more resistant** to manipulation<br><br>


## 📄 Thesis Download
📘 [Download the Full Thesis (PDF)](https://drive.google.com/uc?export=download&id=1JUnWZIoZGqYONHjEL_yZu_EZ7qdZIZ8f)<br><br>


## 🤝 Acknowledgments

- Benjamin Gülker — First Supervisor
- Prof. Dr. Christoph Dörrenbächer — Second Supervisor
- Wael Amri — Backend development & technical support<br><br>

## 🧪 Experimental Design

The experiment was implemented using **Flask**, a lightweight Python web framework. It served as the backend for managing routing, rendering templates, logging user interactions, and storing data.<br><br>
### Structure:

- 📁 /templates/survey/ → HTML files for the survey questions
- 📁 /templates/prototype/ → HTML files for the prototype
- 📁 /static/ → Assets, CSS and JS files for styling and dynamic behavior
- 📁 /main.py → Flask application logic (routing, experiment assignment, logging)


### Backend Features

- Randomized group assignment via session id
- Logging of click events, form submissions, and engagement milestones
- Post-interaction survey on trust, engagement, and digital competence
- Secure handling of participant IDs and anonymized data storag<br><br>


## 📬 Contact
For any questions or collaborations, feel free to contact me:
- 📧 hello@firas.me
- 🌐 [Linkedin](https://www.linkedin.com/in/najarfiras/)
