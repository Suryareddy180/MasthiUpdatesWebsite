# Quick Deployment Reference

## Standard 3-Step Deployment Process

### 1️⃣ Local: Commit & Push
```bash
git add .
git commit -m "Your change description"
git push origin main
```

### 2️⃣ PythonAnywhere: Pull Changes
```bash
cd ~/MasthiUpdatesWebsite
git pull origin main
```

**If static files changed (CSS/JS/images):**
```bash
python manage.py collectstatic --noinput
```

**If models changed:**
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3️⃣ PythonAnywhere: Reload Web App
- Go to **Web** tab
- Click green **Reload** button

---

## Access PythonAnywhere
- **URL:** https://www.pythonanywhere.com
- **Console:** Consoles tab → Bash console
- **Project Path:** `~/MasthiUpdatesWebsite`

---

## Common Commands

| Change Type | Extra Command Needed |
|------------|---------------------|
| Templates (.html) | None - just reload |
| Python code (.py) | None - just reload |
| Static files (CSS/JS) | `collectstatic --noinput` |
| Models (models.py) | `makemigrations` + `migrate` |
| Settings (settings.py) | None - just reload |

---

## Troubleshooting

**Changes not showing?**
- Clear browser cache (Ctrl+F5)
- Check error log: Web tab → Error log

**Static files not updating?**
- Run `collectstatic --noinput`

---

## Full Guide
For detailed instructions, see: `.agent/workflows/deploy-to-production.md`
Or use the command: `/deploy-to-production`
