# Quick Deployment Commands for PythonAnywhere

## Initial Setup (Run Once)
```bash
# 1. Clone repository
git clone https://github.com/Suryareddy180/MasthiUpdatesWebsite.git
cd MasthiUpdatesWebsite

# 2. Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 mysite-virtualenv

# 3. Install dependencies
pip install -r requirements.txt

# 4. Collect static files
python manage.py collectstatic --noinput

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser
```

## Update Deployed App (When you make changes)
```bash
cd ~/MasthiUpdatesWebsite
git pull origin main
workon mysite-virtualenv
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
# Then reload web app from Web tab
```

## Important Paths for PythonAnywhere Web Configuration

**Source code:** `/home/YOUR_USERNAME/MasthiUpdatesWebsite`

**Working directory:** `/home/YOUR_USERNAME/MasthiUpdatesWebsite`

**Virtualenv:** `/home/YOUR_USERNAME/.virtualenvs/mysite-virtualenv`

**Static files:**
- URL: `/static/` → Directory: `/home/YOUR_USERNAME/MasthiUpdatesWebsite/staticfiles`
- URL: `/media/` → Directory: `/home/YOUR_USERNAME/MasthiUpdatesWebsite/media`

## Settings to Update in settings.py (On PythonAnywhere)

```python
DEBUG = False
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com']
```

## Troubleshooting Quick Fixes

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**500 Error:**
- Check error log on Web tab
- Verify ALLOWED_HOSTS includes your domain
- Check if migrations are run

**Module not found:**
```bash
pip install -r requirements.txt
```

---
Remember to replace YOUR_USERNAME with your actual PythonAnywhere username!
