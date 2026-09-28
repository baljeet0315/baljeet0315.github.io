from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER

OUTPUT = "/sessions/fervent-nice-dijkstra/mnt/outputs/Resume - Baljeet Singh.pdf"

BLACK   = colors.HexColor("#111111")
DARK    = colors.HexColor("#222222")
MID     = colors.HexColor("#444444")
MUTED   = colors.HexColor("#777777")
LIGHT   = colors.HexColor("#555555")
RULE    = colors.HexColor("#cccccc")
WHITE   = colors.white

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.7*inch,
    rightMargin=0.7*inch,
    topMargin=0.55*inch,
    bottomMargin=0.55*inch,
    title="Resume - Baljeet Singh",
    author="Baljeet Singh",
    subject="QA Engineer | AI Engineer",
    creator="Baljeet Singh",
)

W = letter[0] - 1.4*inch

def ps(name, **kw):
    return ParagraphStyle(name, **kw)

S = {
    "name":     ps("name",    fontSize=24, fontName="Helvetica-Bold", textColor=BLACK,  spaceAfter=2,  leading=28),
    "subtitle": ps("sub",     fontSize=10, fontName="Helvetica",      textColor=MID,    spaceAfter=2,  leading=14),
    "contact":  ps("cnt",     fontSize=8,  fontName="Helvetica",      textColor=MUTED,  spaceAfter=0,  leading=12),
    "contactR": ps("cntR",    fontSize=8,  fontName="Helvetica",      textColor=MUTED,  spaceAfter=0,  leading=12, alignment=TA_RIGHT),
    "avail":    ps("avail",   fontSize=8,  fontName="Helvetica-Bold", textColor=MID,    spaceAfter=0,  leading=12),
    "section":  ps("sec",     fontSize=9,  fontName="Helvetica-Bold", textColor=BLACK,  spaceBefore=8, spaceAfter=5, leading=12),
    "summary":  ps("summ",    fontSize=9,  fontName="Helvetica",      textColor=LIGHT,  spaceAfter=0,  leading=14),
    "company":  ps("co",      fontSize=10, fontName="Helvetica-Bold", textColor=BLACK,  spaceAfter=0,  leading=14),
    "dates":    ps("dt",      fontSize=8,  fontName="Helvetica",      textColor=MUTED,  leading=14,    alignment=TA_RIGHT),
    "role":     ps("role",    fontSize=9,  fontName="Helvetica-Oblique", textColor=MID, spaceAfter=4,  leading=13),
    "bullet":   ps("bul",     fontSize=9,  fontName="Helvetica",      textColor=LIGHT,  leftIndent=12, spaceAfter=2, leading=13),
    "proj":     ps("proj",    fontSize=9,  fontName="Helvetica-Bold", textColor=DARK,   spaceBefore=6, spaceAfter=2, leading=13),
    "projlink": ps("plink",   fontSize=8,  fontName="Helvetica",      textColor=MUTED,  spaceAfter=3,  leading=12),
    "tools":    ps("tools",   fontSize=8,  fontName="Helvetica",      textColor=MUTED,  spaceBefore=4, spaceAfter=0, leading=12),
    "skilllbl": ps("slbl",    fontSize=9,  fontName="Helvetica-Bold", textColor=BLACK,  leading=13),
    "skilltxt": ps("stxt",    fontSize=9,  fontName="Helvetica",      textColor=LIGHT,  leading=13),
    "edu":      ps("edu",     fontSize=9,  fontName="Helvetica-Bold", textColor=BLACK,  leading=13),
    "edudt":    ps("edudt",   fontSize=9,  fontName="Helvetica",      textColor=MUTED,  leading=13,    alignment=TA_RIGHT),
}

def hr(before=2, after=5):
    return HRFlowable(width="100%", thickness=0.6, color=RULE, spaceBefore=before, spaceAfter=after)

def thick_hr(before=0, after=6):
    return HRFlowable(width="100%", thickness=1.5, color=BLACK, spaceBefore=before, spaceAfter=after)

def section_label(text):
    return [Paragraph(text.upper(), S["section"]), hr(before=0, after=6)]

def bullet(text):
    return Paragraph(f"• {text}", S["bullet"])

def link(url, label=None):
    display = label or url
    return f'<link href="{url}" color="#111111"><u>{display}</u></link>'

def skill_row(label, items):
    return Table(
        [[Paragraph(label, S["skilllbl"]),
          Paragraph(", ".join(items), S["skilltxt"])]],
        colWidths=[1.4*inch, W - 1.4*inch],
        style=TableStyle([
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING",   (0,0), (-1,-1), 0),
            ("RIGHTPADDING",  (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("TOPPADDING",    (0,0), (-1,-1), 0),
        ])
    )

def job_header(company, dates, role, location):
    t = Table(
        [[Paragraph(company, S["company"]),
          Paragraph(dates, S["dates"])]],
        colWidths=[4.2*inch, W - 4.2*inch],
        style=TableStyle([
            ("VALIGN",        (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING",   (0,0), (-1,-1), 0),
            ("RIGHTPADDING",  (0,0), (-1,-1), 0),
            ("BOTTOMPADDING", (0,0), (-1,-1), 1),
            ("TOPPADDING",    (0,0), (-1,-1), 0),
        ])
    )
    return [t, Paragraph(f"{role}  ·  {location}", S["role"])]

story = []

# ── HEADER ────────────────────────────────────────────────────
left_col = [
    Paragraph("Baljeet Singh", S["name"]),
    Paragraph("QA Engineer  &amp;  AI Engineer  ·  7+ years", S["subtitle"]),
    Paragraph("Surrey, BC · Canada", S["contact"]),
    Spacer(1, 3),
    Paragraph("● Open to contract roles", S["avail"]),
]
right_col = [
    Spacer(1, 6),
    Paragraph("647-482-9893", S["contactR"]),
    Paragraph("singhbarry@outlook.com", S["contactR"]),
    Paragraph(link("https://baljeet0315.github.io", "baljeet0315.github.io"), ps("cr2", parent=S["contactR"])),
    Paragraph(link("https://github.com/baljeet0315", "github.com/baljeet0315"), ps("cr3", parent=S["contactR"])),
    Paragraph(link("https://www.linkedin.com/in/baljeet-bal-6b3288206/", "linkedin.com/in/baljeet-bal"), ps("cr4", parent=S["contactR"])),
]

header = Table(
    [[left_col, right_col]],
    colWidths=[3.8*inch, W - 3.8*inch],
    style=TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("TOPPADDING",    (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ])
)
story.append(header)
story.append(Spacer(1, 8))
story.append(thick_hr(before=0, after=8))

# ── SUMMARY ───────────────────────────────────────────────────
story.extend(section_label("Summary"))
story.append(Paragraph(
    "Detail-oriented QA and AI Engineer with over 7 years of experience testing complex digital platforms across "
    "web, mobile, and back-end systems. Experienced in data validation, ETL pipeline testing, semantic model validation, "
    "and Power BI report QA — ensuring source-to-report accuracy across integrated data systems. Skilled in building "
    "agentic AI systems using LangChain, LangGraph, and CrewAI, with production deployments across multiple platforms. "
    "Proven ability to design and execute comprehensive test strategies, lead QA efforts cross-functionally, and deliver "
    "high-quality software under tight deadlines. Experienced in Agile/Scrum environments, Azure DevOps, and data "
    "quality assessment across complex integrated systems.",
    S["summary"]
))
story.append(Spacer(1, 6))

# ── SKILLS ────────────────────────────────────────────────────
story.extend(section_label("Core Skills"))
story.append(skill_row("AI & Agents",  ["LangChain", "LangGraph", "CrewAI", "RAG", "MCP", "n8n", "Claude API", "OpenAI", "ElevenLabs", "Prompt Engineering", "Zero/Few-Shot", "Multi-Agent Systems"]))
story.append(skill_row("Testing & QA", ["Manual Testing", "Automated Testing", "API Testing", "Functional Testing", "Data Validation", "ETL Validation", "Semantic Model Validation", "Power BI Report QA", "Data Profiling", "Star/Snowflake Schema", "BDD", "Test Planning", "AI-Assisted Test Gen", "TEM"]))
story.append(skill_row("Tools",        ["Selenium WebDriver", "Appium", "Postman", "Charles Proxy", "JIRA", "Azure DevOps", "SQL Server", "DAX (Basic)", "Power BI", "DynamoDB", "AWS S3", "Supabase", "Vercel", "Railway", "GitHub"]))
story.append(skill_row("Languages",    ["Python (OOP)", "SQL"]))
story.append(skill_row("Leadership",   ["QA Lead", "Certified Product Owner", "Mentoring", "Agile/Scrum", "Risk Management", "Stakeholder Comms", "Release Sign-off"]))
story.append(Spacer(1, 6))

# ── AI PROJECTS ───────────────────────────────────────────────
story.extend(section_label("AI Projects"))

# YouTube Agent
story.append(Paragraph("YouTube Agent", S["company"]))
story.append(Paragraph(link("https://github.com/baljeet0315/Youtube-Agent"), S["projlink"]))
story.append(Paragraph("Claude · ElevenLabs · Agentic AI · Railway · Supabase · Cloudflare · Clerk · Vercel", S["role"]))
for b in [
    "Built an end-to-end agentic video production pipeline — user enters a prompt, Claude generates a script, an AI video is created, ElevenLabs adds a voiceover, and the final video is automatically uploaded to YouTube",
    "Developed a full-stack UI allowing non-technical users to produce and publish AI-generated videos with a single prompt",
    "Deployed to production on Railway with Cloudflare for storage, Supabase as database, Clerk for authentication, and Vercel for the frontend",
]:
    story.append(bullet(b))
story.append(Spacer(1, 8))

# Welfare Scheme
story.append(Paragraph("Government Welfare Scheme Finder", S["company"]))
story.append(Paragraph(link("https://github.com/baljeet0315/Welfare-scheme"), S["projlink"]))
story.append(Paragraph("LangChain · RAG · Vector DB · Claude · GPT-4 · Conversational AI", S["role"]))
for b in [
    "Built a conversational RAG-powered chatbot that helps Indian citizens discover government welfare schemes they are eligible for based on their personal profile",
    "Implemented a cross-scoring mechanism using both Claude and GPT-4 to validate and improve output quality and accuracy",
    "System guides users through a short Q&A flow and returns matched schemes along with required documents and application steps",
]:
    story.append(bullet(b))
story.append(Spacer(1, 8))

# Chai Hai Order System
story.append(Paragraph("Chai Hai Order System  ·  In Progress", S["company"]))
story.append(Paragraph("WhatsApp Business API · Claude · Webhook · Agentic AI", S["role"]))
for b in [
    "Building an automated order management system for a small business with 200+ customers — customers place orders by sending a WhatsApp message to the business number",
    "Implemented WhatsApp webhook integration with Claude to process and validate incoming orders in natural language",
    "Currently adding inventory management, delivery route optimization, and automated invoice generation",
]:
    story.append(bullet(b))
story.append(Spacer(1, 8))

# Code Review Agent
story.append(Paragraph("Code Review Agent  ·  In Progress", S["company"]))
story.append(Paragraph(link("https://github.com/baljeet0315/Code-Review-Agent"), S["projlink"]))
story.append(Paragraph("LangGraph · RAG · GitHub Integration · Automated Scoring", S["role"]))
for b in [
    "Building an AI-powered code review agent that triggers automatically when code is merged into a GitHub repository",
    "Agent reviews code quality, identifies issues, provides structured feedback, and generates a scored report for the development team",
    "Implemented using LangGraph for agent orchestration and RAG for context-aware code analysis against best practices",
]:
    story.append(bullet(b))
story.append(Spacer(1, 6))

# ── EXPERIENCE ────────────────────────────────────────────────
story.extend(section_label("Experience"))

# Lululemon
story.extend(job_header("Lululemon Athletica", "May 2022 – Present", "QA Engineer (Contract)", "Vancouver, BC"))
for b in [
    "Delivered end-to-end QA across multiple projects on iOS and web platforms, covering front-end and back-end systems",
    "Acted as QA lead on various feature teams — owned task allocation, test planning, coordination, and sign-off",
    "Developed and enhanced an internal automated testing framework to improve regression efficiency and maintainability",
    "Part of a cross-functional team that built an internal Test Creation Agent — QA engineers submit a JIRA ticket link, the agent generates test cases, and upon approval automatically adds them to TestRail",
    "Building an Agentic QA Tool for Analytics tickets to reduce manual validation effort (in progress)",
    "Managed test environments (TEM) across multiple projects; collaborated in Git-based workflows with peer code review",
    "Reported to senior management on test coverage, automation progress, and key performance metrics",
]:
    story.append(bullet(b))

story.append(Paragraph("RISE – Product Catalog Migration (PCM4 to PCM5)", S["proj"]))
for b in [
    "Performing end-to-end data validation for a global product catalog migration, ensuring source-to-target accuracy across schema and structural changes between PCM4 and PCM5",
    "Validating ETL transformation logic — including data ordering, sorting, formatting, and business rules — to confirm data flows correctly into the new system",
    "Assessing downstream impact of schema changes on dependent data consumers and validating data integrity across raw and transformed layers",
    "Writing and executing SQL queries to compare records, profile data, and investigate discrepancies between source and target systems",
    "Supporting consolidation of region-specific catalogs (North America, Europe, Australia) into a single unified global catalog",
]:
    story.append(bullet(b))

story.append(Paragraph("Next Gen E-commerce (NGC) – Web &amp; iOS", S["proj"]))
for b in [
    "Replaced legacy systems with modern microservices for Cart, Shipping, and Payments",
    "Defined and executed comprehensive master test plans across platforms",
    "Performed integration and API testing using Postman; deployed regression suites within CI/CD pipelines via Azure DevOps",
    "Supported A/B testing initiatives to inform go/no-go decisions",
]:
    story.append(bullet(b))

story.append(Paragraph("Estimated Delivery Date (EDD)", S["proj"]))
for b in [
    "Validated end-to-end EDD feature ensuring accurate delivery date calculation across web and iOS",
    "Tested Order-By / Get-By logic for cutoff time handling, timezone accuracy, and edge cases across shipping methods",
    "Performed API testing with Postman; executed regression and integration testing to protect existing Cart/Checkout flows",
]:
    story.append(bullet(b))

story.append(Paragraph("Apple Wallet Order Tracking – Narvar Pilot", S["proj"]))
for b in [
    "Integrated Lululemon app with Apple Wallet and Narvar for real-time order tracking",
    "Used Postman for API validation and Splunk for engagement monitoring",
    "Owned QA planning and cross-functional communication between vendor and internal teams",
]:
    story.append(bullet(b))

story.append(Paragraph("<b>Tools:</b> Selenium WebDriver (Python), Postman, Xcode, Charles Proxy, SQL, DynamoDB, TestRail, Jira, Azure DevOps, Confluence, AWS, Git/Bitbucket, AI test case generation tool", S["tools"]))
story.append(Spacer(1, 10))

# Accedo
story.extend(job_header("Accedo.tv", "Aug 2021 – May 2022", "QA Analyst (Contract)", "Toronto, ON"))
for b in [
    "Led QA for the Peloton OTT application on iOS and tvOS platforms",
    "Designed master test plans; executed API testing using Postman and network debugging with Charles Proxy",
    "Validated back-end data using SQL; monitored app performance via Datadog and Splunk dashboards",
    "Provided L2 incident triage and collaborated with L3 and service management teams",
    "Liaised with client stakeholders to align QA strategy and delivery timelines",
]:
    story.append(bullet(b))
story.append(Spacer(1, 10))

# You.i Labs
story.extend(job_header("You.i Labs", "Apr 2016 – Feb 2020", "QA Analyst", "Ottawa, ON"))
for b in [
    "Led testing of cross-platform OTT applications for major clients across iOS, Android, PS4/5, Xbox, Roku, Samsung, LG, and Nintendo",
    "Executed test cycles covering DRM, video playback, and user sessions using Charles Proxy, Mongo Compass, and Xcode",
    "Developed and maintained Selenium WebDriver-based automation scripts; contributed to framework design",
    "Conducted performance and load testing using Apache JMeter to evaluate back-end stability under varying traffic loads",
    "Mentored new hires, developed onboarding guides, and standardized internal QA processes",
]:
    story.append(bullet(b))
story.append(Spacer(1, 10))

# TCS
story.extend(job_header("Tata Consultancy Services (TCS)", "Mar 2013 – Dec 2015", "System Analyst", "Pune, India"))
for b in [
    "Delivered the BSNL-CDR project using SAP CRM, ensuring high data integrity across 13 integrated modules",
    "Administered EAI systems and messaging databases processing over 5 million transactions daily",
    "Provided production support and maintained failover system readiness for critical services",
    "Validated ETL data transformation pipelines and ensured end-to-end data flow accuracy, completeness, and integrity across 13 integrated modules",
]:
    story.append(bullet(b))

story.append(Spacer(1, 6))

# ── EDUCATION ─────────────────────────────────────────────────
story.extend(section_label("Education & Certifications"))
edu = Table(
    [
        [Paragraph("Certified Product Owner", S["edu"]),          Paragraph("Aug 2020",    S["edudt"])],
        [Paragraph("Bachelor of Engineering – CSVTU, India", S["edu"]), Paragraph("2008 – 2012", S["edudt"])],
    ],
    colWidths=[5*inch, W - 5*inch],
    style=TableStyle([
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",   (0,0), (-1,-1), 0),
        ("RIGHTPADDING",  (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("ALIGN",         (1,0), (1,-1),  "RIGHT"),
    ])
)
story.append(edu)

doc.build(story)
print("Done!")
