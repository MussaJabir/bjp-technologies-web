import hashlib
import hmac
import json
import os
import subprocess

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_DEPLOY_SCRIPT = os.path.join(_BASE_DIR, 'scripts', 'deploy.sh')
_SECRET = os.environ.get('GITHUB_WEBHOOK_SECRET', '')


def _valid_signature(body: bytes, signature: str) -> bool:
    if not _SECRET:
        return False
    expected = 'sha256=' + hmac.new(_SECRET.encode(), body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, signature)


@csrf_exempt
@require_POST
def github_webhook(request):
    if not _valid_signature(request.body, request.headers.get('X-Hub-Signature-256', '')):
        return HttpResponseForbidden('Forbidden')

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponseBadRequest('Invalid payload')

    if payload.get('ref') != 'refs/heads/main':
        return HttpResponse('Skipped')

    # Fully detached so the process survives Passenger restart
    subprocess.Popen(
        ['bash', _DEPLOY_SCRIPT],
        close_fds=True,
        start_new_session=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return HttpResponse('OK')
