# RENDER DEPLOYMENT GUIDE
## Elsheikh Mohamed | ID: 1001486517

---

## STEP 1: PUSH TO GITHUB (4 minutes)

### 1. Create GitHub Repository
- Go to: **https://github.com/new**
- Repository name: `text-processor-elsheikh-6517`
- Visibility: Public
- Click: **"Create repository"**

### 2. Push Code

Open Terminal:

```bash
# Navigate to project
cd ~/Downloads/text_processor_elsheikh_6517

# Initialize and push
git init
git add .
git commit -m "Text processor by Elsheikh Mohamed 6517"
git remote add origin https://github.com/YOUR_USERNAME/text-processor-elsheikh-6517.git
git branch -M main
git push -u origin main
```

**Note:** If asked for password, use Personal Access Token from https://github.com/settings/tokens

---

## STEP 2: DEPLOY TO RENDER (6 minutes)

### 1. Create Account
- Go to: **https://render.com**
- Sign up with GitHub

### 2. Create Web Service
- Click: **"New +"** → **"Web Service"**
- Connect: `text-processor-elsheikh-6517`

### 3. Configure

| Field | Value |
|-------|-------|
| Name | `text-processor-elsheikh-6517` |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Instance Type | Free |

### 4. Deploy
- Click: **"Create Web Service"**
- Wait 2-3 minutes

---

## YOUR LIVE URL
```
https://text-processor-elsheikh-6517.onrender.com
```

---

## TEST YOUR APP

### Question 10:
- S: `aei`
- T: `The cat is amazing`
- C: `*`

### Question 11:
- S: `bc`
- T: `Big cats chase birds`

### Question 12:
- S: `ab`
- T: `The apple is beautiful`
- Stop words: `the`, `is`

---

## SUBMISSION

```
Student: Elsheikh Mohamed
ID: 1001486517
URL: https://text-processor-elsheikh-6517.onrender.com
```

Good luck! 🚀
