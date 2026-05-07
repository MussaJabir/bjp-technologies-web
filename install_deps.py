"""Temporary script — run once via cPanel 'Execute python script' to install missing packages."""
import subprocess
import sys

packages = [
    "django-unfold==0.92.0",
    "Pillow==12.2.0",
]

for pkg in packages:
    print(f"Installing {pkg}...")
    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", pkg],
        capture_output=True,
        text=True,
    )
    print(result.stdout[-500:] if result.stdout else "")
    if result.returncode != 0:
        print(f"ERROR: {result.stderr[-300:]}")
    else:
        print(f"✓ {pkg} installed successfully")

print("\nAll done. You can now delete install_deps.py")
