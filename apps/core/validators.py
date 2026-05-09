import os

from django.core.exceptions import ValidationError

_LOGO_EXTENSIONS = {".svg", ".png", ".webp"}
_FAVICON_EXTENSIONS = {".png", ".ico"}


def validate_logo_file(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in _LOGO_EXTENSIONS:
        raise ValidationError(
            f"Unsupported format '{ext}'. "
            "Accepted formats: SVG, PNG, WebP. "
            "The file must have a transparent background."
        )


def validate_favicon_file(value):
    ext = os.path.splitext(value.name)[1].lower()
    if ext not in _FAVICON_EXTENSIONS:
        raise ValidationError(
            f"Unsupported format '{ext}'. "
            "Accepted formats: PNG, ICO. Must be square, 32×32 pixels minimum."
        )
