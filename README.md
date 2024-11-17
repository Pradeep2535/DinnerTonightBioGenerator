# 🌟 Bio Generator Web Application

A Flask-based web application that generates personalized bios based on user input such as career, interests, personality traits, and relationship goals. The application utilizes the **Gemini API**'s Structured Prompt API for content generation and is hosted on **Vercel**. 🚀

---

## ✨ Features

- **🖥️ User-Friendly Interface**: A responsive frontend built with HTML, CSS, and JavaScript.
- **🤖 Dynamic Bio Generation**: Powered by the Gemini Structured Prompt API for personalized content creation.
- **🌐 Cross-Platform Deployment**: Deployed on **Vercel** for fast and reliable hosting.

---

## 🌍 Demo

Check out the live application: [Bio Generator](https://dinnertonight-6wtz8i1l3-pradeep-ss-projects-eef2a107.vercel.app/)

---

## 🛠️ Technologies Used

### Backend:
- **🐍 Python**: Core programming language.
- **🍃 Flask**: Lightweight web framework to manage the server-side application.
- **✨ Gemini API**: For generating dynamic and contextually relevant bios.

### Frontend:
- **📄 HTML5**: Structure of the web application.
- **🎨 CSS3**: Styling and layout, including responsive design.
- **⚡ JavaScript**: For enhancing interactivity and user experience.

### Hosting:
- **☁️ Vercel**: Deployment platform for hosting the application.

---

## 📦 Installation and Setup

### Prerequisites
- ✅ Python 3.x
- ✅ Vercel CLI (for deployment)
- ✅ A Gemini API key

### 🗂️ Project Structure

DinnerTonightBioGenerator/
├── model/
│   ├── gemini_model.py      # Custom module for interacting with Gemini API
│   ├── secrets.env          # Environment variables (for local use only)
├── templates/
│   ├── index.html           # Frontend HTML file
├── static/
│   ├── css/                 # CSS stylesheets
│   ├── js/                  # JavaScript files
├── app.py                   # Flask application entry point
├── vercel.json              # Vercel deployment configuration
├── requirements.txt         # Python dependencies

