"""Generate BJP Technologies Post-Phase 6 Enhancements Report PDF."""

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

OUTPUT = "docs/BJP_Technologies_PostPhase6_Report.pdf"

NAVY = colors.HexColor("#0D1B4B")
BLUE = colors.HexColor("#1565C0")
CYAN = colors.HexColor("#00C6FF")
GREY = colors.HexColor("#8A94B0")
OFF_WHITE = colors.HexColor("#F4F6FC")
GREEN = colors.HexColor("#2ECC71")
WHITE = colors.white
BLACK = colors.black
LIGHT_GREY = colors.HexColor("#E8ECF4")
GOLD = colors.HexColor("#F39C12")
PURPLE = colors.HexColor("#6C3483")

PAGE_W, PAGE_H = A4
CONTENT_W = 174 * mm


def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 18 * mm, PAGE_W, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H - 19.5 * mm, PAGE_W, 1.5 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(18 * mm, PAGE_H - 12 * mm, "BJP TECHNOLOGIES (T) LIMITED")
    canvas.setFont("Helvetica", 8)
    canvas.drawRightString(
        PAGE_W - 18 * mm, PAGE_H - 12 * mm, "POST-PHASE 6 — PLATFORM ENHANCEMENTS"
    )

    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, 12 * mm, PAGE_W, 1 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(
        18 * mm, 4.5 * mm, "bjptechnologies.co.tz  |  Secure Technology. Scalable Growth."
    )
    canvas.drawRightString(PAGE_W - 18 * mm, 4.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()

    canvas.setFillColor(WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    SIDEBAR_W = 22 * mm
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(SIDEBAR_W, 0, 3, PAGE_H, fill=1, stroke=0)

    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 22 * mm, PAGE_W, 22 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H - 22 * mm, PAGE_W, 2, fill=1, stroke=0)

    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H - 14 * mm, "BJP TECHNOLOGIES (T) LIMITED")
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(CYAN)
    canvas.drawRightString(PAGE_W - 14 * mm, PAGE_H - 14 * mm, "bjptechnologies.co.tz")

    # Phase pill
    pill_x = SIDEBAR_W + 10 * mm
    pill_y = PAGE_H * 0.76
    canvas.setFillColor(BLUE)
    canvas.roundRect(pill_x, pill_y, 72 * mm, 9 * mm, 4, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(
        pill_x + 4 * mm, pill_y + 3 * mm, "POST-PHASE 6  ·  PLATFORM ENHANCEMENTS  ·  MAY 2026"
    )

    # Main headline
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 36)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.645, "PLATFORM")
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.575, "ENHANCEMENTS")

    canvas.setFillColor(CYAN)
    canvas.rect(SIDEBAR_W + 10 * mm, PAGE_H * 0.555, 85 * mm, 3, fill=1, stroke=0)

    canvas.setFillColor(BLUE)
    canvas.setFont("Helvetica-Bold", 15)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.525, "REPORT")

    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 9.5)
    canvas.drawString(
        SIDEBAR_W + 10 * mm, PAGE_H * 0.496, "BJP Technologies (T) Limited — May 2026"
    )

    # Stats cards
    stats = [
        ("11", "Admin\nSections", NAVY),
        ("40+", "Editable\nFields", BLUE),
        ("5", "Modules\nImproved", CYAN),
        ("8", "Repo\nFiles Added", GREEN),
    ]
    card_area_x = SIDEBAR_W + 10 * mm
    card_area_w = PAGE_W - card_area_x - 14 * mm
    col_w = card_area_w / 4
    for i, (val, label, col) in enumerate(stats):
        x = card_area_x + i * col_w
        canvas.setFillColor(LIGHT_GREY)
        canvas.roundRect(x + 3.5, PAGE_H * 0.355 - 1, col_w - 7, 24 * mm, 4, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.roundRect(x + 3, PAGE_H * 0.357, col_w - 7, 24 * mm, 4, fill=1, stroke=0)
        canvas.setFillColor(col)
        canvas.rect(x + 3, PAGE_H * 0.357 + 23 * mm, col_w - 7, 1 * mm, fill=1, stroke=0)
        canvas.setFillColor(col)
        canvas.setFont("Helvetica-Bold", 18)
        canvas.drawCentredString(x + col_w / 2, PAGE_H * 0.357 + 13 * mm, val)
        canvas.setFillColor(GREY)
        canvas.setFont("Helvetica", 7)
        for j, line in enumerate(label.split("\n")):
            canvas.drawCentredString(x + col_w / 2, PAGE_H * 0.357 + 7 * mm - j * 8, line)

    # Tagline strip
    canvas.setFillColor(OFF_WHITE)
    canvas.rect(SIDEBAR_W + 3, PAGE_H * 0.27, PAGE_W - SIDEBAR_W - 3, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawCentredString(
        (PAGE_W + SIDEBAR_W) / 2,
        PAGE_H * 0.27 + 10 * mm,
        "Admin UI  ·  Dynamic Content  ·  CSP Security  ·  GitHub Repository",
    )
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        (PAGE_W + SIDEBAR_W) / 2,
        PAGE_H * 0.27 + 4 * mm,
        "Enhancements delivered after Phase 6 completion",
    )

    # Sidebar vertical label
    canvas.saveState()
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.translate(13 * mm, PAGE_H / 2)
    canvas.rotate(90)
    canvas.drawCentredString(0, 0, "BJP TECHNOLOGIES  (T)  LIMITED")
    canvas.restoreState()

    # Bottom footer
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, 12 * mm, PAGE_W, 1.5 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawCentredString(
        PAGE_W / 2,
        4 * mm,
        "bjptechnologies.co.tz  ·  info@bjptechnologies.co.tz  ·  +255 678 290 994",
    )
    canvas.restoreState()


def build_styles():
    return {
        "section": ParagraphStyle(
            "section",
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=NAVY,
            spaceAfter=4 * mm,
            spaceBefore=6 * mm,
        ),
        "subsection": ParagraphStyle(
            "subsection",
            fontName="Helvetica-Bold",
            fontSize=10.5,
            textColor=BLUE,
            spaceAfter=3 * mm,
            spaceBefore=4 * mm,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=BLACK,
            spaceAfter=3 * mm,
            leading=15,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=9,
            textColor=BLACK,
            spaceAfter=2 * mm,
            leading=14,
            leftIndent=8 * mm,
            bulletIndent=2 * mm,
        ),
        "caption": ParagraphStyle(
            "caption",
            fontName="Helvetica-Oblique",
            fontSize=8,
            textColor=GREY,
            spaceAfter=2 * mm,
        ),
        "highlight": ParagraphStyle(
            "highlight",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=BLUE,
            spaceAfter=3 * mm,
        ),
        "green": ParagraphStyle(
            "green",
            fontName="Helvetica-Bold",
            fontSize=9.5,
            textColor=GREEN,
            spaceAfter=2 * mm,
        ),
        "small": ParagraphStyle(
            "small", fontName="Helvetica", fontSize=8, textColor=GREY, spaceAfter=1 * mm
        ),
    }


def divider(color=CYAN, thickness=1.5):
    return HRFlowable(
        width="100%", thickness=thickness, color=color, spaceAfter=4 * mm, spaceBefore=2 * mm
    )


def section_header(text, styles):
    return [Paragraph(text, styles["section"]), divider()]


def two_col_table(rows, col_widths=None, header_row=True):
    if col_widths is None:
        col_widths = [55 * mm, 119 * mm]
    t = Table(rows, colWidths=col_widths)
    style = [
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
    if header_row:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]
    t.setStyle(TableStyle(style))
    return t


def kpi_row(items):
    cell_data = []
    for val, label, col in items:
        cell_data.append(
            Table(
                [
                    [
                        Paragraph(
                            f"<b>{val}</b>",
                            ParagraphStyle(
                                "k",
                                fontName="Helvetica-Bold",
                                fontSize=20,
                                textColor=col,
                                alignment=1,
                            ),
                        )
                    ],
                    [
                        Paragraph(
                            label,
                            ParagraphStyle(
                                "kl",
                                fontName="Helvetica",
                                fontSize=8,
                                textColor=GREY,
                                alignment=1,
                            ),
                        )
                    ],
                ],
                colWidths=[(CONTENT_W / len(items)) - 4 * mm],
                style=[
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("BACKGROUND", (0, 0), (-1, -1), OFF_WHITE),
                    ("BOX", (0, 0), (-1, -1), 1, LIGHT_GREY),
                    ("TOPPADDING", (0, 0), (-1, -1), 6),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ],
            )
        )
    col_w = [CONTENT_W / len(items)] * len(items)
    outer = Table([cell_data], colWidths=col_w)
    outer.setStyle(
        TableStyle(
            [
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    return outer


def build_story(styles):
    story = []

    # ── Executive Summary ────────────────────────────────────────────────────────
    story += section_header("1. Executive Summary", styles)
    story.append(
        Paragraph(
            "Following the successful launch of the BJP Technologies website in Phase 6, "
            "a series of targeted enhancements were delivered to improve the admin experience, "
            "extend content management capabilities, resolve security issues, and professionalise "
            "the GitHub repository. These changes were delivered across three feature branches "
            "and five areas of improvement.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "The most significant addition is the <b>Dynamic Content Management System</b> — "
            "a SiteSettings singleton model with 40+ editable fields and 11 dedicated admin sections "
            "that allow the client to update all website copy without developer involvement. "
            "Previously, content such as page headlines, counters, body text, and contact details "
            "were hardcoded in HTML templates.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 3 * mm))
    story.append(
        kpi_row(
            [
                ("11", "Admin CMS\nSections", NAVY),
                ("40+", "Editable\nContent Fields", BLUE),
                ("5", "Templates\nFully Dynamic", CYAN),
                ("8", "GitHub Repo\nFiles Added", GREEN),
            ]
        )
    )
    story.append(Spacer(1, 6 * mm))

    # ── Admin UI Overhaul ────────────────────────────────────────────────────────
    story += section_header("2. Admin Panel UI Overhaul", styles)
    story.append(
        Paragraph(
            "The Django admin interface was significantly improved across three modules. "
            "The goal was to make the admin practical for day-to-day use — reducing clutter, "
            "adding direct action controls, and preventing accidental data entry errors.",
            styles["body"],
        )
    )

    story.append(Paragraph("2.1  Services Admin", styles["subsection"]))
    story.append(two_col_table([
        ["Improvement", "Detail"],
        ["Edit & Delete buttons", "Action buttons rendered directly in each list row — no need to navigate into the record just to delete"],
        ["Side-by-side fields", "Name + tagline on row 1, order + active toggle on row 2 — mirrors how users think about the data"],
        ["Slug hidden by default", "Auto-generated slug moved into a collapsed 'Advanced' section — not editable in normal use"],
        ["Icon field collapsed", "Icon SVG class moved into its own collapsible section to reduce visual noise"],
        ["Bulk actions", "Activate and deactivate multiple services at once from the list view"],
        ["Inline order editing", "Order field editable directly in the list without opening each record"],
    ]))
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("2.2  Industries Admin", styles["subsection"]))
    story.append(
        Paragraph(
            "All the same improvements applied to the Industries admin — Edit/Delete action buttons, "
            "side-by-side field layout, collapsed Advanced and Image sections, and bulk "
            "activate/deactivate actions. The admin now presents a consistent experience "
            "across both content modules.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("2.3  Contact Enquiries Admin", styles["subsection"]))
    story.append(two_col_table([
        ["Improvement", "Detail"],
        ["Client fields readonly", "All submitted fields (name, email, phone, message etc.) are read-only — only the status can be changed"],
        ["Auto-mark as Read", "Opening any enquiry automatically changes its status from New → Read — no manual step required"],
        ["Coloured status badges", "New = red, Read = blue, Replied = green — status visible at a glance in the list view"],
        ["Bulk status actions", "Mark selected enquiries as Read, Unread, or Replied in one action"],
        ["No Add button", "The 'Add' button is removed — enquiries only come from the website contact form, never manually created"],
        ["Open / Delete buttons", "Quick action buttons in each list row for the two most common operations"],
    ]))
    story.append(Spacer(1, 4 * mm))

    # ── Security & CSP Fixes ─────────────────────────────────────────────────────
    story += section_header("3. Security & CSP Fixes", styles)
    story.append(
        Paragraph(
            "Two critical issues were discovered and resolved in the Content Security Policy "
            "middleware after deployment. Both caused visible failures in production.",
            styles["body"],
        )
    )

    story.append(two_col_table([
        ["Issue", "Root Cause", "Fix Applied"],
        [
            "Admin panel completely broken — search modal stuck open, all clicks dead",
            "Alpine.js evaluates expressions using new AsyncFunction(), which requires 'unsafe-eval' in script-src. CSP was blocking it silently.",
            "Added 'unsafe-eval' to script-src in ContentSecurityPolicyMiddleware",
        ],
        [
            "Font Awesome icons invisible across the entire site",
            "The Luminos theme loads Font Awesome webfonts from html.themewant.com CDN. CSP font-src only allowed fonts.gstatic.com.",
            "Added https://html.themewant.com and data: to font-src (jarallax embeds a base64 font)",
        ],
    ], col_widths=[52 * mm, 62 * mm, 60 * mm]))
    story.append(Spacer(1, 3 * mm))
    story.append(
        Paragraph(
            "Both fixes were applied to apps/core/middleware.py. The final CSP policy correctly "
            "balances security enforcement with compatibility for all third-party assets used by the Luminos theme.",
            styles["caption"],
        )
    )
    story.append(Spacer(1, 4 * mm))

    # ── Visual Bug Fix ───────────────────────────────────────────────────────────
    story += section_header("4. Visual Bug Fix — Services Page", styles)
    story.append(
        Paragraph(
            "A 750px tall blank section was discovered on the Services list page. "
            "The <b>large-image-area-bg-service-page</b> div was a jarallax background image "
            "container with no visible content — it rendered as dead whitespace between the "
            "banner and the services list. The element was removed entirely.",
            styles["body"],
        )
    )
    story.append(two_col_table([
        ["File", "Action", "Impact"],
        [
            "apps/services/templates/services/list.html",
            "Removed large-image-area-bg-service-page div",
            "Eliminated 750px of blank space between the banner and service list",
        ],
    ], col_widths=[72 * mm, 62 * mm, 40 * mm]))
    story.append(Spacer(1, 4 * mm))

    # ── Dynamic Content System ───────────────────────────────────────────────────
    story += section_header("5. Dynamic Content Management System", styles)
    story.append(
        Paragraph(
            "The largest enhancement in this cycle. Previously, all website copy — headlines, "
            "body paragraphs, counter values, CTA button labels, and contact details — "
            "was hardcoded directly in HTML templates. Any text change required a developer "
            "to edit code, commit, and deploy.",
            styles["body"],
        )
    )
    story.append(
        Paragraph(
            "This has been replaced with a <b>SiteSettings singleton model</b> — a single "
            "database row (always pk=1) containing every editable piece of website content. "
            "The object is passed to every template as <b>{{ company }}</b> via a context processor, "
            "making all fields available site-wide with no additional queries.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("5.1  Architecture", styles["subsection"]))
    story.append(two_col_table([
        ["Component", "Location", "Purpose"],
        ["SiteSettings model", "apps/core/models.py", "Singleton with 40+ fields. pk always = 1. get() method returns or creates the single row."],
        ["Proxy models (×11)", "apps/core/models.py", "Each section (e.g. HeroSectionSettings) is a proxy of SiteSettings — same DB table, separate admin URL."],
        ["Context processor", "apps/core/context_processors.py", "Injects company_info into every request — passes SiteSettings as {{ company }} to all templates."],
        ["Admin sections (×11)", "apps/core/admin.py", "Each proxy model has its own ModelAdmin with relevant fieldsets. changelist_view redirects to the singleton edit form."],
        ["Sidebar navigation", "config/settings/base.py", "Collapsible 'Site Settings' group with 11 sub-links in Unfold sidebar."],
    ], col_widths=[40 * mm, 50 * mm, 84 * mm]))
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("5.2  Admin CMS Sections", styles["subsection"]))
    story.append(
        Paragraph(
            "The 'Site Settings' sidebar group is collapsible — it expands when any "
            "section is active and collapses otherwise. All 11 sections write to the same "
            "database row:",
            styles["body"],
        )
    )
    story.append(two_col_table([
        ["Admin Section", "Fields Editable"],
        ["Company Identity", "Name, tagline, email address, phone number"],
        ["Address", "Office address, postal address, domain name"],
        ["Social Media", "Facebook, Twitter, LinkedIn, YouTube URLs (conditional footer icons)"],
        ["Hero Section", "Home page banner headline, subtext, primary CTA label, secondary CTA label"],
        ["Stats Counters", "4 animated counter pairs on the home page (value + label each)"],
        ["About Strip", "Home page 'Who We Are' section headline and body paragraph"],
        ["About Page", "Banner headline, 4 counters, intro paragraph, 'What We Do' body, 'Our Approach' body"],
        ["Services Page", "Banner headline and subtext paragraph"],
        ["Industries Page", "Banner headline and subtext paragraph"],
        ["Contact Page", "Google Maps embed URL (change if office location moves)"],
        ["Footer CTA", "Call-to-action banner headline, body text, button label"],
    ]))
    story.append(Spacer(1, 4 * mm))

    story.append(Paragraph("5.3  Templates Updated", styles["subsection"]))
    story.append(two_col_table([
        ["Template", "What Was Made Dynamic"],
        ["main/home.html", "Hero headline/subtext/CTAs, 4 stat counters, about strip headline + body, services grid (was hardcoded duplicate — now DB loop)"],
        ["main/about.html", "Banner headline, 4 counters, intro paragraph, 'What We Do' body, 'Our Approach' body, services grid (dynamic loop)"],
        ["services/list.html", "Banner headline and subtext"],
        ["industries/list.html", "Banner headline and subtext"],
        ["contact/contact.html", "Office address, phone, email, Google Maps embed URL"],
        ["core/footer.html", "Footer CTA headline, body, button text + full footer (services, industries, social links all from DB)"],
    ]))
    story.append(Spacer(1, 3 * mm))
    story.append(
        Paragraph(
            "Bug fixed: The about page previously had a hardcoded grid of 6 service cards "
            "that duplicated the Service model data. This was replaced with a dynamic loop — "
            "it now stays in sync automatically when services are edited in admin.",
            styles["caption"],
        )
    )
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("5.4  Database Migrations", styles["subsection"]))
    story.append(two_col_table([
        ["Migration", "Contents"],
        ["0002_add_site_settings", "Initial SiteSettings singleton model — company identity and social media fields"],
        ["0003_add_homepage_content_fields", "14 fields for home page hero, stats counters, and about strip"],
        ["0004_add_sitesettings_proxy_models", "6 proxy models (Company Identity, Address, Social Media, Hero, Stats, About Strip)"],
        ["0005_add_page_content_fields", "24 fields for About, Services, Industries, Contact, Footer sections + 5 new proxy models"],
    ]))
    story.append(Spacer(1, 4 * mm))

    # ── GitHub Repo Polish ───────────────────────────────────────────────────────
    story += section_header("6. GitHub Repository Polish", styles)
    story.append(
        Paragraph(
            "The GitHub repository was brought to professional open-source standards. "
            "A developer joining the project cold can now understand the entire project, "
            "set it up locally, and contribute correctly — solely from the repository files.",
            styles["body"],
        )
    )

    story.append(two_col_table([
        ["File Added", "Contents"],
        ["README.md", "CI/Python/Django/Black/Ruff badges, tech stack table, full local setup guide, environment variables reference, content management guide, deployment notes, branching workflow summary"],
        ["LICENSE", "Proprietary copyright notice — BJP Technologies (T) Limited owns all rights. Prevents unauthorised use or distribution of the codebase."],
        ["SECURITY.md", "Responsible disclosure process for vulnerability reports. Response timeline (48hr acknowledgement, 7-day assessment, 30-day patch). Scope definition. Security practices summary. On-brand for an IT security company."],
        ["CONTRIBUTING.md", "Branching workflow, commit message format (Conventional Commits), definition of done checklist, pull request process, local setup reference."],
        ["CHANGELOG.md", "Full project history from v0.1.0 (Phase 1 — Infrastructure) through v0.6.0 (Phase 6 — Polish & Launch) following Keep a Changelog format."],
        [".github/PULL_REQUEST_TEMPLATE.md", "Every PR auto-populates with type of change checkboxes, migration checklist, screenshots placeholder, and the full definition-of-done checklist."],
        [".github/ISSUE_TEMPLATE/bug_report.md", "Structured bug reports: description, reproduction steps, expected vs actual, environment table, possible cause."],
        [".github/ISSUE_TEMPLATE/feature_request.md", "Structured feature requests: problem statement, proposed solution, alternatives, scope checkboxes, priority, affected components."],
    ]))
    story.append(Spacer(1, 4 * mm))

    # ── Files Changed Summary ────────────────────────────────────────────────────
    story += section_header("7. Files Changed — Complete Reference", styles)
    story.append(two_col_table([
        ["File", "Change Type", "Summary"],
        ["apps/core/models.py", "Modified", "SiteSettings + 11 proxy models added"],
        ["apps/core/admin.py", "Modified", "11 proxy model admins, dashboard callbacks, enquiry badge"],
        ["apps/core/context_processors.py", "Modified", "Returns SiteSettings object as 'company'"],
        ["apps/core/middleware.py", "Modified", "CSP: added unsafe-eval, Luminos CDN, data: to font-src"],
        ["apps/core/templates/core/footer.html", "Modified", "Footer CTA + all contact/social data dynamic"],
        ["apps/core/migrations/0002–0005", "Created", "40+ new fields, 11 proxy models across 4 migrations"],
        ["apps/main/views.py", "Modified", "AboutView passes services queryset to template"],
        ["apps/main/templates/main/home.html", "Modified", "Hero, stats, about strip, services grid all dynamic"],
        ["apps/main/templates/main/about.html", "Modified", "Banner, counters, all body texts, services grid dynamic"],
        ["apps/services/templates/services/list.html", "Modified", "Banner dynamic + removed 750px dead div"],
        ["apps/industries/templates/industries/list.html", "Modified", "Banner headline + subtext dynamic"],
        ["apps/contact/templates/contact/contact.html", "Modified", "Address, phone, email, maps URL dynamic"],
        ["apps/services/admin.py", "Modified", "Action buttons, side-by-side layout, bulk actions"],
        ["apps/industries/admin.py", "Modified", "Same improvements as services admin"],
        ["apps/contact/admin.py", "Modified", "Readonly fields, auto-read, badges, bulk actions"],
        ["config/settings/base.py", "Modified", "Unfold nav: 11-item collapsible Site Settings group"],
        ["README.md", "Created", "Full project documentation with badges"],
        ["LICENSE", "Created", "Proprietary copyright notice"],
        ["SECURITY.md", "Created", "Responsible disclosure process"],
        ["CONTRIBUTING.md", "Created", "Developer onboarding and contribution guide"],
        ["CHANGELOG.md", "Created", "Full project history v0.1.0–v0.6.0"],
        [".github/PULL_REQUEST_TEMPLATE.md", "Created", "Definition-of-done PR checklist"],
        [".github/ISSUE_TEMPLATE/bug_report.md", "Created", "Structured bug reporting"],
        [".github/ISSUE_TEMPLATE/feature_request.md", "Created", "Structured feature requests"],
    ], col_widths=[72 * mm, 26 * mm, 76 * mm]))
    story.append(Spacer(1, 4 * mm))

    # ── Technical Decisions ──────────────────────────────────────────────────────
    story += section_header("8. Key Technical Decisions", styles)
    decisions = [
        (
            "Proxy models instead of separate tables for SiteSettings sections",
            "All site settings belong in one row — splitting into separate models would require joins "
            "or multiple singleton patterns. Proxy models give each section its own admin URL and form "
            "while reading and writing the same database row. Zero query overhead.",
        ),
        (
            "collapsible: True on Site Settings nav group",
            "Unfold's navigation template supports group.collapsible via Alpine.js x-data. "
            "The group auto-opens when any of its items is active and collapses otherwise. "
            "A one-line config change — no custom template override needed.",
        ),
        (
            "About page services grid replaced with dynamic loop (not just made editable)",
            "The hardcoded grid was a silent bug — editing services in admin had no effect on the "
            "about page. A dynamic loop is always in sync. No new admin fields needed.",
        ),
        (
            "Proprietary LICENSE over MIT or GPL",
            "This is a private corporate codebase. A proprietary notice explicitly reserves all rights "
            "to BJP Technologies (T) Limited and prevents any assumption of open-source permissions.",
        ),
        (
            "SECURITY.md included despite private repo",
            "The live site is public-facing. Any researcher finding a vulnerability in the live site "
            "needs a clear disclosure path. SECURITY.md is discovered automatically by GitHub and "
            "linked in the repo's Security tab.",
        ),
    ]
    for title, reason in decisions:
        story.append(Paragraph(f"<b>→ {title}</b>", styles["highlight"]))
        story.append(Paragraph(reason, styles["body"]))

    # ── Closing ──────────────────────────────────────────────────────────────────
    story += section_header("9. Summary", styles)
    story.append(
        Paragraph(
            "These post-Phase 6 enhancements complete the initial development cycle for the "
            "BJP Technologies (T) Limited website. The platform is now fully dynamic, "
            "professionally documented, and operationally self-sufficient for the client. "
            "Content updates, enquiry management, and service/industry administration all operate "
            "through the admin panel with no developer involvement required.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 3 * mm))

    summary_data = [
        ["Area", "Before", "After"],
        ["Website content", "Hardcoded in HTML templates", "40+ fields editable from admin panel"],
        ["Admin navigation", "Single 'Site Settings' page", "11 collapsible per-section links"],
        ["Services admin", "Basic list + form", "Action buttons, side-by-side layout, bulk actions"],
        ["Contact enquiries", "Standard editable admin", "Readonly client data, auto-read, colour badges"],
        ["CSP security", "Admin broken, icons invisible", "Alpine.js and Font Awesome fully working"],
        ["Services page", "750px blank dead space", "Removed — clean layout"],
        ["GitHub repo", "No documentation files", "README, LICENSE, SECURITY, CONTRIBUTING, CHANGELOG"],
    ]
    st = Table(summary_data, colWidths=[40 * mm, 67 * mm, 67 * mm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(st)
    story.append(Spacer(1, 6 * mm))

    story.append(
        Paragraph(
            "BJP Technologies (T) Limited — bjptechnologies.co.tz",
            ParagraphStyle(
                "final",
                fontName="Helvetica-Bold",
                fontSize=11,
                textColor=NAVY,
                alignment=1,
                spaceAfter=2 * mm,
            ),
        )
    )
    story.append(
        Paragraph(
            "Secure Technology. Scalable Growth.",
            ParagraphStyle(
                "tagline",
                fontName="Helvetica-Bold",
                fontSize=9,
                textColor=CYAN,
                alignment=1,
            ),
        )
    )

    return story


def main():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=25 * mm,
        bottomMargin=20 * mm,
    )

    cover_frame = Frame(
        0, 0, PAGE_W, PAGE_H,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id="cover",
    )
    content_frame = Frame(18 * mm, 20 * mm, CONTENT_W, PAGE_H - 45 * mm, id="content")

    cover_template = PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page)
    content_template = PageTemplate(id="content", frames=[content_frame], onPage=header_footer)

    doc.addPageTemplates([cover_template, content_template])

    styles = build_styles()
    story = [Spacer(1, PAGE_H)]
    story.append(Paragraph('<para><seqreset id="page"/></para>', styles["small"]))
    story.extend(build_story(styles))

    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
