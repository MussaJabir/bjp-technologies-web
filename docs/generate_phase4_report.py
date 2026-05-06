"""Generate BJP Technologies Phase 4 Completion Report PDF."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "docs/BJP_Technologies_Phase4_Report.pdf"

# ── Brand colours ──────────────────────────────────────────────────────────────
NAVY = colors.HexColor("#0D1B4B")
CYAN = colors.HexColor("#00C6FF")
GREY = colors.HexColor("#8A94B0")
OFF_WHITE = colors.HexColor("#F4F6FC")
GREEN = colors.HexColor("#2ECC71")
WHITE = colors.white
BLACK = colors.black
LIGHT_GREY = colors.HexColor("#E8ECF4")

PAGE_W, PAGE_H = A4
CONTENT_W = 174 * mm


# ── Header / Footer ────────────────────────────────────────────────────────────
def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawString(18 * mm, PAGE_H - 10 * mm, "BJP TECHNOLOGIES (T) LIMITED")
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(
        PAGE_W - 18 * mm, PAGE_H - 10 * mm, "Phase 4 Completion Report — May 2026"
    )
    canvas.setStrokeColor(LIGHT_GREY)
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)

    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 10 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(18 * mm, 3.5 * mm, "CONFIDENTIAL — For Internal Use Only")
    canvas.drawCentredString(PAGE_W / 2, 3.5 * mm, "bjptechnologies.co.tz")
    canvas.setFont("Helvetica-Bold", 7.5)
    canvas.drawRightString(PAGE_W - 18 * mm, 3.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


# ── Paragraph styles ───────────────────────────────────────────────────────────
cover_title = ParagraphStyle(
    "CoverTitle",
    fontName="Helvetica-Bold",
    fontSize=28,
    textColor=NAVY,
    alignment=1,
    spaceAfter=4,
)
cover_tagline = ParagraphStyle(
    "CoverTagline",
    fontName="Helvetica",
    fontSize=12,
    textColor=CYAN,
    alignment=1,
    spaceAfter=0,
)
cover_report_label = ParagraphStyle(
    "CoverReportLabel",
    fontName="Helvetica",
    fontSize=10,
    textColor=GREY,
    alignment=1,
    spaceAfter=4,
)
cover_phase = ParagraphStyle(
    "CoverPhase",
    fontName="Helvetica-Bold",
    fontSize=48,
    textColor=NAVY,
    alignment=1,
    spaceAfter=0,
)
cover_complete = ParagraphStyle(
    "CoverComplete",
    fontName="Helvetica-Bold",
    fontSize=16,
    textColor=NAVY,
    alignment=1,
    spaceAfter=0,
)
cover_info_label = ParagraphStyle(
    "CoverInfoLabel",
    fontName="Helvetica-Bold",
    fontSize=9,
    textColor=CYAN,
)
cover_info_value = ParagraphStyle(
    "CoverInfoValue",
    fontName="Helvetica",
    fontSize=9,
    textColor=BLACK,
)
intro_style = ParagraphStyle(
    "Intro",
    fontName="Helvetica",
    fontSize=9.5,
    textColor=NAVY,
    leading=15,
    alignment=1,
    spaceAfter=6,
)
body_style = ParagraphStyle(
    "Body",
    fontName="Helvetica",
    fontSize=9.5,
    textColor=BLACK,
    leading=14,
    spaceAfter=6,
)
section_title = ParagraphStyle(
    "SectionTitle",
    fontName="Helvetica-Bold",
    fontSize=11,
    textColor=WHITE,
    spaceAfter=0,
    spaceBefore=0,
)
subsection_title = ParagraphStyle(
    "SubsectionTitle",
    fontName="Helvetica-Bold",
    fontSize=10.5,
    textColor=NAVY,
    spaceBefore=0,
    spaceAfter=0,
)
th = ParagraphStyle("TH", fontName="Helvetica-Bold", fontSize=9, textColor=WHITE)
cell_bold = ParagraphStyle(
    "CellBold",
    fontName="Helvetica-Bold",
    fontSize=9,
    textColor=NAVY,
    leading=13,
)
cell_body = ParagraphStyle(
    "CellBody",
    fontName="Helvetica",
    fontSize=8.5,
    textColor=BLACK,
    leading=12,
)
cell_note = ParagraphStyle(
    "CellNote",
    fontName="Helvetica",
    fontSize=8.5,
    textColor=GREY,
    leading=12,
)
cell_ms = ParagraphStyle(
    "CellMs",
    fontName="Helvetica",
    fontSize=9,
    textColor=BLACK,
    leading=13,
)
status_ok_s = ParagraphStyle(
    "StatusOk",
    fontName="Helvetica-Bold",
    fontSize=9,
    textColor=GREEN,
)
note_italic = ParagraphStyle(
    "NoteItalic",
    fontName="Helvetica-Oblique",
    fontSize=9,
    textColor=GREY,
    alignment=1,
)


# ── Table builders ─────────────────────────────────────────────────────────────
def section_box(title):
    t = Table([[Paragraph(title, section_title)]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), NAVY),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
            ]
        )
    )
    return t


def subsection_line(title):
    t = Table([[Paragraph(title, subsection_title)]], colWidths=[CONTENT_W])
    t.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 1.5, CYAN),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return t


def cover_info_table(rows):
    data = [[Paragraph(k, cover_info_label), Paragraph(v, cover_info_value)] for k, v in rows]
    t = Table(data, colWidths=[45 * mm, 129 * mm])
    t.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return t


def milestone_table(rows):
    header = [Paragraph("<b>Milestone</b>", th), Paragraph("<b>Status</b>", th)]
    data = [header] + rows
    t = Table(data, colWidths=[122 * mm, 52 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("ROWBACKGROUND", (0, 1), (-1, -1), [WHITE, OFF_WHITE]),
                ("GRID", (0, 0), (-1, -1), 0.3, LIGHT_GREY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def ok(text):
    return [Paragraph(text, cell_ms), Paragraph("✓  Complete", status_ok_s)]


def deliverable_table(rows, col_widths=None):
    if col_widths is None:
        col_widths = [88 * mm, 86 * mm]
    header = [Paragraph("<b>Deliverable</b>", th), Paragraph("<b>Notes</b>", th)]
    data = [header]
    for item, note in rows:
        data.append(
            [
                Paragraph(f'<font color="#00C6FF">✓</font>  <b>{item}</b>', cell_bold),
                Paragraph(note, cell_note),
            ]
        )
    t = Table(data, colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("ROWBACKGROUND", (0, 1), (-1, -1), [WHITE, OFF_WHITE]),
                ("GRID", (0, 0), (-1, -1), 0.3, LIGHT_GREY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def info_table(rows):
    data = [
        [
            Paragraph(
                f"<b>{k}</b>",
                ParagraphStyle("ik", fontName="Helvetica-Bold", fontSize=9, textColor=NAVY),
            ),
            Paragraph(v, ParagraphStyle("iv", fontName="Helvetica", fontSize=9, textColor=BLACK)),
        ]
        for k, v in rows
    ]
    t = Table(data, colWidths=[50 * mm, 124 * mm])
    t.setStyle(
        TableStyle(
            [
                ("ROWBACKGROUND", (0, 0), (-1, -1), [WHITE, OFF_WHITE]),
                ("BACKGROUND", (0, 0), (0, -1), OFF_WHITE),
                ("GRID", (0, 0), (-1, -1), 0.3, LIGHT_GREY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def generic_table(headers, rows, col_widths):
    header = [Paragraph(f"<b>{h}</b>", th) for h in headers]
    data = [header] + rows
    t = Table(data, colWidths=col_widths)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("ROWBACKGROUND", (0, 1), (-1, -1), [WHITE, OFF_WHITE]),
                ("GRID", (0, 0), (-1, -1), 0.3, LIGHT_GREY),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


# ── Document build ─────────────────────────────────────────────────────────────
def build():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=22 * mm,
        bottomMargin=17 * mm,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=header_footer)])

    story = []

    # ── Cover page ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 16 * mm))
    story.append(Paragraph("BJP TECHNOLOGIES (T) LIMITED", cover_title))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("Secure Technology. Scalable Growth.", cover_tagline))
    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=CYAN, spaceAfter=6))
    story.append(Paragraph("CONTACT SYSTEM COMPLETION REPORT", cover_report_label))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("PHASE 4", cover_phase))
    story.append(Spacer(1, 2 * mm))
    story.append(Paragraph("COMPLETE", cover_complete))
    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width="100%", thickness=1.5, color=CYAN, spaceAfter=8))
    story.append(
        cover_info_table(
            [
                ("Project", "Corporate Website & Service Platform"),
                ("Company", "BJP Technologies (T) Limited"),
                ("Primary Domain", "bjptechnologies.co.tz"),
                ("Report Date", "May 2026"),
                ("Prepared By", "Development Team"),
                ("Classification", "Confidential — Internal Use Only"),
            ]
        )
    )
    story.append(Spacer(1, 10 * mm))
    story.append(
        Paragraph(
            "This document confirms the successful completion of Phase 4 (Contact System) of the BJP "
            "Technologies corporate website project. A full contact enquiry system has been built — "
            "validated form, database persistence, dual email notifications, IP-based rate limiting, "
            "admin management with status tracking, and 30 automated tests — all passing. Two CI/CD "
            "pipeline defects identified during the PR process were also diagnosed and resolved.",
            intro_style,
        )
    )

    # ── 1. Executive Summary ───────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("1.  Executive Summary"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Phase 4 of the BJP Technologies (T) Limited corporate website is <b>complete</b>. "
            "The full contact system has been implemented: a <b>ContactEnquiry</b> database model, "
            "a validated <b>ContactForm</b>, a <b>ContactView</b> with IP-based rate limiting and "
            "dual email dispatch, a branded success page, and a fully configured Django admin. "
            "Two CI pipeline failures (MySQL port exposure and missing cryptography package) were "
            "diagnosed and fixed. 30 new tests were written — 67 total project tests pass with "
            "zero failures.",
            body_style,
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        milestone_table(
            [
                ok("ContactEnquiry model — 10 fields, BaseModel inheritance, FK to Service"),
                ok("ContactForm (ModelForm) — service dropdown, message min-length, field strip"),
                ok("ContactView — IP capture (X-Forwarded-For), rate limit 5/30 min, DB save"),
                ok(
                    "Notification email to info@bjptechnologies.co.tz via EmailMessage (reply-to set)"
                ),
                ok("Confirmation email auto-reply to enquirer on successful submission"),
                ok("fail_silently=True on both emails — form never blocked by email failures"),
                ok("ContactSuccessView — branded success page with phone fallback CTA"),
                ok("ContactEnquiryAdmin — list_editable status, fieldsets, search, filters"),
                ok(
                    "contact.html — jarallax banner, 3 info cards, Luminos form, inline errors, Google Map"
                ),
                ok(
                    "Google Map updated to exact BJP Technologies coordinates (Mbezi, Dar es Salaam)"
                ),
                ok("success.html — navy check icon, action buttons, phone CTA card"),
                ok("Migration 0001_initial created and applied locally"),
                ok("30 new tests: 8 model · 10 form · 12 view — all passing"),
                ok("67 / 67 total project tests passing"),
                ok("ruff check: 0 errors  |  black --check: all files consistent"),
                ok("CI fix 1: MySQL port 3306 exposed to runner host (ports: - 3306:3306)"),
                ok("CI fix 2: cryptography==44.0.3 added to requirements-dev.txt"),
                ok("Branch feature/phase-4-contact-system pushed to GitHub"),
            ]
        )
    )

    # ── 2. Project Overview ────────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("2.  Project Overview"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        info_table(
            [
                ("Company", "BJP Technologies (T) Limited"),
                ("Location", "Ubungo – Dar es Salaam, Tanzania"),
                ("Primary Domain", "bjptechnologies.co.tz"),
                ("Alias Domain", "technologies.bejundas.co.tz  (301 redirect — separate cPanel)"),
                ("Framework", "Django 6.0.4  |  Python 3.12.12"),
                ("Database", "MySQL 8.0.45 — bjptechn_bjp_db  (cPanel shared hosting)"),
                ("Application Server", "Phusion Passenger (WSGI) — cPanel"),
                ("Static Files", "WhiteNoise — CompressedManifestStaticFilesStorage"),
                ("CSS Framework", "Bootstrap 5 + Luminos template + bjp.css brand layer"),
                ("Version Control", "GitHub — MussaJabir/bjp-technologies-web (private)"),
                ("Active Branch", "feature/phase-4-contact-system (pending PR → develop → main)"),
                ("CI/CD", "GitHub Actions — deploy.yml (test + SSH deploy)"),
                ("Contact", "info@bjptechnologies.co.tz  |  +255 678 290 994"),
            ]
        )
    )

    # ── 3. Deliverables Completed ──────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("3.  Deliverables Completed"))

    # 3.1 Model
    story.append(Spacer(1, 3 * mm))
    story.append(subsection_line("3.1  ContactEnquiry Model"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/contact/models.py — ContactEnquiry",
                    "Inherits BaseModel (UUID pk, created_at, updated_at). 10 fields total.",
                ),
                (
                    "first_name / last_name",
                    "CharField(max_length=80) — both required.",
                ),
                (
                    "email",
                    "EmailField() — required, validated by Django.",
                ),
                (
                    "phone",
                    "CharField(max_length=30, blank=True, default='') — optional.",
                ),
                (
                    "company",
                    "CharField(max_length=120, blank=True, default='') — optional.",
                ),
                (
                    "service",
                    "ForeignKey(Service, on_delete=SET_NULL, null=True, blank=True) — optional service "
                    "of interest. Linked to the 7 active services from Phase 3.",
                ),
                (
                    "message",
                    "TextField() — required. Minimum 10 characters enforced in form clean().",
                ),
                (
                    "ip_address",
                    "GenericIPAddressField(null=True, blank=True) — auto-captured from request, "
                    "used for rate limiting.",
                ),
                (
                    "status",
                    "CharField with choices: new (default) / read / replied. "
                    "Editable directly from the admin list view.",
                ),
                (
                    "full_name property",
                    "Returns '{first_name} {last_name}' — used in admin display and email subjects.",
                ),
                (
                    "apps/contact/migrations/0001_initial.py",
                    "Migration committed to version control. Applied locally. Must be run on cPanel "
                    "after deployment.",
                ),
            ]
        )
    )

    # 3.2 Form
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.2  ContactForm"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/contact/forms.py — ContactForm",
                    "ModelForm for ContactEnquiry. Fields: first_name, last_name, email, phone, "
                    "company, service, message.",
                ),
                (
                    "Service dropdown",
                    "ModelChoiceField — queryset: Service.objects.filter(is_active=True).order_by('order'). "
                    "Empty label: 'Select a service (optional)'.",
                ),
                (
                    "clean_message()",
                    "Raises ValidationError if message.strip() length < 10 characters.",
                ),
                (
                    "clean_first_name() / clean_last_name()",
                    "Strips leading/trailing whitespace before saving.",
                ),
                (
                    "Textarea widget",
                    "rows=5 applied to message field via Meta.widgets.",
                ),
            ]
        )
    )

    # 3.3 Views & Email
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.3  Views & Email Notifications"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "ContactView (FormView)",
                    "GET: renders contact form. POST: validates → rate limit check → save → "
                    "send emails → redirect to /contact/success/.",
                ),
                (
                    "IP capture — _get_client_ip()",
                    "Reads HTTP_X_FORWARDED_FOR first (for proxied requests), falls back to "
                    "REMOTE_ADDR. Handles comma-separated proxy chains.",
                ),
                (
                    "Rate limiting — _is_rate_limited(ip)",
                    "Queries DB for submissions from the same IP in the last 30 minutes. "
                    "Blocks if count >= 5. No external library required.",
                ),
                (
                    "Rate limit exceeded response",
                    "form.add_error(None, ...) — non-field error displayed at the top of the form. "
                    "Enquiry is NOT saved. Page re-renders with error.",
                ),
                (
                    "_send_notification(enquiry)",
                    "EmailMessage to CONTACT_EMAIL (info@bjptechnologies.co.tz). reply_to set to "
                    "enquirer's email — staff can reply with one click. fail_silently=True.",
                ),
                (
                    "_send_confirmation(enquiry)",
                    "EmailMessage to enquirer confirming receipt. Includes message preview (200 chars), "
                    "phone number, and 1-2 business day response time. fail_silently=True.",
                ),
                (
                    "ContactSuccessView (TemplateView)",
                    "Renders contact/success.html at /contact/success/. No model interaction.",
                ),
                (
                    "apps/contact/urls.py",
                    "name='contact' → ContactView. name='success' → ContactSuccessView. "
                    "TemplateView stubs replaced.",
                ),
            ]
        )
    )

    # 3.4 Admin
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.4  Admin Configuration"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/contact/admin.py — ContactEnquiryAdmin",
                    "Full admin configuration for ContactEnquiry model.",
                ),
                (
                    "list_display",
                    "full_name, email, phone, company, service, status, created_at — "
                    "all key fields visible in the list view.",
                ),
                (
                    "list_editable",
                    "status — team can change new → read → replied directly in the list "
                    "without opening each record.",
                ),
                (
                    "list_filter",
                    "status, service, created_at — sidebar filters for quick triage.",
                ),
                (
                    "search_fields",
                    "first_name, last_name, email, company, message — full-text search across "
                    "all key contact fields.",
                ),
                (
                    "readonly_fields",
                    "id, ip_address, created_at, updated_at — meta fields are locked from editing.",
                ),
                (
                    "fieldsets",
                    "Three sections: Contact Details · Enquiry (message + status) · "
                    "Meta (collapsed — id, IP, timestamps).",
                ),
            ]
        )
    )

    # 3.5 Templates
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.5  Page Templates"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "contact/contact.html — Banner",
                    "Jarallax parallax background (contact/01.webp) with navy overlay gradient. "
                    "Breadcrumb navigation, page title, subtitle.",
                ),
                (
                    "contact/contact.html — Info Cards",
                    "3 cards in a responsive row: Office Address (Ubungo, Mbezi, Dar es Salaam) · "
                    "Phone (+255 678 290 994, hours) · Email (info@bjptechnologies.co.tz).",
                ),
                (
                    "contact/contact.html — Form",
                    "Luminos contact-form CSS class. 7 fields: first name + last name (half-input-wrapper), "
                    "email, phone + company (half-input-wrapper), service dropdown, message. "
                    "{% csrf_token %} included.",
                ),
                (
                    "Form — inline field errors",
                    "Each field shows its own error message in red beneath the input on validation failure. "
                    "Non-field errors (rate limit) shown in amber alert block at top.",
                ),
                (
                    "contact/contact.html — Google Map",
                    "Embedded iframe pinned to exact BJP Technologies coordinates: "
                    "6°45'01.5\"S 39°05'24.4\"E (Msakuzi, Mbezi, Dar es Salaam). Zoom level 17.",
                ),
                (
                    "contact/success.html",
                    "Navy circle with cyan check icon, 'Message Received!' heading, "
                    "1-2 business day response note, Back to Home + Explore Services buttons, "
                    "phone fallback card (+255 678 290 994).",
                ),
            ]
        )
    )

    # 3.6 Testing
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.6  Testing & Code Quality"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/contact/tests/test_models.py — 8 tests",
                    "__str__ format · full_name property · status defaults to 'new' · "
                    "phone and company optional (blank=True) · service nullable · "
                    "timestamps set · ip_address stored · ordering newest-first.",
                ),
                (
                    "apps/contact/tests/test_forms.py — 10 tests",
                    "valid form · valid without optional fields · first_name required · "
                    "last_name required · email required · invalid email rejected · "
                    "message required · message too short rejected · message minimum length passes · "
                    "service optional (cleaned_data is None).",
                ),
                (
                    "apps/contact/tests/test_views.py — 12 tests",
                    "GET /contact/ 200 OK · correct template used · GET /contact/success/ 200 OK · "
                    "success template used · POST valid → 302 redirect to success · "
                    "POST valid → enquiry saved to DB · IP address captured from REMOTE_ADDR · "
                    "status defaults to 'new' · POST invalid → 200 with form errors · "
                    "short message → 200 with message error · "
                    "rate limit blocks after 5 same-IP submissions · "
                    "rate limit resets after 30-min window (old records excluded).",
                ),
                (
                    "Total: 30 new tests",
                    "0 failures · 0 errors · 0 skipped.",
                ),
                (
                    "Full project: 67 / 67 tests passing",
                    "All Phase 2, Phase 3, and Phase 4 tests pass together.",
                ),
                ("ruff check .", "0 errors — import sorting, unused imports, all clean."),
                ("black --check .", "All 69 files consistent — formatting enforced."),
            ]
        )
    )

    # ── 4. CI/CD Fixes ────────────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("4.  CI/CD Pipeline Fixes"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Two GitHub Actions pipeline failures were identified and resolved during the Phase 4 "
            "PR process. Both failures affected the pytest step via MySQL connectivity.",
            body_style,
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        generic_table(
            ["Issue", "Root Cause", "Fix Applied"],
            [
                [
                    Paragraph("<b>Run 1 — Connection refused</b>", cell_bold),
                    Paragraph(
                        "MySQL service container was running and healthy inside Docker, but no port "
                        "mapping was configured. The test runner (host) could not reach 127.0.0.1:3306 "
                        "because the container port was not exposed.",
                        cell_body,
                    ),
                    Paragraph(
                        "Added ports: - 3306:3306 to the MySQL service block in deploy.yml. "
                        "This maps the container port to the host runner's localhost.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("<b>Run 2 — RuntimeError: cryptography required</b>", cell_bold),
                    Paragraph(
                        "MySQL 8.0 uses caching_sha2_password as its default authentication plugin. "
                        "PyMySQL requires the cryptography Python package to perform the RSA handshake "
                        "for this auth method. The package was not in requirements-dev.txt so CI "
                        "installed PyMySQL without it.",
                        cell_body,
                    ),
                    Paragraph(
                        "Added cryptography==44.0.3 to requirements-dev.txt. "
                        "This is the official PyMySQL recommendation for MySQL 8.0 compatibility.",
                        cell_note,
                    ),
                ],
            ],
            [38 * mm, 74 * mm, 62 * mm],
        )
    )

    # ── 5. Contact System Architecture ────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("5.  Contact System Architecture"))
    story.append(Spacer(1, 4 * mm))

    story.append(
        generic_table(
            ["Component", "File", "Responsibility"],
            [
                [
                    Paragraph("ContactEnquiry model", cell_bold),
                    Paragraph("apps/contact/models.py", cell_body),
                    Paragraph(
                        "Database table — 10 fields, FK to Service, status choices.", cell_note
                    ),
                ],
                [
                    Paragraph("ContactForm", cell_bold),
                    Paragraph("apps/contact/forms.py", cell_body),
                    Paragraph(
                        "Validation layer — required fields, service dropdown, message length.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("ContactView", cell_bold),
                    Paragraph("apps/contact/views.py", cell_body),
                    Paragraph(
                        "Orchestrates: IP capture → rate limit → save → notify → confirm → redirect.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("ContactSuccessView", cell_bold),
                    Paragraph("apps/contact/views.py", cell_body),
                    Paragraph("Renders success page — no model interaction.", cell_note),
                ],
                [
                    Paragraph("ContactEnquiryAdmin", cell_bold),
                    Paragraph("apps/contact/admin.py", cell_body),
                    Paragraph("Inline status editing, search, filters, fieldsets.", cell_note),
                ],
                [
                    Paragraph("contact.html", cell_bold),
                    Paragraph("apps/contact/templates/contact/contact.html", cell_body),
                    Paragraph(
                        "Banner, info cards, 7-field form, inline errors, Google Map.", cell_note
                    ),
                ],
                [
                    Paragraph("success.html", cell_bold),
                    Paragraph("apps/contact/templates/contact/success.html", cell_body),
                    Paragraph(
                        "Branded confirmation — check icon, actions, phone fallback.", cell_note
                    ),
                ],
                [
                    Paragraph("Migration 0001_initial", cell_bold),
                    Paragraph("apps/contact/migrations/0001_initial.py", cell_body),
                    Paragraph(
                        "ContactEnquiry table — applied locally, pending on cPanel.", cell_note
                    ),
                ],
            ],
            [40 * mm, 68 * mm, 66 * mm],
        )
    )

    # ── 6. Submission Flow ─────────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("6.  Form Submission Flow"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        generic_table(
            ["Step", "Action", "Outcome"],
            [
                [
                    Paragraph("1", cell_bold),
                    Paragraph("User visits /contact/ (GET)", cell_body),
                    Paragraph("ContactView renders blank ContactForm.", cell_note),
                ],
                [
                    Paragraph("2", cell_bold),
                    Paragraph("User submits form (POST)", cell_body),
                    Paragraph(
                        "ContactView.form_valid() called if form passes validation.", cell_note
                    ),
                ],
                [
                    Paragraph("3", cell_bold),
                    Paragraph("IP rate limit check", cell_body),
                    Paragraph(
                        "If >= 5 submissions from same IP in last 30 min → non-field error, "
                        "form re-rendered. No save.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("4", cell_bold),
                    Paragraph("Save enquiry to DB", cell_body),
                    Paragraph(
                        "ContactEnquiry saved with status='new' and captured IP address.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("5", cell_bold),
                    Paragraph("Send notification email", cell_body),
                    Paragraph(
                        "EmailMessage to info@bjptechnologies.co.tz. reply_to=enquirer's email. "
                        "fail_silently=True.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("6", cell_bold),
                    Paragraph("Send confirmation email", cell_body),
                    Paragraph(
                        "EmailMessage to enquirer confirming receipt and 1-2 day response. "
                        "fail_silently=True.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("7", cell_bold),
                    Paragraph("Redirect to /contact/success/", cell_body),
                    Paragraph("ContactSuccessView renders success.html.", cell_note),
                ],
            ],
            [14 * mm, 60 * mm, 100 * mm],
        )
    )

    # ── 7. Known Limitations ───────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("7.  Known Limitations / Pending Items"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        generic_table(
            ["Item", "Detail", "Resolution / Plan"],
            [
                [
                    Paragraph("Migration not applied on cPanel", cell_bold),
                    Paragraph(
                        "ContactEnquiry 0001_initial migration committed but not yet run on "
                        "production MySQL.",
                        cell_body,
                    ),
                    Paragraph(
                        "Run python manage.py migrate via cPanel Python App after deploying branch.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("seed_content (Phase 3) not confirmed on production", cell_bold),
                    Paragraph(
                        "Service records required for the contact form dropdown. If not seeded, "
                        "the dropdown will be empty (form still functional).",
                        cell_body,
                    ),
                    Paragraph(
                        "Run python manage.py seed_content on cPanel after migrate.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("Email backend — not tested on production", cell_bold),
                    Paragraph(
                        "Email settings configured via .env (SMTP/Gmail). Not verified live. "
                        "fail_silently=True means email failures do not surface to the user.",
                        cell_body,
                    ),
                    Paragraph(
                        "Test by submitting the contact form on the live site after deploy "
                        "and verifying receipt at info@bjptechnologies.co.tz.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("HTML email templates not implemented", cell_bold),
                    Paragraph(
                        "Both notification and confirmation emails are plain-text only.",
                        cell_body,
                    ),
                    Paragraph(
                        "Phase 5/6 — add HTML email templates with BJP branding if required.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("SSH auto-deploy still blocked", cell_bold),
                    Paragraph(
                        "Port 22 blocked on shared hosting — GitHub Actions SSH deploy step "
                        "remains inactive. Manual pull via cPanel Git Version Control is the "
                        "interim workaround.",
                        cell_body,
                    ),
                    Paragraph(
                        "Inherited from Phase 1 — resolve when SSH access is available.",
                        cell_note,
                    ),
                ],
            ],
            [42 * mm, 70 * mm, 62 * mm],
        )
    )

    # ── 8. Deploy Checklist ────────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("8.  cPanel Deploy Checklist (After PR Merge)"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        generic_table(
            ["Step", "Command", "Purpose"],
            [
                [
                    Paragraph("1", cell_bold),
                    Paragraph("git pull origin main", cell_body),
                    Paragraph("Pull merged Phase 4 code onto the server.", cell_note),
                ],
                [
                    Paragraph("2", cell_bold),
                    Paragraph("python manage.py migrate --no-input", cell_body),
                    Paragraph(
                        "Applies contact 0001_initial migration — creates ContactEnquiry table.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("3", cell_bold),
                    Paragraph("python manage.py seed_content", cell_body),
                    Paragraph(
                        "Seeds 7 services + 6 industries (Phase 3). Safe to re-run — idempotent.",
                        cell_note,
                    ),
                ],
                [
                    Paragraph("4", cell_bold),
                    Paragraph("python manage.py collectstatic --no-input", cell_body),
                    Paragraph("Collects static files into public/static/.", cell_note),
                ],
                [
                    Paragraph("5", cell_bold),
                    Paragraph("touch tmp/restart.txt", cell_body),
                    Paragraph("Signals Passenger to restart the Django process.", cell_note),
                ],
                [
                    Paragraph("6 — Verify", cell_bold),
                    Paragraph("Visit /contact/ on live site", cell_body),
                    Paragraph(
                        "Submit a test enquiry → check Django admin → check email inbox.",
                        cell_note,
                    ),
                ],
            ],
            [16 * mm, 72 * mm, 86 * mm],
        )
    )

    # ── 9. Phase 5 Preview ─────────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("9.  Phase 5 — Admin & CMS (Next)"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Phase 5 will configure the Django admin as a fully usable CMS — enabling the client to "
            "manage all site content without developer involvement.",
            body_style,
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        generic_table(
            ["Deliverable", "Scope"],
            [
                [
                    Paragraph("Admin branding", cell_bold),
                    Paragraph(
                        "BJP logo and navy/cyan colour scheme applied to /admin/ — replaces the "
                        "default Django admin look.",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("Service admin — rich editing", cell_bold),
                    Paragraph(
                        "Inline editing of name, tagline, description, bullet_points, icon_svg, order. "
                        "Reorder services without touching code.",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("Industry admin — rich editing", cell_bold),
                    Paragraph(
                        "Inline editing of all industry fields. Toggle is_active to hide/show "
                        "industries on the live site.",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("ContactEnquiry admin — workflow", cell_bold),
                    Paragraph(
                        "Already configured in Phase 4 (list_editable status). Phase 5 may add "
                        "bulk actions (mark all selected as read).",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("Superuser credentials", cell_bold),
                    Paragraph(
                        "Document securely outside the repo. Verify superuser exists on production.",
                        cell_body,
                    ),
                ],
            ],
            [52 * mm, 122 * mm],
        )
    )

    story.append(Spacer(1, 8 * mm))
    story.append(
        Paragraph(
            "Phase 5 will begin upon confirmation that Phase 4 is deployed and the contact form "
            "is verified working on the live site.",
            note_italic,
        )
    )

    doc.build(story)
    print(f"✓  Report generated: {OUTPUT}")


if __name__ == "__main__":
    build()
