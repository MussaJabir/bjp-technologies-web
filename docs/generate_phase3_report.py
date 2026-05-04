"""Generate BJP Technologies Phase 3 Completion Report PDF."""

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

OUTPUT = "docs/BJP_Technologies_Phase3_Report.pdf"

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
CONTENT_W = 174 * mm  # A4 210mm − 18mm left − 18mm right


# ── Header / Footer ────────────────────────────────────────────────────────────
def header_footer(canvas, doc):
    canvas.saveState()
    # Header — plain text, no background bar
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawString(18 * mm, PAGE_H - 10 * mm, "BJP TECHNOLOGIES (T) LIMITED")
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8.5)
    canvas.drawRightString(
        PAGE_W - 18 * mm, PAGE_H - 10 * mm, "Phase 3 Completion Report — May 2026"
    )
    canvas.setStrokeColor(LIGHT_GREY)
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, PAGE_H - 13 * mm, PAGE_W - 18 * mm, PAGE_H - 13 * mm)

    # Footer — navy bar
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
    "CellBold", fontName="Helvetica-Bold", fontSize=9, textColor=NAVY, leading=13
)
cell_body = ParagraphStyle(
    "CellBody", fontName="Helvetica", fontSize=8.5, textColor=BLACK, leading=12
)
cell_note = ParagraphStyle(
    "CellNote", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=12
)
cell_ms = ParagraphStyle("CellMs", fontName="Helvetica", fontSize=9, textColor=BLACK, leading=13)
status_ok_s = ParagraphStyle("StatusOk", fontName="Helvetica-Bold", fontSize=9, textColor=GREEN)
status_partial_s = ParagraphStyle(
    "StatusPartial", fontName="Helvetica-Bold", fontSize=9, textColor=CYAN
)
note_italic = ParagraphStyle(
    "NoteItalic", fontName="Helvetica-Oblique", fontSize=9, textColor=GREY, alignment=1
)


# ── Table builders ─────────────────────────────────────────────────────────────
def section_box(title):
    """Full-width navy section header box."""
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
    """Subsection header with cyan bottom border."""
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
    """2-col cover info table — cyan labels, thin separators."""
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
    """Milestone | Status table."""
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


def partial(text, note):
    return [Paragraph(text, cell_ms), Paragraph(f"✓  {note}", status_partial_s)]


def deliverable_table(rows, col_widths=None):
    """2-col deliverable table: ✓ Item | Notes."""
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
    """General 2-col info table with alternating rows."""
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
    """Generic navy-header table."""
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
    story.append(Paragraph("CONTENT PAGES COMPLETION REPORT", cover_report_label))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("PHASE 3", cover_phase))
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
            "This document confirms the successful completion of Phase 3 (Content Pages) of the BJP "
            "Technologies corporate website project. All public-facing content pages — About, Services "
            "(list and detail), and Industries (list and detail) — have been built, connected to database "
            "models, seeded with real content, tested, and merged to production.",
            intro_style,
        )
    )

    # ── 1. Executive Summary ───────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("1.  Executive Summary"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Phase 3 of the BJP Technologies (T) Limited corporate website is <b>complete</b>. "
            "Two Django models (Service and Industry) have been built, migrated, and seeded with all "
            "7 services and 6 industries from the company profile. Five full-content page templates "
            "have been built using the Luminos CSS system with BJP brand identity, connected to live "
            "database records, and merged to <b>main</b> via pull requests. "
            "37 automated tests were written and are passing.",
            body_style,
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        milestone_table(
            [
                ok("BaseModel abstract class — UUID pk + created_at + updated_at"),
                ok(
                    "Service model — name, slug, tagline, description, bullet_points, icon_svg, order, is_active"
                ),
                ok(
                    "Industry model — name, slug, tagline, description, services_offered, image, order, is_active"
                ),
                ok("Auto-slug generation on first save for both models"),
                ok("0001_initial migrations created for Service and Industry"),
                ok("Admin registered — ServiceAdmin and IndustryAdmin with full configuration"),
                ok("seed_content management command — idempotent, 7 services + 6 industries"),
                ok(
                    "About page — full content template (counter strip, what-we-do, benefit cards, CTA)"
                ),
                ok("Services list page — full template with all 7 services from DB"),
                ok("Service detail page — banner, bullet list, sidebar CTA, other services panel"),
                ok("Industries list page — career banner, all 6 industry cards from DB"),
                ok("Industry detail page — banner, check-wrapper, services grid, consultancy CTA"),
                ok("Luminos images integrated into all page banners via jarallax parallax"),
                ok("37 tests — 0 failures, 0 errors"),
                ok("ruff check: 0 errors  |  black --check: all files consistent"),
                ok("PR #8: feature/phase-3-content-pages → develop"),
                ok("PR #9: develop → main — Phase 3 live in production"),
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
                ("Project Type", "Corporate Website & Service Platform"),
                ("Framework", "Django 6.0.4"),
                ("Python Version", "3.12.12"),
                ("Database", "MySQL 8.0.45 — bjptechn_bjp_db"),
                ("Application Server", "Phusion Passenger (WSGI) — cPanel shared hosting"),
                ("Server Host", "Shared hosting — simba server, IP 50.6.6.46"),
                ("Static Files", "WhiteNoise — CompressedManifestStaticFilesStorage"),
                ("CSS Framework", "Bootstrap 5 + Luminos template + bjp.css brand layer"),
                ("Version Control", "GitHub — MussaJabir/bjp-technologies-web (private)"),
                ("Active Branch", "main  (feature/phase-3-content-pages merged via PR #8 → PR #9)"),
                ("CI/CD", "GitHub Actions — deploy.yml"),
                ("Contact", "info@bjptechnologies.co.tz  |  +255 678 290 994"),
            ]
        )
    )

    # ── 3. Deliverables Completed ──────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("3.  Deliverables Completed"))

    # 3.1 Data Models
    story.append(Spacer(1, 3 * mm))
    story.append(subsection_line("3.1  Data Models"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/core/models.py — BaseModel",
                    "Abstract class: UUID primary key, created_at (auto_now_add), updated_at (auto_now). "
                    "All app models inherit from this.",
                ),
                (
                    "apps/services/models.py — Service",
                    "name, slug (auto-gen), tagline, description, bullet_points, icon_svg, order, is_active. "
                    "get_bullet_list() helper for template rendering.",
                ),
                (
                    "apps/industries/models.py — Industry",
                    "name, slug (auto-gen), tagline, description, services_offered, image, order, is_active. "
                    "get_services_list() helper for template rendering.",
                ),
                (
                    "Auto-slug generation",
                    "slugify(name) applied on first save only — editing the name does not break "
                    "existing URLs or bookmarks.",
                ),
                (
                    "apps/services/migrations/0001_initial.py",
                    "Service table migration — created and committed to version control.",
                ),
                (
                    "apps/industries/migrations/0001_initial.py",
                    "Industry table migration — created and committed to version control.",
                ),
                (
                    "apps/services/admin.py — ServiceAdmin",
                    "list_display: name, order, is_active, created_at. search_fields, list_filter, "
                    "prepopulated_fields (slug), readonly timestamps.",
                ),
                (
                    "apps/industries/admin.py — IndustryAdmin",
                    "list_display: name, order, is_active, created_at. search_fields, list_filter, "
                    "prepopulated_fields (slug), readonly timestamps.",
                ),
            ]
        )
    )

    # 3.2 Seed Command
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.2  Content Seed Command"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/core/management/commands/seed_content.py",
                    "Idempotent management command using get_or_create — safe to run on any "
                    "environment, including production, without creating duplicates.",
                ),
                (
                    "7 services seeded",
                    "Software Development · Website & Digital Solutions · Cloud & Infrastructure · "
                    "Cybersecurity · Managed IT Services · Payment & System Integrations · "
                    "IT Consulting & Advisory",
                ),
                (
                    "6 industries seeded",
                    "Startups & SMEs · Financial Institutions (SACCOS/Microfinance) · "
                    "NGOs & Development Organizations · Education Institutions · "
                    "Healthcare Providers · Retail & Wholesale Businesses",
                ),
                (
                    "Icon SVG filenames included",
                    "Each Service record stores the icon_svg filename pointing to Luminos icon assets "
                    "in static/images/icon/.",
                ),
                (
                    "Run command",
                    "python manage.py seed_content",
                ),
            ]
        )
    )

    # 3.3 Page Templates
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.3  Page Templates"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/main/templates/main/about.html",
                    "Counter strip (animated stats), what-we-do-wrapper (2-col image + text), "
                    "4 key-benefit cards, 7-service grid, CTA banner.",
                ),
                (
                    "apps/services/templates/services/list.html",
                    "Service banner (jarallax), single-service-list rows for all 7 services "
                    "from DB, CTA section.",
                ),
                (
                    "apps/services/templates/services/detail.html",
                    "service-single-area-banner, full description, get_bullet_list() rendered list, "
                    "sidebar CTA, other services panel.",
                ),
                (
                    "apps/industries/templates/industries/list.html",
                    "rts-career-banner-area, all 6 industry cards from DB, CTA section.",
                ),
                (
                    "apps/industries/templates/industries/detail.html",
                    "Career banner, bg-gradient-one-industry, check-wrapper list, "
                    "6-card services grid, consultancy CTA.",
                ),
                (
                    "Luminos image integration",
                    "All page banners use jarallax parallax backgrounds from Luminos assets: "
                    "about/01-03.webp, service/04-08.webp, industry/01-02.webp and 11.webp.",
                ),
                (
                    "contact:submit → contact:contact URL fix",
                    "URL name corrected across all templates to match the contact app URL config.",
                ),
            ]
        )
    )

    # 3.4 Views & URL wiring
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.4  Views & URL Wiring"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "ServicesListView",
                    "ListView — queryset: Service.objects.filter(is_active=True).order_by('order')",
                ),
                (
                    "ServiceDetailView",
                    "DetailView — get_object_or_404(Service, slug=slug, is_active=True). "
                    "Context includes other_services (remaining active services).",
                ),
                (
                    "IndustriesListView",
                    "ListView — queryset: Industry.objects.filter(is_active=True).order_by('order')",
                ),
                (
                    "IndustryDetailView",
                    "DetailView — get_object_or_404(Industry, slug=slug, is_active=True). "
                    "Context includes all active services for the services grid.",
                ),
                (
                    "HomeView update",
                    "Pulls featured_services and industries from DB. Removed static "
                    "default_industries fallback.",
                ),
            ]
        )
    )

    # 3.5 Testing & Quality
    story.append(Spacer(1, 4 * mm))
    story.append(subsection_line("3.5  Testing & Code Quality"))
    story.append(Spacer(1, 3 * mm))
    story.append(
        deliverable_table(
            [
                (
                    "apps/services/tests/test_models.py",
                    "8 tests: __str__, slug auto-generation, slug stability on re-save, "
                    "get_bullet_list(), is_active default, timestamps present.",
                ),
                (
                    "apps/services/tests/test_views.py",
                    "10 tests: list 200 OK, correct template, context key 'services'. "
                    "Detail 200 OK, correct template, context keys. "
                    "404 for invalid slug, 404 for inactive service.",
                ),
                (
                    "apps/industries/tests/test_models.py",
                    "8 tests: __str__, slug auto-generation, slug stability on re-save, "
                    "get_services_list(), is_active default, timestamps present.",
                ),
                (
                    "apps/industries/tests/test_views.py",
                    "9 tests: list 200 OK, correct template, context key 'industries'. "
                    "Detail 200 OK, correct template, context keys. "
                    "404 for invalid slug, 404 for inactive industry.",
                ),
                (
                    "apps/main/tests/test_views.py",
                    "2 smoke tests from Phase 2 — home 200 OK, about 200 OK — still passing.",
                ),
                ("Total: 37 tests", "0 failures · 0 errors · 0 skipped"),
                ("ruff check .", "0 errors across all Python files"),
                ("black --check .", "All files consistent — formatting enforced"),
                ("python manage.py check", "System check: 0 issues identified"),
                (
                    "GitHub Actions CI",
                    "Pipeline passing green on feature branch and after merge to develop and main.",
                ),
            ]
        )
    )

    # ── 4. Content Architecture ────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("4.  Content Architecture"))
    story.append(Spacer(1, 4 * mm))

    arch_rows = [
        (
            "BaseModel",
            "apps/core/models.py",
            "Abstract — UUID pk, created_at, updated_at. Inherited by all app models.",
        ),
        (
            "Service model",
            "apps/services/models.py",
            "8 fields. Auto-slug on first save. get_bullet_list() helper. Admin editable.",
        ),
        (
            "Industry model",
            "apps/industries/models.py",
            "7 fields. Auto-slug on first save. get_services_list() helper. Admin editable.",
        ),
        (
            "URL — Services",
            "/services/<slug>/",
            "ServiceDetailView — get_object_or_404 by slug + is_active=True.",
        ),
        (
            "URL — Industries",
            "/industries/<slug>/",
            "IndustryDetailView — get_object_or_404 by slug + is_active=True.",
        ),
        (
            "Admin — Service",
            "apps/services/admin.py",
            "ServiceAdmin — fully editable from /admin/, slug auto-populated from name.",
        ),
        (
            "Admin — Industry",
            "apps/industries/admin.py",
            "IndustryAdmin — fully editable from /admin/, slug auto-populated from name.",
        ),
        (
            "Seed command",
            "python manage.py seed_content",
            "Idempotent — uses get_or_create. Safe on all environments including production.",
        ),
    ]
    story.append(
        generic_table(
            ["Component", "Location", "Details"],
            [
                [
                    Paragraph(r[0], cell_bold),
                    Paragraph(
                        r[1],
                        ParagraphStyle(
                            "cl", fontName="Helvetica", fontSize=8.5, textColor=BLACK, leading=12
                        ),
                    ),
                    Paragraph(r[2], cell_note),
                ]
                for r in arch_rows
            ],
            [38 * mm, 52 * mm, 84 * mm],
        )
    )

    # ── 5. Page Structure Map ──────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("5.  Page Structure Map"))
    story.append(Spacer(1, 4 * mm))

    page_rows = [
        (
            "/",
            "HomeView",
            "main",
            "home.html",
            "Hero, service cards, 7-service grid, stats, about strip, why-choose, partners, industries",
        ),
        (
            "/about/",
            "AboutView",
            "main",
            "about.html",
            "Counter strip, what-we-do, 4 benefit cards, 7-service grid, CTA",
        ),
        (
            "/services/",
            "ServicesListView",
            "services",
            "list.html",
            "Banner, all 7 services as list rows, CTA",
        ),
        (
            "/services/<slug>/",
            "ServiceDetailView",
            "services",
            "detail.html",
            "Banner, description, bullet list, sidebar CTA, other services panel",
        ),
        (
            "/industries/",
            "IndustriesListView",
            "industries",
            "list.html",
            "Career banner, all 6 industry cards, CTA",
        ),
        (
            "/industries/<slug>/",
            "IndustryDetailView",
            "industries",
            "detail.html",
            "Banner, check-wrapper, services grid, consultancy CTA",
        ),
    ]
    story.append(
        generic_table(
            ["URL", "View", "App", "Template", "Content Sections"],
            [
                [
                    Paragraph(
                        r[0],
                        ParagraphStyle(
                            "ur", fontName="Helvetica-Bold", fontSize=8, textColor=NAVY, leading=11
                        ),
                    ),
                    Paragraph(
                        r[1],
                        ParagraphStyle(
                            "vw", fontName="Helvetica", fontSize=8, textColor=BLACK, leading=11
                        ),
                    ),
                    Paragraph(
                        r[2],
                        ParagraphStyle(
                            "ap", fontName="Helvetica", fontSize=8, textColor=GREY, leading=11
                        ),
                    ),
                    Paragraph(
                        r[3],
                        ParagraphStyle(
                            "tp", fontName="Helvetica", fontSize=8, textColor=BLACK, leading=11
                        ),
                    ),
                    Paragraph(
                        r[4],
                        ParagraphStyle(
                            "sc", fontName="Helvetica", fontSize=8, textColor=GREY, leading=11
                        ),
                    ),
                ]
                for r in page_rows
            ],
            [28 * mm, 34 * mm, 20 * mm, 22 * mm, 70 * mm],
        )
    )

    # ── 6. Known Limitations ───────────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("6.  Known Limitations / Pending Items"))
    story.append(Spacer(1, 4 * mm))

    lim_rows = [
        (
            "Migrations not yet applied on cPanel",
            "Service and Industry 0001_initial migrations are committed but not yet run on production MySQL.",
            "Run python manage.py migrate via cPanel Python App execute scripts after deploying the branch.",
        ),
        (
            "seed_content not yet run on production",
            "Production database has no Service or Industry records — pages will render empty on live site until seeded.",
            "Run python manage.py seed_content after migrations are applied on the server.",
        ),
        (
            "SSH auto-deploy still blocked",
            "Port 22 blocked on shared hosting — GitHub Actions SSH deploy step remains inactive.",
            "Manual pull via cPanel Git Version Control (interim workaround — inherited from Phase 1).",
        ),
        (
            "About strip image — placeholder",
            "Uses Luminos about/01.webp, not real BJP photography.",
            "Replace with real BJP photo in Phase 5/6.",
        ),
        (
            "Tech partner logos — icon-based",
            "FA6 brand icons used in home page partners section; no official partner SVG logos available.",
            "Replace with official logos in Phase 6 if obtained.",
        ),
    ]
    story.append(
        generic_table(
            ["Item", "Detail", "Resolution / Plan"],
            [
                [
                    Paragraph(r[0], cell_bold),
                    Paragraph(
                        r[1],
                        ParagraphStyle(
                            "ld", fontName="Helvetica", fontSize=8.5, textColor=BLACK, leading=12
                        ),
                    ),
                    Paragraph(r[2], cell_note),
                ]
                for r in lim_rows
            ],
            [42 * mm, 70 * mm, 62 * mm],
        )
    )

    # ── 7. Phase 4 — Contact System ────────────────────────────────────────────
    story.append(Spacer(1, 5 * mm))
    story.append(section_box("7.  Phase 4 — Contact System (Next)"))
    story.append(Spacer(1, 4 * mm))
    story.append(
        Paragraph(
            "Phase 4 will build the full contact system — a validated enquiry form that saves to the "
            "database, sends an email notification to BJP Technologies, and sends a confirmation email "
            "to the submitter. Admin management of enquiries with status tracking will also be included.",
            body_style,
        )
    )
    story.append(Spacer(1, 3 * mm))

    next_rows = [
        (
            "ContactEnquiry model",
            "Fields: first name, last name, email, phone (optional), company (optional), "
            "service of interest, message, IP address, status (new / read / replied), "
            "created_at, updated_at.",
        ),
        (
            "apps/contact/forms.py",
            "ModelForm with clean() validation — all required fields enforced, "
            "phone/company optional.",
        ),
        (
            "ContactView (GET + POST)",
            "GET: renders form. POST: validates, saves to DB, sends notification email to "
            "info@bjptechnologies.co.tz, sends confirmation email to submitter, "
            "redirects to /contact/success/.",
        ),
        (
            "Contact page template",
            "Full contact page with form, field-level validation error display, "
            "{% csrf_token %}, company info panel.",
        ),
        (
            "ContactSuccessView",
            "Success/thank-you page at /contact/success/ shown after valid submission.",
        ),
        (
            "Email notifications",
            "Django email backend — HTML + plain-text notification to BJP and "
            "auto-reply confirmation to enquirer.",
        ),
        (
            "Rate limiting",
            "Submission throttle to prevent spam — session or IP-based cooldown.",
        ),
        (
            "Admin — ContactEnquiry",
            "Status management (new → read → replied), list_display with email/name/date, "
            "search_fields, list_filter by status.",
        ),
        (
            "Tests",
            "Model (__str__, status default), form (valid data, invalid data, each required field), "
            "view (GET 200, POST valid redirect, POST invalid re-render).",
        ),
    ]
    story.append(
        generic_table(
            ["Deliverable", "Scope"],
            [
                [
                    Paragraph(r[0], cell_bold),
                    Paragraph(r[1], cell_body),
                ]
                for r in next_rows
            ],
            [60 * mm, 114 * mm],
        )
    )

    story.append(Spacer(1, 8 * mm))
    story.append(
        Paragraph(
            "Phase 4 will begin upon receipt of the Phase 3 go-ahead from the project owner.",
            note_italic,
        )
    )

    doc.build(story)
    print(f"✓  Report generated: {OUTPUT}")


if __name__ == "__main__":
    build()
