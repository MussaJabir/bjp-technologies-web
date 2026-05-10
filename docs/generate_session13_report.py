"""Generate BJP Technologies Session 13 Report PDF."""

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "docs/BJP_Technologies_Session13_Report.pdf"

NAVY = colors.HexColor("#0D1B4B")
BLUE = colors.HexColor("#1565C0")
CYAN = colors.HexColor("#00C6FF")
GREY = colors.HexColor("#8A94B0")
OFF_WHITE = colors.HexColor("#F4F6FC")
GREEN = colors.HexColor("#2ECC71")
WHITE = colors.white
BLACK = colors.black
LIGHT_GREY = colors.HexColor("#E8ECF4")

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
    canvas.drawRightString(PAGE_W - 18 * mm, PAGE_H - 12 * mm, "SESSION 13 — WORK REPORT")

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
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, PAGE_H * 0.38, PAGE_W, 2 * mm, fill=1, stroke=0)
    canvas.rect(0, PAGE_H * 0.38 - 4 * mm, PAGE_W, 1 * mm, fill=1, stroke=0)

    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 28)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.62, "BJP TECHNOLOGIES")
    canvas.setFont("Helvetica", 16)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.62 - 12 * mm, "(T) LIMITED")

    canvas.setFillColor(CYAN)
    canvas.setFont("Helvetica-Bold", 20)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.45, "SESSION 13")
    canvas.setFont("Helvetica-Bold", 14)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.45 - 9 * mm, "WORK REPORT")

    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 10)
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.30, "Date: 10 May 2026")
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.30 - 6 * mm, "Project: bjptechnologies.co.tz")
    canvas.drawCentredString(PAGE_W / 2, PAGE_H * 0.30 - 12 * mm, "Phase 6 — Polish & Launch")

    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        PAGE_W / 2, 20 * mm, "Secure Technology. Scalable Growth."
    )
    canvas.restoreState()


def build_styles():
    return {
        "section": ParagraphStyle(
            "section",
            fontName="Helvetica-Bold",
            fontSize=13,
            textColor=NAVY,
            spaceBefore=8 * mm,
            spaceAfter=3 * mm,
        ),
        "subsection": ParagraphStyle(
            "subsection",
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=BLUE,
            spaceBefore=4 * mm,
            spaceAfter=2 * mm,
        ),
        "body": ParagraphStyle(
            "body",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=BLACK,
            leading=14,
            spaceAfter=3 * mm,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            fontName="Helvetica",
            fontSize=9.5,
            textColor=BLACK,
            leading=14,
            leftIndent=10 * mm,
            spaceAfter=1.5 * mm,
        ),
        "code": ParagraphStyle(
            "code",
            fontName="Courier",
            fontSize=8.5,
            textColor=BLUE,
            leading=13,
            leftIndent=6 * mm,
            spaceAfter=2 * mm,
            backColor=OFF_WHITE,
        ),
        "label": ParagraphStyle(
            "label",
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=NAVY,
        ),
        "tag": ParagraphStyle(
            "tag",
            fontName="Helvetica",
            fontSize=8.5,
            textColor=BLUE,
        ),
    }


def ruled_table(data, col_widths, header_bg=NAVY, header_fg=WHITE):
    style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), header_fg),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, LIGHT_GREY]),
        ("GRID", (0, 0), (-1, -1), 0.4, GREY),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ])
    return Table(data, colWidths=col_widths, style=style, repeatRows=1)


def build_story(styles):
    s = styles
    story = []

    # ── Section 1: GitHub About ─────────────────────────────────────────────
    story.append(Paragraph("1. GitHub Repository About Section", s["section"]))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=CYAN, spaceAfter=3 * mm))

    story.append(Paragraph("<b>Problem:</b>", s["subsection"]))
    story.append(Paragraph(
        "The repository had no description, website URL, or topic tags — presenting "
        "a blank 'About' panel to anyone visiting the repo on GitHub.",
        s["body"],
    ))

    story.append(Paragraph("<b>Resolution:</b>", s["subsection"]))
    story.append(Paragraph(
        "The About section was populated using <font name='Courier'>gh repo edit</font> via the GitHub CLI:",
        s["body"],
    ))

    about_data = [
        ["Field", "Value"],
        ["Description", "Corporate website for BJP Technologies (T) Limited — IT solutions\ncompany in Tanzania. Built with Django 6, MySQL, and deployed on cPanel."],
        ["Website", "https://bjptechnologies.co.tz"],
        ["Topics", "django, python, mysql, cpanel, corporate-website, tanzania"],
    ]
    story.append(ruled_table(about_data, [35 * mm, CONTENT_W - 35 * mm]))

    # ── Section 2: Counter Bug ───────────────────────────────────────────────
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("2. Homepage Counter Bug Fix", s["section"]))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=CYAN, spaceAfter=3 * mm))

    story.append(Paragraph("<b>Problem:</b>", s["subsection"]))
    story.append(Paragraph(
        "The homepage stats section displayed four counters: <b>7</b> IT Service Lines, "
        "<b>6</b> Industries Served, <b>24/7</b> Monitoring &amp; Support, and "
        "<b>100%</b> Dedicated to Your Success. The first two animated correctly. "
        "The last two displayed as <b>0</b>.",
        s["body"],
    ))
    story.append(Paragraph(
        "Root cause: the <font name='Courier'>counter-up.js</font> plugin reads each "
        "<font name='Courier'>.counter</font> span's text content and parses it as a "
        "number. Values containing non-numeric characters (<font name='Courier'>24/7</font>, "
        "<font name='Courier'>100%</font>) produce <font name='Courier'>NaN</font>, "
        "which the plugin renders as <b>0</b>, overwriting the correct value.",
        s["body"],
    ))

    story.append(Paragraph("<b>Fix:</b>", s["subsection"]))
    story.append(Paragraph(
        "Modified <font name='Courier'>static/js/main.js</font> — the "
        "<font name='Courier'>counterUp</font> function now iterates each "
        "<font name='Courier'>.counter</font> span and applies the animation only "
        "when the value matches a purely numeric pattern "
        "(<font name='Courier'>/^[\\d,]+(\\.[\\d]+)?$/</font>). "
        "Non-numeric values are displayed as-is without animation.",
        s["body"],
    ))
    story.append(Paragraph(
        "<b>Branch merged:</b> <font name='Courier'>fix/homepage-counter-non-numeric</font>",
        s["body"],
    ))

    # ── Section 3: Automated Deploy ──────────────────────────────────────────
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("3. Automated cPanel Deployment", s["section"]))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=CYAN, spaceAfter=3 * mm))

    story.append(Paragraph("<b>Problem:</b>", s["subsection"]))
    story.append(Paragraph(
        "Every deployment required manual intervention: log into cPanel, navigate to "
        "Git Version Control, and click Pull. There was no automation triggered by "
        "merges to the main branch.",
        s["body"],
    ))

    story.append(Paragraph("<b>Goal:</b> Auto-deploy on every merge to main.", s["body"]))

    story.append(Paragraph("<b>Approaches Investigated and Ruled Out:</b>", s["subsection"]))
    ruled_out = [
        ["Approach", "Reason Failed"],
        ["SSH into cPanel (port 22)", "Port blocked by hosting provider"],
        ["cPanel UAPI — port 2083", "OpenResty proxy returns HTTP 415 for all external calls"],
        ["cPanel JSON API", "Same proxy, same HTTP 415 error"],
        ["SSH deploy key for private repo", "No terminal access to configure ~/.ssh/config"],
        ["PAT in Git Version Control URL", "cPanel UI explicitly rejects passwords in clone URLs"],
    ]
    story.append(ruled_table(ruled_out, [65 * mm, CONTENT_W - 65 * mm]))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("<b>Final Solution: GitHub Webhook + Django Endpoint</b>", s["subsection"]))
    story.append(Paragraph(
        "Since the cPanel API is blocked from external IPs but the live Django site "
        "is publicly reachable, a webhook-based approach was implemented:",
        s["body"],
    ))

    flow_data = [
        ["Step", "Action"],
        ["1", "Merge PR into main on GitHub"],
        ["2", "GitHub fires a POST webhook to https://bjptechnologies.co.tz/deploy/webhook/"],
        ["3", "Django validates the HMAC-SHA256 signature using GITHUB_WEBHOOK_SECRET"],
        ["4", "Django spawns scripts/deploy.sh as a fully detached background process"],
        ["5", "deploy.sh runs: git pull origin main"],
        ["6", "deploy.sh runs: pip install -r requirements.txt"],
        ["7", "deploy.sh runs: python manage.py migrate --no-input"],
        ["8", "deploy.sh runs: python manage.py collectstatic --no-input"],
        ["9", "deploy.sh touches tmp/restart.txt — Passenger restarts with new code"],
    ]
    story.append(ruled_table(flow_data, [15 * mm, CONTENT_W - 15 * mm]))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("<b>Files Created / Modified:</b>", s["subsection"]))
    files_data = [
        ["File", "Action", "Notes"],
        ["apps/core/webhook.py", "Created", "Django webhook view with HMAC-SHA256 validation"],
        ["scripts/deploy.sh", "Created", "Shell script: git pull, pip, migrate, collectstatic, restart"],
        ["config/urls.py", "Modified", "Registered /deploy/webhook/ route"],
        [".github/workflows/deploy.yml", "Modified", "Removed broken deploy job — tests only now"],
        [".cpanel.yml", "Created", "cPanel post-deploy config (fallback for manual pulls)"],
        [".env.example", "Modified", "Added GITHUB_WEBHOOK_SECRET variable"],
    ]
    story.append(ruled_table(
        files_data,
        [55 * mm, 28 * mm, CONTENT_W - 55 * mm - 28 * mm],
    ))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("<b>Server-Side Setup (Manual, One-Time):</b>", s["subsection"]))
    for item in [
        "Generated a cryptographically random GITHUB_WEBHOOK_SECRET token",
        "Added GITHUB_WEBHOOK_SECRET to the server .env file via cPanel File Manager",
        "Configured GitHub webhook: payload URL, secret, push events only, SSL verification on",
        "Performed one manual git pull via cPanel Git Version Control to bootstrap the endpoint",
    ]:
        story.append(Paragraph(f"&#8226; &nbsp; {item}", s["bullet"]))

    story.append(Spacer(1, 3 * mm))
    story.append(Paragraph("<b>Result:</b>", s["subsection"]))
    story.append(Paragraph(
        "Webhook delivery confirmed returning HTTP 200. Deploy script confirmed running "
        "on the server — log output visible at "
        "<font name='Courier'>/tmp/bjp_deploy.log</font>. "
        "Automated deployment is fully operational.",
        s["body"],
    ))

    # ── Section 4: Current State ─────────────────────────────────────────────
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("4. Current Project State", s["section"]))
    story.append(HRFlowable(width=CONTENT_W, thickness=1, color=CYAN, spaceAfter=3 * mm))

    status_data = [
        ["Area", "Status", "Notes"],
        ["Phase 6 — Polish & Launch", "In Progress", "Ongoing"],
        ["Automated deployment", "Complete", "GitHub webhook fully operational"],
        ["Page load speed", "Pending", "Target: under 3 seconds"],
        ["Image optimisation", "Pending", "All images to be compressed"],
        ["Final security audit", "Pending", "No secrets, no DEBUG, no SQL exposure"],
        ["Go-live sign-off", "Pending", "Awaiting all Phase 6 items"],
        ["Private repository", "Blocked", "Host blocks SSH + PAT auth — needs provider help or VPS"],
    ]
    story.append(ruled_table(
        status_data,
        [60 * mm, 32 * mm, CONTENT_W - 60 * mm - 32 * mm],
    ))

    story.append(Spacer(1, 6 * mm))
    story.append(HRFlowable(width=CONTENT_W, thickness=0.5, color=GREY, spaceAfter=3 * mm))
    story.append(Paragraph(
        "<i>Report prepared by Claude Code (Sonnet 4.6) — BJP Technologies (T) Limited "
        "— bjptechnologies.co.tz</i>",
        ParagraphStyle("footer_note", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY),
    ))

    return story


def main():
    doc = BaseDocTemplate(OUTPUT, pagesize=A4)

    cover_frame = Frame(
        0, 0, PAGE_W, PAGE_H,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
        id="cover",
    )
    content_frame = Frame(18 * mm, 20 * mm, CONTENT_W, PAGE_H - 45 * mm, id="content")

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page),
        PageTemplate(id="content", frames=[content_frame], onPage=header_footer),
    ])

    styles = build_styles()
    story = [NextPageTemplate('content'), PageBreak()]
    story += build_story(styles)

    doc.build(story)
    print(f"PDF saved: {OUTPUT}")


if __name__ == "__main__":
    main()
