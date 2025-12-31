# PythonAnywhere Deployment Guide for Masthi Updates

## Prerequisites Checklist ✅
- [x] Updated requirements.txt
- [x] Removed db.sqlite3 from .gitignore
- [x] Removed media from .gitignore
- [x] Added STATIC_ROOT to settings.py
- [x] Code pushed to GitHub

---

## Step-by-Step Deployment Instructions

### 1️⃣ Initial Setup on PythonAnywhere

1. **Create Account**
   - Go to [pythonanywhere.com](https://www.pythonanywhere.com)
   - Sign up for a free account (or login if you have one)

2. **Open Bash Console**
   - Click on "Consoles" tab
   - Click "Bash" to open a new bash console

### 2️⃣ Clone Your Repository

```bash
# Clone your repository
git clone https://github.com/Suryareddy180/MasthiUpdatesWebsite.git

# Navigate to the project directory
cd MasthiUpdatesWebsite

# Verify files are present
ls
```

### 3️⃣ Create Virtual Environment

```bash
# Create virtual environment with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv

# Activate the virtual environment (it should activate automatically)
workon mysite-virtualenv

# Install all dependencies
pip install -r requirements.txt
```

**Note:** If you get errors about specific packages, you may need to install them individually.

### 4️⃣ Configure Web App

1. **Create Web App**
   - Click on "Web" tab (open in new tab)
   - Click "Add a new web app"
   - Click "Next" on the domain name page
   - Select "Manual configuration" (NOT Django wizard)
   - Select **Python 3.10**
   - Click "Next"

2. **Configure Code Section**
   
   **Source code:** `/home/YOUR_USERNAME/MasthiUpdatesWebsite`
   
   **Working directory:** `/home/YOUR_USERNAME/MasthiUpdatesWebsite`

3. **Configure Virtual Environment**
   
   **Virtualenv:** `/home/YOUR_USERNAME/.virtualenvs/mysite-virtualenv`

### 5️⃣ Configure WSGI File

Click on the WSGI configuration file link and replace its contents with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/MasthiUpdatesWebsite'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_main.settings'

# Activate virtual environment
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** Replace `YOUR_USERNAME` with your actual PythonAnywhere username!

### 6️⃣ Configure Static Files

In the **Static files** section on the Web tab, add:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/YOUR_USERNAME/MasthiUpdatesWebsite/staticfiles` |
| `/media/` | `/home/YOUR_USERNAME/MasthiUpdatesWebsite/media` |

### 7️⃣ Collect Static Files

Go back to your Bash console and run:

```bash
# Make sure you're in the project directory
cd ~/MasthiUpdatesWebsite

# Activate virtual environment
workon mysite-virtualenv

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser (optional, if you want a new admin account)
python manage.py createsuperuser
```

### 8️⃣ Update Settings for Production

**IMPORTANT:** Before deploying, you need to update `settings.py`:

1. Go to the "Files" tab on PythonAnywhere
2. Navigate to `/home/YOUR_USERNAME/MasthiUpdatesWebsite/blog_main/settings.py`
3. Update these settings:

```python
# Change DEBUG to False
DEBUG = False

# Add your PythonAnywhere domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']

# Optional: Add WhiteNoise for better static file serving
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    # ... rest of middleware
]
```

### 9️⃣ Reload Web App

1. Go back to the "Web" tab
2. Click the big green **"Reload YOUR_USERNAME.pythonanywhere.com"** button
3. Wait for it to reload (about 10-20 seconds)

### 🔟 Test Your Deployment

1. Click on the link to your site: `https://YOUR_USERNAME.pythonanywhere.com`
2. Test the following:
   - ✅ Homepage loads correctly
   - ✅ Static files (CSS, JS, images) are working
   - ✅ Dark/Light mode toggle works
   - ✅ Blog posts display correctly
   - ✅ Admin panel accessible at `/admin/`
   - ✅ Dashboard accessible at `/dashboard/`

---

## Troubleshooting

### Static Files Not Loading
```bash
# Re-collect static files
python manage.py collectstatic --noinput

# Check STATIC_ROOT in settings.py
# Make sure it points to: BASE_DIR / 'staticfiles'
```

### ImportError or Module Not Found
```bash
# Reinstall requirements
pip install -r requirements.txt

# Check if virtual environment is activated
workon mysite-virtualenv
```

### 500 Internal Server Error
1. Check error log on PythonAnywhere Web tab
2. Look for the error log link
3. Common issues:
   - ALLOWED_HOSTS not configured
   - Database migrations not run
   - Missing environment variables

### Database Issues
```bash
# Run migrations again
python manage.py migrate

# Check if db.sqlite3 exists
ls -la db.sqlite3
```

---

## Post-Deployment Checklist

- [ ] Site loads successfully
- [ ] All static files working (CSS, JS, images)
- [ ] Admin panel accessible
- [ ] Dashboard accessible
- [ ] User registration works
- [ ] Login/Logout works
- [ ] Blog posts display correctly
- [ ] Comments functionality works
- [ ] Dark/Light mode toggle works
- [ ] Media files (uploaded images) display correctly

---

## Updating Your Deployed App

When you make changes to your code:

```bash
# SSH into PythonAnywhere bash console
cd ~/MasthiUpdatesWebsite

# Pull latest changes from GitHub
git pull origin main

# Activate virtual environment
workon mysite-virtualenv

# Install any new dependencies
pip install -r requirements.txt

# Run migrations if models changed
python manage.py migrate

# Collect static files if CSS/JS changed
python manage.py collectstatic --noinput

# Then reload your web app from the Web tab
```

---

## Important Notes

⚠️ **Free Account Limitations:**
- Your app will sleep after 3 months of inactivity
- Limited CPU time per day
- One web app only
- No scheduled tasks

💡 **Tips:**
- Keep DEBUG = False in production
- Use environment variables for sensitive data
- Regularly backup your database
- Monitor error logs for issues

🎉 **Congratulations!** Your Masthi Updates blog is now live on PythonAnywhere!

---

## Support

If you encounter issues:
- Check PythonAnywhere forums
- Review error logs on the Web tab
- Consult Django documentation
- Check your GitHub repository for any missing files
