"""Generate BJP Technologies — Logo & Branding Admin Feature Report PDF."""

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

OUTPUT = "docs/BJP_Technologies_Logo_Branding_Report.pdf"

NAVY = colors.HexColor("#0D1B4B")
BLUE = colors.HexColor("#1565C0")
CYAN = colors.HexColor("#00C6FF")
GREY = colors.HexColor("#8A94B0")
OFF_WHITE = colors.HexColor("#F4F6FC")
WHITE = colors.white
BLACK = colors.black
LIGHT_GREY = colors.HexColor("#E8ECF4")
GREEN = colors.HexColor("#2ECC71")
AMBER = colors.HexColor("#F39C12")

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
        PAGE_W - 18 * mm, PAGE_H - 12 * mm, "LOGO & BRANDING ADMIN FEATURE"
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
    canvas.setFont("Helvetica-Bold", 11)
    canvas.drawString(30 * mm, PAGE_H - 14 * mm, "BJP TECHNOLOGIES (T) LIMITED")

    # Title block
    title_y = PAGE_H - 72 * mm
    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawString(30 * mm, title_y, "Logo & Branding")
    canvas.setFont("Helvetica-Bold", 26)
    canvas.drawString(30 * mm, title_y - 12 * mm, "Admin Feature")
    canvas.setFillColor(CYAN)
    canvas.rect(30 * mm, title_y - 15 * mm, 60 * mm, 2, fill=1, stroke=0)
    canvas.setFillColor(GREY)
    canvas.setFont("Helvetica", 11)
    canvas.drawString(30 * mm, title_y - 22 * mm, "Feature Implementation Report")
    canvas.setFont("Helvetica", 10)
    canvas.drawString(30 * mm, title_y - 29 * mm, "May 2026  |  Branch: feature/logo-branding-admin")

    # Stats cards
    stats = [
        ("2", "New Fields\nAdded"),
        ("1", "Proxy Model\nCreated"),
        ("3", "Templates\nUpdated"),
        ("1", "Migration\nApplied"),
    ]
    card_x = 30 * mm
    card_y = PAGE_H - 148 * mm
    card_w = 36 * mm
    card_h = 24 * mm
    gap = 4 * mm

    for value, label in stats:
        canvas.setFillColor(OFF_WHITE)
        canvas.roundRect(card_x, card_y, card_w, card_h, 3, fill=1, stroke=0)
        canvas.setFillColor(CYAN)
        canvas.rect(card_x, card_y + card_h - 3, card_w, 3, fill=1, stroke=0)
        canvas.setFillColor(NAVY)
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(card_x + card_w / 2, card_y + 12, value)
        canvas.setFillColor(GREY)
        canvas.setFont("Helvetica", 7)
        lines = label.split("\n")
        for i, line in enumerate(lines):
            canvas.drawCentredString(card_x + card_w / 2, card_y + 6 - i * 8, line)
        card_x += card_w + gap

    # Tagline strip
    strip_y = 28 * mm
    canvas.setFillColor(NAVY)
    canvas.rect(0, strip_y, PAGE_W, 18 * mm, fill=1, stroke=0)
    canvas.setFillColor(CYAN)
    canvas.rect(0, strip_y + 18 * mm, PAGE_W, 1.5, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 10)
    canvas.drawCentredString(
        PAGE_W / 2, strip_y + 10 * mm, "Admin-editable logo and favicon — zero code, zero deploy."
    )
    canvas.setFont("Helvetica", 9)
    canvas.drawCentredString(
        PAGE_W / 2,
        strip_y + 4 * mm,
        "Client uploads once. Site updates everywhere. Static fallback always in place.",
    )

    canvas.restoreState()


def build_styles():
    return {
        "h1": ParagraphStyle(
            "h1", fontName="Helvetica-Bold", fontSize=15, textColor=NAVY,
            spaceAfter=4, spaceBefore=14,
        ),
        "h2": ParagraphStyle(
            "h2", fontName="Helvetica-Bold", fontSize=11, textColor=BLUE,
            spaceAfter=3, spaceBefore=10,
        ),
        "body": ParagraphStyle(
            "body", fontName="Helvetica", fontSize=9.5, textColor=BLACK,
            leading=14, spaceAfter=6,
        ),
        "mono": ParagraphStyle(
            "mono", fontName="Courier", fontSize=8.5, textColor=NAVY,
            leading=13, spaceAfter=4, leftIndent=6,
        ),
        "caption": ParagraphStyle(
            "caption", fontName="Helvetica-Oblique", fontSize=8, textColor=GREY,
            spaceAfter=4,
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName="Helvetica", fontSize=9.5, textColor=BLACK,
            leading=14, spaceAfter=3, leftIndent=12, firstLineIndent=-8,
        ),
    }


def hr(color=LIGHT_GREY, thickness=0.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=6, spaceBefore=6)


def section_title(text, s):
    return [Paragraph(text, s["h1"]), hr(CYAN, 1.5)]


def table(data, col_widths, header=True):
    style = [
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, OFF_WHITE]),
        ("GRID", (0, 0), (-1, -1), 0.3, LIGHT_GREY),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTCOLOR", (0, 0), (-1, 0), WHITE),
        ]
    return Table(data, colWidths=col_widths, style=TableStyle(style), hAlign="LEFT")


def build_pdf():
    doc = BaseDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=24 * mm,
        bottomMargin=20 * mm,
    )

    cover_frame = Frame(0, 0, PAGE_W, PAGE_H, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0)
    content_frame = Frame(
        18 * mm, 18 * mm, CONTENT_W, PAGE_H - 42 * mm,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
    )

    doc.addPageTemplates([
        PageTemplate(id="cover", frames=[cover_frame], onPage=cover_page),
        PageTemplate(id="content", frames=[content_frame], onPage=header_footer),
    ])

    s = build_styles()
    story = [Spacer(1, PAGE_H)]  # cover page filler

    # --- 1. Overview ---
    story += section_title("1. Overview", s)
    story.append(Paragraph(
        "This report documents the implementation of admin-editable logo and favicon "
        "management for the BJP Technologies website. Prior to this feature, the company "
        "logo and favicon were hardcoded as static files — replacing them required a "
        "developer, a code change, and a deployment. This feature moves that control "
        "entirely into the Django admin panel.",
        s["body"],
    ))
    story.append(Paragraph(
        "The client can now upload a new logo or favicon at any time from "
        "<b>Admin → Site Settings → Logo &amp; Branding</b> with no developer involvement. "
        "The site continues to display the existing static logo until a new one is uploaded, "
        "so there is zero risk of a broken header during the transition.",
        s["body"],
    ))
    story.append(Spacer(1, 4))

    # --- 2. Design Decisions ---
    story += section_title("2. Design Decisions", s)

    story.append(Paragraph("<b>Single logo field, not two</b>", s["h2"]))
    story.append(Paragraph(
        "An earlier consideration was to add two logo fields — one for dark backgrounds "
        "(navbar, footer) and one for light backgrounds. This was rejected because it places "
        "the burden on the client to upload and maintain two matching files every rebrand. "
        "A missed upload results in a mismatched header and footer.",
        s["body"],
    ))
    story.append(Paragraph(
        "Instead, a single <code>logo</code> field is used. The CSS filter "
        "<code>filter: brightness(0) invert(1)</code> applied to the <code>&lt;img&gt;</code> "
        "element in the navbar and footer converts any uploaded logo to white automatically. "
        "The client uploads once; the correct colour variant is rendered in all placements "
        "via CSS.",
        s["body"],
    ))

    story.append(Paragraph("<b>FileField, not ImageField</b>", s["h2"]))
    story.append(Paragraph(
        "Django's <code>ImageField</code> uses Pillow for validation. Pillow cannot decode "
        "SVG files, so uploading an SVG would be rejected even though SVG is the preferred "
        "logo format. A <code>FileField</code> with a custom validator is used instead, "
        "explicitly accepting SVG, PNG, and WebP while rejecting JPEG (no transparency "
        "support), GIF, BMP, and other non-web formats.",
        s["body"],
    ))

    story.append(Paragraph("<b>Static file fallback</b>", s["h2"]))
    story.append(Paragraph(
        "All three templates (navbar, footer, base.html) check <code>{% if company.logo %}</code> "
        "before rendering the uploaded file. If no logo has been uploaded, the existing static "
        "file is used. This ensures the live site is visually identical to before the feature "
        "was deployed — until the client chooses to upload.",
        s["body"],
    ))
    story.append(Spacer(1, 4))

    # --- 3. Files Changed ---
    story += section_title("3. Files Changed", s)
    files_data = [
        ["File", "Action", "Purpose"],
        ["apps/core/validators.py", "Created", "validate_logo_file, validate_favicon_file"],
        ["apps/core/models.py", "Modified", "logo + favicon FileFields; LogoBrandingSettings proxy"],
        ["apps/core/admin.py", "Modified", "LogoBrandingSettingsAdmin with live previews"],
        ["apps/core/migrations/0006_…", "Created", "DB columns for logo and favicon"],
        ["config/settings/base.py", "Modified", "Logo & Branding link in Unfold sidebar"],
        ["config/urls.py", "Modified", "Media serving in development (DEBUG only)"],
        ["apps/core/templates/core/navbar.html", "Modified", "Dynamic logo with static fallback"],
        ["apps/core/templates/core/footer.html", "Modified", "Dynamic logo with static fallback"],
        ["apps/core/templates/core/base.html", "Modified", "Dynamic favicon with static fallback"],
    ]
    story.append(table(
        files_data,
        [62 * mm, 26 * mm, 86 * mm],
    ))
    story.append(Spacer(1, 6))

    # --- 4. Accepted File Formats ---
    story += section_title("4. Accepted File Formats", s)
    fmt_data = [
        ["Field", "Accepted Formats", "Rejected Formats", "Reason for Restriction"],
        ["Logo", "SVG, PNG, WebP", "JPEG, GIF, BMP, TIFF",
         "JPEG has no transparency — logo background bleeds on dark navbar"],
        ["Favicon", "PNG, ICO", "SVG, JPEG, GIF",
         "Browsers expect raster favicons; PNG/ICO are universally supported"],
    ]
    story.append(table(
        fmt_data,
        [28 * mm, 34 * mm, 38 * mm, 74 * mm],
    ))
    story.append(Paragraph(
        "Validation is enforced server-side in <code>apps/core/validators.py</code>. "
        "Uploading a rejected format displays a clear error message in the admin panel "
        "before saving.",
        s["caption"],
    ))
    story.append(Spacer(1, 6))

    # --- 5. How It Works ---
    story += section_title("5. How It Works", s)

    story.append(Paragraph("<b>Logo placement — navbar and footer</b>", s["h2"]))
    story.append(Paragraph(
        "Both the navbar and footer now contain a conditional block:",
        s["body"],
    ))
    story.append(Paragraph(
        "{% if company.logo %}\n"
        "    &lt;img src=\"{{ company.logo.url }}\" style=\"filter: brightness(0) invert(1);\"&gt;\n"
        "{% else %}\n"
        "    &lt;img src=\"{% static 'images/logo/bjp-logo-horizontal-light.png' %}\"&gt;\n"
        "{% endif %}",
        s["mono"],
    ))
    story.append(Paragraph(
        "The CSS filter converts the uploaded logo to pure white, matching the existing "
        "static white logo on the dark navy header and footer backgrounds.",
        s["body"],
    ))

    story.append(Paragraph("<b>Favicon — base.html</b>", s["h2"]))
    story.append(Paragraph(
        "The <code>&lt;head&gt;</code> block checks for an uploaded favicon. If present, "
        "a single <code>&lt;link rel=\"icon\"&gt;</code> tag points to the uploaded file. "
        "If absent, all three original static favicon sizes (32px, 64px, 256px apple-touch) "
        "remain in use.",
        s["body"],
    ))

    story.append(Paragraph("<b>Admin preview</b>", s["h2"]))
    story.append(Paragraph(
        "The Logo &amp; Branding admin section renders a live preview immediately below the "
        "upload widget on the same row. The logo preview uses a navy (#0D1B4B) background "
        "so the client sees exactly how the logo will appear on the site — not on a white "
        "admin background that would be misleading for a white or light-coloured logo.",
        s["body"],
    ))
    story.append(Spacer(1, 4))

    # --- 6. Migration ---
    story += section_title("6. Migration", s)
    story.append(Paragraph(
        "Migration <code>0006_add_logo_branding_fields</code> adds two nullable columns "
        "to the existing <code>core_sitesettings</code> table:",
        s["body"],
    ))
    mig_data = [
        ["Column", "Type", "Default", "Nullable"],
        ["logo", "VARCHAR(100)", "— (empty string)", "Yes (blank=True)"],
        ["favicon", "VARCHAR(100)", "— (empty string)", "Yes (blank=True)"],
    ]
    story.append(table(mig_data, [40 * mm, 40 * mm, 50 * mm, 44 * mm]))
    story.append(Paragraph(
        "Both columns are non-destructive additions. No existing data is modified. "
        "The migration is safe to run on the live production database.",
        s["body"],
    ))
    story.append(Spacer(1, 4))

    # --- 7. cPanel Deployment Steps ---
    story += section_title("7. cPanel Deployment Steps", s)
    story.append(Paragraph(
        "After merging <code>feature/logo-branding-admin → develop → main</code> and the "
        "CI/CD pipeline completes, run the following on the cPanel server:",
        s["body"],
    ))
    steps = [
        ("1", "cd ~/bjp-technologies-web", "Navigate to project root"),
        ("2", "git pull origin main", "Pull the latest merged code"),
        ("3", "source ~/virtualenv/bjp-technologies-web/3.11/bin/activate", "Activate virtualenv"),
        ("4", "python manage.py migrate", "Apply migration 0006 — adds logo + favicon columns"),
        ("5", "touch tmp/restart.txt", "Restart Passenger — picks up the new code"),
    ]
    steps_data = [["Step", "Command", "Purpose"]] + [list(r) for r in steps]
    story.append(table(steps_data, [14 * mm, 84 * mm, 76 * mm]))
    story.append(Paragraph(
        "After the restart, navigate to Admin → Site Settings → Logo &amp; Branding to upload "
        "the company logo and favicon. No collectstatic is required — uploaded files are served "
        "from MEDIA_ROOT, not the static file pipeline.",
        s["body"],
    ))
    story.append(Spacer(1, 4))

    # --- 8. Summary ---
    story += section_title("8. Summary", s)
    summary_data = [
        ["Item", "Detail"],
        ["Feature", "Admin-editable logo and favicon"],
        ["Branch", "feature/logo-branding-admin"],
        ["Migration", "0006_add_logo_branding_fields"],
        ["New files", "apps/core/validators.py, migration file"],
        ["Modified files", "models.py, admin.py, base.py, urls.py, 3 templates"],
        ["Tests", "67 / 67 passing — no regressions"],
        ["Linting", "ruff ✓  black ✓"],
        ["Visual change on deploy", "None — static fallback until client uploads"],
        ["Client action required", "Upload logo via Admin → Site Settings → Logo & Branding"],
    ]
    story.append(table(summary_data, [60 * mm, 114 * mm]))

    doc.build(story)
    print(f"Generated: {OUTPUT}")


if __name__ == "__main__":
    build_pdf()
