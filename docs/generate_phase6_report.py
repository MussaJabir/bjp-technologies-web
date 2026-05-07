"""Generate BJP Technologies Phase 6 Completion Report PDF."""

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

OUTPUT = "docs/BJP_Technologies_Phase6_Report.pdf"

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
    canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 12 * mm, "PHASE 6 — POLISH & LAUNCH")

    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, 12 * mm, PAGE_W, 1 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(18 * mm, 4.5 * mm, "bjptechnologies.co.tz  |  Secure Technology. Scalable Growth.")
    canvas.drawRightString(PAGE_W - 18 * mm, 4.5 * mm, f"Page {doc.page}")
    canvas.restoreState()


def cover_page(canvas, doc):
    canvas.saveState()

    # White background
    canvas.setFillColor(WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Navy left sidebar
    SIDEBAR_W = 22 * mm
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, SIDEBAR_W, PAGE_H, fill=1, stroke=0)

    # Cyan accent stripe next to sidebar
    canvas.setFillColor(CYAN)
    canvas.rect(SIDEBAR_W, 0, 3, PAGE_H, fill=1, stroke=0)

    # Navy top bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 22 * mm, PAGE_W, 22 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H - 22 * mm, PAGE_W, 2, fill=1, stroke=0)

    # Top bar text
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H - 14 * mm, "BJP TECHNOLOGIES (T) LIMITED")
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(CYAN)
    canvas.drawRightString(PAGE_W - 14 * mm, PAGE_H - 14 * mm, "bjptechnologies.co.tz")

    # Phase pill
    pill_x = SIDEBAR_W + 10 * mm
    pill_y = PAGE_H * 0.76
    canvas.setFillColor(NAVY)
    canvas.roundRect(pill_x, pill_y, 58 * mm, 9 * mm, 4, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(pill_x + 4 * mm, pill_y + 3 * mm, "PHASE 6  ·  POLISH & LAUNCH  ·  MAY 2026")

    # Main headline
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 40)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.64, "POLISH &")
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.56, "LAUNCH")

    # Cyan underline accent
    canvas.setFillColor(CYAN)
    canvas.rect(SIDEBAR_W + 10 * mm, PAGE_H * 0.54, 70 * mm, 3, fill=1, stroke=0)

    canvas.setFillColor(colors.HexColor("#1565C0"))
    canvas.setFont("Helvetica-Bold", 15)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.505, "COMPLETION REPORT")

    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 9.5)
    canvas.drawString(SIDEBAR_W + 10 * mm, PAGE_H * 0.475, "BJP Technologies (T) Limited — May 2026")

    # LIVE badge
    canvas.setFillColor(GREEN)
    canvas.roundRect(SIDEBAR_W + 10 * mm, PAGE_H * 0.415, 85 * mm, 13 * mm, 4, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(SIDEBAR_W + 16 * mm, PAGE_H * 0.415 + 4 * mm, "LIVE  ·  bjptechnologies.co.tz")

    # Stats cards — white cards, navy numbers, grey labels
    stats = [
        ("18", "Google\nIndexed Pages", NAVY),
        ("100%", "Security\nHeaders", BLUE),
        ("6/6", "Phases\nCompleted", GREEN),
        ("HTTPS", "SSL\nEnforced", NAVY),
    ]
    card_area_x = SIDEBAR_W + 10 * mm
    card_area_w = PAGE_W - card_area_x - 14 * mm
    col_w = card_area_w / 4
    for i, (val, label, col) in enumerate(stats):
        x = card_area_x + i * col_w
        # Card shadow effect
        canvas.setFillColor(LIGHT_GREY)
        canvas.roundRect(x + 3.5, PAGE_H * 0.285 - 1, col_w - 7, 24 * mm, 4, fill=1, stroke=0)
        # Card
        canvas.setFillColor(WHITE)
        canvas.roundRect(x + 3, PAGE_H * 0.287, col_w - 7, 24 * mm, 4, fill=1, stroke=0)
        # Top accent
        canvas.setFillColor(col)
        canvas.rect(x + 3, PAGE_H * 0.287 + 23 * mm, col_w - 7, 1 * mm, fill=1, stroke=0)
        # Value
        canvas.setFillColor(col)
        canvas.setFont("Helvetica-Bold", 18)
        canvas.drawCentredString(x + col_w / 2, PAGE_H * 0.287 + 13 * mm, val)
        # Label
        canvas.setFillColor(GREY)
        canvas.setFont("Helvetica", 7)
        for j, line in enumerate(label.split("\n")):
            canvas.drawCentredString(x + col_w / 2, PAGE_H * 0.287 + 7 * mm - j * 8, line)

    # Tagline area
    canvas.setFillColor(OFF_WHITE)
    canvas.rect(SIDEBAR_W + 3, PAGE_H * 0.20, PAGE_W - SIDEBAR_W - 3, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawCentredString((PAGE_W + SIDEBAR_W) / 2, PAGE_H * 0.20 + 10 * mm,
                             "Secure Technology.  Scalable Growth.")
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString((PAGE_W + SIDEBAR_W) / 2, PAGE_H * 0.20 + 4 * mm,
                             "Software Development  ·  Cybersecurity  ·  Cloud  ·  Payments  ·  Managed IT")

    # Vertical label in sidebar
    canvas.saveState()
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.translate(13 * mm, PAGE_H / 2)
    canvas.rotate(90)
    canvas.drawCentredString(0, 0, "BJP TECHNOLOGIES  (T)  LIMITED")
    canvas.restoreState()

    # Bottom footer strip
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, 12 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, 12 * mm, PAGE_W, 1.5 * mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawCentredString(PAGE_W / 2, 4 * mm,
                             "bjptechnologies.co.tz  ·  info@bjptechnologies.co.tz  ·  +255 678 290 994")
    canvas.restoreState()


def build_styles():
    return {
        "section": ParagraphStyle("section", fontName="Helvetica-Bold", fontSize=13,
                                   textColor=NAVY, spaceAfter=4 * mm, spaceBefore=6 * mm),
        "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5,
                                textColor=BLACK, spaceAfter=3 * mm, leading=15),
        "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9,
                                  textColor=BLACK, spaceAfter=2 * mm, leading=14,
                                  leftIndent=8 * mm, bulletIndent=2 * mm),
        "caption": ParagraphStyle("caption", fontName="Helvetica-Oblique", fontSize=8,
                                   textColor=GREY, spaceAfter=2 * mm),
        "highlight": ParagraphStyle("highlight", fontName="Helvetica-Bold", fontSize=10,
                                     textColor=BLUE, spaceAfter=3 * mm),
        "green": ParagraphStyle("green", fontName="Helvetica-Bold", fontSize=9.5,
                                 textColor=GREEN, spaceAfter=2 * mm),
        "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8,
                                 textColor=GREY, spaceAfter=1 * mm),
    }


def divider(color=CYAN, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4 * mm, spaceBefore=2 * mm)


def section_header(text, styles):
    return [
        Paragraph(text, styles["section"]),
        divider(),
    ]


def status_table(rows, styles):
    data = [["Deliverable", "Status", "Notes"]]
    data.extend(rows)
    t = Table(data, colWidths=[80 * mm, 22 * mm, 72 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("ALIGN", (1, 0), (1, -1), "CENTER"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    return t


def kpi_row(items):
    """items: list of (value, label, color) tuples."""
    cell_data = []
    for val, label, col in items:
        cell_data.append(
            Table(
                [[Paragraph(f'<font color="{col.hexval()}" size="20"><b>{val}</b></font>', ParagraphStyle("k", fontName="Helvetica-Bold", fontSize=20, textColor=col, alignment=1))],
                 [Paragraph(label, ParagraphStyle("kl", fontName="Helvetica", fontSize=8, textColor=GREY, alignment=1))]],
                colWidths=[(CONTENT_W / len(items)) - 4 * mm],
                style=[("ALIGN", (0, 0), (-1, -1), "CENTER"),
                       ("BACKGROUND", (0, 0), (-1, -1), OFF_WHITE),
                       ("BOX", (0, 0), (-1, -1), 1, LIGHT_GREY),
                       ("TOPPADDING", (0, 0), (-1, -1), 6),
                       ("BOTTOMPADDING", (0, 0), (-1, -1), 6)],
            )
        )
    col_w = [(CONTENT_W / len(items))] * len(items)
    outer = Table([cell_data], colWidths=col_w)
    outer.setStyle(TableStyle([("ALIGN", (0, 0), (-1, -1), "CENTER"),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                                ("LEFTPADDING", (0, 0), (-1, -1), 2),
                                ("RIGHTPADDING", (0, 0), (-1, -1), 2)]))
    return outer


def build_story(styles):
    story = []

    # ── Executive Summary ───────────────────────────────────────────────────────
    story += section_header("1. Executive Summary", styles)
    story.append(Paragraph(
        "Phase 6 marks the completion of the BJP Technologies (T) Limited website project. "
        "This phase focused on production hardening: SEO infrastructure, security header enforcement, "
        "per-page Open Graph metadata, sitemap generation, and robots.txt configuration. "
        "The site is fully live at <b>bjptechnologies.co.tz</b>, indexed by Google, and secured with "
        "industry-standard HTTP security headers.",
        styles["body"]
    ))
    story.append(Paragraph(
        "The site went live during Phase 4 and has been accumulating Google search impressions since. "
        "By the time Phase 6 was completed, <b>18 pages were already indexed</b> by Google and the site "
        "appears in search results for 'bjp technologies' — with Google's AI Overview correctly "
        "identifying BJP Technologies (T) Limited as a Tanzanian IT solutions company.",
        styles["body"]
    ))
    story.append(Spacer(1, 3 * mm))

    story.append(kpi_row([
        ("18", "Pages Indexed\nby Google", GREEN),
        ("100%", "Security Headers\nConfigured", BLUE),
        ("LIVE", "bjptechnologies\n.co.tz", CYAN),
        ("6/6", "Project Phases\nCompleted", NAVY),
    ]))
    story.append(Spacer(1, 5 * mm))

    # ── Google Search Presence ──────────────────────────────────────────────────
    story += section_header("2. Google Search Presence", styles)
    story.append(Paragraph(
        "The site was submitted to Google Search Console before Phase 6 began. "
        "As of 7 May 2026, the following is confirmed:",
        styles["body"]
    ))
    google_data = [
        ["Metric", "Value", "Status"],
        ["Domain verified in Search Console", "bjptechnologies.co.tz", "✅ Confirmed"],
        ["Pages indexed", "18 pages", "✅ Indexed"],
        ["Search appearance", "Appears for 'bjp technologies'", "✅ Ranking"],
        ["Google AI Overview", "Identifies BJP Technologies (T) Ltd as Tanzanian IT company", "✅ Featured"],
        ["HTTPS status", "Valid SSL certificate, enforced", "✅ Secure"],
        ["sitemap.xml", "Generated — submit in Search Console", "🔄 Pending submission"],
        ["robots.txt", "Deployed — Google will auto-discover", "✅ Live"],
    ]
    gt = Table(google_data, colWidths=[70 * mm, 65 * mm, 39 * mm])
    gt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(gt)
    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph(
        "Action required: In Google Search Console → Indexing → Sitemaps → submit "
        "https://bjptechnologies.co.tz/sitemap.xml to accelerate re-indexing of all pages.",
        styles["caption"]
    ))

    # ── SEO Deliverables ────────────────────────────────────────────────────────
    story += section_header("3. SEO Infrastructure", styles)
    story.append(Paragraph(
        "Three core SEO components were implemented in Phase 6:",
        styles["body"]
    ))

    story.append(Paragraph("<b>3.1  robots.txt</b>", styles["highlight"]))
    story.append(Paragraph(
        "Served at <b>bjptechnologies.co.tz/robots.txt</b> via Django's TemplateView with "
        "content_type='text/plain'. Instructs all crawlers to allow the entire site except /admin/. "
        "References the sitemap URL so Google discovers it automatically.",
        styles["body"]
    ))

    story.append(Paragraph("<b>3.2  sitemap.xml</b>", styles["highlight"]))
    story.append(Paragraph(
        "Generated dynamically at <b>bjptechnologies.co.tz/sitemap.xml</b> using "
        "django.contrib.sitemaps. Three sitemap classes cover the full site:",
        styles["body"]
    ))
    sitemap_data = [
        ["Sitemap Class", "Pages Covered", "Priority", "Changefreq"],
        ["StaticViewSitemap", "Home, About, Services list, Industries list, Contact", "0.8", "Monthly"],
        ["ServiceSitemap", "All 7 active service detail pages", "0.7", "Monthly"],
        ["IndustrySitemap", "All 6 active industry detail pages", "0.7", "Monthly"],
    ]
    st = Table(sitemap_data, colWidths=[48 * mm, 72 * mm, 22 * mm, 32 * mm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("ALIGN", (2, 0), (3, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(st)
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("<b>3.3  Per-Page Open Graph Tags</b>", styles["highlight"]))
    story.append(Paragraph(
        "All 7 page templates now declare unique og:title, og:description, and og:url. "
        "When any BJP Technologies page is shared on LinkedIn, WhatsApp, or Twitter, "
        "the preview card shows the specific page title and description — not a generic fallback. "
        "Service and Industry detail pages use model data dynamically.",
        styles["body"]
    ))
    og_data = [
        ["Template", "og:title", "og:url"],
        ["home.html", "BJP Technologies (T) Limited — Secure Technology...", "/"],
        ["about.html", "About Us — BJP Technologies (T) Limited", "/about/"],
        ["services/list.html", "Our Services — BJP Technologies (T) Limited", "/services/"],
        ["services/detail.html", "{{ service.name }} — BJP Technologies...", "/services/<slug>/"],
        ["industries/list.html", "Industries We Serve — BJP Technologies...", "/industries/"],
        ["industries/detail.html", "{{ industry.name }} — BJP Technologies...", "/industries/<slug>/"],
        ["contact/contact.html", "Contact Us — BJP Technologies (T) Limited", "/contact/"],
    ]
    ot = Table(og_data, colWidths=[50 * mm, 80 * mm, 44 * mm])
    ot.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ot)
    story.append(Spacer(1, 4 * mm))

    # ── Security Audit ──────────────────────────────────────────────────────────
    story += section_header("4. Security Audit Results", styles)
    story.append(Paragraph(
        "A live header audit was performed against the production server using curl. "
        "All critical security headers are present and correctly configured:",
        styles["body"]
    ))
    sec_rows = [
        ["Strict-Transport-Security", "✅ PASS", "max-age=31536000; includeSubDomains; preload"],
        ["X-Frame-Options", "✅ PASS", "DENY — clickjacking blocked"],
        ["X-Content-Type-Options", "✅ PASS", "nosniff"],
        ["Referrer-Policy", "✅ PASS", "same-origin"],
        ["Cross-Origin-Opener-Policy", "✅ PASS", "same-origin"],
        ["Content-Security-Policy", "✅ ADDED", "Phase 6 — restricts scripts, fonts, frames"],
        ["CSRF Cookie Secure", "✅ PASS", "Enforced in production settings"],
        ["Session Cookie Secure", "✅ PASS", "Enforced in production settings"],
        ["SSL Redirect", "✅ PASS", "SECURE_SSL_REDIRECT = True"],
        ["DEBUG", "✅ PASS", "False in production — confirmed"],
    ]
    story.append(status_table(sec_rows, styles))
    story.append(Spacer(1, 3 * mm))

    story.append(Paragraph("<b>Content Security Policy (Phase 6 addition):</b>", styles["highlight"]))
    story.append(Paragraph(
        "A custom CSP middleware (apps/core/middleware.py) was added to the production MIDDLEWARE stack. "
        "It restricts script execution to self + inline (required for Luminos JS), styles to self + "
        "Google Fonts, fonts to self + fonts.gstatic.com, and blocks all framing. "
        "Applied production-only to avoid false positives during local development.",
        styles["body"]
    ))

    # ── Live Pages ──────────────────────────────────────────────────────────────
    story += section_header("5. Live Pages Verified", styles)
    story.append(Paragraph(
        "All pages were verified live during the Phase 6 audit session:",
        styles["body"]
    ))
    pages_data = [
        ["URL", "Page Title", "HTTP Status"],
        ["bjptechnologies.co.tz/", "BJP Technologies (T) Limited | Secure Technology...", "200 ✅"],
        ["bjptechnologies.co.tz/about/", "About Us — BJP Technologies (T) Limited", "200 ✅"],
        ["bjptechnologies.co.tz/services/", "Our Services — BJP Technologies (T) Limited", "200 ✅"],
        ["bjptechnologies.co.tz/industries/", "Industries We Serve — BJP Technologies (T) Ltd", "200 ✅"],
        ["bjptechnologies.co.tz/contact/", "Contact Us — BJP Technologies (T) Limited", "200 ✅"],
        ["bjptechnologies.co.tz/services/<slug>/", "7 service detail pages (e.g. Cybersecurity)", "200 ✅"],
        ["bjptechnologies.co.tz/industries/<slug>/", "6 industry detail pages (e.g. Healthcare)", "200 ✅"],
        ["bjptechnologies.co.tz/admin/", "BJP Technologies Admin (django-unfold)", "200 ✅"],
        ["bjptechnologies.co.tz/sitemap.xml", "XML sitemap — all 15 URLs", "200 ✅"],
        ["bjptechnologies.co.tz/robots.txt", "User-agent: * / Allow: / / Disallow: /admin/", "200 ✅"],
        ["bjptechnologies.co.tz/invalid-page/", "Custom 404 — branded BJP error page", "404 ✅"],
    ]
    pt = Table(pages_data, colWidths=[75 * mm, 75 * mm, 24 * mm])
    pt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("ALIGN", (2, 0), (2, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(pt)
    story.append(Spacer(1, 4 * mm))

    # ── Admin & CMS Summary ─────────────────────────────────────────────────────
    story += section_header("6. Admin & CMS (Phase 5 Summary)", styles)
    story.append(Paragraph(
        "The admin interface was completed in Phase 5 using <b>django-unfold 0.92.0</b> — "
        "a modern Tailwind CSS-based admin replacement chosen for its full Django 6 compatibility "
        "and extensive customisation capabilities. Wagtail CMS was evaluated but replaced due to "
        "React sidebar incompatibilities with DOM-level CSS injection.",
        styles["body"]
    ))

    admin_features = [
        ["Feature", "Details"],
        ["Custom KPI Dashboard", "4 metric cards: Active Services, Active Industries, Unread Enquiries, Total"],
        ["Enquiry Status Panel", "Breakdown of new/read/replied with segmented progress bar"],
        ["Recent Enquiries Feed", "Live list of last 6 enquiries with name, email, service, date, status badge"],
        ["Sidebar Navigation", "Icons, badge counter (unread enquiries), grouped sections"],
        ["BJP Brand Theme", "Navy/blue color scale, BJPmark logo, professional enterprise look"],
        ["Admin Users", "bjpadmin superuser created on production server"],
        ["Wagtail Cleanup", "46 legacy Wagtail tables auto-dropped via RunPython migration"],
    ]
    at = Table(admin_features, colWidths=[55 * mm, 119 * mm])
    at.setStyle(TableStyle([
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
    story.append(at)
    story.append(Spacer(1, 4 * mm))

    # ── Full Project Summary ────────────────────────────────────────────────────
    story += section_header("7. Full Project Completion Summary", styles)
    story.append(Paragraph(
        "BJP Technologies (T) Limited website — all 6 phases complete:",
        styles["body"]
    ))
    project_data = [
        ["Phase", "Name", "Key Deliverables", "Status"],
        ["1", "Infrastructure", "Django 6 + MySQL + cPanel + GitHub Actions CI/CD", "✅"],
        ["2", "Core Foundation", "Base templates, BJP brand CSS, navbar, footer, 404/500", "✅"],
        ["3", "Content Pages", "Home, About, Services (7), Industries (6) — model-driven", "✅"],
        ["4", "Contact System", "Contact form, email notifications, rate limiting, admin", "✅"],
        ["5", "Admin & CMS", "django-unfold dashboard, KPI cards, enquiry management", "✅"],
        ["6", "Polish & Launch", "Sitemap, robots.txt, OG tags, CSP, Google indexed 18 pages", "✅"],
    ]
    pjt = Table(project_data, colWidths=[14 * mm, 35 * mm, 108 * mm, 17 * mm])
    pjt.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("ALIGN", (3, 0), (3, -1), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(pjt)
    story.append(Spacer(1, 5 * mm))

    # ── Visit the Site CTA ──────────────────────────────────────────────────────
    story += section_header("8. Visit the Live Website", styles)

    cta_inner = Table([
        [Paragraph(
            '<font color="#00C6FF" size="22"><b>bjptechnologies.co.tz</b></font>',
            ParagraphStyle("cta", fontName="Helvetica-Bold", fontSize=22, textColor=CYAN, alignment=1)
        )],
        [Paragraph(
            "Tanzania's Premier IT Solutions Partner",
            ParagraphStyle("ctasub", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE, alignment=1)
        )],
        [Spacer(1, 3 * mm)],
        [Paragraph(
            "Software Development  ·  Cybersecurity  ·  Cloud Infrastructure\n"
            "Payment Integrations  ·  Managed IT  ·  IT Consulting",
            ParagraphStyle("ctaservices", fontName="Helvetica", fontSize=9, textColor=GREY, alignment=1, leading=16)
        )],
        [Spacer(1, 4 * mm)],
        [Table(
            [[
                Paragraph("Our Services", ParagraphStyle("btn", fontName="Helvetica-Bold", fontSize=9, textColor=NAVY, alignment=1)),
                Spacer(8 * mm, 1),
                Paragraph("Contact Us", ParagraphStyle("btn2", fontName="Helvetica-Bold", fontSize=9, textColor=WHITE, alignment=1)),
            ]],
            colWidths=[55 * mm, 8 * mm, 55 * mm],
            style=[
                ("BACKGROUND", (0, 0), (0, 0), CYAN),
                ("BACKGROUND", (2, 0), (2, 0), BLUE),
                ("TOPPADDING", (0, 0), (-1, -1), 6),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ]
        )],
    ], colWidths=[CONTENT_W - 20 * mm])
    cta_inner.setStyle(TableStyle([
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    cta_outer = Table([[cta_inner]], colWidths=[CONTENT_W])
    cta_outer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("BOX", (0, 0), (-1, -1), 2, CYAN),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(cta_outer)
    story.append(Spacer(1, 5 * mm))

    # ── Technical Decisions ─────────────────────────────────────────────────────
    story += section_header("9. Key Technical Decisions", styles)
    decisions = [
        ("sitemap.xml uses location() not get_absolute_url()",
         "Keeps models decoupled from URL configuration. Sitemap classes reference URL names directly."),
        ("robots.txt served via TemplateView (text/plain)",
         "No extra package or file serving config. Django template system handles it natively."),
        ("CSP in production MIDDLEWARE override only",
         "Development builds skip CSP enforcement to avoid false positives. Production applies it server-wide."),
        ("Wagtail replaced with django-unfold",
         "Wagtail's React sidebar conflicts with DOM-level CSS injection, causing infinite re-render loops. "
         "django-unfold is Tailwind-based with no React dependency."),
        ("Superuser created via File Manager script (not env vars)",
         "cPanel rejects env var values containing ! and @ characters. File Manager bypass avoids "
         "the 'Invalid parameter passed' API error while keeping credentials out of git."),
    ]
    for title, reason in decisions:
        story.append(Paragraph(f"<b>→ {title}</b>", styles["highlight"]))
        story.append(Paragraph(reason, styles["body"]))

    # ── Next Steps ──────────────────────────────────────────────────────────────
    story += section_header("10. Recommended Next Steps", styles)
    next_steps = [
        ("Submit sitemap to Google Search Console",
         "Search Console → Indexing → Sitemaps → paste https://bjptechnologies.co.tz/sitemap.xml → Submit"),
        ("Run Google PageSpeed Insights",
         "Test at pagespeed.web.dev — target score above 80 on mobile. Identify largest contentful paint candidates."),
        ("Image optimisation review",
         "Audit static/images/ for files over 200KB. Convert hero images to WebP format for faster load times."),
        ("Set up Google Analytics 4",
         "Add GA4 measurement ID to track visitor sessions, page views, and contact form conversions."),
        ("Social media profiles",
         "Link bjptechnologies.co.tz to LinkedIn, Facebook, and Twitter/X profiles for brand signals."),
        ("SSL auto-renewal check",
         "Confirm cPanel AutoSSL is enabled and the certificate renews automatically before expiry."),
    ]
    ns_data = [["#", "Action", "Detail"]]
    for i, (action, detail) in enumerate(next_steps, 1):
        ns_data.append([str(i), action, detail])
    ns_t = Table(ns_data, colWidths=[8 * mm, 55 * mm, 111 * mm])
    ns_t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 8.5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("FONTNAME", (1, 1), (1, -1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [OFF_WHITE, WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.4, LIGHT_GREY),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ns_t)
    story.append(Spacer(1, 6 * mm))

    story.append(Paragraph(
        "BJP Technologies (T) Limited — bjptechnologies.co.tz — is production-ready, "
        "Google-indexed, and secure. The platform is built to scale.",
        ParagraphStyle("final", fontName="Helvetica-Bold", fontSize=10, textColor=BLUE,
                       alignment=1, spaceAfter=3 * mm)
    ))

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

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0, id="cover")
    content_frame = Frame(18 * mm, 20 * mm, CONTENT_W, PAGE_H - 45 * mm, id="content")

    cover_template = PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page)
    content_template = PageTemplate(id="content", frames=[content_frame], onPage=header_footer)

    doc.addPageTemplates([cover_template, content_template])

    styles = build_styles()
    story = [Spacer(1, PAGE_H)]  # blank cover page spacer
    story.append(Paragraph('<para><seqreset id="page"/></para>', styles["small"]))
    story.extend(build_story(styles))

    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    main()
