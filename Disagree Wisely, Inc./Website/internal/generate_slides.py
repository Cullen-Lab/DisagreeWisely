#!/usr/bin/env python3
"""Generate board meeting slides PDF using reportlab."""

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT

W, H = landscape(letter)
OUT = "/Users/dibella/Desktop/Sway/Disagree Wisely, Inc./Website/Board Meeting - March 6 2026.pdf"

# Colors
NAVY = HexColor("#1a3a5c")
BLUE = HexColor("#2d5a8a")
GRAY = HexColor("#666666")
LIGHT_GRAY = HexColor("#999999")
BG_BLUE = HexColor("#f0f5ff")
BG_RED = HexColor("#fff5f5")
BG_GREEN = HexColor("#f0fff4")
BG_TABLE = HexColor("#f5f7fa")
WHITE = HexColor("#ffffff")
RED = HexColor("#c53030")
GREEN_D = HexColor("#276749")

# Styles
styles = getSampleStyleSheet()

S_TITLE = ParagraphStyle("SlideTitle", fontName="Helvetica-Bold", fontSize=26, textColor=NAVY, leading=30, spaceAfter=4)
S_SUBTITLE = ParagraphStyle("SlideSub", fontName="Helvetica", fontSize=13, textColor=GRAY, spaceAfter=8)
S_H2 = ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=17, textColor=NAVY, spaceBefore=14, spaceAfter=6)
S_H3 = ParagraphStyle("H3", fontName="Helvetica-Bold", fontSize=14, textColor=BLUE, spaceBefore=10, spaceAfter=4)
S_BODY = ParagraphStyle("Body", fontName="Helvetica", fontSize=12, textColor=HexColor("#1a1a1a"), leading=16, spaceAfter=3)
S_BULLET = ParagraphStyle("Bullet", fontName="Helvetica", fontSize=12, textColor=HexColor("#1a1a1a"), leading=16, spaceAfter=3, leftIndent=20, bulletIndent=6, bulletFontSize=12)
S_SUB_BULLET = ParagraphStyle("SubBullet", fontName="Helvetica", fontSize=11, textColor=HexColor("#444444"), leading=15, spaceAfter=2, leftIndent=40, bulletIndent=26, bulletFontSize=11)
S_NOTE = ParagraphStyle("Note", fontName="Helvetica", fontSize=11, textColor=HexColor("#333333"), leading=15, spaceAfter=4)
S_CENTER = ParagraphStyle("Center", fontName="Helvetica-Bold", fontSize=36, textColor=NAVY, alignment=TA_CENTER, leading=42)
S_CENTER_SUB = ParagraphStyle("CenterSub", fontName="Helvetica", fontSize=16, textColor=GRAY, alignment=TA_CENTER, spaceAfter=6)
S_CENTER_SM = ParagraphStyle("CenterSm", fontName="Helvetica", fontSize=12, textColor=LIGHT_GRAY, alignment=TA_CENTER)
S_FOOTER = ParagraphStyle("Footer", fontName="Helvetica", fontSize=9, textColor=LIGHT_GRAY)
S_BIG_NUM = ParagraphStyle("BigNum", fontName="Helvetica-Bold", fontSize=32, textColor=NAVY, alignment=TA_CENTER, leading=36)
S_BIG_LABEL = ParagraphStyle("BigLabel", fontName="Helvetica", fontSize=11, textColor=GRAY, alignment=TA_CENTER, spaceAfter=4)
S_TABLE_HEAD = ParagraphStyle("THead", fontName="Helvetica-Bold", fontSize=10, textColor=NAVY)
S_TABLE_CELL = ParagraphStyle("TCell", fontName="Helvetica", fontSize=11, textColor=HexColor("#1a1a1a"), leading=14)
S_TABLE_TAG = ParagraphStyle("TTag", fontName="Helvetica-Bold", fontSize=10, textColor=BLUE)

def b(text):
    return f"<b>{text}</b>"

def bullet(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", S_BULLET)

def sub_bullet(text):
    return Paragraph(f"<bullet>&ndash;</bullet> {text}", S_SUB_BULLET)

def note_box(text, bg=BG_BLUE):
    t = Table([[Paragraph(text, S_NOTE)]], colWidths=[W - 2*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("LEFTPADDING", (0,0), (-1,-1), 12),
        ("RIGHTPADDING", (0,0), (-1,-1), 12),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

def page_header(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(LIGHT_GRAY)
    canvas.drawString(0.7*inch, 0.45*inch, "Disagree Wisely, Inc. \u2014 Confidential")
    canvas.drawRightString(W - 0.7*inch, 0.45*inch, str(doc.page))
    canvas.restoreState()

story = []

# ── SLIDE 1: Title ──────────────────────────────
story.append(Spacer(1, 2.2*inch))
story.append(Paragraph("DISAGREE WISELY, INC.", ParagraphStyle("eyebrow", fontName="Helvetica", fontSize=14, textColor=GRAY, alignment=TA_CENTER, spaceAfter=20, tracking=200)))
story.append(Paragraph("First Full Board Meeting", S_CENTER))
story.append(Spacer(1, 12))
story.append(Paragraph("March 6, 2026 \u00b7 Zoom", S_CENTER_SUB))
story.append(Spacer(1, 6))
story.append(Paragraph("Also serving as the 2026 Annual Meeting (Bylaws \u00a74.1)", S_CENTER_SM))
story.append(Spacer(1, 40))
story.append(Paragraph("Simon Cullen \u00b7 Nicholas DiBella \u00b7 Neil Thomason \u00b7 Ken Stern \u00b7 Barbara Oakley", S_CENTER_SM))
story.append(PageBreak())

# ── SLIDE 2: Agenda ─────────────────────────────
story.append(Paragraph("Agenda", S_TITLE))
story.append(Paragraph("60 minutes (extendable to 90\u2013120 min)", S_SUBTITLE))
story.append(Spacer(1, 8))

agenda_data = [
    [Paragraph("Time", S_TABLE_HEAD), Paragraph("Topic", S_TABLE_HEAD), Paragraph("Lead", S_TABLE_HEAD)],
    ["5 min", "Welcome & Introductions", "Simon"],
    ["10 min", "Annual Governance: Officer Elections, COI Attestation", "Simon"],
    ["15 min", "501(c)(3) & Restructuring Update", "Simon"],
    ["5 min", "Sway IP & CMU Dispute", "Simon"],
    ["10 min", "Financial Report", "Nick"],
    ["5 min", "Growth & Impact", "Simon"],
    ["5 min", "Q&A & Open Discussion", "All"],
    ["5 min", "Next Steps & Adjournment", "Simon"],
]
for i in range(1, len(agenda_data)):
    row = agenda_data[i]
    agenda_data[i] = [
        Paragraph(row[0], ParagraphStyle("tc", fontName="Helvetica", fontSize=11, textColor=GRAY)),
        Paragraph(row[1], S_TABLE_CELL),
        Paragraph(row[2], S_TABLE_TAG),
    ]

t = Table(agenda_data, colWidths=[0.8*inch, 6.5*inch, 0.9*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BG_TABLE),
    ("BOTTOMPADDING", (0,0), (-1,0), 6),
    ("TOPPADDING", (0,0), (-1,0), 6),
    ("LINEBELOW", (0,0), (-1,0), 1.5, NAVY),
    ("LINEBELOW", (0,1), (-1,-1), 0.5, HexColor("#eeeeee")),
    ("TOPPADDING", (0,1), (-1,-1), 5),
    ("BOTTOMPADDING", (0,1), (-1,-1), 5),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
]))
story.append(t)
story.append(Spacer(1, 16))
story.append(note_box("<b>If time extends:</b> The Q&A block expands naturally. Extended topics: strategic priorities, PBC structure, CMU IP details, fundraising strategy, leveraging Ken and Barbara's networks."))
story.append(PageBreak())

# ── SLIDE 3: Governance ─────────────────────────
story.append(Paragraph("Annual Governance Items", S_TITLE))
story.append(Paragraph("Simon \u2014 10 min", S_SUBTITLE))
story.append(Spacer(1, 4))
story.append(Paragraph("Officer Elections (Bylaws \u00a75.1)", S_H2))
story.append(bullet("Propose re-electing current officers and director:"))
story.append(sub_bullet("<b>Simon Cullen</b> \u2014 President & CEO"))
story.append(sub_bullet("<b>Nicholas DiBella</b> \u2014 Secretary, Treasurer & CTOO"))
story.append(sub_bullet("<b>Neil Thomason</b> \u2014 Director"))
story.append(bullet("Vote individually; each person <b>abstains</b> from own vote (remaining 4 vote)"))
story.append(bullet("Simple majority of those voting required"))
story.append(Spacer(1, 4))
story.append(Paragraph("Conflict of Interest Attestation", S_H2))
story.append(bullet("COI policy will be sent after the meeting; each director replies by email with attestation"))
story.append(bullet("<b>Simon & Nick disclose:</b> compensated officers (through HxA, not DW funds) and co-owners of the Sway IP"))
story.append(bullet("Board expanded to 5 with <b>disinterested majority</b> (Thomason, Stern, Oakley) for this reason"))
story.append(Spacer(1, 4))
story.append(Paragraph("Bylaws Receipt", S_H2))
story.append(bullet("Bylaws will be sent after the meeting; Ken and Barbara reply by email confirming receipt and agreement"))
story.append(bullet("Email confirmations preserved as the record"))
story.append(PageBreak())

# ── SLIDE 4: Restructuring ──────────────────────
story.append(Paragraph("501(c)(3) & Restructuring", S_TITLE))
story.append(Paragraph("Simon \u2014 15 min (part 1 of 2)", S_SUBTITLE))
story.append(Spacer(1, 4))
story.append(Paragraph("Why We Are Restructuring", S_H2))
story.append(bullet("DW originally intended to house research, education, <i>and</i> Sway development"))
story.append(bullet("Foundation Group recommended a <b>clean separation</b>: DW = research & education; Sway IP \u2192 separate for-profit PBC"))
story.append(bullet("Common nonprofit/for-profit structure. Keeps DW's tax-exempt status clean."))
story.append(bullet("DW accesses Sway for its programs under a free license from the co-founders"))
story.append(Spacer(1, 4))
story.append(Paragraph("Application Status", S_H2))
story.append(bullet("Foundation Group (Ren Henderson) finalizing IRS Form 1023"))
story.append(bullet("Target submission: <b>mid-April 2026</b>"))
story.append(bullet("Requesting <b>expedited IRS review</b> \u2014 FIPSE grant (~$800K) cannot be disbursed without approval"))
story.append(bullet("Supporting letter from grantor (Notre Dame) requested"))
story.append(Spacer(1, 4))
story.append(Paragraph("For-Profit PBC", S_H2))
story.append(bullet("Planned but not yet incorporated"))
story.append(bullet("Will hold Sway IP, handle product development, license platform to DW at no cost"))
story.append(PageBreak())

# ── SLIDE 5: Compliance Transition ──────────────
story.append(Paragraph("The Compliance Transition", S_TITLE))
story.append(Paragraph("Simon \u2014 15 min (part 2 of 2)", S_SUBTITLE))
story.append(Spacer(1, 4))
story.append(note_box("<b>Key issue:</b> The operational separation is not yet complete. Some development costs continue to flow through DW via the HxA/AVDF services agreement during the transition.", BG_RED))
story.append(Spacer(1, 6))
story.append(Paragraph("HxA/AVDF Agreement", S_H2))
story.append(bullet("Phase 2 (Jan\u2013Nov 2026) commits DW to \u201cexecute technical development\u201d \u2014 predates restructuring"))
story.append(bullet("Simon proposed amending. HxA ED Michael Regnier (March 5): <b>not feasible</b> with 3 months left"))
story.append(bullet("Practical outcome: DW continues invoicing for some dev costs likely through May/June 2026 (when AVDF dev budget is used up). <b>DW fully reimbursed</b> \u2014 net cost to DW is zero."))
story.append(Spacer(1, 4))
story.append(Paragraph("Learning Agency / Tools Competition (~$125K)", S_H2))
story.append(bullet("$150K prize. $25K spent (Instructor Insights \u2014 complete). ~$125K remains."))
story.append(bullet("Funds can no longer be spent on IP/development through DW"))
story.append(bullet("Original plan: return ~$125K to LA for redirection to PBC"))
story.append(bullet("<b>Update:</b> Kristyn confirmed funds are <b>restricted to nonprofits</b> \u2014 cannot redirect to for-profit"))
story.append(bullet("<b>Proposed:</b> Use ~$125K for DW salaries <i>not related to IP generation</i> (research, education, ops)"))
story.append(bullet("<b>Board discussion needed</b>"))
story.append(Spacer(1, 6))
story.append(note_box("<b>Mitigating factors:</b> Restructuring is genuine and proactive. DW voluntarily stopped spending LA development funds before being told to. Budget projections show clean separation going forward.", BG_GREEN))
story.append(PageBreak())

# ── SLIDE 6: CMU IP ─────────────────────────────
story.append(Paragraph("Sway IP & CMU Dispute", S_TITLE))
story.append(Paragraph("Simon \u2014 5 min", S_SUBTITLE))
story.append(Spacer(1, 4))
story.append(note_box("This is Simon and Nick\u2019s <b>personal matter</b> (DW does not own Sway IP), but the board should be aware because DW\u2019s programs depend on Sway."))
story.append(Spacer(1, 6))
story.append(Paragraph("Background", S_H2))
story.append(bullet("CMU asserts a <b>joint ownership interest</b> based on claimed contributions by CMU staff/interns (2023\u20132024)"))
story.append(bullet("Simon and Nick assert sole ownership under CMU IP Policy \u00a73-6-1: educational courseware belongs to the creator \u201cin all cases\u201d"))
story.append(bullet("CMU-affiliated code in current codebase: <b>0.77%</b> (454 lines of commodity boilerplate)"))
story.append(Spacer(1, 4))
story.append(Paragraph("Current Status", S_H2))
story.append(bullet("Legal counsel (David Kalson, Dentons) represented through early 2026; assessed position as strong"))
story.append(bullet("After CMU General Counsel declined to waive ownership, Simon & Nick ended Dentons engagement (Feb 2026)"))
story.append(bullet("We are <b>evaluating our options</b>. CMU notified to expect direct contact or new representation."))
story.append(bullet("Board input welcome, though technically outside DW\u2019s purview"))
story.append(Spacer(1, 4))
story.append(Paragraph("Risk to DW", S_H2))
story.append(bullet("<b>Low in the near term.</b> Sway operates at 80+ institutions. CMU has taken no action to restrict use."))
story.append(bullet("If dispute escalated, could create uncertainty around IP underpinning DW\u2019s programs \u2014 but considered unlikely"))
story.append(PageBreak())

# ── SLIDE 7: Financials ─────────────────────────
story.append(Paragraph("Financial Report", S_TITLE))
story.append(Paragraph("Nick \u2014 10 min", S_SUBTITLE))
story.append(Spacer(1, 8))

# Stats boxes
stats_data = [
    [Paragraph("<b>~$173K</b>", ParagraphStyle("bn", fontName="Helvetica-Bold", fontSize=28, textColor=NAVY, alignment=TA_CENTER)),
     Paragraph("<b>~$125K</b>", ParagraphStyle("bn2", fontName="Helvetica-Bold", fontSize=28, textColor=NAVY, alignment=TA_CENTER))],
    [Paragraph("Cash on Hand", S_BIG_LABEL),
     Paragraph("Tools Competition (retain for non-IP salaries)", S_BIG_LABEL)],
]
st = Table(stats_data, colWidths=[3.5*inch, 3.5*inch])
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BG_TABLE),
    ("TOPPADDING", (0,0), (-1,0), 12),
    ("BOTTOMPADDING", (0,1), (-1,1), 10),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ("ROUNDEDCORNERS", [6,6,6,6]),
]))
story.append(st)
story.append(Spacer(1, 12))

# Two columns via table
left_content = [
    Paragraph("Active Revenue", S_H3),
    Paragraph("\u2022 HxA/AVDF: ~$284K (two phases)", S_BODY),
    Paragraph("\u2022 Craig Snider: $50K", S_BODY),
    Paragraph("\u2022 Lindy Snider: $25K", S_BODY),
    Paragraph("\u2022 Sway Classroom: $13,171", S_BODY),
    Paragraph("\u2022 Ben Delo: $20K", S_BODY),
    Spacer(1, 6),
    Paragraph("Secured (awaiting 501(c)(3))", S_H3),
    Paragraph("\u2022 <b>FIPSE: ~$800K</b> \u2014 critical near-term", S_BODY),
]

right_content = [
    Paragraph("Pending Applications", S_H3),
    Paragraph("\u2022 ECI: ~$233K (Wake Forest/NC State)", S_BODY),
    Paragraph("\u2022 NewSchools Venture Fund", S_BODY),
    Paragraph("\u2022 TWCF: $5M+ (if invited to full app)", S_BODY),
    Spacer(1, 6),
    Paragraph("Compensation", S_H3),
    Paragraph("\u2022 <b>No one paid from DW funds</b>", S_BODY),
    Paragraph("\u2022 All compensation via HxA reimbursement", S_BODY),
    Paragraph("\u2022 Board members: uncompensated", S_BODY),
]

cols = Table(
    [[left_content, right_content]],
    colWidths=[4*inch, 4*inch],
)
cols.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (0,0), 0),
    ("LEFTPADDING", (1,0), (1,0), 20),
]))
story.append(cols)
story.append(Spacer(1, 10))
story.append(note_box("<b>Banking:</b> BlueVine (Coastal Community Bank, FDIC). Access: Cullen & DiBella. Payroll: Gusto. Payments: Bill.com. Fiscal year: Jan 1 \u2013 Dec 31."))
story.append(PageBreak())

# ── SLIDE 8: Growth ─────────────────────────────
story.append(Paragraph("Growth & Impact", S_TITLE))
story.append(Paragraph("Simon \u2014 5 min", S_SUBTITLE))
story.append(Spacer(1, 8))

# Stats
gstats = [
    [Paragraph("<b>80+</b>", ParagraphStyle("g1", fontName="Helvetica-Bold", fontSize=32, textColor=NAVY, alignment=TA_CENTER)),
     Paragraph("<b>~10,000</b>", ParagraphStyle("g2", fontName="Helvetica-Bold", fontSize=32, textColor=NAVY, alignment=TA_CENTER)),
     Paragraph("<b>3\u20134x</b>", ParagraphStyle("g3", fontName="Helvetica-Bold", fontSize=32, textColor=NAVY, alignment=TA_CENTER))],
    [Paragraph("Institutions", S_BIG_LABEL),
     Paragraph("Students", S_BIG_LABEL),
     Paragraph("Growth (2025)", S_BIG_LABEL)],
]
gt = Table(gstats, colWidths=[2.6*inch, 2.6*inch, 2.6*inch])
gt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BG_TABLE),
    ("TOPPADDING", (0,0), (-1,0), 12),
    ("BOTTOMPADDING", (0,1), (-1,1), 10),
    ("ALIGN", (0,0), (-1,-1), "CENTER"),
]))
story.append(gt)
story.append(Spacer(1, 14))

left_g = [
    Paragraph("Highlights", S_H3),
    Paragraph("\u2022 <b>Chronicle of Higher Education</b> dedicated feature", S_BODY),
    Paragraph("\u2022 Adopted at R1s, liberal arts colleges, community colleges, HBCUs, HSIs", S_BODY),
    Paragraph("\u2022 Instructor Insights dashboard complete", S_BODY),
    Paragraph("\u2022 Rachel Sipser hired (Dir. of Communications)", S_BODY),
]

right_g = [
    Paragraph("Research & Expansion", S_H3),
    Paragraph("\u2022 Active research: bias studies, impact assessments", S_BODY),
    Paragraph("\u2022 Growing faculty research partnerships", S_BODY),
    Paragraph("\u2022 Sway Classroom (K\u201312) \u2014 Dr. Strambler (Yale)", S_BODY),
    Paragraph("\u2022 $4M DOE/FIPSE consortium (125 campuses)", S_BODY),
]

gcols = Table([[left_g, right_g]], colWidths=[4*inch, 4*inch])
gcols.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (0,0), 0),
    ("LEFTPADDING", (1,0), (1,0), 20),
]))
story.append(gcols)
story.append(PageBreak())

# ── SLIDE 9: Q&A + Next Steps ───────────────────
story.append(Paragraph("Q&A & Next Steps", S_TITLE))
story.append(Paragraph("All \u2014 10 min", S_SUBTITLE))
story.append(Spacer(1, 8))

story.append(Paragraph("Open Discussion", S_H2))
story.append(bullet("Any questions or concerns about what we\u2019ve covered?"))
story.append(bullet("What areas of the organization are you most interested in being involved with?"))
story.append(bullet("Connections that might help with fundraising, partnerships, or research?"))
story.append(Spacer(1, 6))

story.append(Paragraph("Post-Meeting Follow-Ups (by email)", S_H2))
story.append(bullet("<b>COI Policy</b> \u2014 reply with attestation"))
story.append(bullet("<b>Bylaws</b> \u2014 Ken & Barbara reply confirming receipt"))
story.append(bullet("<b>Onboarding Guide</b> \u2014 written reference for today\u2019s discussion + insurance, policies, financials"))
story.append(bullet("<b>Board Reference Site</b> \u2014 full documents, history, compliance calendar"))
story.append(bullet("<b>Meeting minutes</b> \u2014 drafted from transcript, sent for review; recording destroyed after"))
story.append(Spacer(1, 6))

story.append(Paragraph("Going Forward", S_H2))
story.append(bullet("<b>Next meeting:</b> Q2 2026 (quarterly)"))
story.append(bullet("<b>Email votes:</b> reply-all with your vote; email signature = signed consent"))
story.append(bullet("<b>Response time:</b> 5\u20137 days for votes; few days for general matters"))
story.append(bullet("<b>Time commitment:</b> ~1\u20132 hours/month"))
story.append(bullet("Pursue grant pipeline (ECI, NewSchools, TWCF)"))
story.append(Spacer(1, 30))
story.append(Paragraph("Thank you for joining the board. We are glad to have you.", ParagraphStyle("thanks", fontName="Helvetica", fontSize=15, textColor=GRAY, alignment=TA_CENTER)))

# Build
doc = SimpleDocTemplate(
    OUT,
    pagesize=landscape(letter),
    leftMargin=0.7*inch,
    rightMargin=0.7*inch,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
)
doc.build(story, onFirstPage=page_header, onLaterPages=page_header)
print(f"PDF generated: {OUT}")
