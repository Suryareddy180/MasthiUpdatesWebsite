---
description: Deploy local changes to PythonAnywhere production
---

# Deploy to Production (PythonAnywhere)

Follow these steps whenever you make changes locally and want to deploy them to your production website at **masthiupdates1.pythonanywhere.com**.

## Step 1: Commit Changes Locally

```bash
# Check what files have changed
git status

# Add all changed files (or specify individual files)
git add .

# Commit with a descriptive message
git commit -m "Your descriptive commit message here"
```

**Example commit messages:**
- `"Fix timezone configuration for IST"`
- `"Redesign 404 error page with better contrast"`
- `"Add new blog post feature"`

## Step 2: Push to GitHub

```bash
# Push changes to your GitHub repository
git push origin main
```

**Note:** Make sure you're pushing to the correct branch (usually `main` or `master`).

## Step 3: Update Production Server

### Option A: Using PythonAnywhere Web Console (Recommended)

1. Go to https://www.pythonanywhere.com and log in
2. Click on the **Consoles** tab
3. Start a new **Bash console** (or use an existing one)
4. Run these commands:

```bash
# Navigate to your project directory
cd ~/MasthiUpdatesWebsite

# Pull the latest changes from GitHub
git pull origin main

# If you made changes to static files (CSS, JS, images)
python manage.py collectstatic --noinput

# If you made database model changes
python manage.py makemigrations
python manage.py migrate
```

### Option B: Using SSH (if enabled)

```bash
ssh masthiupdates1@ssh.pythonanywhere.com
cd ~/MasthiUpdatesWebsite
git pull origin main
python manage.py collectstatic --noinput
# Exit SSH
exit
```

## Step 4: Reload Web Application

1. Go to the **Web** tab in PythonAnywhere
2. Find your web app: `masthiupdates1.pythonanywhere.com`
3. Click the green **Reload** button (usually at the top right)

> **CRITICAL:** The reload is REQUIRED for changes to take effect!

## Step 5: Verify Deployment

1. Visit your website: https://masthiupdates1.pythonanywhere.com
2. Test the changes you made
3. Check the error log if something doesn't work:
   - Go to **Web** tab → **Log files** → **Error log**

## Quick Reference Commands

### For Template/Python Changes Only
```bash
# Local
git add .
git commit -m "Description"
git push origin main

# PythonAnywhere Console
cd ~/MasthiUpdatesWebsite
git pull origin main
# Then reload web app via Web tab
```

### For Static File Changes (CSS/JS/Images)
```bash
# Local
git add .
git commit -m "Description"
git push origin main

# PythonAnywhere Console
cd ~/MasthiUpdatesWebsite
git pull origin main
python manage.py collectstatic --noinput
# Then reload web app via Web tab
```

### For Database Model Changes
```bash
# Local
git add .
git commit -m "Description"
git push origin main

# PythonAnywhere Console
cd ~/MasthiUpdatesWebsite
git pull origin main
python manage.py makemigrations
python manage.py migrate
# Then reload web app via Web tab
```

## Common Issues & Solutions

### Issue: Changes not appearing after reload
**Solution:** Clear your browser cache (Ctrl+F5) or try incognito mode

### Issue: Static files not updating
**Solution:** Run `python manage.py collectstatic --noinput` on PythonAnywhere

### Issue: Git pull conflicts
**Solution:** 
```bash
# Stash local changes on server
git stash
git pull origin main
git stash pop
```

### Issue: Permission errors
**Solution:** Check file permissions or contact PythonAnywhere support

## Important Notes

- **Always test locally** before deploying to production
- **Backup your database** before major changes
- **Check error logs** if something breaks after deployment
- **Don't edit files directly** on PythonAnywhere - always use Git workflow
- **Settings.py changes** require web app reload to take effect
- **Template changes** require web app reload (Django caches templates)

## Emergency Rollback

If deployment breaks something:

```bash
# On PythonAnywhere Console
cd ~/MasthiUpdatesWebsite
git log  # Find the last working commit hash
git reset --hard <commit-hash>
# Then reload web app
```
