"""Generate BJP Technologies Phase 5 Completion Report PDF."""

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

OUTPUT = "docs/BJP_Technologies_Phase5_Report.pdf"

# ── Brand colours ──────────────────────────────────────────────────────────────
NAVY = colors.HexColor("#0D1B4B")
BLUE = colors.HexColor("#1565C0")
CYAN = colors.HexColor("#00C6FF")
GREY = colors.HexColor("#8A94B0")
OFF_WHITE = colors.HexColor("#F4F6FC")
GREEN = colors.HexColor("#2ECC71")
WHITE = colors.white
BLACK = colors.black
LIGHT_GREY = colors.HexColor("#E8ECF4")
RED = colors.HexColor("#E74C3C")

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
        PAGE_W - 18 * mm, PAGE_H - 10 * mm, "Phase 5 Completion Report — May 2026"
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
status_removed = ParagraphStyle(
    "StatusRemoved",
    fontName="Helvetica-Bold",
    fontSize=9,
    textColor=RED,
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


def removed(text):
    return [Paragraph(text, cell_ms), Paragraph("✗  Removed", status_removed)]


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


def sp(h=6):
    return Spacer(1, h * mm)


def hr():
    return HRFlowable(width="100%", thickness=0.5, color=LIGHT_GREY, spaceAfter=4)


# ── Document build ─────────────────────────────────────────────────────────────
def build():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="main",
    )
    doc.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=header_footer)])

    story = []

    # ── Cover page ─────────────────────────────────────────────────────────────
    story += [
        sp(22),
        Paragraph("BJP Technologies (T) Limited", cover_title),
        Paragraph("Secure Technology. Scalable Growth.", cover_tagline),
        sp(8),
        HRFlowable(width="60%", thickness=2, color=CYAN, hAlign="CENTER"),
        sp(8),
        Paragraph("PHASE", cover_report_label),
        Paragraph("5", cover_phase),
        Paragraph("COMPLETION REPORT", cover_complete),
        sp(6),
        Paragraph("Admin &amp; CMS Dashboard", cover_tagline),
        sp(12),
        HRFlowable(width="40%", thickness=0.5, color=LIGHT_GREY, hAlign="CENTER"),
        sp(10),
        cover_info_table(
            [
                ("Project", "BJP Technologies Corporate Website"),
                ("Phase", "Phase 5 — Admin & CMS Dashboard"),
                ("Completed", "May 2026"),
                ("Branch", "feature/phase-5-admin-cms"),
                ("Stack", "Django 6.0.4 · django-unfold 0.92.0 · Tailwind CSS"),
                ("Prepared by", "Claude Sonnet 4.6 (Anthropic) for MussaJabir"),
                ("Status", "✓ Complete — Ready to merge to develop"),
            ]
        ),
        sp(10),
        Paragraph(
            "This report documents the complete replacement of Wagtail CMS with "
            "django-unfold as the admin dashboard, including brand theming, custom "
            "dashboard panels, database cleanup, and all related deliverables.",
            intro_style,
        ),
    ]

    # ── 1. Executive Summary ───────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("1.  Executive Summary"),
        sp(4),
        Paragraph(
            "Phase 5 set out to deliver a polished, branded admin interface that "
            "BJP Technologies staff could use to manage website content and monitor "
            "contact enquiries. The initial choice of Wagtail 7.3.1 was replaced "
            "mid-phase after its React-based sidebar proved incompatible with our "
            "CSS/JS customisation requirements — the sidebar repeatedly unmounted "
            "due to MutationObserver-triggered React re-render loops.",
            body_style,
        ),
        Paragraph(
            "The replacement decision was based on a structured evaluation of five "
            "alternatives. <b>django-unfold 0.92.0</b> was selected: it is built on "
            "Tailwind CSS, ships with Django 6 support, provides a "
            "DASHBOARD_CALLBACK hook for fully custom dashboards, and requires no "
            "React runtime. The migration was completed in a single session with "
            "zero test regressions.",
            body_style,
        ),
        Paragraph(
            "The final admin features a navy-to-blue branded sidebar with the BJP "
            "mark logo, a four-card KPI dashboard showing live service/industry/"
            "enquiry counts, an enquiry status breakdown panel, and a recent "
            "enquiries list. All 67 automated tests continue to pass.",
            body_style,
        ),
    ]

    # ── 2. Phase Milestones ────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("2.  Phase Milestones"),
        sp(4),
        milestone_table(
            [
                ok("Wagtail 7.3.1 installed and integrated"),
                ok("BJP brand CSS applied to Wagtail admin (sidebar, buttons, panels)"),
                ok("Services + Industries grouped under 'Website Content' menu"),
                ok("ContactEnquiry managed via Wagtail snippets"),
                ok("Dashboard KPI cards (services, industries, enquiries)"),
                ok("Recent enquiries panel on dashboard"),
                removed("Wagtail sidebar logo (React re-render loop — sidebar vanished)"),
                ok("Root cause identified: MutationObserver modifying React-managed DOM"),
                ok("Evaluated 5 admin alternatives with live demo research"),
                ok("Migrated to django-unfold 0.92.0 (Django 6 compatible)"),
                ok("BJP brand colors configured via UNFOLD color scale"),
                ok("BJP mark logo in sidebar — stable, no React dependency"),
                ok("Sidebar navigation with icons and unread enquiry badge"),
                ok("Custom dashboard: 4 KPI cards + status breakdown + enquiry list"),
                ok("All Wagtail apps and dependencies removed from requirements"),
                ok("46 orphaned Wagtail/taggit DB tables dropped"),
                ok("Auto-cleanup migration (core/0001) — runs on manage.py migrate"),
                ok("Admin URL restored to /admin/ (was /django-admin/ under Wagtail)"),
                ok("All 67 tests passing after migration"),
                ok("ruff + black clean throughout"),
            ]
        ),
    ]

    # ── 3. Technology Decision ─────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("3.  Technology Decision — Wagtail → django-unfold"),
        sp(4),
        subsection_line("3.1  Why Wagtail Was Replaced"),
        sp(3),
        Paragraph(
            "Wagtail 7's admin sidebar is a React component mounted at "
            "<b>#wagtail-sidebar</b>. Customising the logo required modifying "
            "<b>.sidebar-wagtail-branding__icon-wrapper</b> — a React-managed DOM "
            "node. Every modification triggered a React re-render cycle that "
            "created a fresh wrapper element (without our <i>data-bjp</i> guard), "
            "causing our MutationObserver to fire again, producing an infinite "
            "re-render loop. React eventually unmounted the entire sidebar "
            "component, leaving only the page content visible.",
            body_style,
        ),
        Paragraph(
            "The only safe approach would have been to fork Wagtail's React source "
            "and rebuild the sidebar bundle — disproportionate effort for a "
            "corporate website admin panel.",
            body_style,
        ),
        sp(3),
        subsection_line("3.2  Alternatives Evaluated"),
        sp(3),
        generic_table(
            ["Option", "Technology", "Django 6", "UI Quality", "Decision"],
            [
                [
                    Paragraph("django-unfold", cell_bold),
                    Paragraph("Tailwind CSS", cell_body),
                    Paragraph("✓ v0.92.0", cell_body),
                    Paragraph("Modern, clean", cell_body),
                    Paragraph('<font color="#2ECC71"><b>Selected</b></font>', cell_bold),
                ],
                [
                    Paragraph("Jazzmin", cell_body),
                    Paragraph("AdminLTE 3 / Bootstrap 5", cell_body),
                    Paragraph("✓ confirmed", cell_body),
                    Paragraph("Good, dated feel", cell_body),
                    Paragraph("Runner-up", cell_body),
                ],
                [
                    Paragraph("Grappelli", cell_body),
                    Paragraph("Vue.js v2", cell_body),
                    Paragraph("Uncertain", cell_body),
                    Paragraph("Dated", cell_body),
                    Paragraph("Rejected", cell_body),
                ],
                [
                    Paragraph("Custom (scratch)", cell_body),
                    Paragraph("Django + Tailwind", cell_body),
                    Paragraph("✓", cell_body),
                    Paragraph("Maximum freedom", cell_body),
                    Paragraph("Too costly", cell_body),
                ],
                [
                    Paragraph("Continue Wagtail", cell_body),
                    Paragraph("React", cell_body),
                    Paragraph("✓", cell_body),
                    Paragraph("Cannot customise", cell_body),
                    Paragraph("Rejected", cell_body),
                ],
            ],
            [38 * mm, 46 * mm, 22 * mm, 34 * mm, 34 * mm],
        ),
        sp(3),
        subsection_line("3.3  Why django-unfold Was Chosen"),
        sp(3),
        deliverable_table(
            [
                (
                    "Django 6 native support",
                    "v0.92.0 released February 2026 — latest version at time of migration",
                ),
                (
                    "No React runtime",
                    "Pure Tailwind CSS — all customisation via config and templates, "
                    "no DOM manipulation risks",
                ),
                (
                    "DASHBOARD_CALLBACK hook",
                    "Python callable injects live data (services, industries, enquiry counts) "
                    "into the dashboard template",
                ),
                (
                    "UNFOLD color scale",
                    "BJP navy (#0D1B4B) and blue (#1565C0) applied via a 50–950 "
                    "Tailwind-compatible color scale in settings",
                ),
                (
                    "Sidebar navigation config",
                    "Declarative SIDEBAR dict: icons, collapsible groups, reverse_lazy URLs, "
                    "live badge callbacks",
                ),
                (
                    "Drop-in migration",
                    "Change ModelAdmin base class — all existing fieldsets, list_display, "
                    "search_fields carry over unchanged",
                ),
                (
                    "Official Django endorsement",
                    "Featured in Django Project's official Admin Theme Roundup, April 2025",
                ),
            ]
        ),
    ]

    # ── 4. Deliverables ────────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("4.  Deliverables"),
        sp(4),
        subsection_line("4.1  Admin Configuration"),
        sp(3),
        deliverable_table(
            [
                (
                    "UNFOLD settings block",
                    "config/settings/base.py — brand colors, logo, sidebar nav, "
                    "DASHBOARD_CALLBACK, enquiry badge",
                ),
                (
                    "Admin URL at /admin/",
                    "config/urls.py — restored from /django-admin/ "
                    "(Wagtail had displaced it to /cms/)",
                ),
                (
                    "unfold.admin.ModelAdmin",
                    "All four admin classes (Service, Industry, ContactEnquiry, core) "
                    "updated to Unfold base",
                ),
                (
                    "dashboard_callback",
                    "apps/core/admin.py — injects services_total, industries_total, "
                    "enquiries_new/read/replied, recent_enquiries into dashboard context",
                ),
                (
                    "enquiry_badge",
                    "apps/core/admin.py — returns unread count as string; displayed "
                    "as a live badge on the Contact Enquiries sidebar item",
                ),
            ]
        ),
        sp(3),
        subsection_line("4.2  Dashboard Template"),
        sp(3),
        deliverable_table(
            [
                (
                    "4 KPI cards",
                    "templates/admin/index.html — Active Services (navy gradient), "
                    "Active Industries, Unread Enquiries (blue highlight when > 0), "
                    "Total Received",
                ),
                (
                    "Enquiry Status panel",
                    "Segmented progress bar showing New / Read / Replied proportions "
                    "with colour-coded dots and counts",
                ),
                (
                    "Recent Enquiries list",
                    "Last 6 enquiries with name, email, service, date and status badge "
                    "(NEW / READ / REPLIED)",
                ),
                (
                    "Arrow navigation",
                    "Every KPI card links directly to the relevant model changelist in admin",
                ),
                (
                    "Dark mode ready",
                    "All Tailwind classes use dark: variants — works with Unfold's "
                    "built-in dark mode toggle",
                ),
            ]
        ),
        sp(3),
        subsection_line("4.3  Brand Theming"),
        sp(3),
        info_table(
            [
                (
                    "Logo",
                    "bjp-mark-transparent.png — BJP three-circle mark, "
                    "36 px, transparent background, rendered at top of sidebar",
                ),
                (
                    "Primary color",
                    "#1565C0 (blue) as Unfold primary-500; " "#0D1B4B (navy) as primary-800",
                ),
                (
                    "Sidebar",
                    "Declarative nav: Dashboard, Website Content "
                    "(Services + Industries), Enquiries, Administration",
                ),
                ("Badge", "Live unread enquiry count on sidebar Enquiries item"),
                ("Icons", "Material Symbols Outlined — arrow_outward on KPI cards"),
            ]
        ),
    ]

    # ── 5. Database Cleanup ────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("5.  Database Cleanup"),
        sp(4),
        Paragraph(
            "Removing Wagtail from INSTALLED_APPS does not automatically drop its "
            "database tables. To keep the schema clean, two complementary cleanup "
            "steps were applied:",
            body_style,
        ),
        sp(2),
        subsection_line("5.1  Immediate local cleanup"),
        sp(3),
        Paragraph(
            "A Django shell script dropped all 46 Wagtail/taggit tables from the "
            "local SQLite development database and removed their entries from "
            "<i>django_migrations</i>. The database was verified to contain only "
            "the 14 tables required by the project.",
            body_style,
        ),
        generic_table(
            ["Category", "Tables Dropped"],
            [
                [
                    Paragraph("wagtailcore", cell_bold),
                    Paragraph(
                        "page, pagelogentry, pagesubscription, pageviewrestriction, "
                        "revision, referenceindex, modellogentry, comment, commentreply, "
                        "site, locale, collection, collectionviewrestriction, "
                        "groupcollectionpermission, grouppagepermission, groupsitepermission, "
                        "task, taskstate, workflow, workflowcontenttype, workflowpage, "
                        "workflowstate, workflowtask, groupapprovaltask, uploadedfile",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("wagtailadmin", cell_bold),
                    Paragraph("admin, editingsession", cell_body),
                ],
                [Paragraph("wagtailimages", cell_bold), Paragraph("image, rendition", cell_body)],
                [
                    Paragraph(
                        "wagtaildocs / embeds / forms / redirects / search / users", cell_bold
                    ),
                    Paragraph(
                        "document, embed, formsubmission, redirect, "
                        "indexentry (+ 5 FTS variants), userprofile",
                        cell_body,
                    ),
                ],
                [Paragraph("taggit", cell_bold), Paragraph("tag, taggeditem", cell_body)],
                [Paragraph("Total", cell_bold), Paragraph("<b>46 tables dropped</b>", cell_bold)],
            ],
            [50 * mm, 124 * mm],
        ),
        sp(3),
        subsection_line("5.2  Automated migration (production-safe)"),
        sp(3),
        Paragraph(
            "A <b>RunPython</b> migration was created at "
            "<b>apps/core/migrations/0001_drop_wagtail_tables.py</b>. "
            "When <i>manage.py migrate</i> runs on any environment that still has "
            "the Wagtail tables (e.g. production MySQL), Django will automatically "
            "apply this migration and drop all 46 tables plus clean the migration "
            "history. Key design decisions:",
            body_style,
        ),
        deliverable_table(
            [
                (
                    "DROP TABLE IF EXISTS",
                    "Every DROP uses IF EXISTS — migration is a safe no-op on clean "
                    "databases (local dev, fresh CI environments)",
                ),
                (
                    "FK checks disabled",
                    "MySQL: SET FOREIGN_KEY_CHECKS=0 / SQLite: PRAGMA foreign_keys=OFF "
                    "before dropping, re-enabled after — prevents constraint errors",
                ),
                (
                    "django_migrations cleanup",
                    "DELETE FROM django_migrations WHERE app IN (...) removes the 13 "
                    "Wagtail app entries so the history stays accurate",
                ),
                (
                    "Irreversible",
                    "reverse_code=noop — we cannot recreate Wagtail tables on rollback "
                    "and should not need to",
                ),
                (
                    "Cross-database",
                    "Handles both SQLite (dev/CI) and MySQL (production cPanel) "
                    "via connection.vendor",
                ),
            ]
        ),
    ]

    # ── 6. Files Changed ──────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("6.  Files Changed"),
        sp(4),
        generic_table(
            ["File", "Action", "Summary"],
            [
                [
                    Paragraph("requirements.txt", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph(
                        "Removed wagtail, django-modelcluster, django-taggit; "
                        "added django-unfold==0.92.0",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("config/settings/base.py", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph(
                        "Replaced Wagtail INSTALLED_APPS/MIDDLEWARE/settings with "
                        "Unfold apps + full UNFOLD config block",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("config/urls.py", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph("Removed Wagtail URLs; restored admin to /admin/", cell_body),
                ],
                [
                    Paragraph("apps/core/admin.py", cell_bold),
                    Paragraph("Rewritten", cell_body),
                    Paragraph("dashboard_callback + enquiry_badge functions", cell_body),
                ],
                [
                    Paragraph("apps/core/migrations/0001_*.py", cell_bold),
                    Paragraph("Created", cell_body),
                    Paragraph(
                        "RunPython migration — drops 46 Wagtail tables on migrate", cell_body
                    ),
                ],
                [
                    Paragraph("apps/services/admin.py", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph("ServiceAdmin → unfold.admin.ModelAdmin", cell_body),
                ],
                [
                    Paragraph("apps/industries/admin.py", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph("IndustryAdmin → unfold.admin.ModelAdmin", cell_body),
                ],
                [
                    Paragraph("apps/contact/admin.py", cell_bold),
                    Paragraph("Modified", cell_body),
                    Paragraph("ContactEnquiryAdmin → unfold.admin.ModelAdmin", cell_body),
                ],
                [
                    Paragraph("templates/admin/index.html", cell_bold),
                    Paragraph("Created", cell_body),
                    Paragraph(
                        "Custom dashboard: KPI cards, status panel, enquiries list", cell_body
                    ),
                ],
                [
                    Paragraph("apps/*/wagtail_hooks.py (×4)", cell_bold),
                    Paragraph("Deleted", cell_body),
                    Paragraph(
                        "All Wagtail hook files removed from core, services, "
                        "industries, contact",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("templates/wagtailadmin/ (×4 files)", cell_bold),
                    Paragraph("Deleted", cell_body),
                    Paragraph("Wagtail branding templates (logo, favicon) removed", cell_body),
                ],
                [
                    Paragraph("templates/core/wagtail/ (×2 files)", cell_bold),
                    Paragraph("Deleted", cell_body),
                    Paragraph(
                        "Old dashboard_stats.html and dashboard_enquiries.html removed", cell_body
                    ),
                ],
                [
                    Paragraph("static/css/wagtail_brand.css", cell_bold),
                    Paragraph("Cleaned", cell_body),
                    Paragraph(
                        "Removed Wagtail-specific overrides; reduced to minimal .bjp-sl-img rule",
                        cell_body,
                    ),
                ],
            ],
            [60 * mm, 22 * mm, 92 * mm],
        ),
    ]

    # ── 7. Git Commits ────────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("7.  Git Commit History"),
        sp(4),
        generic_table(
            ["Commit", "Type", "Description"],
            [
                [
                    Paragraph("736d018", cell_bold),
                    Paragraph("feat", cell_body),
                    Paragraph(
                        "Phase 5 — Wagtail 7.3.1 CMS integration with BJP brand admin", cell_body
                    ),
                ],
                [
                    Paragraph("d78db63", cell_bold),
                    Paragraph("feat", cell_body),
                    Paragraph("Add site overview stats panel to dashboard", cell_body),
                ],
                [
                    Paragraph("8204536", cell_bold),
                    Paragraph("feat", cell_body),
                    Paragraph("Redesign dashboard KPI cards — compact premium style", cell_body),
                ],
                [
                    Paragraph("a6808ce", cell_bold),
                    Paragraph("fix", cell_body),
                    Paragraph(
                        "Replace Wagtail bird logo with BJP horizontal light logo", cell_body
                    ),
                ],
                [
                    Paragraph("529f71c", cell_bold),
                    Paragraph("fix", cell_body),
                    Paragraph(
                        "Stop sidebar vanishing — remove MutationObserver, switch to BJP mark logo",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("3e2dafe", cell_bold),
                    Paragraph("feat", cell_body),
                    Paragraph(
                        "Replace Wagtail with django-unfold 0.92.0 — Phase 5 admin", cell_body
                    ),
                ],
                [
                    Paragraph("b8843ba", cell_bold),
                    Paragraph("fix", cell_body),
                    Paragraph(
                        "Add breathing room between dashboard rows; drop 46 Wagtail DB tables",
                        cell_body,
                    ),
                ],
                [
                    Paragraph("d16ec90", cell_bold),
                    Paragraph("chore", cell_body),
                    Paragraph(
                        "Add migration to auto-drop Wagtail tables on manage.py migrate", cell_body
                    ),
                ],
                [
                    Paragraph("f0f70a9", cell_bold),
                    Paragraph("fix", cell_body),
                    Paragraph(
                        "Add breathing room between header, KPI cards and enquiry panels", cell_body
                    ),
                ],
            ],
            [22 * mm, 18 * mm, 134 * mm],
        ),
    ]

    # ── 8. Test Results ────────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("8.  Test Results"),
        sp(4),
        info_table(
            [
                ("Test runner", "pytest 9.0.3 + pytest-django 4.12.0"),
                ("Total tests", "67 tests across 8 test modules"),
                ("Result", "67 passed, 0 failed, 0 errors"),
                (
                    "Coverage areas",
                    "Contact forms/models/views · Industries models/views · "
                    "Services models/views · Main views",
                ),
                (
                    "Lint",
                    "ruff check .  →  All checks passed\n" "black --check .  →  74 files unchanged",
                ),
                (
                    "Django check",
                    "python manage.py check  →  0 errors (6 deployment warnings, expected in dev)",
                ),
            ]
        ),
    ]

    # ── 9. Admin Feature Summary ──────────────────────────────────────────────
    story += [
        sp(4),
        section_box("9.  Admin Feature Summary"),
        sp(4),
        subsection_line("9.1  Sidebar Navigation"),
        sp(3),
        generic_table(
            ["Section", "Items", "Extras"],
            [
                [
                    Paragraph("Dashboard", cell_bold),
                    Paragraph("Overview", cell_body),
                    Paragraph("Links to admin index", cell_body),
                ],
                [
                    Paragraph("Website Content", cell_bold),
                    Paragraph("Services · Industries", cell_body),
                    Paragraph("Direct changelist links", cell_body),
                ],
                [
                    Paragraph("Enquiries", cell_bold),
                    Paragraph("Contact Enquiries", cell_body),
                    Paragraph("Live unread badge count", cell_body),
                ],
                [
                    Paragraph("Administration", cell_bold),
                    Paragraph("Users", cell_body),
                    Paragraph("Django auth management", cell_body),
                ],
            ],
            [40 * mm, 70 * mm, 64 * mm],
        ),
        sp(3),
        subsection_line("9.2  Dashboard Panels"),
        sp(3),
        deliverable_table(
            [
                (
                    "Active Services card",
                    "Navy gradient card — live count of is_active=True services with "
                    "total services sub-label and arrow link to changelist",
                ),
                (
                    "Active Industries card",
                    "Light card — live count of is_active=True industries with total "
                    "industries sub-label",
                ),
                (
                    "Unread Enquiries card",
                    "Blue highlight when count > 0, grey when zero — shows NEW badge "
                    "inline with count; links to enquiry changelist",
                ),
                (
                    "Total Received card",
                    "All-time enquiry count — always visible as a historical reference",
                ),
                (
                    "Enquiry Status panel",
                    "Segmented progress bar — New (blue) / Read (grey) / Replied (green) "
                    "with per-status counts",
                ),
                (
                    "Recent Enquiries list",
                    "Last 6 enquiries: full name, email, service, date, colour-coded "
                    "status badge; 'View all' link to changelist",
                ),
            ]
        ),
    ]

    # ── 10. Next Phase ────────────────────────────────────────────────────────
    story += [
        sp(4),
        section_box("10.  Next Phase — Phase 6: Polish & Launch"),
        sp(4),
        Paragraph(
            "With the admin and CMS complete, Phase 6 targets production readiness. "
            "All deliverables below are required before the site goes live at "
            "bjptechnologies.co.tz.",
            body_style,
        ),
        sp(2),
        milestone_table(
            [
                [
                    Paragraph(
                        "Security settings verified (HSTS, CSRF, XSS, SSL redirect)", cell_ms
                    ),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("DEBUG=False confirmed in production settings", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("Meta tags and Open Graph tags on all pages", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("Sitemap generated (django.contrib.sitemaps)", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("robots.txt configured", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("Page load speed tested (target < 3s)", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("All images optimised", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph(
                        "Final security audit (no secrets, no debug, no SQL exposure)", cell_ms
                    ),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("DNS confirmed pointing to cPanel", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("SSL certificate active and auto-renewing", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
                [
                    Paragraph("Go-live sign-off", cell_ms),
                    Paragraph(
                        "⏳  Pending",
                        ParagraphStyle("pend", fontName="Helvetica", fontSize=9, textColor=GREY),
                    ),
                ],
            ]
        ),
        sp(6),
        hr(),
        sp(2),
        Paragraph(
            "BJP Technologies (T) Limited  |  bjptechnologies.co.tz  |  "
            "info@bjptechnologies.co.tz  |  +255 678 290 994",
            note_italic,
        ),
    ]

    doc.build(story)
    print(f"PDF generated: {OUTPUT}")


if __name__ == "__main__":
    build()
