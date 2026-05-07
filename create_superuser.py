"""One-time script — run via cPanel 'Execute python script', then delete."""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
django.setup()

from django.contrib.auth import get_user_model  # noqa: E402

User = get_user_model()

username = os.environ.get("SU_USERNAME", "admin")
email = os.environ.get("SU_EMAIL", "")
password = os.environ.get("SU_PASSWORD", "")

if not email or not password:
    print("ERROR: Set SU_EMAIL and SU_PASSWORD in cPanel environment variables first.")
else:
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists. No changes made.")
    else:
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
