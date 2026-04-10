# 📊 Reddit Engagement Dashboard

A Python-powered automated system that tracks the most relevant discussions on **r/n8n** and **r/automation**, calculating real-time engagement and displaying results in a premium, responsive web dashboard.

## 🚀 Features
- **Auto-Fetching**: Retrieves the 100 most recent posts from targeted subreddits.
- **Engagement Analysis**: Calculates a custom engagement score based on (Upvotes + Comments).
- **Auto-Translation**: Automatically translates trending post titles to Portuguese (PT-BR) for better readability.
- **Automated Updates**: Integrated with **GitHub Actions** to refresh data daily without manual intervention.
- **Premium Dashboard**: A modern, tabbed interface to visualize the Top 5 most engaging posts per category.

## 🧠 About the Project
This project was designed to bridge the gap between community-driven insights and automated data processing. By scraping Reddit's public API endpoints and applying a ranking algorithm, it identifies what truly matters in the automation community right now. 
The main goal is to showcase the integration between **Python backend logic** (data processing) and **Frontend visualization** (HTML/JS/CSS), all while keeping the data fresh through a CI/CD pipeline.

## 🏗️ Project Structure
```
reddit-automation-app/
├── .github/workflows/
│   └── update_data.yml      # CI/CD pipeline for auto-updates
├── dashboard/
│   ├── src/data/posts.json  # Processed data
│   ├── index.html           # Main dashboard UI
│   ├── style.css            # Premium styling
│   └── app.js               # Frontend logic
├── execution/
│   └── fetch_reddit_posts.py # Core Python bot
├── requirements.txt         # Dependencies
└── .gitignore               # Security & cleanup
```

## ⚙️ Technologies Used
- **Python**: Data fetching, ranking algorithm, and translation.
- **JavaScript (Vanilla)**: Dynamic UI rendering and tab management.
- **CSS3**: Modern layout with glassmorphism and animations.
- **GitHub Actions**: Daily automation and data persistence.
- **Google Translator API**: via `deep-translator` for localization.

## ▶️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/danidds07/reddit-automation-app.git
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Fetch latest data
```bash
python execution/fetch_reddit_posts.py
```

### 4. Open the Dashboard
To avoid CORS issues when fetching the JSON file, run a local server:
```bash
# Using Python
python -m http.server 8000 -d docs
```
Then visit `http://localhost:8000` in your browser.

## 🎯 Purpose
Created for portfolio purposes to demonstrate proficiency in:
- API integration without complex OAuth (using public endpoints).
- Data processing and ranking logic.
- Automated workflows (CI/CD).
- Web design with a focus on User Experience (UX).

## 📈 Future Improvements
- [ ] Add support for more subreddits via configuration file.
- [ ] Implement sentiment analysis on the top comments.
- [ ] Add an "Official Reddit API" mode (OAuth) for high-frequency updates.
- [ ] Create email/telegram alerts for extremely high-engagement posts.

## 👨‍💻 Author
Developed by **Daniel Augusto Silva** (danidds07)

---
⭐ If you find this project interesting, feel free to give it a star!
