# 📰 Financial News AutoPoster (MVP)

This project is a **proof-of-concept automation tool** that:

- Scrapes the latest news from **Financial Times**
- Uses **OpenAI GPT-4o** to rewrite each story into a short, engaging social media post.
- Logs every step
- Outputs results to console and JSON
---

## Project Goals

#### ✅ Ingest real-world financial headlines  
#### ✅ Rewrite them using GPT in our brand's tone  
#### ✅ Output usable copy for social platforms  
#### ✅ Handle failures gracefully and log the flow
---

## 🔐 .env File Setup

Create a `.env` file in the root directory with the following:

```env
OPENAI_API_KEY=your_openai_api_key_here
```
---

## ⚙️ Installation (Recommended: Virtual Environment)
### Step 1: Create and activate a virtual environment
``` bash
# Create venv (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# or on Windows
python -m venv venv
venv\Scripts\activate
```
---
### Step 2: Install dependencies
``` bash
pip install -r requirements.txt
```
---
## 💻 How to Run the Project
``` bash
python main.py
# or
python3 main.py
```
---
