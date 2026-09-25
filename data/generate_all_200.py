import json
import os

items = []

def add(item_id, name, cat, subcat, model, desc, target, personas, channels, ticket, cycle, rel_ind, vendors, clients, keywords):
    items.append({
        "id": item_id,
        "name": name,
        "category": cat,
        "sub_category": subcat,
        "business_model": model,
        "description": desc,
        "target_audience": target,
        "ideal_buyer_personas": personas,
        "lead_generation_channels": channels,
        "typical_ticket_size": ticket,
        "sales_cycle": cycle,
        "graph_nodes": {
            "related_industries": rel_ind,
            "common_vendor_needs": vendors,
            "common_client_types": clients
        },
        "search_keywords": keywords
    })

# --- 1. Technology & Software (20) ---
add("b2b-saas-provider", "B2B Software-as-a-Service (SaaS)", "Technology & Software", "Cloud Software", "B2B",
    "Companies providing cloud-based software tools for business operations, productivity, or enterprise workflows.",
    "Mid-market to Enterprise Operations, IT, and Department Heads",
    ["CTO", "VP of Engineering", "Head of Operations", "CIO"],
    ["LinkedIn Cold Outreach", "Account-Based Marketing (ABM)", "SEO & Content Marketing"],
    "High ($10k - $100k+ ARR)", "3 to 9 months",
    ["Enterprise Software", "Cloud Infrastructure"], ["SOC2 Compliance Auditors", "DevOps Consultants", "B2B Growth Agencies"], ["Mid-Market Companies", "Fast-Growing Startups"],
    ["saas", "b2b software", "cloud application", "subscription software"])

add("b2c-mobile-app-developer", "B2C Mobile App Business", "Technology & Software", "Consumer Software", "B2C",
    "Consumer-facing mobile applications monetization through subscriptions, in-app purchases, or ad networks.",
    "Individual smartphone users across specific lifestyle, productivity, or gaming demographics",
    ["App Store Users", "Mobile Gaming Enthusiasts", "Fitness & Health Seekers"],
    ["App Store Optimization (ASO)", "Meta & TikTok Ads", "Influencer Marketing"],
    "Low ($5 - $100/yr)", "Immediate (< 1 day)",
    ["Consumer Tech", "Mobile Gaming"], ["Mobile App Development Studios", "ASO Consultants", "User Acquisition Agencies"], ["General Consumers", "Mobile Gamers"],
    ["mobile app", "b2c app", "ios app", "android app"])

add("ai-ml-solutions-agency", "AI & Machine Learning Agency", "Technology & Software", "Artificial Intelligence", "B2B",
    "Consulting and development agencies building custom AI models, LLM agents, and predictive analytics for enterprises.",
    "Enterprises and tech scale-ups looking to integrate AI into existing processes",
    ["VP of Innovation", "Chief AI Officer", "Director of Data Science", "CTO"],
    ["Thought Leadership & Whitepapers", "LinkedIn Outreach", "AI Industry Summits"],
    "Enterprise ($25k - $250k+ per project)", "2 to 6 months",
    ["Artificial Intelligence", "Data Engineering"], ["Data Annotation Services", "GPU Cloud Providers", "AI Ethics Counsel"], ["Healthcare Enterprises", "FinTech Firms", "Logistics Companies"],
    ["ai agency", "machine learning consulting", "llm integration", "generative ai"])

add("managed-service-provider", "Managed Service Provider (MSP / IT Support)", "Technology & Software", "IT Infrastructure", "B2B",
    "Outsourced IT services managing network infrastructure, cybersecurity, helpdesk, and cloud migration for SMBs.",
    "Small to medium businesses without dedicated internal IT departments",
    ["CEO", "Managing Partner", "Director of Operations", "Office Manager"],
    ["Local B2B Networking", "Cold Calling", "Google Local PPC"],
    "Medium ($1,500 - $15,000/mo MRR)", "1 to 3 months",
    ["IT Services", "Cybersecurity"], ["Hardware Distributors", "SaaS Licensing Partners", "Field Technicians"], ["Law Firms", "Accounting Practices", "Medical Clinics"],
    ["msp", "it support", "managed IT", "network management"])

add("cybersecurity-consulting-firm", "Cybersecurity Consulting Firm", "Technology & Software", "Information Security", "B2B",
    "Specialized security consultancies providing penetration testing, vulnerability audits, incident response, and compliance.",
    "Fintech, Healthcare, E-commerce, and Defense sector companies handling sensitive data",
    ["CISO", "Head of Compliance", "VP of Engineering"],
    ["Industry Security Conferences", "Security Audits / Free Scans", "B2B Webinars"],
    "High ($15k - $150k per engagement)", "2 to 6 months",
    ["Information Security", "Compliance & Audit"], ["Penetration Testing Tools", "Security Awareness Training Platforms"], ["Financial Institutions", "Healthcare Providers", "SaaS Vendors"],
    ["cybersecurity", "pen testing", "ciso consulting", "soc2 compliance"])

add("cloud-infrastructure-devops-agency", "Cloud Infrastructure & DevOps Agency", "Technology & Software", "Cloud Computing", "B2B",
    "Consultancies assisting engineering teams with AWS/GCP/Azure migrations, Kubernetes orchestration, CI/CD pipelines, and FinOps.",
    "Software startups and scale-ups needing high-availability infrastructure",
    ["VP of Engineering", "DevOps Lead", "CTO"],
    ["Tech Communities & GitHub", "Cloud Partner Networks", "LinkedIn Technical Content"],
    "High ($10k - $50k project / $5k-$20k retainer)", "1 to 3 months",
    ["Cloud Computing", "DevOps"], ["Cloud Monitoring Tools", "Security Scanners", "FinOps Analytics Platforms"], ["SaaS Companies", "E-commerce Platforms", "FinTech Scaleups"],
    ["devops agency", "cloud migration", "aws consulting", "kubernetes agency"])

add("web-custom-software-dev-shop", "Custom Software & Web Development Agency", "Technology & Software", "Software Engineering", "B2B",
    "Agencies building bespoke web applications, enterprise software platforms, and custom digital tools.",
    "Non-technical founders, mid-market legacy businesses modernizing systems",
    ["Founder / CEO", "Chief Digital Officer", "Product Manager"],
    ["Clutch / DesignRush Listings", "SEO & Technical Case Studies", "Referrals"],
    "High ($20k - $200k+ per build)", "2 to 5 months",
    ["Web Development", "Software Engineering"], ["UI/UX Contractors", "QA Automation Engineers", "Cloud Hosting Partners"], ["Non-Tech Enterprises", "Early-Stage Startups"],
    ["custom software dev", "web app development", "dev shop", "software agency"])

add("blockchain-web3-dev-studio", "Blockchain & Web3 Development Studio", "Technology & Software", "Blockchain", "B2B",
    "Development studios crafting smart contracts, decentralized apps (dApps), tokenomics, and Web3 security protocols.",
    "Crypto protocols, Web3 startups, brands launching digital assets",
    ["Web3 Project Founder", "Blockchain Architect", "Head of Ecosystem"],
    ["X (Twitter) Spaces & Threads", "Discord Communities", "Crypto Hackathons"],
    "High ($30k - $200k per project)", "1 to 3 months",
    ["Blockchain", "FinTech"], ["Smart Contract Auditors", "Tokenomics Consultants", "Community Managers"], ["DeFi Protocols", "Web3 Gaming Projects"],
    ["web3 dev studio", "blockchain development", "smart contract agency", "dapp developer"])

add("iot-embedded-systems-developer", "IoT & Embedded Systems Developer", "Technology & Software", "Hardware & IoT", "B2B",
    "Hardware and firmware engineering firms designing connected devices, sensor networks, and industrial IoT solutions.",
    "Industrial manufacturers, smart home device brands, healthcare hardware companies",
    ["VP of Hardware Engineering", "Product Director", "Operations Director"],
    ["Industrial Trade Shows", "Engineering Publications", "Direct Outreach"],
    "Enterprise ($50k - $500k+)", "4 to 12 months",
    ["Internet of Things", "Hardware Engineering"], ["PCB Fabricators", "Rapid Prototyping Labs", "Regulatory Testers"], ["Smart Home Brands", "Industrial Automation Companies"],
    ["iot developer", "embedded systems", "firmware engineering", "connected device"])

add("ecommerce-development-agency", "E-Commerce Development & Integration Agency", "Technology & Software", "E-Commerce Solutions", "B2B",
    "Specialized web agencies focusing on Shopify Plus, Magento, and Headless e-commerce architecture.",
    "Fast-growing D2C brands and traditional retail brands migrating online",
    ["Head of E-Commerce", "VP of Digital", "D2C Brand Founder"],
    ["Shopify Partner Ecosystem", "E-Commerce Events", "Case Studies & SEO"],
    "High ($15k - $100k build + retainer)", "1 to 3 months",
    ["E-Commerce", "Digital Retail"], ["CRO Consultants", "Payment Gateway Integrators", "3PL Partners"], ["Apparel Brands", "Consumer Electronics Sellers"],
    ["shopify plus agency", "ecommerce dev", "headless ecommerce", "magento agency"])

add("data-analytics-bi-agency", "Data Analytics & Business Intelligence Agency", "Technology & Software", "Data & Analytics", "B2B",
    "Consultancies setting up modern data stacks (Snowflake, dbt, Looker, Tableau) and predictive business dashboards.",
    "Mid-market companies struggling to unify fragmented operational and sales data",
    ["Head of Analytics", "VP of Revenue Operations", "CFO", "COO"],
    ["LinkedIn Thought Leadership", "Data Tool Ecosystem Partnerships", "Webinars"],
    "High ($20k - $100k project)", "2 to 4 months",
    ["Data Engineering", "Business Intelligence"], ["Data Warehouse Providers", "ETL Tool Vendors", "BI Platform Partners"], ["E-commerce Enterprises", "Financial Institutions"],
    ["bi consultancy", "data analytics agency", "snowflake consultant", "tableau dev"])

add("ar-vr-immersive-tech-agency", "AR/VR & Immersive Tech Studio", "Technology & Software", "Spatial Computing", "B2B",
    "Studios building augmented reality filters, VR training simulations, and 3D product visualizations.",
    "Enterprise training departments, retail brands, industrial manufacturing units",
    ["Director of Innovation", "Corporate Training Lead", "Marketing Director"],
    ["Spatial Computing Expos", "Interactive Web Demos", "LinkedIn Showcase Videos"],
    "High ($25k - $150k)", "2 to 5 months",
    ["Augmented Reality", "Virtual Reality"], ["3D Modeling Artists", "Unity/Unreal Developers", "VR Headset Hardware Suppliers"], ["Aviation Training Units", "Furniture Retailers"],
    ["ar agency", "vr studio", "spatial computing dev", "3d product visualization"])

add("nocode-automation-agency", "No-Code / Low-Code Automation Agency", "Technology & Software", "Workflow Automation", "B2B",
    "Agencies automating internal business workflows using tools like Make, Zapier, Airtable, and Retool.",
    "Lean SMBs, real estate agencies, recruitment firms, and fast-growing startups",
    ["COO", "Founder", "Operations Manager"],
    ["YouTube Tutorials", "Zapier/Make Experts Directory", "X Growth Posts"],
    "Medium ($3k - $20k build + retainer)", "1 to 3 weeks",
    ["Workflow Automation", "No-Code Tech"], ["SaaS API Integrators", "Airtable Developers", "AI Prompt Engineers"], ["Real Estate Brokerages", "Marketing Agencies"],
    ["zapier consultant", "make automation agency", "nocode dev", "airtable consultant"])

add("game-development-studio", "Indie & Client Game Development Studio", "Technology & Software", "Gaming", "B2B / B2C",
    "Studios creating PC, console, and mobile video games either independently or as work-for-hire for publishers.",
    "Game Publishers, Gaming Consoles, Brands seeking Advergames",
    ["Publishing Director", "Brand Marketing Director", "Game Producer"],
    ["Game Developers Conference (GDC)", "Pitching to Publishers", "Steam Community Demos"],
    "High ($50k - $500k+)", "3 to 12 months",
    ["Video Games", "Interactive Entertainment"], ["Sound Designers", "Concept Artists", "QA Game Testers"], ["Game Publishers", "Brands"],
    ["game dev studio", "unity game developer", "unreal engine studio", "work for hire game dev"])

add("qa-software-testing-agency", "QA & Software Testing Agency", "Technology & Software", "Software Quality", "B2B",
    "Outsourced quality assurance teams providing manual, automated, performance, and load testing services.",
    "Software engineering teams without full-time dedicated QA departments",
    ["VP of Engineering", "Engineering Manager", "Product Owner"],
    ["Tech Partnerships", "Cold Outreach to Engineering Leads", "Content on Automated Testing"],
    "Medium ($5k - $30k/mo retainer)", "1 to 2 months",
    ["Software Testing", "Quality Assurance"], ["Automation Tool Platforms", "Device Cloud Labs", "Security Testers"], ["SaaS Companies", "FinTech Apps"],
    ["qa testing agency", "software quality assurance", "automated testing service", "outsourced qa"])

add("erp-crm-implementation-consultancy", "ERP & CRM Implementation Consultancy", "Technology & Software", "Enterprise Systems", "B2B",
    "Specialists implementing, customizing, and integrating Salesforce, Hubspot, NetSuite, or SAP for enterprises.",
    "Mid-market to enterprise companies upgrading legacy operational platforms",
    ["CIO", "VP of Sales Operations", "Director of IT"],
    ["Platform Ecosystem Partner Networks", "Industry Conventions", "Co-selling with Vendors"],
    "Enterprise ($30k - $300k+)", "3 to 6 months",
    ["Enterprise Systems", "CRM Integration"], ["Certified System Administrators", "Data Migration Tools", "Custom Integration Coders"], ["Manufacturing Plants", "Distribution Centers"],
    ["salesforce partner", "netsuite implementation", "hubspot agency", "crm consultant"])

add("api-integration-services-provider", "API & Integration Services Provider", "Technology & Software", "Middleware & APIs", "B2B",
    "Engineering firms connecting disparate software systems, building custom APIs, and managing ESB platforms.",
    "Enterprises with sprawling software tech stacks requiring seamless data synchronization",
    ["Enterprise Architect", "Head of Integrations", "CTO"],
    ["Technical Whitepapers", "MuleSoft / Boomi Partner Directories", "B2B Email Outreach"],
    "High ($20k - $100k per project)", "2 to 4 months",
    ["API Engineering", "System Integration"], ["API Management Platforms", "Security Gateway Vendors", "DevOps Engineers"], ["Financial Institutions", "Healthcare Systems"],
    ["api integration service", "middleware consultant", "custom api development", "mulesoft partner"])

add("healthtech-telemedicine-platform", "HealthTech & Telemedicine Platform", "Technology & Software", "Digital Health", "B2B / B2B2C",
    "Software companies developing HIPAA-compliant patient portals, remote monitoring tools, and EHR integrations.",
    "Hospitals, Private Clinics, Medical Group Practices, Health Insurance Providers",
    ["Chief Medical Officer", "Head of Clinical Operations", "Hospital IT Director"],
    ["Medical Trade Shows (HIMSS)", "Direct Sales Reps", "Healthcare Partner Networks"],
    "Enterprise ($20k - $200k ARR)", "4 to 12 months",
    ["Digital Health", "Medical Software"], ["HIPAA Compliance Consultants", "Medical Device API Integrators", "Cloud Security Teams"], ["Hospital Networks", "Outpatient Clinics"],
    ["healthtech platform", "telemedicine software", "hipaa software", "ehr integration"])

add("fintech-solutions-provider", "FinTech Solutions Provider", "Technology & Software", "Financial Technology", "B2B",
    "Software platforms offering white-label banking, payment gateway integrations, fraud detection, and lending APIs.",
    "Financial institutions, Neo-banks, E-commerce marketplaces, Lenders",
    ["Head of Payments", "Chief Risk Officer", "Chief Product Officer"],
    ["FinTech Conferences (Money20/20)", "B2B Technical Sales", "Industry Whitepapers"],
    "Enterprise ($50k - $500k+ ARR)", "4 to 9 months",
    ["Financial Technology", "Payment Processing"], ["PCI-DSS Auditors", "Banking API Providers", "KYC / AML Software Vendors"], ["Digital Banks", "Loan Providers"],
    ["fintech platform", "payment gateway provider", "banking as a service", "kyc software"])

add("edtech-platform-developer", "EdTech Platform Developer", "Technology & Software", "Educational Tech", "B2B / B2C",
    "Software platforms delivering Learning Management Systems (LMS), interactive educational content, and student analytics.",
    "K-12 School Districts, Universities, Corporate L&D Departments",
    ["Director of Learning Technology", "University Provost", "Corporate L&D Manager"],
    ["Educational Conventions (ISTE)", "RFP Bidding Processes", "Direct Outreach to School Districts"],
    "High ($10k - $150k ARR)", "3 to 12 months",
    ["Educational Technology", "Learning Management Systems"], ["Instructional Designers", "Gamification Consultants", "FERPA Compliance Experts"], ["School Districts", "Higher Ed Institutions"],
    ["edtech platform", "lms software", "digital learning platform", "e-learning software"])

# --- 2. Professional Services & Consulting (20) ---
add("management-consulting-firm", "Management Consulting Firm", "Professional Services & Consulting", "Corporate Advisory", "B2B",
    "Consultancies advising executive leadership on corporate strategy, restructuring, operational efficiency, and growth.",
    "C-Suite executives at mid-market to Fortune 500 corporations",
    ["CEO", "Chief Strategy Officer", "Board of Directors"],
    ["Executive Networking", "Thought Leadership Publishing", "Alumni Referral Networks"],
    "Enterprise ($50k - $500k+ per engagement)", "3 to 9 months",
    ["Management Consulting", "Corporate Strategy"], ["Market Research Analysts", "Financial Modelers", "Executive Coaches"], ["Corporations", "Private Equity Firms"],
    ["management consulting", "strategy consultant", "corporate advisory", "operational efficiency"])

add("human-resources-recruiting-agency", "Human Resources & Recruiting Agency", "Professional Services & Consulting", "Talent Acquisition", "B2B",
    "Recruitment and staffing agencies providing contingency placement, executive search, and RPO services.",
    "Growing companies needing mid-to-senior talent acquisition",
    ["VP of HR", "Chief People Officer", "Hiring Managers"],
    ["LinkedIn Recruiter Outreach", "Cold Sales Email", "HR Conferences"],
    "Medium ($5k - $30k per placement)", "1 to 2 months",
    ["Recruiting", "Human Resources"], ["Applicant Tracking Systems", "Background Check Vendors", "Job Boards"], ["Tech Scaleups", "Professional Services Firms"],
    ["recruiting agency", "staffing firm", "headhunter", "talent acquisition"])

add("virtual-assistant-bpo-provider", "Virtual Assistant & Business BPO Provider", "Professional Services & Consulting", "Outsourced Operations", "B2B",
    "Offshore and nearshore BPO agencies supplying virtual assistants, admin support, and customer care teams.",
    "Busy executives, agency owners, lean founders, e-commerce brands",
    ["CEO", "Founder", "Director of Operations"],
    ["Content Marketing", "Cold Outbound Email", "Podcasts & Founder Communities"],
    "Medium ($1,000 - $10,000/mo retainer)", "1 to 4 weeks",
    ["Business Process Outsourcing", "Virtual Assistants"], ["Time Tracking Platforms", "VoIP Providers", "Training Software"], ["Digital Agencies", "E-Commerce Brands"],
    ["virtual assistant", "bpo provider", "outsourced admin", "offshore staffing"])

add("executive-search-firm", "Executive Search & Retained Headhunting", "Professional Services & Consulting", "Executive Talent", "B2B",
    "Boutique retained search firms specializing in sourcing C-level executives and VP-level leaders for high-growth firms.",
    "Venture capital backed startups, public corporations, board directors",
    ["Board Member", "Managing Director", "CEO"],
    ["Executive Relationship Building", "Private Dinners", "Industry Leadership Reports"],
    "High ($25k - $100k+ retainer per role)", "2 to 4 months",
    ["Executive Recruitment", "Talent Management"], ["Executive Compensation Data Providers", "Reference Check Services"], ["PE Portfolio Companies", "Public Corporations"],
    ["executive search", "retained headhunter", "c-suite recruiter", "leadership placement"])

add("fractional-cfo-financial-advisory", "Fractional CFO & Financial Advisory", "Professional Services & Consulting", "Financial Consulting", "B2B",
    "Financial advisory firms offering outsourced CFO leadership, financial modeling, cash flow forecasting, and fundraising support.",
    "Startups scaling past $1M ARR, SMBs without full-time CFO budget",
    ["Founder / CEO", "Managing Partner"],
    ["Referrals from CPA Firms & VCs", "LinkedIn Advisory Content", "Local Founder Events"],
    "Medium ($3k - $15k/mo retainer)", "2 to 6 weeks",
    ["Fractional CFO", "Financial Planning"], ["Financial Modeling Tools", "Accounting Software", "Tax Advisory Partners"], ["High-Growth Startups", "Established SMBs"],
    ["fractional cfo", "outsourced cfo", "financial modeling", "fundraising advisor"])

add("corporate-compliance-regulatory-agency", "Corporate Compliance & Regulatory Advisory", "Professional Services & Consulting", "Governance & Risk", "B2B",
    "Advisory firms guiding businesses through complex regulatory frameworks (GDPR, HIPAA, OSHA, SEC, ISO).",
    "Highly regulated industries including medical, financial, and manufacturing companies",
    ["Chief Compliance Officer", "General Counsel", "VP of Operations"],
    ["Industry Regulatory Seminars", "Direct Outreach to Risk Officers", "Partner Referrals"],
    "High ($15k - $100k engagement)", "2 to 5 months",
    ["Regulatory Compliance", "Risk Management"], ["Compliance Tracking Platforms", "Auditing Tools", "Legal Counsel"], ["Medical Manufacturers", "Fintech Companies"],
    ["compliance agency", "regulatory advisory", "gdpr consultant", "iso certification"])

add("supply-chain-logistics-advisory", "Supply Chain & Logistics Advisory", "Professional Services & Consulting", "Supply Chain", "B2B",
    "Consultants optimizing supply chain networks, inventory forecasting, vendor management, and freight routes.",
    "Manufacturers, importers, retail distributors, and e-commerce brands",
    ["VP of Supply Chain", "Director of Logistics", "COO"],
    ["Logistics Trade Shows", "Case Studies on Cost Savings", "Direct Outbound"],
    "High ($20k - $150k project)", "2 to 6 months",
    ["Supply Chain", "Logistics Consulting"], ["Freight Management Software", "Warehouse Automation Providers"], ["Manufacturing Companies", "Retail Distributors"],
    ["supply chain consultant", "logistics advisory", "inventory optimization", "freight consulting"])

add("sustainability-esg-consulting-firm", "Sustainability & ESG Consulting Firm", "Professional Services & Consulting", "Corporate Sustainability", "B2B",
    "Consultancies assisting enterprises with Environmental, Social, and Governance (ESG) strategy, carbon accounting, and reporting.",
    "Public corporations, consumer brands, enterprise manufacturers under stakeholder pressure",
    ["Chief Sustainability Officer", "VP of ESG", "Investor Relations Lead"],
    ["ESG Conferences", "Carbon Footprint Audits", "Corporate CSR Reports"],
    "High ($25k - $200k engagement)", "3 to 6 months",
    ["ESG Consulting", "Corporate Sustainability"], ["Carbon Accounting Platforms", "Lifecycle Assessment Software"], ["Public Corporations", "Global Brands"],
    ["esg consultant", "sustainability advisory", "carbon footprint audit", "csr reporting"])

add("ma-advisory-boutique-investment-bank", "M&A Advisory & Boutique Investment Bank", "Professional Services & Consulting", "Mergers & Acquisitions", "B2B",
    "M&A advisors facilitating business buyouts, sell-side representation, valuation, and capital raising for SMBs.",
    "Business owners planning an exit, PE firms seeking add-on acquisitions",
    ["Business Owner / Founder", "PE Operating Partner"],
    ["Direct Mail to Business Owners", "Valuation Workshops", "CPA & Legal Networks"],
    "High ($50k - $500k+ success fee)", "6 to 18 months",
    ["Mergers & Acquisitions", "Investment Banking"], ["Data Room Providers", "Business Valuation Tools", "M&A Legal Firms"], ["Selling Business Owners", "Private Equity Groups"],
    ["ma advisor", "sell side M&A", "business broker", "boutique investment bank"])

add("public-relations-pr-agency", "Public Relations (PR) Agency", "Professional Services & Consulting", "Media Relations", "B2B",
    "PR agencies managing media coverage, press releases, crisis communications, and thought leadership placement.",
    "Brands launching major products, tech scaleups, high-profile executives",
    ["VP of Communications", "Chief Marketing Officer", "CEO"],
    ["Journalist Pitching", "Industry Media Awards", "Agency Pitch Competitions"],
    "Medium ($5k - $25k/mo retainer)", "1 to 3 months",
    ["Public Relations", "Media Communications"], ["Media Database Tools (MuckRack/Cision)", "Press Release Wire Services"], ["Tech Scaleups", "Consumer Goods Brands"],
    ["pr agency", "public relations firm", "media placement", "press outreach"])

add("intellectual-property-patent-consulting", "Intellectual Property & Patent Consulting", "Professional Services & Consulting", "IP Strategy", "B2B",
    "Specialists helping tech hardware, biotech, and software firms audit, register, and monetize patent portfolios.",
    "Biotech, Hardware startups, R&D labs, Inventive enterprises",
    ["Head of R&D", "Chief Legal Counsel", "Founder"],
    ["R&D Conference Networking", "Patent Landscape Reports", "Legal Partner Referrals"],
    "High ($10k - $80k per filing / audit)", "2 to 6 months",
    ["Intellectual Property", "Patent Law"], ["Patent Search Databases", "Foreign Filing Partners"], ["Biotech Firms", "Hardware Startups"],
    ["patent consultant", "intellectual property agency", "ip strategy", "patent audit"])

add("translation-localization-agency", "Translation & Localization Agency", "Professional Services & Consulting", "Language Services", "B2B",
    "Language service providers translating software, technical manuals, marketing copy, and legal documents for global expansion.",
    "Global enterprises, software companies, pharmaceutical brands",
    ["Localization Manager", "VP of International Expansion", "Marketing Lead"],
    ["Localization Conferences (LocWorld)", "Translation Memory Tool Integrations", "Inbound SEO"],
    "Medium ($5k - $50k per project / retainer)", "1 to 2 months",
    ["Translation Services", "Localization"], ["CAT Tools", "TMS Software", "Native Linguist Networks"], ["Global Software Firms", "Pharma Corporations"],
    ["translation agency", "localization provider", "multilingual translation", "software localization"])

add("corporate-event-planning-production", "Corporate Event Planning & Production Agency", "Professional Services & Consulting", "Event Management", "B2B",
    "Agencies designing, organizing, and executing large-scale corporate conferences, trade expos, and product launches.",
    "Enterprise corporations, trade associations, tech companies",
    ["VP of Field Marketing", "Event Director", "HR Operations Lead"],
    ["Corporate Event Showcases", "B2B Outreach to Event Directors", "Venue Partnerships"],
    "High ($30k - $300k+ event budget)", "3 to 9 months",
    ["Event Production", "Corporate Events"], ["Audio/Visual Suppliers", "Event Ticketing Platforms", "Catering Vendors"], ["Enterprise Tech Companies", "Trade Associations"],
    ["corporate event planner", "event production agency", "conference organizer", "trade show manager"])

add("risk-management-consultancy", "Risk Management Consultancy", "Professional Services & Consulting", "Corporate Risk", "B2B",
    "Advisors identifying operational, financial, geopolitical, and supply chain risks for mid-to-large corporations.",
    "Multi-national corporations, insurance underwriters, financial institutions",
    ["Chief Risk Officer (CRO)", "VP of Internal Audit", "CFO"],
    ["Industry Whitepapers", "Executive Roundtables", "Direct C-Suite Sales"],
    "High ($25k - $150k engagement)", "2 to 5 months",
    ["Risk Management", "Corporate Governance"], ["Risk Modeling Software", "Crisis Management PR Partners"], ["Multi-National Enterprises", "Financial Institutions"],
    ["risk management consultant", "corporate risk advisory", "enterprise risk management"])

add("change-management-consulting", "Change Management Consulting", "Professional Services & Consulting", "Organizational Change", "B2B",
    "Consultants helping companies navigate large software rollouts, corporate restructurings, or post-merger integrations.",
    "Enterprises undergoing major technological or organizational transformations",
    ["Chief Human Resources Officer", "VP of Transformation", "COO"],
    ["Executive Networking", "Transformation Case Studies", "Management Consultancies Referrals"],
    "High ($30k - $200k project)", "3 to 6 months",
    ["Organizational Change", "Corporate Transformation"], ["Employee Survey Tools", "Internal Communication Platforms"], ["Global Corporations", "Healthcare Networks"],
    ["change management consultant", "organizational transformation", "post merger integration"])

add("grant-writing-fundraising-agency", "Grant Writing & Fundraising Agency", "Professional Services & Consulting", "Non-Profit Advisory", "B2B",
    "Specialists crafting grant applications, foundation proposals, and capital campaigns for non-profits and research institutions.",
    "Non-profit organizations, educational institutions, municipal bodies, biotech research labs",
    ["Executive Director", "Director of Development", "Head of Research"],
    ["Non-Profit Conferences", "Grants Database Partnerships", "Targeted Email"],
    "Medium ($3k - $15k project / success fees)", "1 to 3 months",
    ["Grant Writing", "Non-Profit Advisory"], ["Grant Search Databases", "Donor CRM Platforms"], ["Non-Profits", "Research Universities"],
    ["grant writer", "fundraising consultant", "non profit grant writing", "foundation proposal"])

add("customer-experience-cx-consulting", "Customer Experience (CX) Consulting", "Professional Services & Consulting", "Customer Journey", "B2B",
    "Agencies auditing customer touchpoints, reducing churn, and optimizing CSAT/NPS scores across omnichannel platforms.",
    "B2C enterprises, SaaS companies, retail banks, telecommunications providers",
    ["Chief Customer Officer", "VP of Customer Success", "Head of Support"],
    ["CX Industry Summits", "NPS Benchmark Reports", "LinkedIn Outreach"],
    "High ($20k - $100k project)", "2 to 4 months",
    ["Customer Experience", "Customer Success"], ["Survey & Feedback Tools", "Journey Mapping Software"], ["Subscription Services", "Telecom Providers"],
    ["cx consultant", "customer experience agency", "nps optimization", "customer churn reduction"])

add("iso-certification-consultancy", "ISO Certification Consultancy", "Professional Services & Consulting", "Quality Standards", "B2B",
    "Consultants guiding manufacturing and technology companies to achieve ISO 9001, ISO 27001, or ISO 13485 certifications.",
    "Manufacturers, aerospace suppliers, software vendors needing standard certification",
    ["Quality Assurance Manager", "Plant Manager", "CTO"],
    ["Inbound Search (SEO)", "Industrial Supplier Networks", "Direct Outreach"],
    "Medium ($10k - $40k project)", "2 to 6 months",
    ["Quality Management", "ISO Certification"], ["Internal Audit Software", "Document Management Systems"], ["Precision Manufacturers", "SaaS Vendors"],
    ["iso 9001 consultant", "iso 27001 certification", "quality management agency", "iso auditor"])

add("outplacement-career-transition-services", "Outplacement & Career Transition Services", "Professional Services & Consulting", "HR Services", "B2B",
    "Providers supporting laid-off employees with career coaching, resume writing, and job placement sponsored by employers.",
    "Corporations undergoing downsizing or restructuring",
    ["VP of HR", "Chief People Officer", "Legal Counsel"],
    ["HR Executive Outbound", "Corporate Layoff Monitoring", "HR Associations"],
    "Medium ($1,500 - $5,000 per employee package)", "1 to 4 weeks",
    ["Career Transition", "Outplacement"], ["Career Coaching Staff", "Resume Builders", "Job Placement Platforms"], ["Downsizing Corporations", "Tech Enterprises"],
    ["outplacement services", "career transition agency", "severance career coaching", "corporate layoff support"])

add("sales-enablement-training-agency", "Sales Enablement & Training Agency", "Professional Services & Consulting", "Sales Operations", "B2B",
    "Agencies training sales teams, building sales playbooks, and optimizing sales tech stacks to improve win rates.",
    "B2B companies scaling their outbound and inbound sales forces",
    ["VP of Sales", "Chief Revenue Officer (CRO)", "Sales Enablement Director"],
    ["LinkedIn Sales Content", "Podcast Guesting", "Outbound Email"],
    "High ($15k - $75k engagement)", "1 to 3 months",
    ["Sales Training", "Sales Enablement"], ["Sales Engagement Platforms", "LMS Tools", "Call Recording Software"], ["B2B Tech Scaleups", "Professional Services"],
    ["sales training agency", "sales enablement consultant", "sales playbook development", "cro consulting"])

print(f"Total items so far: {len(items)}")

# --- 3. Construction, Building & Trades (20) ---
add("commercial-roofing-contractor", "Commercial Roofing Contractor", "Construction, Building & Trades", "Roofing Services", "B2B",
    "Contractors installing, repairing, and maintaining large-scale flat, TPO, and metal roofs for commercial buildings.",
    "Property managers, commercial building owners, real estate developers",
    ["Property Manager", "Facility Director", "General Contractor"],
    ["Local B2B Cold Outreach", "Google Local Services Ads", "Storm Damage Outbound"],
    "High ($20k - $250k+ per job)", "1 to 3 months",
    ["Commercial Construction", "Property Maintenance"], ["Roofing Material Distributors", "Safety Compliance Auditors"], ["Property Management Firms", "Industrial Parks"],
    ["commercial roofing", "tpo roofing", "flat roof repair", "roofing contractor"])

add("residential-roofing-contractor", "Residential Roofing Contractor", "Construction, Building & Trades", "Roofing Services", "B2C",
    "Roofing specialists offering roof replacement, asphalt shingle repair, and storm damage restoration for homeowners.",
    "Single-family homeowners, residential landlords",
    ["Homeowner", "Residential Landlord"],
    ["Door-to-door Canvas", "Google PPC Ads", "Direct Mail Postcards", "Meta Local Ads"],
    "Medium ($8k - $25k per roof)", "1 to 3 weeks",
    ["Residential Construction", "Home Improvement"], ["Insurance Adjusters", "Lumber/Shingle Suppliers"], ["Homeowners", "Real Estate Agents"],
    ["roof replacement", "roof repair", "asphalt shingles", "storm damage roofing"])

add("hvac-service-installation", "HVAC Service & Installation Contractor", "Construction, Building & Trades", "HVAC", "B2B / B2C",
    "Heating, ventilation, and air conditioning contractors providing maintenance subscriptions, system replacement, and emergency repair.",
    "Homeowners and commercial property operators requiring climate control",
    ["Homeowner", "Building Manager", "Facilities Director"],
    ["Local Radio/TV Ads", "Google PPC & LSA", "Annual Maintenance Plans"],
    "Medium ($5k - $40k per installation)", "1 to 4 weeks",
    ["HVAC", "Climate Control"], ["Equipment Distributors (Carrier/Trane)", "Fleet Vehicle Leasing"], ["Homeowners", "Commercial Office Buildings"],
    ["hvac contractor", "air conditioning repair", "heating installation", "furnace replacement"])

add("plumbing-piping-company", "Plumbing & Commercial Piping Company", "Construction, Building & Trades", "Plumbing", "B2B / B2C",
    "Licensed plumbing firms handling residential drain cleaning, pipe repiping, water heater installs, and commercial gas piping.",
    "Residential property owners, restaurants, commercial facilities",
    ["Homeowner", "Restaurant Manager", "Commercial Facility Director"],
    ["Emergency Local SEO", "Google LSA", "Yelp/Angie Listings"],
    "Medium ($500 - $15k+ per job)", "Immediate to 2 weeks",
    ["Plumbing", "Utilities Maintenance"], ["Plumbing Supply Wholesalers", "Excavation Contractors"], ["Residential Properties", "Commercial Kitchens"],
    ["plumbing company", "emergency plumber", "commercial piping", "water heater replacement"])

add("electrical-contracting-firm", "Electrical Contracting Firm", "Construction, Building & Trades", "Electrical", "B2B / B2C",
    "Electrical contractors performing wiring, panel upgrades, EV charger installs, and commercial lighting retrofits.",
    "Commercial developers, industrial plants, homeowners",
    ["General Contractor", "Plant Manager", "Homeowner"],
    ["B2B Builder Partnering", "Google Local Ads", "Electrical Trade Associations"],
    "Medium ($1k - $50k per contract)", "1 to 4 weeks",
    ["Electrical Engineering", "Construction Trades"], ["Electrical Wholesalers", "Utility Providers"], ["General Contractors", "EV Owners"],
    ["electrician contractor", "commercial electrical wiring", "ev charger installer", "panel upgrade"])

add("solar-panel-installation", "Solar Panel Installation & Energy Company", "Construction, Building & Trades", "Renewable Energy", "B2B / B2C",
    "Clean energy contractors designing and installing photovoltaic solar arrays, battery storage, and smart energy monitoring.",
    "Homeowners seeking lower electric bills, commercial facilities meeting sustainability targets",
    ["Homeowner", "Sustainability Director", "CFO"],
    ["Canvassing & Door-to-Door", "Targeted Social Ads", "Solar Marketplace Partnerships"],
    "High ($15k - $100k+ system cost)", "1 to 2 months",
    ["Renewable Energy", "Solar Technology"], ["Solar Inverter Manufacturers", "PE Financing Partners"], ["Residential Homeowners", "Commercial Facilities"],
    ["solar installation", "commercial solar panel", "battery backup", "solar contractor"])

add("commercial-general-contractor", "Commercial General Contracting Firm", "Construction, Building & Trades", "General Contracting", "B2B",
    "General contractors overseeing commercial tenant build-outs, ground-up retail construction, and office renovations.",
    "Commercial real estate developers, franchise chains, corporate enterprises",
    ["CRE Developer", "Director of Construction", "Franchise Regional Owner"],
    ["RFP Submissions", "CRE Developer Networking", "Industry Trade Shows"],
    "Enterprise ($100k - $5M+ per build)", "3 to 12 months",
    ["Commercial Construction", "Real Estate Development"], ["Subcontractors", "Architects", "Heavy Equipment Leasing"], ["Retail Chains", "Corporate Offices"],
    ["commercial general contractor", "tenant improvement contractor", "commercial buildout", "ground up construction"])

add("residential-custom-home-builder", "Residential Custom Home Builder", "Construction, Building & Trades", "Residential Building", "B2C",
    "Luxury home builders constructing high-end custom homes, luxury estates, and major residential additions.",
    "High-net-worth individuals, landowners, luxury homebuyers",
    ["High-Net-Worth Homebuyer", "Architect Partner", "Luxury Real Estate Agent"],
    ["Architect & Realtor Referral Networks", "Luxury Home Expos", "Instagram Showcase"],
    "Enterprise ($500k - $3M+ per home)", "6 to 18 months",
    ["Residential Building", "Luxury Real Estate"], ["Custom Millwork Shops", "Interior Designers", "Structural Engineers"], ["High-Net-Worth Individuals", "Landowners"],
    ["custom home builder", "luxury home construction", "custom home contractor", "architectural home builder"])

add("landscaping-hardscaping-company", "Landscaping & Hardscaping Company", "Construction, Building & Trades", "Outdoor Living", "B2B / B2C",
    "Outdoor design and build firms installing stone patios, retaining walls, irrigation systems, and commercial grounds maintenance.",
    "Homeowners wanting outdoor living spaces, HOA communities, commercial centers",
    ["Homeowner", "HOA Board President", "Commercial Property Manager"],
    ["Yard Signage", "Neighborhood Direct Mail", "Google Local PPC"],
    "Medium ($3k - $50k+ installation)", "1 to 4 weeks",
    ["Landscaping", "Outdoor Architecture"], ["Nursery Wholesalers", "Stone/Paver Suppliers"], ["Residential Estates", "HOA Communities"],
    ["landscaping contractor", "hardscaping company", "patio installer", "commercial grounds maintenance"])

add("commercial-painting-contractor", "Commercial Painting Contractor", "Construction, Building & Trades", "Painting Services", "B2B",
    "High-volume painting contractors providing exterior/interior painting, epoxy floor coating, and protective industrial coatings.",
    "Facility managers, general contractors, warehouse operators",
    ["Facility Manager", "General Contractor", "Property Manager"],
    ["Direct B2B Sales Outreach", "GC Partnering Directories", "Commercial Real Estate Expos"],
    "Medium ($10k - $80k per project)", "2 to 6 weeks",
    ["Painting Services", "Industrial Coatings"], ["Sherwin-Williams/PPG Commercial", "Scaffolding Suppliers"], ["Warehouses", "Shopping Centers"],
    ["commercial painting", "epoxy floor coating", "industrial painting contractor", "building repainting"])

add("kitchen-bath-remodeling", "Kitchen & Bath Remodeling Company", "Construction, Building & Trades", "Interior Remodeling", "B2C",
    "Specialized design-build remodeling contractors transforming kitchens, master bathrooms, and custom cabinetry.",
    "Homeowners investing in interior home upgrades and property value boost",
    ["Homeowner", "Interior Decorator"],
    ["Showroom Traffic", "Meta/Pinterest Visual Ads", "Home Improvement Shows"],
    "High ($20k - $100k project)", "1 to 3 months",
    ["Home Remodeling", "Interior Architecture"], ["Cabinet Manufacturers", "Countertop Fabricators", "Tile Suppliers"], ["Homeowners", "Real Estate Investors"],
    ["kitchen remodeling", "bathroom remodeling contractor", "custom cabinets", "home renovation"])

add("drywall-insulation-installer", "Drywall & Insulation Contracting Company", "Construction, Building & Trades", "Wall & Insulation", "B2B / B2C",
    "Subcontractors installing spray foam insulation, acoustic ceilings, and drywall hanging/finishing for new builds.",
    "General contractors, home builders, energy efficiency audit clients",
    ["General Contractor", "Home Builder", "Commercial Project Manager"],
    ["GC Subcontractor Bidding", "Energy Efficiency Rebate Networks", "Trade Cold Calls"],
    "Medium ($5k - $30k per project)", "1 to 3 weeks",
    ["Insulation", "Drywall Construction"], ["Spray Foam Suppliers", "Drywall Supply Houses"], ["Residential Builders", "Commercial GCs"],
    ["drywall contractor", "spray foam insulation", "drywall hanging finishing", "acoustic ceiling contractor"])

add("concrete-paving-contractor", "Concrete & Paving Contracting Firm", "Construction, Building & Trades", "Paving & Foundation", "B2B / B2C",
    "Heavy hardscape contractors pouring concrete foundations, commercial parking lots, asphalt paving, and stamped concrete.",
    "Commercial developers, municipalities, residential homeowners",
    ["Site Developer", "Municipal Project Director", "Commercial Property Manager"],
    ["B2B Bidding Marketplaces", "CRE Outreach", "Google Local Ads"],
    "High ($15k - $150k+ per contract)", "2 to 6 weeks",
    ["Concrete Construction", "Paving Trades"], ["Ready-Mix Concrete Suppliers", "Heavy Machinery Leasing"], ["Commercial Property Owners", "Municipalities"],
    ["concrete contractor", "commercial paving", "asphalt parking lot", "foundation pouring"])

add("demolition-site-preparation", "Demolition & Site Preparation Company", "Construction, Building & Trades", "Site Work", "B2B",
    "Excavation and demolition contractors clearing land, grading terrain, demolishing structures, and installing underground utilities.",
    "Land developers, civil engineering firms, commercial general contractors",
    ["Civil Engineer", "Land Developer", "General Contractor Lead"],
    ["Civil Bidding Portals", "Developer Relationship Sales", "Industry Networking"],
    "High ($25k - $200k+ site prep)", "1 to 3 months",
    ["Site Preparation", "Demolition"], ["Heavy Equipment Manufacturers (CAT/Deere)", "Hazardous Material Disposal"], ["Commercial Developers", "Civil Construction"],
    ["demolition contractor", "excavation site prep", "land grading company", "commercial land clearing"])

add("scaffolding-equipment-rental", "Scaffolding & Construction Equipment Rental", "Construction, Building & Trades", "Equipment Supply", "B2B",
    "Suppliers renting scaffolding rigs, aerial lifts, cranes, and heavy machinery to construction job sites.",
    "General contractors, masonry firms, window restoration contractors",
    ["Safety Director", "Construction Project Manager", "Jobsite Superintendent"],
    ["Jobsite Sales Rep Outreach", "Construction Directories", "Trade Expos"],
    "Medium ($2k - $25k/mo equipment lease)", "1 to 2 weeks",
    ["Construction Equipment", "Heavy Machinery"], ["Machinery Manufacturers", "Safety Equipment Distributors"], ["Commercial GCs", "Masonry Contractors"],
    ["scaffolding rental", "construction machinery lease", "aerial lift rental", "crane hire"])

add("window-door-replacement", "Window & Door Replacement Contractor", "Construction, Building & Trades", "Building Envelope", "B2B / B2C",
    "Contractors installing energy-efficient replacement windows, impact doors, and commercial storefront glass.",
    "Homeowners seeking lower energy costs, storm protection, and commercial building managers",
    ["Homeowner", "Commercial Building Manager"],
    ["Direct Mail Postcards", "Home Shows", "Google LSA & Meta Ads"],
    "Medium ($7k - $40k per job)", "2 to 4 weeks",
    ["Building Envelope", "Glass & Windows"], ["Window Manufacturers (Andersen/Marvin)", "Glass Fabricators"], ["Residential Homeowners", "Retail Storefronts"],
    ["replacement windows", "impact doors", "storefront glass installation", "window contractor"])

add("flooring-installation-company", "Flooring Installation & Refinishing Company", "Construction, Building & Trades", "Flooring Trades", "B2B / B2C",
    "Flooring contractors installing hardwood, polished concrete, luxury vinyl plank (LVP), and commercial carpeting.",
    "Homeowners remodeling, commercial offices, multi-family housing developers",
    ["Homeowner", "Multi-Family Property Manager", "Interior Designer"],
    ["Local Showroom Leads", "Google PPC Ads", "Designer Referral Networks"],
    "Medium ($3k - $30k job size)", "1 to 3 weeks",
    ["Flooring", "Interior Finishes"], ["Flooring Distributors", "Adhesive Manufacturers"], ["Homeowners", "Commercial Office Managers"],
    ["flooring contractor", "hardwood floor installation", "polished concrete", "commercial carpet installer"])

add("fire-protection-sprinkler", "Fire Protection & Sprinkler Systems Company", "Construction, Building & Trades", "Building Safety", "B2B",
    "Fire safety contractors engineering, inspecting, and installing commercial fire sprinkler networks and suppression systems.",
    "Commercial building owners, industrial plant managers, general contractors",
    ["Fire Safety Director", "Facility Engineer", "General Contractor"],
    ["Local Building Code Inspection Lists", "B2B Outbound", "GC Bidding"],
    "High ($15k - $120k contract)", "1 to 3 months",
    ["Fire Protection", "Building Safety"], ["Sprinkler Head Manufacturers", "Backflow Testing Equipment"], ["Warehouses", "High-Rise Buildings"],
    ["fire sprinkler contractor", "commercial fire protection", "fire suppression system", "building fire safety"])

add("pool-installation-maintenance", "Pool Installation & Maintenance Company", "Construction, Building & Trades", "Outdoor Recreation", "B2B / B2C",
    "Contractors designing custom inground concrete/fiberglass pools and offering recurring residential/resort pool care.",
    "Homeowners building luxury backyards, hotels, homeowners associations",
    ["Homeowner", "Hotel General Manager", "HOA Board Director"],
    ["Meta Visual Ads", "Local Search (Google Ads)", "Home & Garden Shows"],
    "High ($40k - $150k pool build)", "1 to 4 months",
    ["Pool Construction", "Outdoor Living"], ["Pool Chemical Suppliers", "Excavators", "Concrete Suppliers"], ["Luxury Homeowners", "Resorts & Hotels"],
    ["inground pool builder", "custom pool contractor", "pool maintenance service", "commercial pool repair"])

add("architectural-woodworking-millwork", "Architectural Woodworking & Millwork Firm", "Construction, Building & Trades", "Custom Woodwork", "B2B",
    "Custom woodshops fabricating architectural millwork, bespoke reception desks, wall paneling, and cabinetry for commercial spaces.",
    "Interior architects, commercial general contractors, luxury retail brands",
    ["Interior Architect", "Commercial GC Lead", "Retail Store Designer"],
    ["Architectural Firm Partnering", "Trade Showrooms", "Portfolio Pitching"],
    "High ($20k - $200k build)", "2 to 4 months",
    ["Millwork", "Architectural Design"], ["Exotic Hardwood Distributors", "CNC Router Suppliers"], ["Corporate Headquarters", "Luxury Retail Stores"],
    ["architectural millwork", "custom woodwork contractor", "commercial cabinetry", "bespoke reception desk"])

# --- 4. Healthcare, Medical & Wellness (20) ---
add("dental-practice-clinic", "Dental Practice & Specialty Clinic", "Healthcare, Medical & Wellness", "Dental Services", "B2C",
    "General dentistry, cosmetic dentistry, and dental implant centers providing preventive care, veneers, and oral surgery.",
    "Local residents, families, individuals needing restorative dental care",
    ["Patients", "Parents", "Seniors needing implants"],
    ["Google Local SEO", "Dental Direct Mailers", "Local Social Ads", "Insurance Networks"],
    "Medium ($300 - $15,000 per treatment plan)", "Immediate to 1 month",
    ["Dentistry", "Healthcare"], ["Dental Supply Distributors (Henry Schein)", "Dental Lab Partners"], ["Local Patients", "Families"],
    ["dental practice", "cosmetic dentist", "dental implants", "teeth whitening clinic"])

add("medical-spa-medspa", "Medical Spa (MedSpa) & Aesthetics Clinic", "Healthcare, Medical & Wellness", "Aesthetic Medicine", "B2C",
    "Physician-supervised aesthetic clinics providing Botox, dermal fillers, laser hair removal, and skin rejuvenation treatments.",
    "Demographics interested in non-invasive cosmetic procedures and anti-aging care",
    ["Self-Care Consumers", "Anti-Aging Clients", "Bridal Clients"],
    ["Instagram / TikTok Before-and-Afters", "Local Meta Ads", "Membership Rewards Programs"],
    "Medium ($500 - $4,000 per package)", "Immediate to 2 weeks",
    ["Aesthetic Medicine", "Wellness & Beauty"], ["Laser Device Manufacturers (Candela/InMode)", "Injectable Distributors"], ["Local Consumers", "Skincare Enthusiasts"],
    ["medspa", "botox clinic", "dermal filler medspa", "laser skin rejuvenation"])

add("physical-therapy-clinic", "Physical Therapy & Rehabilitation Clinic", "Healthcare, Medical & Wellness", "Rehabilitation", "B2C",
    "Outpatient clinics treating orthopedic injuries, post-surgical recovery, sports rehab, and chronic pain management.",
    "Injured athletes, post-op surgery patients, elderly individuals with mobility issues",
    ["Post-Op Patients", "Athletes", "Ortho Doctor Referrals"],
    ["Physician Referral Outreach", "Local SEO & Maps", "Community Sports Sponsorships"],
    "Medium ($1,000 - $3,000 per care plan)", "1 to 2 months",
    ["Physical Therapy", "Rehabilitation"], ["Rehab Equipment Manufacturers", "EMR Billing Platforms"], ["Local Patients", "Orthopedic Surgeons"],
    ["physical therapy clinic", "sports rehab", "post surgery physical therapy", "physiotherapy"])

add("chiropractic-clinic", "Chiropractic & Spine Wellness Clinic", "Healthcare, Medical & Wellness", "Chiropractic", "B2C",
    "Chiropractors providing spinal alignment, decompression therapy, sciatica treatment, and wellness adjustments.",
    "Individuals with back pain, posture issues, car accident injury victims",
    ["Back Pain Patients", "Personal Injury Victims", "Desk Workers"],
    ["Google Local Ads", "Personal Injury Attorney Referrals", "Social Video Content"],
    "Low to Medium ($500 - $3,000 treatment package)", "1 to 3 weeks",
    ["Chiropractic", "Holistic Health"], ["X-Ray Equipment Suppliers", "Spinal Decompression Table Vendors"], ["Local Residents", "Car Accident Victims"],
    ["chiropractor", "spinal decompression", "back pain clinic", "chiropractic adjustment"])

add("private-mental-health-practice", "Private Mental Health Practice & Therapy Clinic", "Healthcare, Medical & Wellness", "Mental Health", "B2C",
    "Group therapy practices offering psychotherapy, psychiatry, anxiety/depression treatment, and marriage counseling.",
    "Adults, couples, adolescents seeking mental health support",
    ["Individual Patients", "Couples", "Parents seeking child therapy"],
    ["Psychology Today Listings", "Google Organic Search", "Primary Care Doctor Referrals"],
    "Medium ($150 - $250/hr session)", "Ongoing (3 to 12 months)",
    ["Mental Healthcare", "Psychology"], ["Telehealth Software Platforms", "EHR Systems"], ["Individuals", "Couples"], ["private therapy practice", "psychotherapist", "mental health counselor", "psychiatrist clinic"])

add("home-healthcare-senior-care", "Home Healthcare & Senior Care Agency", "Healthcare, Medical & Wellness", "Senior Services", "B2B / B2C",
    "In-home non-medical caregiving and skilled nursing services for elderly or disabled individuals needing daily assistance.",
    "Adult children of aging parents, seniors wishing to age in place",
    ["Adult Children (Family Decision Makers)", "Hospital Discharge Planners"],
    ["Hospital Discharge Planner Outreach", "Senior Living Advisors", "Google Local Ads"],
    "Medium ($3k - $10k/mo care cost)", "1 to 3 weeks",
    ["Home Healthcare", "Elder Care"], ["Caregiver Management Software", "Background Check Services"], ["Elderly Patients", "Families"],
    ["home healthcare agency", "senior caregiving", "in home nurse", "elder care service"])

add("veterinary-hospital-clinic", "Veterinary Hospital & Animal Clinic", "Healthcare, Medical & Wellness", "Veterinary Care", "B2C",
    "Full-service animal hospitals offering pet wellness exams, surgery, vaccinations, and emergency pet care.",
    "Pet owners (dog and cat owners, exotic pet owners)",
    ["Pet Owners", "Dog/Cat Parents"],
    ["Google Maps / Local SEO", "Pet Boarding Partner Referrals", "Social Media Pet Tips"],
    "Medium ($200 - $3,000 per visit / surgery)", "Immediate",
    ["Veterinary Medicine", "Pet Health"], ["Pharma Distributors (Covetrus)", "Vet Diagnostic Equipment"], ["Pet Owners", "Local Animal Shelters"],
    ["veterinary clinic", "animal hospital", "vet surgeon", "pet emergency hospital"])

add("urgent-care-center", "Walk-In Urgent Care Center", "Healthcare, Medical & Wellness", "Urgent Care", "B2C",
    "Walk-in medical clinics treating non-life-threatening illness, minor injuries, X-rays, and occupational health testing.",
    "Local residents needing immediate non-emergency medical care without ER wait times",
    ["Injured Patients", "Sick Residents", "Employers needing drug tests"],
    ["High-Visibility Signage", "Google Urgent Care Ads", "Employer Occupational Health Contracts"],
    "Medium ($150 - $1,500 per visit)", "Immediate",
    ["Urgent Care", "Occupational Medicine"], ["Medical Lab Supplies", "Digital X-Ray Systems"], ["Walk-in Patients", "Local Employers"],
    ["urgent care clinic", "walk in medical center", "occupational health testing", "emergency clinic alternative"])

add("optometry-eye-care-practice", "Optometry & Eye Care Practice", "Healthcare, Medical & Wellness", "Vision Care", "B2C",
    "Eye care clinics offering comprehensive eye exams, prescription glasses, contact lenses, and dry eye treatment.",
    "Local residents, children, adults needing vision correction",
    ["Vision Patients", "Parents of School-Age Kids", "Seniors"],
    ["Vision Insurance Provider Portals", "Google Local Search", "Direct Mail Reminders"],
    "Medium ($200 - $1,200 per visit/glasses)", "Immediate to 2 weeks",
    ["Optometry", "Vision Care"], ["Eyewear Frame Wholesalers", "Optical Lens Labs"], ["Local Patients", "Corporate Vision Plan Holders"],
    ["optometrist practice", "eye doctor exam", "designer eyeglasses clinic", "contact lens provider"])

add("dermatology-clinic", "Medical & Surgical Dermatology Clinic", "Healthcare, Medical & Wellness", "Dermatology", "B2C",
    "Physician clinics treating skin cancer screenings, acne, eczema, psoriasis, and minor surgical excisions.",
    "Patients with clinical skin conditions or seeking annual mole checks",
    ["Dermatology Patients", "Skin Cancer Screening Patients"],
    ["Primary Care Referrals", "Google Organic Search", "Insurance Network Directories"],
    "Medium ($200 - $3,000 treatment cost)", "1 to 4 weeks",
    ["Dermatology", "Clinical Medicine"], ["Dermpath Labs", "Surgical Instrument Suppliers"], ["Patients", "General Practitioners"],
    ["dermatologist clinic", "skin cancer screening", "acne dermatologist", "surgical dermatology"])

add("acupuncture-holistic-health", "Acupuncture & Holistic Health Center", "Healthcare, Medical & Wellness", "Alternative Medicine", "B2C",
    "Holistic clinics providing acupuncture, cupping, herbal medicine, and naturopathic care for pain and stress.",
    "Wellness-conscious consumers, chronic pain sufferers seeking non-pharmaceutical relief",
    ["Chronic Pain Patients", "Holistic Wellness Seekers"],
    ["Local Google Search", "Wellness Workshops", "Integrative MD Referrals"],
    "Low to Medium ($100 - $1,500 series cost)", "1 to 2 weeks",
    ["Alternative Medicine", "Acupuncture"], ["Herbal Distributors", "Acupuncture Supply Houses"], ["Patients", "Yoga Studios"],
    ["acupuncture clinic", "holistic medicine", "naturopathic doctor", "cupping therapy"])

add("weight-loss-bariatric-clinic", "Medical Weight Loss & Bariatric Clinic", "Healthcare, Medical & Wellness", "Metabolic Health", "B2C",
    "Medical clinics providing GLP-1 weight loss programs, metabolic testing, nutrition coaching, and bariatric surgery.",
    "Adults struggling with obesity or metabolic health conditions",
    ["Weight Loss Clients", "Bariatric Surgery Candidates"],
    ["Google PPC & Social Video Ads", "Patient Transformation Stories", "Physician Referrals"],
    "High ($1,500 - $20,000 surgical/med program)", "1 to 3 months",
    ["Weight Loss", "Metabolic Medicine"], ["Compound Pharmacy Partners", "Body Composition Scale Makers"], ["Patients", "Insurance Providers"],
    ["medical weight loss clinic", "glp1 program provider", "bariatric surgery clinic", "weight loss doctor"])

add("telehealth-service-provider", "Virtual Telehealth Service Provider", "Healthcare, Medical & Wellness", "Digital Health", "B2C",
    "Direct-to-consumer virtual healthcare platforms offering online consultations, prescription renewals, and specialist care.",
    "Busy individuals wanting instant virtual doctor visits for minor ailments or ongoing prescriptions",
    ["Online Patients", "Remote Workers", "Uninsured Individuals"],
    ["Meta & Google Ads", "SEO Content Marketing", "Corporate Wellness Benefits Integration"],
    "Low to Medium ($50 - $300 per visit/subscription)", "Immediate",
    ["Telehealth", "Virtual Medicine"], ["HIPAA Video Platforms", "E-Prescribing Networks"], ["Consumers", "Employer Health Plans"],
    ["telehealth provider", "online doctor visit", "virtual consultation clinic", "prescription telehealth"])

add("mobile-phlebotomy-lab-testing", "Mobile Phlebotomy & Lab Testing Service", "Healthcare, Medical & Wellness", "Lab Services", "B2B / B2C",
    "Mobile healthcare providers dispatching phlebotomists to homes or offices for blood draws and specimen collection.",
    "Homebound patients, executive wellness programs, clinical trial participants",
    ["Homebound Seniors", "Corporate Wellness Directors", "Clinical Research Organizations"],
    ["Clinical Trial Partnerships", "Home Care Agency Outreach", "Google Local Ads"],
    "Medium ($100 - $600 per draw)", "1 to 3 days",
    ["Phlebotomy", "Diagnostic Testing"], ["Reference Diagnostic Labs (Quest/Labcorp)", "Medical Logistics Providers"], ["Patients", "Clinical Research Labs"],
    ["mobile phlebotomy", "home blood draw", "corporate lab testing", "specimen collection service"])

add("boutique-fitness-pilates-studio", "Boutique Fitness & Reformer Pilates Studio", "Healthcare, Medical & Wellness", "Fitness & Wellness", "B2C",
    "Boutique fitness centers offering group Reformer Pilates, HIIT, Lagree, or specialized barre classes.",
    "Fitness enthusiasts, young professionals, wellness conscious individuals",
    ["Pilates Enthusiasts", "Fitness Club Members"],
    ["Instagram Visual Content", "Introductory Class Discounts", "ClassPass Partnerships"],
    "Medium ($150 - $350/mo membership)", "Immediate to 1 week",
    ["Boutique Fitness", "Pilates"], ["Pilates Equipment Manufacturers (Balanced Body)", "Studio Software (Mindbody)"], ["Fitness Enthusiasts", "Local Residents"],
    ["pilates studio", "reformer pilates", "boutique fitness center", "lagree fitness studio"])

add("addiction-treatment-rehab-center", "Addiction Treatment & Rehab Facility", "Healthcare, Medical & Wellness", "Behavioral Health", "B2B / B2C",
    "Residential and outpatient rehabilitation centers offering medical detox, addiction therapy, and recovery care.",
    "Individuals suffering from substance abuse, families seeking intervention for loved ones",
    ["Family Members", "Patients", "Hospital Interventionists"],
    ["National Search PPC (LegitScript Certified)", "Physician & ER Referrals", "Alumni Networks"],
    "Enterprise ($15k - $60k per stay)", "Immediate to 2 weeks",
    ["Addiction Recovery", "Behavioral Health"], ["Detox Medication Suppliers", "Drug Testing Labs", "Behavioral Health EHRs"], ["Patients", "Insurance Carriers"],
    ["addiction rehab center", "substance abuse treatment", "medical detox facility", "outpatient addiction rehab"])

add("sleep-medicine-clinic", "Sleep Medicine & CPAP Therapy Clinic", "Healthcare, Medical & Wellness", "Sleep Health", "B2B / B2C",
    "Specialized clinics diagnosing sleep apnea, conducting sleep studies (PSG), and fitting CPAP/oral appliances.",
    "Patients with chronic snoring, sleep apnea, or daytime fatigue",
    ["Sleep Apnea Patients", "ENT & Primary Care Referrals"],
    ["Primary Care MD Outreach", "Google Organic Search", "Sleep Apnea Awareness Ads"],
    "Medium ($1,000 - $4,000 study/device)", "2 to 4 weeks",
    ["Sleep Medicine", "Pulmonology"], ["CPAP Manufacturers (ResMed/Philips)", "Home Sleep Test Suppliers"], ["Patients", "Primary Care Doctors"],
    ["sleep medicine clinic", "sleep study center", "cpap clinic", "sleep apnea doctor"])

add("orthodontic-practice", "Orthodontic Practice & Invisalign Center", "Healthcare, Medical & Wellness", "Orthodontics", "B2C",
    "Orthodontists providing metal braces, clear ceramic braces, and Invisalign clear aligners for kids and adults.",
    "Parents of teenagers, adults wanting straight teeth and smile makeovers",
    ["Parents of Teens", "Adult Invisalign Candidates"],
    ["General Dentist Referrals", "Local Social Ads", "School Community Sponsorships"],
    "High ($3,000 - $7,000 treatment cost)", "1 to 3 weeks",
    ["Orthodontics", "Cosmetic Dentistry"], ["Invisalign/Align Technology", "3D Intraoral Scanner Suppliers"], ["Teenagers", "Adult Patients"],
    ["orthodontist clinic", "invisalign provider", "braces for teens", "clear aligners clinic"])

add("audiology-hearing-aid-clinic", "Audiology & Hearing Aid Clinic", "Healthcare, Medical & Wellness", "Hearing Health", "B2C",
    "Hearing care centers offering comprehensive diagnostic hearing tests, tinnitus relief, and hearing aid fitting.",
    "Seniors, aging adults experiencing hearing loss, individuals exposed to industrial noise",
    ["Senior Citizens", "Adult Children of Aging Parents"],
    ["Direct Mail Newspaper/Flyers", "Google Local Ads", "Senior Community Talks"],
    "High ($2,000 - $6,000 pair of hearing aids)", "1 to 3 weeks",
    ["Audiology", "Hearing Health"], ["Hearing Aid Manufacturers (Phonak/Oticon)", "Audiology Testing Equipment"], ["Seniors", "ENT Doctors"],
    ["audiologist clinic", "hearing aid center", "hearing test clinic", "tinnitus relief provider"])

add("compounding-pharmacy", "Specialty Compounding Pharmacy", "Healthcare, Medical & Wellness", "Pharmacy Services", "B2B / B2C",
    "Custom compounding pharmacies preparing specialized non-sterile and sterile medications, HRT, and vet meds.",
    "Patients requiring custom drug dosages/formulations, integrative medicine doctors, veterinarians",
    ["Prescribing Physicians", "Veterinarians", "HRT Patients"],
    ["Physician Office Sales Rep Visits", "Specialty Doctor Seminars", "Direct Medical Outreach"],
    "Medium ($100 - $1,000/mo custom prescriptions)", "1 to 2 weeks",
    ["Compounding Pharmacy", "Pharmaceuticals"], ["Bulk API Chemical Suppliers", "Cleanroom Equipment Vendors"], ["Integrative MDs", "Veterinarians"],
    ["compounding pharmacy", "custom medication pharmacy", "hrt compounding", "veterinary compounding"])

# --- 5. Marketing, Media & Creative Agencies (20) ---
add("seo-agency", "Search Engine Optimization (SEO) Agency", "Marketing, Media & Creative Agencies", "Search Marketing", "B2B",
    "Digital agencies specializing in organic ranking, technical SEO, link building, and content optimization.",
    "E-commerce stores, B2B SaaS, local service firms seeking inbound traffic",
    ["CMO", "Head of Growth", "Director of Marketing"],
    ["Inbound Organic Content", "SEO Audit Outreach", "LinkedIn Growth Posts"],
    "Medium ($2,500 - $15,000/mo retainer)", "1 to 2 months",
    ["Search Marketing", "Digital Marketing"], ["Ahrefs/SEMrush Platforms", "Link Building Outsource Networks"], ["E-commerce Brands", "B2B Software Companies"],
    ["seo agency", "search engine optimization", "technical seo consultant", "link building agency"])

add("ppc-paid-media-agency", "Pay-Per-Click (PPC) & Paid Media Agency", "Marketing, Media & Creative Agencies", "Paid Acquisition", "B2B",
    "Performance marketing agencies managing Google Ads, Bing Ads, Meta Ads, and YouTube advertising campaigns.",
    "Companies needing predictable lead volume or immediate direct response sales",
    ["VP of Marketing", "Growth Lead", "E-commerce Director"],
    ["Free Ad Account Audits", "Case Studies", "LinkedIn Cold Email"],
    "Medium ($3,000 - $20,000/mo management fee)", "2 to 4 weeks",
    ["Paid Media", "Digital Advertising"], ["Ad Management Software", "Attribution Tracking Platforms"], ["High-Growth E-commerce", "Lead Gen Clients"],
    ["ppc agency", "google ads management", "paid search agency", "performance marketing"])

add("social-media-marketing-agency", "Social Media Marketing Agency (SMMA)", "Marketing, Media & Creative Agencies", "Social Media", "B2B",
    "Creative agencies managing organic social strategy, short-form video creation (Reels/TikTok), and community engagement.",
    "Consumer brands, lifestyle companies, local businesses building brand awareness",
    ["Social Media Manager", "Brand Manager", "CMO"],
    ["Instagram / TikTok Demos", "Social Proof Showcase", "Outbound DM Outreach"],
    "Medium ($2,000 - $10,000/mo retainer)", "1 to 3 weeks",
    ["Social Media Marketing", "Content Creation"], ["Social Scheduling Software", "Video Editing Freelancers"], ["Consumer Brands", "Local Restaurants"],
    ["smma", "social media agency", "tiktok content agency", "instagram growth agency"])

add("content-marketing-copywriting-agency", "Content Marketing & Copywriting Agency", "Marketing, Media & Creative Agencies", "Content Strategy", "B2B",
    "Agencies producing long-form blog posts, whitepapers, case studies, and email newsletter sequences.",
    "B2B tech companies, fintechs, professional service firms establishing thought leadership",
    ["Head of Content", "VP of Marketing", "Content Strategist"],
    ["Content Sample Portfolios", "LinkedIn Content", "Inbound Inquiries"],
    "Medium ($3,000 - $15,000/mo retainer)", "2 to 4 weeks",
    ["Content Marketing", "Copywriting"], ["AI Copy Assistance Software", "Freelance Writer Pools"], ["B2B SaaS Companies", "Consulting Firms"],
    ["content marketing agency", "b2b copywriting", "whitepaper writing", "thought leadership content"])

add("video-production-studio", "Full-Service Commercial Video Production Studio", "Marketing, Media & Creative Agencies", "Video Production", "B2B",
    "Production companies crafting high-end commercial ads, corporate brand films, product showcase videos, and mini-docs.",
    "Corporate brand marketing teams, ad agencies, product companies",
    ["Executive Producer", "Creative Director", "CMO"],
    ["Showreel Presentations", "Agency Partner Networking", "Direct Outbound"],
    "High ($10k - $100k per video shoot)", "1 to 2 months",
    ["Video Production", "Commercial Film"], ["Camera Gear Rental Houses", "VFX & Color Grading Artists"], ["Corporate Brands", "Ad Agencies"],
    ["video production studio", "commercial video agency", "brand video production", "corporate video studio"])

add("brand-strategy-design-studio", "Brand Strategy & Visual Identity Studio", "Marketing, Media & Creative Agencies", "Branding", "B2B",
    "Design studios creating brand positioning, logo identities, visual guidelines, and packaging design.",
    "Startups rebranding, consumer brands launching new products, corporate restructures",
    ["Founder", "VP of Brand", "Chief Marketing Officer"],
    ["Behance / Dribbble Showcases", "Design Awards", "Referrals"],
    "High ($15k - $80k per rebrand)", "2 to 4 months",
    ["Branding Design", "Visual Identity"], ["Font & Asset Licensing", "Packaging Prototype Printers"], ["D2C Brands", "Enterprise Tech Firms"],
    ["branding agency", "brand strategy studio", "logo design agency", "packaging design firm"])

add("influencer-creator-marketing-agency", "Influencer & Creator Marketing Agency", "Marketing, Media & Creative Agencies", "Influencer Marketing", "B2B",
    "Agencies managing influencer outreach, creator campaigns, contract negotiations, and UGC asset generation.",
    "D2C consumer brands, mobile app publishers, gaming studios",
    ["Head of Influencer Marketing", "CMO", "E-commerce Lead"],
    ["Case Studies on ROI", "Creator Network Pitching", "Cold Email to D2C Founders"],
    "Medium to High ($5,000 - $50,000/mo campaign)", "2 to 4 weeks",
    ["Influencer Marketing", "Creator Economy"], ["Influencer Database Tools (Modash/Grin)", "Talent Managers"], ["D2C Apparel Brands", "Beauty Companies"],
    ["influencer marketing agency", "ugc creator agency", "tiktok influencer agency", "creator campaign management"])

add("email-lifecycle-marketing-agency", "Email & Lifecycle Marketing Agency (Klaviyo Specialists)", "Marketing, Media & Creative Agencies", "Email Marketing", "B2B",
    "Specialty agencies designing email automations, SMS campaigns, loyalty flows, and churn-reduction strategies.",
    "E-commerce brands on Shopify/Klaviyo, SaaS platforms tracking user onboarding",
    ["Retention Manager", "Head of E-commerce", "CMO"],
    ["Klaviyo Audit Outreach", "Case Studies on Revenue Lift", "Shopify Partner Directory"],
    "Medium ($3,000 - $12,000/mo retainer)", "1 to 3 weeks",
    ["Email Marketing", "Customer Lifecycle"], ["Email Design Software", "SMS Marketing Platforms (Attentive)"], ["Shopify D2C Brands", "Subscription Box Businesses"],
    ["klaviyo agency", "email marketing agency", "ecommerce email retainer", "lifecycle marketing"])

add("podcast-production-distribution", "Podcast Production & Distribution Agency", "Marketing, Media & Creative Agencies", "Audio Media", "B2B",
    "Audio agencies editing, producing, launching, and syndicating corporate B2B podcasts and founder shows.",
    "B2B companies using podcasts for ABM networking and brand awareness",
    ["Head of Media", "VP of Content", "Executive Producer"],
    ["Sample Podcast Clips", "LinkedIn Outreach to Founders", "Inbound SEO"],
    "Medium ($2,500 - $8,000/mo production fee)", "2 to 4 weeks",
    ["Podcast Production", "Audio Media"], ["Podcast Hosting Platforms", "Audio Engineers"], ["B2B SaaS Companies", "Venture Capital Firms"],
    ["podcast production agency", "b2b podcast agency", "corporate podcast editor", "audio branding studio"])

add("performance-marketing-agency", "Data-Driven Performance Marketing Agency", "Marketing, Media & Creative Agencies", "Performance Growth", "B2B",
    "Full-funnel growth agencies combining paid ads, landing page design, conversion optimization, and analytics.",
    "High-growth scaleups, backed startups needing rapid customer acquisition",
    ["VP of Growth", "Chief Revenue Officer", "CMO"],
    ["Performance Case Studies", "Growth Audits", "LinkedIn Outbound"],
    "High ($5,000 - $30,000/mo + revenue share)", "2 to 4 weeks",
    ["Performance Marketing", "Growth Marketing"], ["Attribution Analytics Software", "Landing Page Builders"], ["VC Backed Scaleups", "E-commerce Brands"],
    ["performance marketing agency", "growth marketing agency", "full funnel marketing", "customer acquisition agency"])

add("ui-ux-design-product-studio", "UI/UX Design & Digital Product Studio", "Marketing, Media & Creative Agencies", "Digital Product Design", "B2B",
    "UI/UX agencies designing mobile app interfaces, complex web platforms, design systems, and wireframes.",
    "Software startups, enterprise product teams, digital platforms",
    ["Head of Product", "VP of Design", "CTO"],
    ["Dribbble / Figma Community Showcases", "Product Case Studies", "Design Network Referrals"],
    "High ($15k - $90k project)", "1 to 3 months",
    ["UI/UX Design", "Product Design"], ["Figma / Design Tools", "User Testing Platforms"], ["SaaS Companies", "Fintech Product Teams"],
    ["ui ux agency", "product design studio", "figma design agency", "app interface designer"])

add("3d-animation-vfx-studio", "3D Animation & Visual Effects (VFX) Studio", "Marketing, Media & Creative Agencies", "3D & VFX", "B2B",
    "Creative studios creating 3D product renders, CGI commercials, architectural walkthroughs, and visual effects.",
    "Product manufacturers, architectural firms, ad agencies",
    ["Creative Director", "Art Director", "Marketing Manager"],
    ["3D Showreels", "VFX Industry Portfolios", "Agency Partnerships"],
    "High ($15k - $120k per project)", "1 to 3 months",
    ["3D Animation", "Visual Effects"], ["Render Farm Providers", "Cinema4D/Maya/Blender Plugins"], ["Industrial Designers", "Ad Agencies"],
    ["3d animation studio", "cgi studio", "vfx studio", "3d product rendering"])

add("outdoor-billboard-advertising", "Outdoor & Billboard Advertising Agency", "Marketing, Media & Creative Agencies", "Out-of-Home Advertising", "B2B",
    "OOH agencies buying and managing digital billboards, transit ads, airport displays, and street furniture placements.",
    "Consumer brands launching nationwide awareness campaigns, local service brands",
    ["Director of Media Buying", "VP of Brand Marketing", "CMO"],
    ["Location Traffic Reports", "OOH Media Portfolios", "Direct Sales Outreach"],
    "High ($10k - $200k+ media spend)", "2 to 6 weeks",
    ["Out-of-Home Advertising", "Billboard Media"], ["Billboard Operator Networks (ClearChannel/Outfront)", "Location Data Analytics"], ["National Consumer Brands", "Law Firms"],
    ["billboard advertising agency", "ooh media agency", "digital billboard buying", "transit advertising"])

add("affiliate-marketing-agency", "Affiliate Marketing & Partner Management Agency", "Marketing, Media & Creative Agencies", "Affiliate Marketing", "B2B",
    "Agencies recruiting, managing, and scaling affiliate partners, publisher networks, and referral channels.",
    "E-commerce brands, digital subscription services, financial products",
    ["Head of Partnerships", "Affiliate Manager", "CMO"],
    ["Affiliate Network Relationships", "E-commerce Events", "Cold Outreach to Brands"],
    "Medium ($3,000 - $10,000/mo + % of revenue)", "2 to 4 weeks",
    ["Affiliate Marketing", "Partner Marketing"], ["Impact/CJ/ShareASale Platforms", "Publisher Networks"], ["D2C Brands", "Financial Publishers"],
    ["affiliate marketing agency", "partner management agency", "impact radius management", "affiliate growth agency"])

add("conversion-rate-optimization-agency", "Conversion Rate Optimization (CRO) Agency", "Marketing, Media & Creative Agencies", "CRO & Analytics", "B2B",
    "Data-driven agencies running A/B tests, user heatmaps, and landing page UX tweaks to boost website sales conversion.",
    "High-traffic e-commerce stores, B2B SaaS companies with heavy ad spend",
    ["Head of E-commerce", "VP of Digital Marketing", "Growth Director"],
    ["Free CRO Audits", "A/B Testing Case Studies", "LinkedIn Growth Outreach"],
    "High ($5,000 - $20,000/mo retainer)", "1 to 2 months",
    ["Conversion Optimization", "UX Analytics"], ["VWO / Optimizely / Hotjar Tools", "A/B Testing Developers"], ["High Traffic E-commerce Stores", "SaaS Websites"],
    ["cro agency", "conversion rate optimization", "ab testing agency", "landing page optimization"])

add("audio-production-sound-design", "Audio Production & Sound Design Studio", "Marketing, Media & Creative Agencies", "Audio Engineering", "B2B",
    "Sound studios creating sonic branding, commercial voiceovers, sound effects for games, and audio mix/mastering.",
    "Game dev studios, ad agencies, film producers, app creators",
    ["Audio Lead", "Creative Director", "Video Producer"],
    ["Audio Showreels", "Voice Talent Networks", "Agency Cold Outreach"],
    "Medium ($2,000 - $20,000 project)", "1 to 4 weeks",
    ["Sound Design", "Audio Engineering"], ["Voiceover Talent Agencies", "Audio Plugins / ProTools"], ["Ad Agencies", "Video Game Studios"],
    ["sound design studio", "sonic branding agency", "commercial audio production", "voiceover agency"])

add("commercial-photography-studio", "Commercial Photography Studio", "Marketing, Media & Creative Agencies", "Commercial Photography", "B2B",
    "Professional photographers capturing product studio shots, lifestyle fashion campaigns, corporate headshots, and architecture.",
    "Product brands, e-commerce stores, fashion labels, corporate firms",
    ["Art Director", "Brand Director", "E-commerce Manager"],
    ["Visual Portfolio Showcase", "Instagram Network", "Agency Outreach"],
    "Medium ($2,500 - $25,000 per shoot)", "1 to 2 weeks",
    ["Commercial Photography", "Product Photography"], ["Photo Studio Space Rentals", "Retouching Studios"], ["E-commerce Brands", "Fashion Retailers"],
    ["commercial photography studio", "product photography agency", "e-commerce photographer", "corporate headshot studio"])

add("event-marketing-experiential-agency", "Experiential & Event Marketing Agency", "Marketing, Media & Creative Agencies", "Experiential Marketing", "B2B",
    "Agencies building pop-up brand activations, trade show booths, interactive installations, and experiential brand campaigns.",
    "Major consumer brands, tech companies, beverage companies launching campaigns",
    ["Director of Experiential Marketing", "VP of Brand", "CMO"],
    ["Activation Video Recaps", "Brand Pitch Competitions", "Industry Trade Shows"],
    "High ($25k - $250k+ per activation)", "2 to 5 months",
    ["Experiential Marketing", "Brand Activations"], ["Fabrication Workshops", "Event Staffing Agencies"], ["Global Consumer Brands", "Enterprise Tech"],
    ["experiential marketing agency", "brand activation studio", "trade show booth design", "pop up event planner"])

add("direct-mail-marketing-agency", "Direct Mail & Print Marketing Agency", "Marketing, Media & Creative Agencies", "Offline Marketing", "B2B",
    "Agencies executing programmatic direct mail campaigns, high-end catalog mailings, and door hanger drops integrated with digital analytics.",
    "E-commerce brands seeking offline retargeting, local real estate brokers, home service companies",
    ["VP of Direct Marketing", "CMO", "Growth Manager"],
    ["Sample Mailer Kits", "Case Studies on Direct Mail ROI", "Digital Integration Pitching"],
    "Medium to High ($5,000 - $50,000 campaign spend)", "2 to 4 weeks",
    ["Direct Mail", "Print Marketing"], ["Commercial Printing Houses", "USPS Address Data Verification"], ["E-commerce Retargeting Brands", "Home Service Contractors"],
    ["direct mail agency", "programmatic direct mail", "print marketing agency", "postcard marketing"])

add("local-seo-gbp-management-agency", "Local SEO & Google Business Profile Agency", "Marketing, Media & Creative Agencies", "Local Search", "B2B",
    "Agencies helping multi-location businesses, clinics, and service contractors rank in the Google 3-Pack and map searches.",
    "Local multi-location franchises, medical practice networks, legal firms, home services",
    ["Local Marketing Director", "Franchise Marketing Manager", "Business Owner"],
    ["Free Audit Reports", "Local Map Rank Tracker Proof", "Cold Calling/Email"],
    "Medium ($1,000 - $5,000/mo retainer)", "1 to 3 weeks",
    ["Local SEO", "Google Business Profile"], ["Local Citation Networks (BrightLocal/Whitespark)", "Review Management Software"], ["Law Firms", "Medical Practice Chains"],
    ["local seo agency", "google business profile management", "map pack ranking agency", "multi location seo"])

# --- 6. Real Estate, Property & Facility Management (15) ---
add("residential-real-estate-brokerage", "Residential Real Estate Brokerage", "Real Estate, Property & Facility Management", "Real Estate Brokerage", "B2C",
    "Brokerages assisting home buyers and sellers with residential real estate transactions, market evaluations, and contract negotiations.",
    "Homebuyers, home sellers, real estate investors",
    ["Homebuyer", "Home Seller", "Property Investor"],
    ["Zillow/Realtor.com Leads", "Open Houses", "Local Farming Direct Mail", "Social Ads"],
    "High ($6k - $30k commission per sale)", "1 to 3 months",
    ["Real Estate Brokerage", "Residential Property"], ["MLS Software Systems", "Real Estate Photography/Videography"], ["Homebuyers", "Home Sellers"],
    ["real estate brokerage", "residential real estate agent", "realtor agency", "home listing agent"])

add("commercial-real-estate-brokerage", "Commercial Real Estate Brokerage", "Real Estate, Property & Facility Management", "Commercial Brokerage", "B2B",
    "Brokerages specializing in office, retail, industrial, and multi-family leasing, tenant representation, and property sales.",
    "Commercial landlords, corporate tenants, real estate investment firms",
    ["Commercial Landlord", "Corporate Real Estate Director", "CRE Investor"],
    ["CoStar/LoopNet Outbound", "Direct Cold Outreach to Business Owners", "CRE Networking Events"],
    "Enterprise ($15k - $200k+ commission)", "3 to 12 months",
    ["Commercial Real Estate", "CRE Brokerage"], ["CRE Data Platforms (CoStar)", "Title Companies"], ["Corporate Tenants", "Commercial Property Owners"],
    ["commercial real estate broker", "cre tenant representation", "commercial leasing agency", "industrial cre broker"])

add("residential-property-management", "Residential Property Management Company", "Real Estate, Property & Facility Management", "Property Management", "B2B / B2C",
    "Management firms taking care of tenant screening, rent collection, maintenance, and lease renewals for rental property owners.",
    "Individual real estate investors, out-of-state landlords, multi-family building owners",
    ["Property Owner", "Real Estate Investor", "HOA Director"],
    ["Investor Group Networking", "Google PPC Ads", "Direct Outbound to Landlords"],
    "Medium ($100 - $300/mo per unit management fee)", "1 to 3 weeks",
    ["Property Management", "Residential Leasing"], ["AppFolio / Buildium Platforms", "Maintenance Contractors"], ["Rental Property Owners", "Tenants"],
    ["property management company", "residential rental manager", "landlord tenant management", "multi family property manager"])

add("commercial-property-management", "Commercial Property Management Firm", "Real Estate, Property & Facility Management", "Commercial Management", "B2B",
    "Management companies overseeing operations, maintenance contracts, tenant relations, and financial reporting for office buildings and shopping centers.",
    "Commercial real estate REITs, institutional investors, office park owners",
    ["Asset Manager", "CRE Fund Manager", "Building Owner"],
    ["CRE Owner Outbound", "Industry Associations (BOMA)", "Referrals"],
    "High ($3k - $25k/mo per building)", "1 to 3 months",
    ["Commercial Property Management", "Facility Operations"], ["Janitorial & HVAC Vendors", "CRE Accounting Tools"], ["Office Building Owners", "Shopping Center REITs"],
    ["commercial property management", "office building manager", "retail center management", "facility operations firm"])

add("home-staging-interior-styling", "Home Staging & Interior Styling Firm", "Real Estate, Property & Facility Management", "Property Staging", "B2B / B2C",
    "Staging companies furnishing and decorating vacant homes to accelerate sales and maximize home seller listing price.",
    "Real estate agents, luxury home sellers, real estate flippers",
    ["Real Estate Agent", "Home Seller", "Real Estate Investor"],
    ["Realtor Relationship Sales", "Instagram Visual Portfolios", "Local Brokerage Presentations"],
    "Medium ($2,000 - $10,000 per staged home)", "1 to 2 weeks",
    ["Home Staging", "Interior Styling"], ["Furniture Warehouse Logistics", "Real Estate Photographers"], ["Luxury Home Sellers", "Realtors"],
    ["home staging company", "vacant home staging", "real estate staging", "interior styling for sellers"])

add("real-estate-appraisal-agency", "Real Estate Appraisal Agency", "Real Estate, Property & Facility Management", "Valuation", "B2B",
    "Licensed appraisers delivering certified property valuations for mortgage lenders, estate planning, and tax appeals.",
    "Mortgage lenders, banks, estate lawyers, tax appeal clients",
    ["Chief Appraiser", "Mortgage Underwriter", "Estate Attorney"],
    ["Bank & Credit Union Approved Lists", "Attorney Networking", "Direct Outbound"],
    "Medium ($400 - $3,000 per appraisal)", "1 to 2 weeks",
    ["Real Estate Valuation", "Property Appraisal"], ["Appraisal Data Software", "MLS Databases"], ["Mortgage Lenders", "Law Firms"],
    ["real estate appraiser", "commercial property appraisal", "home valuation service", "certified appraiser"])

add("title-settlement-services", "Title & Settlement Services Company", "Real Estate, Property & Facility Management", "Title Services", "B2B",
    "Title insurance companies managing title searches, escrow accounts, and property closing ceremonies.",
    "Real estate agents, mortgage lenders, real estate attorneys, home buyers",
    ["Real Estate Agent", "Mortgage Loan Officer", "Real Estate Attorney"],
    ["Realtor/Lender Relationship Marketing", "Co-hosted Educational Seminars", "Direct Outbound"],
    "Medium ($1,000 - $3,500 per closing)", "Immediate to 2 weeks",
    ["Title Insurance", "Escrow Services"], ["Title Underwriters (First American/Fidelity)", "Closing Software"], ["Home Buyers", "Mortgage Lenders"],
    ["title company", "escrow closing service", "title insurance provider", "settlement agent"])

add("home-inspection-service", "Residential & Commercial Home Inspection", "Real Estate, Property & Facility Management", "Property Inspection", "B2B / B2C",
    "Certified inspectors evaluating home foundation, roof, plumbing, and electrical systems prior to property purchase.",
    "Homebuyers under contract, real estate agents, commercial buyers",
    ["Homebuyer", "Realtor", "Commercial Property Buyer"],
    ["Realtor Office Presentations", "Google Local Ads & Reviews", "Real Estate Agent Partnering"],
    "Medium ($400 - $1,200 per inspection)", "Immediate to 1 week",
    ["Home Inspection", "Building Inspection"], ["Inspection Report Software (Spectora)", "Thermal Imaging Tools"], ["Homebuyers", "Real Estate Agents"],
    ["home inspection service", "certified home inspector", "commercial property inspection", "building inspection"])

add("commercial-cleaning-janitorial", "Commercial Cleaning & Janitorial Agency", "Real Estate, Property & Facility Management", "Facility Cleaning", "B2B",
    "Janitorial companies providing daily office cleaning, floor stripping/waxing, medical facility sanitization, and post-construction cleanup.",
    "Office building managers, medical practices, schools, warehouses",
    ["Facility Manager", "Office Manager", "Property Manager"],
    ["Cold Calling Office Managers", "Direct Mail to Local Businesses", "Google Local Ads"],
    "Medium ($1,000 - $15,000/mo retainer)", "1 to 3 weeks",
    ["Commercial Cleaning", "Janitorial Services"], ["Cleaning Chemical Suppliers", "Commercial Floor Buffer Vendors"], ["Corporate Offices", "Medical Clinics"],
    ["commercial cleaning company", "janitorial service", "office cleaning agency", "medical facility cleaning"])

add("vacation-rental-airbnb-management", "Vacation Rental & Airbnb Management Firm", "Real Estate, Property & Facility Management", "Short-Term Rental Management", "B2B / B2C",
    "Property managers optimizing short-term rental listings (Airbnb/VRBO), dynamic pricing, guest check-in, and turnovers.",
    "Vacation home owners, real estate investors seeking short-term rental yields",
    ["Vacation Home Owner", "Short-Term Rental Investor"],
    ["Direct Mail to Second-Home Owners", "Google Search Ads", "Local Realtor Referrals"],
    "Medium (15% - 30% of booking revenue)", "1 to 3 weeks",
    ["Short-Term Rentals", "Vacation Rental Management"], ["Turnover Cleaning Teams", "Dynamic Pricing Software (PriceLabs)"], ["Vacation Home Owners", "Travelers"],
    ["airbnb management company", "vacation rental manager", "short term rental management", "vrbo management"])

add("land-development-urban-planning", "Land Development & Urban Planning Consultancy", "Real Estate, Property & Facility Management", "Land Planning", "B2B",
    "Consultants guiding real estate developers through zoning approvals, land entitlement, environmental impact studies, and site master planning.",
    "Real estate developers, land investors, municipal authorities",
    ["Director of Entitlements", "Real Estate Developer", "Land Acquisition Manager"],
    ["Developer Networking", "Municipal Planning Conferences", "Direct Outbound"],
    "High ($20k - $150k project)", "2 to 6 months",
    ["Land Planning", "Urban Development"], ["GIS Software Providers", "Civil Engineering Partners"], ["Real Estate Developers", "Municipalities"],
    ["land development consultant", "urban planning firm", "zoning entitlement consultant", "master planning agency"])

add("self-storage-facility-operator", "Self-Storage Facility Business", "Real Estate, Property & Facility Management", "Storage Operations", "B2C / B2B",
    "Operators of climate-controlled storage units, RV/boat storage, and commercial inventory storage facilities.",
    "Individuals moving/downsizing, businesses storing equipment or records",
    ["Residential Renters", "Small Business Owners", "Moving Consumers"],
    ["High-Visibility Local Signage", "Google Local Search Ads", "Moving Company Partnerships"],
    "Low to Medium ($75 - $400/mo per unit)", "Immediate",
    ["Self-Storage", "Storage Operations"], ["Storage Management Software (SiteLink)", "Security System Providers"], ["Local Residents", "Small Businesses"],
    ["self storage facility", "climate controlled storage", "rv storage yard", "commercial storage units"])

add("real-estate-syndication-reit", "Real Estate Syndication & Private Fund", "Real Estate, Property & Facility Management", "Real Estate Investment", "B2B / B2C",
    "Private equity real estate firms pooling investor capital to buy commercial multi-family complexes, industrial parks, or retail centers.",
    "Accredited investors seeking passive real estate yield and tax benefits",
    ["Accredited Investor", "High-Net-Worth Individual", "Family Office Lead"],
    ["Investor Webinars", "Podcasts", "Financial Planner Partnerships", "Direct Investor Networking"],
    "High ($50,000 - $500,000 minimum investment)", "1 to 3 months",
    ["Real Estate Investment", "Private Equity"], ["Investor Relations Software (Juniper Square)", "CRE Legal Counsel"], ["Accredited Investors", "Family Offices"],
    ["real estate syndication", "private equity real estate", "multifamily investment fund", "reit fund manager"])

add("hoa-community-management", "HOA & Community Association Management Firm", "Real Estate, Property & Facility Management", "Community Management", "B2B",
    "Management agencies assisting Homeowners Associations (HOAs) and condo boards with dues collection, vendor management, and rule enforcement.",
    "HOA board of directors, condominium associations",
    ["HOA Board President", "Condo Association Treasurer"],
    ["Direct Outreach to HOA Boards", "Community Management Expos", "Board RFP Bidding"],
    "Medium ($1,500 - $10,000/mo management retainer)", "1 to 3 months",
    ["HOA Management", "Community Association"], ["HOA Management Software (VANTACA)", "Legal Counsel"], ["HOA Boards", "Condo Associations"],
    ["hoa management company", "condo association manager", "community management firm", "hoa accounting service"])

add("building-automation-smart-security", "Building Automation & Smart Security Solutions", "Real Estate, Property & Facility Management", "Building Tech", "B2B",
    "Integrators installing access control, CCTV surveillance, smart HVAC controls, and IoT sensor systems for commercial facilities.",
    "Commercial building owners, school districts, facility managers",
    ["Facility Security Director", "Chief Security Officer", "Building Owner"],
    ["Commercial Security Expos", "GC & Electrical Subordinate Partnerships", "Direct Sales Outbound"],
    "High ($10k - $150k project)", "1 to 3 months",
    ["Building Automation", "Commercial Security"], ["Access Control Hardware (Verkada/Brivo)", "CCTV Camera Wholesalers"], ["Commercial Buildings", "School Districts"],
    ["building automation system", "commercial access control", "security camera installation", "smart building integrator"])

# --- 7. Financial Services, Legal & Insurance (15) ---
add("wealth-management-financial-planning", "Wealth Management & Financial Advisory Firm", "Financial Services, Legal & Insurance", "Wealth Management", "B2C / B2B",
    "Fiduciary financial advisors providing portfolio management, retirement planning, tax optimization, and estate planning.",
    "High-net-worth individuals, pre-retirees, business owners selling companies",
    ["High-Net-Worth Client", "Pre-Retiree", "Business Owner"],
    ["Educational Retirement Webinars", "CPA & Attorney Referrals", "Local Community Dinners"],
    "High ($5,000 - $50,000+/yr AUM fee)", "1 to 3 months",
    ["Wealth Management", "Financial Advisory"], ["Custodian Platforms (Schwab/Fidelity)", "Financial Planning Software (eMoney)"], ["High-Net-Worth Individuals", "Retirees"],
    ["wealth management firm", "financial advisor", "fiduciary financial planner", "retirement planning firm"])

add("commercial-insurance-brokerage", "Commercial Insurance Brokerage", "Financial Services, Legal & Insurance", "Commercial Insurance", "B2B",
    "Brokers sourcing business insurance policies (General Liability, Workers Comp, Cyber, D&O, Property) for enterprise clients.",
    "Business owners, CEOs, CFOs across construction, manufacturing, and tech sectors",
    ["CFO", "Risk Manager", "Business Owner"],
    ["Direct B2B Cold Calling", "Industry Trade Association Networking", "Policy Audit Offers"],
    "High ($2,000 - $50,000+ commission retainer)", "1 to 3 months",
    ["Commercial Insurance", "Risk Underwriting"], ["Insurance Carriers (Travelers/Hartford)", "Risk Assessment Software"], ["Construction Companies", "Manufacturers"],
    ["commercial insurance broker", "business insurance agency", "workers comp insurance", "cyber liability insurance"])

add("personal-lines-insurance-agency", "Personal Lines Insurance Agency", "Financial Services, Legal & Insurance", "Personal Insurance", "B2C",
    "Independent agents selling auto, home, umbrella, and life insurance policies to individuals and families.",
    "Homeowners, auto owners, heads of households",
    ["Homeowner", "Auto Owner", "Family Decision Maker"],
    ["Real Estate & Mortgage Lender Referrals", "Google Local Ads", "Direct Mailers"],
    "Medium ($500 - $3,000 annual policy premiums)", "Immediate to 1 week",
    ["Personal Insurance", "Property & Casualty"], ["Insurance Carriers (Progressive/Allstate)", "Comparative Rater Tools"], ["Local Residents", "Families"],
    ["personal insurance agent", "home and auto insurance", "independent insurance agency", "life insurance broker"])

add("bookkeeping-accounting-firm", "Bookkeeping & Outsourced Accounting Firm", "Financial Services, Legal & Insurance", "Bookkeeping", "B2B",
    "Accounting practices handling monthly bookkeeping, bank reconciliations, accounts payable/receivable, and financial reporting.",
    "Small to mid-sized businesses, startups, professional service agencies",
    ["Business Owner", "Founder", "General Manager"],
    ["QuickBooks / Xero Advisor Directories", "Local Business Networking", "Content Marketing"],
    "Medium ($500 - $3,000/mo retainer)", "1 to 3 weeks",
    ["Bookkeeping", "Outsourced Accounting"], ["QuickBooks Online / Xero", "Receipt Management Software"], ["Small Businesses", "Agencies"],
    ["bookkeeping firm", "outsourced bookkeeping", "quickbooks online accountant", "monthly bookkeeping service"])

add("cpa-tax-advisory-firm", "CPA & Tax Advisory Firm", "Financial Services, Legal & Insurance", "Tax Advisory", "B2B / B2C",
    "Certified Public Accountants delivering tax return preparation, strategic tax mitigation planning, and IRS audit representation.",
    "High-income earners, business owners, corporations",
    ["Business Owner", "High-Net-Worth Individual", "Corporate Controller"],
    ["Client Referral Programs", "Local Search (Google Ads)", "Tax Saving Webinars"],
    "Medium to High ($1,500 - $15,000/yr tax fee)", "1 to 4 weeks",
    ["Tax Advisory", "CPA Services"], ["Tax Software (UltraTax/Drake)", "IRS Portal Tools"], ["Business Owners", "High Earners"],
    ["cpa firm", "tax advisory service", "tax planning accountant", "irs audit representation"])

add("corporate-business-law-firm", "Corporate & Business Law Firm", "Financial Services, Legal & Insurance", "Corporate Law", "B2B",
    "Attorneys advising companies on contract drafting, M&A transactions, corporate governance, shareholder agreements, and IP.",
    "Business founders, corporate executive teams, investors",
    ["CEO", "General Counsel", "Managing Partner"],
    ["Executive Referral Networks", "Legal Content Marketing", "PE / Investment Bank Referrals"],
    "High ($350 - $850/hr legal retainer)", "Ongoing",
    ["Corporate Law", "Business Legal Services"], ["Legal Practice Management Software (Clio)", "Document Assembly Tools"], ["Corporations", "Startups"],
    ["corporate law firm", "business attorney", "m&a lawyer", "contract lawyer"])

add("personal-injury-law-firm", "Personal Injury Law Firm", "Financial Services, Legal & Insurance", "Personal Injury Law", "B2C",
    "Trial lawyers representing victims of auto accidents, slip and falls, medical malpractice, and workplace injuries.",
    "Injured individuals seeking financial compensation from insurance companies",
    ["Injured Victim", "Accident Patient"],
    ["High-Budget Google PPC & LSA", "Billboard Advertising", "TV Commercials", "Medical Provider Referrals"],
    "Enterprise (33% - 40% contingency fee of settlement)", "3 to 18 months",
    ["Personal Injury", "Litigation Law"], ["Case Management Software (Filevine)", "Medical Record Retrieval Services"], ["Accident Victims", "Medical Patients"],
    ["personal injury lawyer", "car accident attorney", "medical malpractice firm", "injury litigation attorney"])

add("estate-planning-elder-law", "Estate Planning & Elder Law Practice", "Financial Services, Legal & Insurance", "Estate Law", "B2C",
    "Attorneys drafting wills, living trusts, power of attorney, asset protection, and probate administration.",
    "Seniors, parents with minor children, wealthy families protecting assets",
    ["Seniors", "Parents", "Wealthy Individuals"],
    ["Financial Advisor & CPA Referrals", "Local Estate Planning Seminars", "Google Local Search"],
    "Medium to High ($2,000 - $10,000 per estate plan)", "2 to 6 weeks",
    ["Estate Planning", "Elder Law"], ["Trust Drafting Software", "Probate Court Systems"], ["Families", "Seniors"],
    ["estate planning attorney", "living trust lawyer", "probate law firm", "elder law attorney"])

add("commercial-loan-brokerage", "Commercial Loan & Business Financing Brokerage", "Financial Services, Legal & Insurance", "Commercial Financing", "B2B",
    "Brokers securing SBA loans, commercial real estate mortgages, equipment financing, and lines of credit for SMBs.",
    "Business owners seeking expansion capital, real estate investors, franchise buyers",
    ["Business Owner", "CRE Investor", "Franchise Buyer"],
    ["B2B Direct Outreach", "Banker Referrals (Turned-down applicants)", "Financing Webinars"],
    "High (1% - 5% points on loan volume)", "1 to 3 months",
    ["Business Financing", "Commercial Lending"], ["Lender Networks (Banks/Alternative Lenders)", "Loan Application Software"], ["SMB Owners", "Real Estate Investors"],
    ["commercial loan broker", "sba loan broker", "business financing agency", "equipment lease broker"])

add("debt-collection-revenue-recovery", "Commercial Debt Collection & Revenue Recovery Agency", "Financial Services, Legal & Insurance", "Debt Recovery", "B2B",
    "Agencies recovering delinquent receivables, unpaid invoices, and charged-off accounts for businesses.",
    "Medical practices, commercial suppliers, B2B vendors, property management firms",
    ["Credit Manager", "CFO", "Accounts Receivable Lead"],
    ["Direct Mail to Accounts Receivable Departments", "B2B Cold Calling", "Credit Association Events"],
    "Medium (15% - 40% contingency on recovered debt)", "2 to 8 weeks",
    ["Debt Collection", "Accounts Receivable"], ["Skip Tracing Software", "Collection Management Software"], ["Medical Clinics", "Wholesale Distributors"],
    ["commercial debt collection", "b2b revenue recovery", "unpaid invoice collection", "debt recovery agency"])

add("payroll-processing-hr-advisory", "Payroll Processing & HR Advisory Service", "Financial Services, Legal & Insurance", "Payroll Services", "B2B",
    "Service providers managing employee payroll, tax withholdings, direct deposits, benefits administration, and HR compliance.",
    "Small to mid-sized employers wanting simplified payroll and tax filing",
    ["Business Owner", "HR Manager", "Payroll Administrator"],
    ["CPA Referrals", "Local Sales Rep Outreach", "Google Local Ads"],
    "Medium ($150 - $1,500/mo fee based on headcount)", "1 to 2 weeks",
    ["Payroll Processing", "HR Administration"], ["Payroll Software Platforms", "Time & Attendance Trackers"], ["Small Employers", "Growing Companies"],
    ["payroll processing service", "outsourced payroll company", "hr administration", "small business payroll"])

add("mortgage-brokerage-firm", "Mortgage Brokerage Firm", "Financial Services, Legal & Insurance", "Mortgage Lending", "B2C",
    "Independent mortgage brokers matching homebuyers with optimal conventional, FHA, VA, and jumbo home loans.",
    "Homebuyers purchasing property, homeowners refinancing mortgages",
    ["Homebuyer", "Homeowner refinancing"],
    ["Real Estate Agent Partnering", "Google Local Search", "Past Client Referral Campaigns"],
    "High ($3,000 - $12,000 commission per closed loan)", "1 to 2 months",
    ["Mortgage Lending", "Residential Loans"], ["Wholesale Lenders (UWM/Rocket Pro)", "Loan Origination Software"], ["Homebuyers", "Real Estate Agents"],
    ["mortgage broker", "home loan specialist", "refinance mortgage company", "fha loan broker"])

add("venture-capital-private-equity", "Venture Capital & Private Equity Firm", "Financial Services, Legal & Insurance", "Private Capital", "B2B",
    "Investment firms providing equity capital, strategic guidance, and buyout capital to high-growth startups or mature SMBs.",
    "Tech founders seeking Series A/B, business owners planning buyouts or growth capital",
    ["Startup Founder", "CEO", "Investment Banker"],
    ["Inbound Dealflow Pitching", "Founder Demo Days", "Investment Bank Networks"],
    "Enterprise ($1M - $50M+ equity investment)", "3 to 6 months",
    ["Private Equity", "Venture Capital"], ["Pitchbook / Crunchbase Data", "Legal Deal Counsel"], ["High Growth Startups", "Profitable SMBs"],
    ["venture capital firm", "private equity fund", "growth equity investor", "startup investor"])

add("merchant-cash-advance-lender", "Alternative Business Lender (MCA Provider)", "Financial Services, Legal & Insurance", "Alternative Finance", "B2B",
    "Financial companies providing rapid working capital advances based on daily credit card sales or bank deposits.",
    "SMB owners needing fast cash flow for inventory, payroll, or emergency equipment",
    ["Small Business Owner", "Restaurant Owner", "Retailer"],
    ["ISO / Broker Partner Networks", "Direct Outbound Telemarketing", "UCC-1 Lead Lists"],
    "Medium to High ($5,000 - $150,000 advance size)", "Immediate (< 48 hrs)",
    ["Alternative Finance", "Working Capital"], ["Bank Verification Software (Plaid)", "UCC Data Scraping Tools"], ["Restaurants", "Retail Stores"],
    ["merchant cash advance", "working capital lender", "fast business loan", "alternative business financing"])

add("forensic-accounting-fraud-investigation", "Forensic Accounting & Fraud Investigation Firm", "Financial Services, Legal & Insurance", "Forensic Accounting", "B2B",
    "CPAs and certified fraud examiners investigating embezzlement, partnership disputes, matrimonial asset searches, and corporate fraud.",
    "Litigation attorneys, corporate boards, insurance fraud departments, divorcing spouses",
    ["Litigation Attorney", "Board Audit Committee", "Corporate Counsel"],
    ["Law Firm Relationship Sales", "Expert Witness Portfolios", "Legal Seminars"],
    "High ($15k - $100k engagement)", "1 to 4 months",
    ["Forensic Accounting", "Fraud Investigation"], ["Data Extraction Tools", "Financial Audit Software"], ["Law Firms", "Corporate Boards"],
    ["forensic accounting firm", "fraud investigation cpa", "asset search accountant", "litigation support cpa"])

# --- 8. Retail, E-Commerce & Consumer Brands (20) ---
add("d2c-apparel-brand", "Direct-to-Consumer (D2C) Apparel Brand", "Retail, E-Commerce & Consumer Brands", "Apparel & Fashion", "B2C",
    "Consumer clothing brands selling directly via online storefronts using social media ads and influencer partnerships.",
    "Fashion-conscious consumers, niche demographic style shoppers",
    ["Gen Z / Millennial Shoppers", "Fashion Enthusiasts"],
    ["Meta / TikTok Ads", "Influencer Gifting Campaigns", "Email/SMS Retention Flows"],
    "Low to Medium ($50 - $250 average order value)", "Immediate (< 1 day)",
    ["Apparel", "E-Commerce"], ["Cut & Sew Manufacturers", "3PL Fulfillment Warehouses"], ["Online Shoppers", "Influencers"],
    ["d2c apparel brand", "online clothing store", "fashion e-commerce", "direct to consumer clothing"])

add("specialty-coffee-roaster", "Specialty Coffee Roaster & E-Commerce", "Retail, E-Commerce & Consumer Brands", "Food & Beverage", "B2C / B2B",
    "Artisanal coffee roasters selling single-origin beans online via subscription and wholesaling to cafes and offices.",
    "Coffee enthusiasts, local independent cafes, corporate offices",
    ["Coffee Aficionado", "Cafe Owner", "Office Manager"],
    ["Coffee Subscription Ads", "Local Cafe Wholesale Outreach", "SEO Content on Brewing"],
    "Low to Medium ($20 retail bag / $500/mo wholesale)", "Immediate to 2 weeks",
    ["Specialty Coffee", "Food & Beverage"], ["Green Coffee Importers", "Commercial Roasting Equipment"], ["Retail Consumers", "Independent Cafes"],
    ["specialty coffee roaster", "coffee subscription box", "wholesale coffee beans", "artisan coffee brand"])

add("craft-brewery-microbrewery", "Craft Brewery & Taproom", "Retail, E-Commerce & Consumer Brands", "Craft Beverage", "B2C / B2B",
    "Independent breweries producing craft beer, hard seltzers, and operating local taprooms and distributor sales.",
    "Local beer lovers, restaurants, liquor store distributors",
    ["Taproom Customer", "Bar Manager", "Beverage Distributor"],
    ["Taproom Events", "Instagram Local Ads", "Distributor Sales Representatives"],
    "Low to Medium ($15 taproom visit / $5k distributor order)", "Immediate to 1 month",
    ["Craft Brewery", "Beverage Manufacturing"], ["Hops & Grain Wholesalers", "Canning/Bottling Lines"], ["Local Taproom Guests", "Liquor Stores"],
    ["craft brewery", "microbrewery taproom", "local craft beer", "beer distributor brand"])

add("luxury-goods-jewelry-retailer", "Luxury Goods & Custom Jewelry Retailer", "Retail, E-Commerce & Consumer Brands", "Luxury & Jewelry", "B2C",
    "High-end jewelers crafting custom engagement rings, fine diamond jewelry, and luxury watches.",
    "Engagement couples, high-net-worth jewelry collectors",
    ["Engaged Couple", "Luxury Collector", "Gift Buyer"],
    ["Pinterest & Instagram Visual Ads", "Google Search Ads for Rings", "Local Showroom Appointments"],
    "High ($2,000 - $30,000 per purchase)", "1 to 6 weeks",
    ["Fine Jewelry", "Luxury Goods"], ["Diamond Importers", "Custom Jewelry CAD Designers"], ["Engaged Couples", "High-Net-Worth Individuals"],
    ["custom jeweler", "engagement ring store", "luxury jewelry brand", "diamond jeweler"])

add("organic-skincare-beauty-brand", "Organic Beauty & Skincare Brand", "Retail, E-Commerce & Consumer Brands", "Beauty & Cosmetics", "B2C",
    "Clean beauty brands formulating non-toxic skincare products, serums, and organic cosmetics sold online and in boutiques.",
    "Skincare conscious consumers, eco-friendly beauty shoppers",
    ["Clean Beauty Consumer", "Skincare Enthusiast"],
    ["UGC Creator Video Ads", "Beauty Blogger Reviews", "Subscription Box Placement"],
    "Medium ($40 - $180 cart size)", "Immediate (< 1 day)",
    ["Clean Beauty", "Cosmetics"], ["Cosmetic Contract Formulators", "Eco Packaging Suppliers"], ["Retail Consumers", "Boutique Retailers"],
    ["organic skincare brand", "clean beauty e-commerce", "natural cosmetics", "serum skincare line"])

add("pet-supplies-accessories-brand", "Pet Supplies & Accessories Brand", "Retail, E-Commerce & Consumer Brands", "Pet Products", "B2C",
    "Pet brands creating ergonomic dog harnesses, organic pet treats, orthopedic dog beds, and smart pet tech.",
    "Passionate pet owners treat their pets as family members",
    ["Dog/Cat Parent", "Pet Lover"],
    ["Meta / TikTok Pet Videos", "Pet Influencer Partnerships", "Amazon Storefront Marketing"],
    "Medium ($30 - $150 order value)", "Immediate",
    ["Pet Care", "Consumer Products"], ["Pet Product Manufacturers", "Amazon PPC Agencies"], ["Pet Owners", "Veterinary Clinics"],
    ["pet supplies brand", "dog accessories store", "organic pet treats", "orthopedic dog bed"])

add("gourmet-food-beverage-manufacturer", "Gourmet Food & Specialty Beverage Brand", "Retail, E-Commerce & Consumer Brands", "Specialty Foods", "B2C / B2B",
    "Artisanal food manufacturers producing hot sauces, gourmet chocolates, organic snacks, or botanical beverages.",
    "Foodies, specialty grocery stores, corporate gift buyers",
    ["Gourmet Food Shopper", "Specialty Grocery Buyer"],
    ["Trade Shows (Fancy Food Show)", "Amazon Launch", "Influencer Unboxing Videos"],
    "Low to Medium ($10 retail / $2k wholesale order)", "Immediate to 1 month",
    ["Specialty Food", "Consumer Packaged Goods (CPG)"], ["Co-Packers", "Food Safety Testing Labs"], ["Grocery Stores", "Retail Consumers"],
    ["gourmet food brand", "specialty hot sauce", "artisanal chocolate", "cpg food manufacturer"])

add("home-goods-decor-ecommerce", "Home Goods & Interior Decor E-Commerce", "Retail, E-Commerce & Consumer Brands", "Home & Living", "B2C",
    "Online home decor brands offering handcrafted rugs, lighting fixtures, ceramics, and wall art.",
    "Homeowners decorating spaces, interior design lovers",
    ["Homeowner", "Interior Design Enthusiast"],
    ["Pinterest Shopping Ads", "Instagram Decor Reels", "Email Design Catalogues"],
    "Medium ($100 - $800 average order)", "Immediate to 1 week",
    ["Home Goods", "Interior Decor"], ["Overseas Craft Manufacturers", "Freight Forwarders"], ["Homeowners", "Interior Designers"],
    ["home decor store", "online rug retailer", "modern lighting e-commerce", "interior home goods"])

add("fitness-sports-equipment-retailer", "Fitness & Sports Equipment Retailer", "Retail, E-Commerce & Consumer Brands", "Sports & Fitness", "B2C / B2B",
    "Brands selling home gym equipment, adjustable dumbbells, recovery boots, and specialized sports gear.",
    "Fitness enthusiasts, home gym owners, commercial gym operators",
    ["Home Gym Owner", "Crossfit Athlete", "Gym Manager"],
    ["YouTube Fitness Reviews", "Google Shopping Ads", "Fitness Creator Sponsorships"],
    "Medium to High ($150 - $2,500 system cost)", "1 to 2 weeks",
    ["Fitness Equipment", "Sports Goods"], ["Fitness Hardware Factories", "Heavy Freight Shipping Services"], ["Home Gym Buyers", "Commercial Gyms"],
    ["fitness equipment brand", "home gym equipment", "dumbbells retailer", "sports gear e-commerce"])

add("automotive-parts-accessories-ecommerce", "Automotive Parts & Performance E-Commerce", "Retail, E-Commerce & Consumer Brands", "Automotive Aftermarket", "B2C / B2B",
    "Online auto part stores selling performance exhaust systems, aftermarket wheels, off-road LED lights, and restoration parts.",
    "Car enthusiasts, off-road rig builders, DIY auto mechanics",
    ["Car Enthusiast", "Off-Road Driver", "Mechanic"],
    ["Automotive Forum Marketing", "YouTube Build Guides", "Google Search Ads for Part Numbers"],
    "Medium ($150 - $1,500 cart size)", "Immediate to 1 week",
    ["Automotive Aftermarket", "Auto Parts"], ["Auto Part Wholesalers", "Fitment Database Software"], ["Car Enthusiasts", "Independent Auto Shops"],
    ["auto parts e-commerce", "aftermarket car parts", "off road truck accessories", "performance exhaust store"])

add("wholesale-electronics-distributor", "Wholesale Electronics & Gadgets Distributor", "Retail, E-Commerce & Consumer Brands", "Electronics Wholesale", "B2B",
    "B2B distributors supplying refurbished smartphones, computer accessories, and consumer gadgets to retail stores and repair shops.",
    "Independent electronics repair shops, Amazon resellers, regional retail stores",
    ["Retail Store Owner", "Repair Shop Owner", "Amazon Seller"],
    ["B2B Wholesale Portals", "Direct Sales Outreach", "Electronics Trade Shows"],
    "High ($2,000 - $30,000 bulk order)", "1 to 2 weeks",
    ["Consumer Electronics", "Wholesale Distribution"], ["OEM Electronics Manufacturers", "Freight Carriers"], ["Electronics Repair Shops", "Retail Stores"],
    ["wholesale electronics", "bulk smartphone distributor", "electronics wholesaler", "gadget supplier"])

add("subscription-box-service-provider", "Subscription Box Service Provider", "Retail, E-Commerce & Consumer Brands", "Subscription Commerce", "B2C",
    "Curated monthly subscription box services delivering niche products (beauty, snacks, books, pet treats, gear).",
    "Niche hobbyists, gift givers, convenience shoppers",
    ["Subscription Box Subscriber", "Hobbyist"],
    ["Meta / TikTok Unboxing Ads", "Affiliate Review Sites", "Influencer Sponsorships"],
    "Low to Medium ($30 - $70/mo subscription)", "Immediate (< 1 day)",
    ["Subscription Commerce", "Consumer Packaged Goods"], ["Custom Box Printers", "Kitting & Assembly 3PLs"], ["Subscribers", "CPG Brand Partners"],
    ["subscription box service", "monthly curation box", "beauty subscription box", "niche subscription company"])

add("eco-friendly-sustainable-brand", "Eco-Friendly & Sustainable Products Brand", "Retail, E-Commerce & Consumer Brands", "Sustainable Goods", "B2C",
    "Brands manufacturing zero-waste household goods, compostable cleaning products, and plastic-free essentials.",
    "Environmentally conscious consumers, zero-waste lifestyle advocates",
    ["Eco-Conscious Shopper", "Zero-Waste Advocate"],
    ["Educational Eco Content", "Meta Ads", "Environmental Non-profit Partnerships"],
    "Medium ($30 - $120 order value)", "Immediate",
    ["Sustainable Products", "Eco-Friendly Commerce"], ["Bioplastic Formulators", "Compostable Packaging Suppliers"], ["Eco Shoppers", "Refill Shops"],
    ["sustainable products brand", "zero waste shop", "eco friendly cleaning", "plastic free goods"])

add("children-toys-educational-games", "Children's Toys & Educational Games Brand", "Retail, E-Commerce & Consumer Brands", "Toys & Games", "B2C",
    "Toy brands creating Montessori wood toys, STEM educational kits, and interactive children's games.",
    "Parents of young children, grandparents, elementary educators",
    ["Parent", "Grandparent", "Elementary Teacher"],
    ["Parenting Bloggers", "Pinterest Toy Gift Guides", "Amazon Ads"],
    "Medium ($30 - $150 kit cost)", "Immediate",
    ["Toys & Games", "Educational Products"], ["Wood/Plastic Toy Factories", "Child Safety Testing Labs"], ["Parents", "Schools"],
    ["educational toy brand", "montessori wooden toys", "stem learning kits", "childrens game company"])

add("custom-print-on-demand-store", "Custom Print-on-Demand (POD) E-Commerce", "Retail, E-Commerce & Consumer Brands", "Print-on-Demand", "B2C",
    "E-commerce stores selling custom printed t-shirts, mugs, wall art, and merch fulfilled automatically via POD suppliers.",
    "Meme enthusiasts, niche fanbase communities, gift shoppers",
    ["Niche Fanbase Shopper", "Gift Buyer"],
    ["Meta Niche Ads", "TikTok Viral Designs", "SEO for Niche Quotes"],
    "Low ($25 - $75 cart size)", "Immediate",
    ["Print on Demand", "E-Commerce"], ["POD Fulfillment Printers (Printify/Printful)", "Vector Designers"], ["Niche Consumers", "Gift Shoppers"],
    ["print on demand store", "custom t shirt e-commerce", "pod merch store", "custom printed goods"])

add("outdoor-camping-gear-brand", "Outdoor & Camping Gear Brand", "Retail, E-Commerce & Consumer Brands", "Outdoor Recreation", "B2C",
    "Brands manufacturing lightweight backpacking tents, sleeping pads, camp stoves, and hiking equipment.",
    "Backpackers, campers, outdoor adventure enthusiasts",
    ["Backpacker", "Outdoor Enthusiast", "Camper"],
    ["YouTube Gear Reviews", "Outdoor Influencer Trips", "SEO Hiking Guides"],
    "Medium to High ($80 - $600 equipment price)", "Immediate to 1 week",
    ["Outdoor Recreation", "Camping Equipment"], ["Technical Fabric Factories", "Product Field Testers"], ["Hikers & Campers", "Outdoor Retailers"],
    ["camping gear brand", "outdoor equipment store", "backpacking tents e-commerce", "hiking gear company"])

add("ergonomic-office-furniture-retailer", "Ergonomic Office Furniture Retailer", "Retail, E-Commerce & Consumer Brands", "Office Furniture", "B2C / B2B",
    "Direct-to-consumer and corporate retailers selling standing desks, ergonomic mesh chairs, and monitor arms.",
    "Remote tech workers, corporate office outfitters",
    ["Remote Worker", "Office Operations Manager", "Ergonomic Consultant"],
    ["Google Search Ads", "YouTube Workspace Setup Reviews", "B2B Office Outfitting Outreach"],
    "High ($400 - $2,000 per desk/chair setup)", "1 to 2 weeks",
    ["Ergonomic Furniture", "Office Supplies"], ["Furniture Component Factories", "Freight Shipping Services"], ["Remote Workers", "Corporate Offices"],
    ["standing desk brand", "ergonomic office chair", "office furniture retailer", "remote workspace gear"])

add("artisanal-bakery-confectionery", "Artisanal Bakery & Specialty Confectionery", "Retail, E-Commerce & Consumer Brands", "Bakery & Sweets", "B2C / B2B",
    "Specialty bakeries shipping gourmet cookies, macarons, custom cakes, and artisanal sourdough nationwide.",
    "Dessert lovers, corporate gift buyers, wedding event planners",
    ["Dessert Lover", "Corporate Gift Buyer", "Wedding Planner"],
    ["Instagram / TikTok Food Porn Videos", "Corporate Holiday Gift Mailers", "Local Showroom"],
    "Low to Medium ($40 retail box / $500 corporate order)", "Immediate to 1 week",
    ["Artisanal Bakery", "Confectionery"], ["Commercial Baking Suppliers", "Insulated Shipping Packaging"], ["Consumers", "Corporate Events"],
    ["artisanal bakery", "gourmet cookie shipping", "custom cake shop", "specialty confectionery"])

add("dietary-supplement-brand", "Nutraceutical & Dietary Supplement Brand", "Retail, E-Commerce & Consumer Brands", "Nutraceuticals", "B2C",
    "Supplement companies marketing vitamins, protein powders, nootropics, and wellness gummies.",
    "Health-conscious consumers, biohackers, athletes",
    ["Health Conscious Consumer", "Fitness Athlete", "Biohacker"],
    ["Meta / TikTok Ads", "Podcast Sponsorships", "Amazon Storefront Marketing"],
    "Medium ($40 - $120 monthly subscription)", "Immediate",
    ["Nutraceuticals", "Dietary Supplements"], ["Contract Supplement Manufacturers", "Third-Party Lab Testing Services"], ["Consumers", "Gyms"],
    ["dietary supplement brand", "nutraceutical e-commerce", "protein powder company", "nootropics brand"])

add("wine-spirits-distributor", "Craft Wine & Spirits Brand / Distillery", "Retail, E-Commerce & Consumer Brands", "Wine & Spirits", "B2C / B2B",
    "Boutique wineries, craft distilleries, and DTC wine clubs shipping small-batch bourbon, gin, or organic wine.",
    "Wine & spirits enthusiasts, upscale restaurants, liquor store buyers",
    ["Wine Club Member", "Spirits Enthusiast", "Beverage Director"],
    ["Wine Club Subscriptions", "Tasting Room Visits", "State Distributor Networks"],
    "Medium ($30 bottle / $200 quarterly shipment)", "Immediate to 2 weeks",
    ["Wine & Spirits", "Craft Distillery"], ["Glass Bottle Manufacturers", "Compliance Compliance Software (ShipCompliant)"], ["Consumers", "Restaurants"],
    ["craft distillery", "boutique winery", "dtc wine club", "small batch bourbon brand"])

# --- 9. Education, Coaching & Training (15) ---
add("executive-leadership-coaching", "Executive & Leadership Coaching Firm", "Education, Coaching & Training", "Executive Coaching", "B2B",
    "Executive coaches working 1-on-1 with CEOs, founders, and VPs to hone leadership, communication, and management skills.",
    "C-suite executives, high-potential managers, venture backed founders",
    ["CEO", "Founder", "VP of HR"],
    ["Executive Referral Networks", "LinkedIn Thought Leadership", "Corporate L&D Contracts"],
    "High ($5,000 - $25,000 per coaching package)", "1 to 2 months",
    ["Executive Coaching", "Leadership Development"], ["Assessment Tools (360 Feedback/Hogan)", "Coaching Platforms"], ["CEOs", "Enterprise Leadership Teams"],
    ["executive coach", "leadership coaching firm", "ceo coach", "management coaching"])

add("online-academy-digital-course", "Online Academy & Digital Course Creator", "Education, Coaching & Training", "E-Learning", "B2C",
    "Digital educators and academies selling cohort-based courses, video masterclasses, and skill certifications.",
    "Career switchers, professionals upskilling, hobbyists",
    ["Online Student", "Career Switcher"],
    ["YouTube Educational Content", "Webinar Funnels", "Meta Ad Retargeting"],
    "Medium ($200 - $2,000 per course)", "Immediate to 1 week",
    ["Digital Education", "E-Learning"], ["Course Platforms (Kajabi/Teachable)", "Community Tools (Circle)"], ["Online Learners", "Professionals"],
    ["online academy", "digital course creator", "cohort based course", "e-learning platform"])

add("coding-tech-bootcamp", "Coding & Tech Career Bootcamp", "Education, Coaching & Training", "Tech Training", "B2C / B2B",
    "Intensive bootcamps teaching full-stack software development, data science, UX design, and cybersecurity with job placement help.",
    "Adults seeking high-paying tech career transitions",
    ["Career Transitioner", "Bootcamp Applicant"],
    ["Google Search Ads", "Income Share Agreement (ISA) Offers", "Tech Event Sponsorships"],
    "High ($8,000 - $18,000 tuition cost)", "2 to 6 weeks",
    ["Tech Education", "Career Bootcamps"], ["LMS Platforms", "Employer Hiring Networks"], ["Students", "Tech Employers"],
    ["coding bootcamp", "software engineering bootcamp", "ux design bootcamp", "data science school"])

add("corporate-training-l-and-d", "Corporate Training & L&D Agency", "Education, Coaching & Training", "Corporate Training", "B2B",
    "Agencies developing and facilitating corporate workshops on DE&I, cybersecurity awareness, sales skills, and compliance.",
    "Enterprise HR departments, Chief Learning Officers",
    ["Chief Learning Officer", "VP of HR", "Corporate L&D Director"],
    ["B2B Outbound to HR Executives", "L&D Conference Booths", "Corporate Webinars"],
    "High ($10,000 - $60,000 enterprise contract)", "2 to 4 months",
    ["Corporate Training", "Learning & Development"], ["Instructional Designers", "Workshop Facilitators"], ["Corporations", "Government Agencies"],
    ["corporate training agency", "l&d workshops", "employee training provider", "corporate compliance training"])

add("k12-tutoring-academic-center", "K-12 Tutoring & Academic Enrichment Center", "Education, Coaching & Training", "Academic Tutoring", "B2C",
    "Learning centers offering 1-on-1 math, reading, science, and homework tutoring for elementary through high school students.",
    "Parents of students struggling in school or seeking academic acceleration",
    ["Parent", "K-12 Student"],
    ["Local Google Search", "School PTA Sponsorships", "Direct Mailers"],
    "Medium ($200 - $600/mo tutoring fee)", "Immediate to 1 week",
    ["K-12 Education", "Tutoring Services"], ["Curriculum Publishers", "Scheduling Software"], ["Parents", "K-12 Students"],
    ["tutoring center", "math tutor company", "k12 academic tutoring", "reading enrichment center"])

add("career-coaching-resume-writing", "Career Coaching & Resume Writing Service", "Education, Coaching & Training", "Career Services", "B2C",
    "Professional career coaches crafting ATS-optimized resumes, LinkedIn profiles, and interview preparation coaching.",
    "Job seekers, mid-career professionals aiming for promotions or career changes",
    ["Job Seeker", "Mid-Career Professional"],
    ["LinkedIn Organic Content", "Google Search Ads for Resume Writing", "TikTok Career Advice"],
    "Medium ($200 - $1,200 package price)", "Immediate to 1 week",
    ["Career Services", "Resume Writing"], ["ATS Scanning Software", "Career Coaches"], ["Job Seekers", "Professionals"],
    ["career coach", "resume writing service", "linkedin profile writer", "interview coaching"])

add("test-preparation-center", "SAT / ACT / GRE Test Preparation Center", "Education, Coaching & Training", "Test Prep", "B2C",
    "Specialized test prep centers helping high schoolers and college grads maximize SAT, ACT, GRE, LSAT, or MCAT scores.",
    "High school juniors/seniors applying to college, pre-med/pre-law students",
    ["Parent of High Schooler", "Pre-Law / Pre-Med Student"],
    ["High School Guidance Counselor Partnering", "Google Search Ads", "Free Practice Test Events"],
    "Medium to High ($500 - $3,500 course cost)", "1 to 3 weeks",
    ["Test Preparation", "Higher Education"], ["Practice Exam Software", "Tutor Staff"], ["Students", "Parents"],
    ["sat test prep center", "lsat tutor company", "act prep course", "mcat test preparation"])

add("music-arts-academy", "Music & Performing Arts Academy", "Education, Coaching & Training", "Arts Education", "B2C",
    "Private academies teaching piano, guitar, vocal lessons, acting, and musical theater to kids and adults.",
    "Parents encouraging arts education for kids, adult music hobbyists",
    ["Parent", "Adult Music Student"],
    ["Local Community Ads", "Recital Showcases", "Google Maps / Local SEO"],
    "Medium ($150 - $350/mo lesson fee)", "Immediate to 1 week",
    ["Music Education", "Performing Arts"], ["Instrument Wholesalers", "Sheet Music Publishers"], ["Kids & Adults", "Schools"],
    ["music academy", "piano lessons studio", "guitar instructor school", "performing arts academy"])

add("vocational-trade-certification-school", "Vocational & Trade Certification School", "Education, Coaching & Training", "Trade Education", "B2C / B2B",
    "Post-secondary trade schools certifying students in HVAC, welding, commercial truck driving (CDL), or electrician trades.",
    "High school grads preferring hands-on trades, adults seeking quick trade qualifications",
    ["Trade Student", "CDL Applicant", "Employer seeking apprentices"],
    ["Local TV & Radio Ads", "Google Search Ads", "Trade Employer Hiring Fairs"],
    "High ($4,000 - $15,000 tuition)", "2 to 4 weeks",
    ["Vocational Training", "Trade School"], ["Trade Equipment Suppliers", "Job Placement Coordinators"], ["Students", "Construction/Logistics Employers"],
    ["trade school", "cdl training academy", "hvac trade certification", "welding school"])

add("language-learning-institute", "Language Learning Institute & Virtual School", "Education, Coaching & Training", "Language Education", "B2C / B2B",
    "Language schools delivering conversational Spanish, English (ESL), Mandarin, or French classes for individuals and corporate expats.",
    "Expatriates, international business professionals, language hobbyists",
    ["Adult Language Learner", "Expat Professional", "Corporate HR Director"],
    ["Google Ads for Language Classes", "Corporate Expat Partnering", "Social Media Demos"],
    "Medium ($200 - $1,500 course fee)", "1 to 2 weeks",
    ["Language Education", "ESL Training"], ["Language Software", "Native Instructors"], ["Individuals", "Corporations"],
    ["language learning institute", "esl school", "spanish language academy", "corporate language training"])

add("personal-fitness-coaching-business", "Personal Fitness & Online Strength Coaching", "Education, Coaching & Training", "Fitness Coaching", "B2C",
    "Personal trainers offering 1-on-1 gym coaching or customized online workout and nutrition plans via apps.",
    "Individuals seeking weight loss, muscle gain, or athletic accountability",
    ["Fitness Client", "Gym Goer"],
    ["Instagram Fitness Transformation Posts", "Local Gym Referral Marketing", "TikTok Videos"],
    "Medium ($200 - $800/mo coaching fee)", "Immediate to 1 week",
    ["Fitness Coaching", "Personal Training"], ["Fitness App Software (Trainerize)", "Nutritional Databases"], ["Clients", "Local Gyms"],
    ["personal trainer", "online fitness coach", "strength training coach", "nutrition coaching"])

add("public-speaking-communication-institute", "Public Speaking & Communication Institute", "Education, Coaching & Training", "Communication Training", "B2B / B2C",
    "Institutes coaching executives, authors, and professionals in keynote speaking, media interviews, and elevator pitches.",
    "Executives, startup founders pitching investors, keynote speakers",
    ["Executive", "Startup Founder", "Keynote Speaker"],
    ["LinkedIn Video Pitches", "Executive Referrals", "PR Agency Partnerships"],
    "High ($3,000 - $15,000 coaching package)", "1 to 2 months",
    ["Public Speaking", "Communications"], ["Speech Coaches", "Media Training Studios"], ["Executives", "Founders"],
    ["public speaking coach", "executive communication training", "media training agency", "speechwriting consultant"])

add("early-childhood-daycare-center", "Early Childhood Education & Daycare Center", "Education, Coaching & Training", "Child Care", "B2C",
    "Licensed childcare centers providing infant care, toddler programs, and preschool early learning curriculum.",
    "Working parents with children aged 0 to 5 years",
    ["Working Parent", "Mother/Father"],
    ["Google Local Search / Maps", "Parent Tour Signups", "Community Neighborhood Ads"],
    "High ($1,000 - $2,500/mo per child)", "1 to 4 weeks",
    ["Early Childhood", "Childcare"], ["Early Learning Curriculum Providers", "Playground Suppliers"], ["Parents", "Young Children"],
    ["daycare center", "preschool learning center", "infant child care", "early childhood academy"])

add("flight-instruction-pilot-school", "Flight Instruction & Pilot School", "Education, Coaching & Training", "Aviation Education", "B2C",
    "Aviation academies offering Private Pilot Licenses (PPL), commercial flight training, and instrument ratings.",
    "Aspiring commercial pilots, aviation hobbyists",
    ["Student Pilot", "Aviation Enthusiast"],
    ["Discovery Flight Ads", "Local Airport Open Houses", "Aviation Forum Search Ads"],
    "Enterprise ($10,000 - $80,000 flight training)", "2 to 6 weeks",
    ["Aviation Training", "Flight School"], ["Aircraft Leasing Firms", "Flight Simulator Manufacturers"], ["Student Pilots", "Airlines"],
    ["flight school", "pilot training academy", "private pilot license school", "commercial aviation training"])

add("financial-literacy-trading-academy", "Financial Literacy & Options Trading Academy", "Education, Coaching & Training", "Financial Education", "B2C",
    "Educational platforms teaching stock trading, options strategies, real estate investing, or personal budgeting.",
    "Retail investors, individuals looking to generate passive income or trade markets",
    ["Retail Trader", "Individual Investor"],
    ["YouTube Live Webinars", "Social Proof P&L Content", "Meta Ad Funnels"],
    "Medium to High ($500 - $3,000 academy membership)", "Immediate to 1 week",
    ["Financial Education", "Trading Academies"], ["Trading Chart Software (TradingView)", "Community Discord Platforms"], ["Retail Investors", "Traders"],
    ["trading academy", "options trading course", "financial literacy school", "stock market education"])

# --- 10. Manufacturing, Supply Chain & Industrial (15) ---
add("custom-cnc-machining-parts", "Custom CNC Machining & Precision Parts Workshop", "Manufacturing, Supply Chain & Industrial", "Precision Machining", "B2B",
    "Machining workshops providing precision CNC milling, turning, rapid prototyping, and aerospace metal fabrication.",
    "Aerospace engineers, medical device hardware leads, automotive manufacturers",
    ["Mechanical Engineer", "Sourcing Manager", "VP of Manufacturing"],
    ["B2B Manufacturing Portals (ThomasNet/Xometry)", "CAD File Quote Outreach", "Trade Shows"],
    "High ($5,000 - $100,000 job order)", "2 to 6 weeks",
    ["Precision Machining", "Metal Fabrication"], ["CNC Machine Makers (Haas)", "Raw Metal Distributors"], ["Aerospace Defense", "Medical Hardware"],
    ["cnc machining shop", "precision machine shop", "metal prototyping manufacturer", "custom cnc parts"])

add("3pl-warehousing-provider", "Third-Party Logistics (3PL) & Warehousing Provider", "Manufacturing, Supply Chain & Industrial", "3PL & Warehousing", "B2B",
    "Logistics companies offering outsourced warehousing, pick-and-pack fulfillment, inventory management, and B2C shipping.",
    "E-commerce brands, importers, retail product manufacturers scaling fulfillment",
    ["VP of Logistics", "Head of E-Commerce Operations", "Founder"],
    ["Shopify 3PL Directory", "Inbound SEO Content on Fulfillment", "LinkedIn Cold Email"],
    "High ($5,000 - $50,000/mo fulfillment retainer)", "1 to 2 months",
    ["3PL Fulfillment", "Logistics Operations"], ["Warehouse Management Systems (WMS)", "Forklift & Racking Suppliers"], ["E-commerce Brands", "Importers"],
    ["3pl provider", "fulfillment warehouse", "outsourced warehousing", "pick and pack 3pl"])

add("freight-brokerage-logistics", "Freight Brokerage & Logistics Agency", "Manufacturing, Supply Chain & Industrial", "Freight Logistics", "B2B",
    "Freight brokers connecting commercial shippers with truckload (TL), less-than-truckload (LTL), and refrigerated carriers.",
    "Manufacturers, agricultural producers, retail distributors needing freight transportation",
    ["Shipping Manager", "Logistics Coordinator", "VP of Supply Chain"],
    ["Direct Cold Outbound Telemarketing", "Load Board Partnering (DAT)", "Shipper Directories"],
    "High ($1,500 - $8,000 per truckload shipment)", "Immediate",
    ["Freight Brokerage", "Logistics & Trucking"], ["Carrier Networks", "TMS Software Providers"], ["Manufacturing Plants", "Distributors"],
    ["freight broker", "truckload logistics company", "ltl freight agency", "freight shipping broker"])

add("custom-industrial-packaging-supplier", "Custom Industrial Packaging Supplier", "Manufacturing, Supply Chain & Industrial", "Packaging Manufacturing", "B2B",
    "Manufacturers designing custom corrugated boxes, protective foam inserts, and eco-friendly shipping materials.",
    "E-commerce brands, industrial equipment makers, food distributors",
    ["Packaging Engineer", "Supply Chain Lead", "Procurement Director"],
    ["Sample Box Request Outbound", "Packaging Expos (Pack Expo)", "Inbound SEO"],
    "High ($10,000 - $100,000 packaging order)", "2 to 4 weeks",
    ["Industrial Packaging", "Corrugated Manufacturing"], ["Paper Mill Suppliers", "Die Cutting Machine Makers"], ["E-commerce Wholesalers", "Industrial Component Makers"],
    ["custom packaging supplier", "corrugated box manufacturer", "industrial protective packaging", "custom shipping boxes"])

add("plastic-injection-molding-manufacturer", "Plastic Injection Molding Manufacturer", "Manufacturing, Supply Chain & Industrial", "Plastic Manufacturing", "B2B",
    "Contract manufacturers tooling custom molds and mass-producing plastic components for medical, automotive, and consumer goods.",
    "Product designers, hardware engineers, medical device companies",
    ["Product Development Manager", "Procurement Director", "Hardware Founder"],
    ["Tooling Quote Outreach", "Medical Device Expos", "Supplier Databases"],
    "Enterprise ($25,000 tooling + $100,000 production run)", "2 to 6 months",
    ["Plastic Manufacturing", "Injection Molding"], ["Resin Distributors", "Mold Tooling Shops"], ["Consumer Product Brands", "Medical Device Companies"],
    ["plastic injection molding", "custom mold manufacturer", "plastic parts factory", "contract plastic molding"])

add("industrial-equipment-maintenance", "Industrial Equipment Maintenance & Repair", "Manufacturing, Supply Chain & Industrial", "Industrial Maintenance", "B2B",
    "Field service technicians repairing hydraulic systems, conveyor belts, industrial compressors, and manufacturing machinery.",
    "Plant managers, factory operations leads, warehouse managers",
    ["Plant Manager", "Maintenance Director", "Factory Operations Lead"],
    ["Emergency Service Local Search", "Preventative Maintenance Subscriptions", "Direct Outbound"],
    "High ($2,000 - $30,000 service call / contract)", "Immediate to 2 weeks",
    ["Industrial Maintenance", "Machinery Repair"], ["Replacement Part Distributors", "Hydraulic Hose Suppliers"], ["Manufacturing Plants", "Distribution Centers"],
    ["industrial equipment repair", "factory machinery maintenance", "conveyor system service", "hydraulic repair company"])

add("electronics-contract-manufacturing", "Electronics Contract Manufacturing (EMS / PCB)", "Manufacturing, Supply Chain & Industrial", "Electronics Manufacturing", "B2B",
    "EMS providers delivering Printed Circuit Board Assembly (PCBA), surface mount technology (SMT), and box build assembly.",
    "IoT device startups, medical tech brands, automotive electronics makers",
    ["VP of Hardware", "Electrical Engineer", "Sourcing Lead"],
    ["PCB Quote Requests", "Electronics Expos", "Direct Outreach to Hardware Teams"],
    "Enterprise ($30,000 - $300,000 production run)", "1 to 3 months",
    ["Electronics Manufacturing", "PCBA Assembly"], ["Semiconductor Distributors", "SMT Machine Suppliers"], ["IoT Companies", "Hardware Startups"],
    ["pcb assembly manufacturer", "electronics contract manufacturing", "ems provider", "smt assembly factory"])

add("chemical-raw-materials-distributor", "Chemical & Raw Materials Distributor", "Manufacturing, Supply Chain & Industrial", "Chemical Wholesale", "B2B",
    "Distributors supplying specialty industrial chemicals, solvents, polymers, and raw ingredients to factories.",
    "Chemical manufacturers, pharmaceutical labs, cosmetic formulators, paint producers",
    ["Chemical Procurement Officer", "Formulation Chemist", "Plant Director"],
    ["Chemical Industry Trade Shows", "Direct Outbound Sales", "Spec Sheet Downloads"],
    "Enterprise ($20,000 - $250,000 bulk order)", "1 to 3 months",
    ["Chemical Distribution", "Raw Materials"], ["Chemical Producers (Dow/BASF)", "Hazardous Freight Haulers"], ["Paint Manufacturers", "Pharma Labs"],
    ["chemical distributor", "industrial solvent supplier", "raw material wholesaler", "specialty chemical supplier"])

add("sheet-metal-fabrication-workshop", "Sheet Metal Fabrication Workshop", "Manufacturing, Supply Chain & Industrial", "Metal Fabrication", "B2B",
    "Metal shops cutting, bending, laser cutting, and welding sheet metal enclosures, brackets, and structural framing.",
    "HVAC contractors, industrial enclosure buyers, architectural metal clients",
    ["Engineering Manager", "Production Coordinator", "GC Procurement Lead"],
    ["Laser Cutting Quote Portal", "Local Industrial Outbound", "Trade Bidding"],
    "High ($5,000 - $60,000 contract)", "2 to 4 weeks",
    ["Sheet Metal Fabrication", "Welding & Cutting"], ["Laser Cutter Suppliers (Bystronic)", "Steel/Aluminum Mills"], ["HVAC Manufacturers", "Enclosure Builders"],
    ["sheet metal fabrication", "laser cutting shop", "custom metal enclosures", "welding metal workshop"])

add("commercial-printing-large-format", "Commercial Printing & Large Format Graphics House", "Manufacturing, Supply Chain & Industrial", "Commercial Printing", "B2B",
    "Print shops manufacturing trade show banners, vehicle wraps, retail signage, packaging, and corporate brochures.",
    "Marketing directors, event coordinators, fleet operators, retail brands",
    ["Marketing Director", "Event Coordinator", "Fleet Operations Manager"],
    ["Sample Signage Outbound", "Google Local B2B Ads", "Agency Reseller Programs"],
    "Medium ($1,500 - $20,000 order size)", "1 to 2 weeks",
    ["Commercial Printing", "Large Format Signage"], ["Vinyl / Media Wholesalers", "Large Format Printer Makers (HP/Epson)"], ["Retail Brands", "Fleet Operators"],
    ["commercial printing house", "large format printing", "vehicle wrap company", "trade show banner printing"])

add("textile-garment-manufacturer", "Textile & Garment Contract Manufacturer", "Manufacturing, Supply Chain & Industrial", "Apparel Manufacturing", "B2B",
    "Apparel factories offering tech pack development, fabric sourcing, pattern making, and mass garment production.",
    "Apparel brands, uniform companies, merchandise labels",
    ["Apparel Designer", "Production Manager", "Brand Founder"],
    ["Tech Pack Submission Outreach", "Apparel Sourcing Expos (Texworld)", "Direct Outbound"],
    "High ($15,000 - $150,000 batch order)", "2 to 4 months",
    ["Textile Manufacturing", "Garment Production"], ["Fabric Mills", "Industrial Sewing Machine Suppliers"], ["Fashion Brands", "Uniform Companies"],
    ["garment manufacturer", "apparel contract factory", "clothing tech pack maker", "textile manufacturing plant"])

add("fleet-maintenance-repair-service", "Fleet Maintenance & Commercial Repair Service", "Manufacturing, Supply Chain & Industrial", "Fleet Maintenance", "B2B",
    "Mechanic operations servicing commercial van fleets, semi-trucks, delivery vehicles, and construction fleets.",
    "Delivery companies, logistics fleets, trade contractor fleets, municipal transport",
    ["Fleet Manager", "Operations Director", "Transportation Supervisor"],
    ["Fleet Audit Cold Calls", "Direct Mail to Commercial Fleet Owners", "Local SEO"],
    "High ($3,000 - $25,000/mo fleet maintenance contract)", "1 to 3 weeks",
    ["Fleet Maintenance", "Commercial Auto Repair"], ["Commercial Tire Distributors", "Diesel OEM Parts Suppliers"], ["Delivery Companies", "Logistics Fleets"],
    ["fleet maintenance service", "commercial truck repair", "van fleet mechanic", "diesel fleet maintenance"])

add("food-beverage-copacker", "Food & Beverage Contract Manufacturer (Co-Packer)", "Manufacturing, Supply Chain & Industrial", "Food Co-Packing", "B2B",
    "FDA-registered co-packers bottling, canning, and pouch-filling sauces, beverages, and packaged snacks for CPG brands.",
    "Emerging food & beverage brands, scaleup CPG companies",
    ["VP of Operations", "CPG Founder", "Supply Chain Director"],
    ["Co-Packer Directories", "Specialty Food Expos", "R&D Lab Referrals"],
    "Enterprise ($30,000 - $250,000 minimum run)", "2 to 6 months",
    ["Food Manufacturing", "Co-Packing"], ["Bottling/Canning Equipment Makers", "Ingredient Suppliers"], ["Beverage Brands", "Sauce Companies"],
    ["food copacker", "beverage contract manufacturer", "sauce bottling factory", "cpg copacking plant"])

add("commercial-recycling-waste-management", "Commercial Recycling & Waste Management", "Manufacturing, Supply Chain & Industrial", "Waste Management", "B2B",
    "Waste services providing dumpster rentals, commercial trash compaction, scrap metal recycling, and e-waste disposal.",
    "Manufacturing plants, construction sites, shopping centers, corporate campuses",
    ["Facilities Director", "EHS Manager", "Construction Superintendent"],
    ["Commercial Audit Outreach", "Local B2B Cold Outbound", "Google Local Ads"],
    "Medium to High ($1,000 - $15,000/mo waste contract)", "1 to 2 weeks",
    ["Waste Management", "Commercial Recycling"], ["Dumpster / Compactor Manufacturers", "Scrap Metal Refineries"], ["Industrial Plants", "Construction Sites"],
    ["commercial waste management", "dumpster rental company", "scrap metal recycling", "industrial waste disposal"])

add("robotics-industrial-automation-integrator", "Robotics & Industrial Automation Integrator", "Manufacturing, Supply Chain & Industrial", "Industrial Robotics", "B2B",
    "Engineering firms designing robotic arm assembly lines, automated guided vehicles (AGVs), and conveyor sorting systems.",
    "Automotive assembly plants, e-commerce fulfillment centers, food processing factories",
    ["VP of Automation", "Chief Engineer", "Plant Operations Director"],
    ["Robotics Expos (Automate)", "Industrial Engineering Case Studies", "Direct Outbound"],
    "Enterprise ($100,000 - $1,500,000+ system build)", "3 to 12 months",
    ["Industrial Robotics", "Factory Automation"], ["Robotic Arm Makers (FANUC/ABB)", "PLC System Coders"], ["Automotive Factories", "Fulfillment Centers"],
    ["robotics integrator", "industrial automation company", "robotic arm assembly system", "factory automation engineer"])

# --- 11. Hospitality, Food & Entertainment (10) ---
add("boutique-hotel-bed-and-breakfast", "Boutique Hotel & Bed & Breakfast", "Hospitality, Food & Entertainment", "Boutique Hospitality", "B2C",
    "Independently owned boutique hotels and historic inns offering personalized guest experiences and luxury rooms.",
    "Travelers seeking unique boutique accommodations vs corporate chain hotels",
    ["Leisure Traveler", "Vacationing Couple"],
    ["OTA Listings (Booking.com/Expedia)", "Instagram Travel Content", "Google Hotel Ads"],
    "Medium ($200 - $600/night room rate)", "Immediate",
    ["Boutique Hospitality", "Hotels"], ["Property Management Systems (Cloudbeds)", "Hospitality Linen Suppliers"], ["Travelers", "Tourists"],
    ["boutique hotel", "bed and breakfast inn", "luxury boutique lodge", "historic inn accommodation"])

add("corporate-wedding-catering-service", "Corporate & Wedding Catering Service", "Hospitality, Food & Entertainment", "Catering Services", "B2B / B2C",
    "Full-service catering companies providing gourmet menus, bar service, and event staffing for corporate galas and weddings.",
    "Bride & grooms, corporate event planners, non-profit gala committees",
    ["Corporate Event Planner", "Bride / Groom", "Gala Director"],
    ["Wedding Venue Preferred Vendor Lists", "Corporate Event Planner Outreach", "Tasting Events"],
    "High ($3,000 - $35,000 per event catering)", "1 to 6 months",
    ["Catering", "Event Services"], ["Commercial Kitchen Equipment", "Event Staffing Services"], ["Weddings", "Corporate Galas"],
    ["catering company", "wedding caterer", "corporate event catering", "gourmet buffet catering"])

add("event-venue-conference-center", "Event Venue & Conference Center Operator", "Hospitality, Food & Entertainment", "Event Venues", "B2B / B2C",
    "Venues hosting weddings, trade conventions, corporate retreats, and private parties.",
    "Wedding couples, event planners, trade associations, corporate meeting hosts",
    ["Event Planner", "Corporate Meeting Planner", "Engaged Couple"],
    ["Venue Directory Listings (The Knot/WeddingWire)", "Virtual Venue Tours", "Google Ads"],
    "High ($5,000 - $50,000 venue rental fee)", "2 to 12 months",
    ["Event Venues", "Hospitality"], ["AV Technical Suppliers", "Event Catering Partners"], ["Corporations", "Engaged Couples"],
    ["event venue rental", "conference center operator", "wedding venue venue", "corporate retreat facility"])

add("restaurant-franchise-operator", "Multi-Unit Restaurant Franchise Operator", "Hospitality, Food & Entertainment", "Restaurant Franchising", "B2C / B2B",
    "Multi-unit operators managing quick-service (QSR) or fast-casual restaurant franchise locations.",
    "Diners seeking fast-casual food, franchise brand licensors",
    ["Diner", "Local Customer"],
    ["Franchise Local PPC & Mobile App Rewards", "High Visibility Local Signage", "Local Delivery Apps"],
    "Low ($12 - $30 average check size)", "Immediate",
    ["Restaurant Franchising", "Foodservice"], ["POS System Providers (Toast)", "Food Distributors (Sysco/US Foods)"], ["Local Diners", "Franchise Licensors"],
    ["restaurant franchise operator", "fast casual restaurant", "qsr franchise chain", "multi unit restaurant operator"])

add("craft-cocktail-bar-lounge", "Craft Cocktail Bar & Lounge", "Hospitality, Food & Entertainment", "Nightlife & Bars", "B2C",
    "Speakeasy-style cocktail lounges serving artisanal mixology drinks, rare spirits, and small plates.",
    "Nightlife enthusiasts, date night couples, young professionals",
    ["Cocktail Enthusiast", "Date Night Couple"],
    ["Instagram / TikTok Mixology Videos", "Google Maps Reviews", "Local PR / Food Blogs"],
    "Low to Medium ($40 - $120 tab per guest)", "Immediate",
    ["Mixology", "Nightlife & Hospitality"], ["Spirits Distributors", "Bar Equipment Suppliers"], ["Nightlife Guests", "Event Groups"],
    ["craft cocktail bar", "speakeasy lounge", "mixology bar", "artisan cocktail lounge"])

add("luxury-travel-agency-tour-operator", "Luxury Travel Agency & Customized Tour Operator", "Hospitality, Food & Entertainment", "Travel & Tourism", "B2C",
    "Boutique travel advisors curating custom luxury vacations, safari itineraries, private jet charters, and villa rentals.",
    "High-net-worth individuals, honeymooners, luxury family vacationers",
    ["High-Net-Worth Traveler", "Honeymoon Couple"],
    ["Virtuoso Travel Network", "Instagram Travel Inspiration", "High-Net-Worth Client Referrals"],
    "High ($5,000 - $50,000+ trip cost)", "1 to 4 months",
    ["Luxury Travel", "Tourism"], ["Luxury Hotel Partners", "Private Jet / Yacht Brokers"], ["Luxury Travelers", "Honeymooners"],
    ["luxury travel agency", "custom tour operator", "bespoke vacation planner", "luxury travel advisor"])

add("ghost-kitchen-delivery-brand", "Ghost Kitchen & Virtual Restaurant Fleet", "Hospitality, Food & Entertainment", "Virtual Restaurants", "B2C",
    "Delivery-only restaurant concepts operating out of commercial commissary kitchens using DoorDash/UberEats.",
    "Convenience-oriented food delivery consumers",
    ["Delivery App User", "Late-Night Diner"],
    ["UberEats / DoorDash In-App Ads", "TikTok Local Food Promos", "Virtual Brand Aggregators"],
    "Low ($15 - $40 order size)", "Immediate",
    ["Ghost Kitchens", "Food Delivery"], ["Commissary Kitchen Facilities", "Delivery Aggregator Software"], ["Delivery Customers", "Kitchen Operators"],
    ["ghost kitchen brand", "virtual restaurant fleet", "delivery only food concept", "commissary kitchen brand"])

add("escape-room-entertainment-center", "Escape Room & Family Entertainment Center", "Hospitality, Food & Entertainment", "Experiential Entertainment", "B2C / B2B",
    "Immersive escape rooms, axe throwing venues, arcade bars, and indoor trampoline parks for group fun.",
    "Families, birthday parties, corporate team building groups",
    ["Party Organizer", "Corporate HR (Team Building)", "Young Adult Group"],
    ["Google Search Ads", "TripAdvisor Reviews", "Corporate Team Building Outbound"],
    "Medium ($30 per ticket / $1,000 private party rental)", "Immediate to 2 weeks",
    ["Experiential Entertainment", "Family Recreation"], ["Theme Prop Builders", "Ticketing & Booking Software"], ["Families", "Corporate Team Building Groups"],
    ["escape room venue", "family entertainment center", "corporate team building venue", "experiential amusement center"])

add("yacht-boat-charter-service", "Private Yacht & Boat Charter Service", "Hospitality, Food & Entertainment", "Marine Hospitality", "B2C / B2B",
    "Luxury boat charter companies offering private captained yacht cruises, sunset sails, and corporate harbor events.",
    "High-net-worth vacationers, bachelor/bachelorette parties, corporate hosts",
    ["Luxury Vacationer", "Corporate Party Host", "Charter Client"],
    ["Google Search Ads for Boat Charters", "Instagram Yacht Content", "Concierge Referrals"],
    "High ($1,500 - $15,000 per charter cruise)", "1 to 4 weeks",
    ["Yacht Charters", "Marine Recreation"], ["Marina Facilities", "Captains & Crew Staffing"], ["Luxury Tourists", "Corporate Groups"],
    ["yacht charter service", "private boat rental", "luxury catamaran cruise", "captained yacht charter"])

add("food-truck-fleet-operator", "Food Truck Fleet & Event Catering Operator", "Hospitality, Food & Entertainment", "Mobile Foodservice", "B2C / B2B",
    "Gourmet food truck operators catering corporate lunches, food truck festivals, weddings, and brewery pop-ups.",
    "Festival goers, corporate office park lunches, private event hosts",
    ["Event Coordinator", "Corporate Office Manager", "Festival Organizer"],
    ["Street Food App Listings", "Catering Outbound to Offices", "Instagram Food Videos"],
    "Medium ($12 lunch / $2,000 event catering package)", "Immediate to 2 weeks",
    ["Food Trucks", "Mobile Foodservice"], ["Commercial Vehicle Customizers", "Commissary Kitchens"], ["Festival Goers", "Corporate Office Parks"],
    ["food truck operator", "gourmet food truck catering", "mobile food vendor", "food truck fleet"])

# --- 12. Personal Services & Lifestyle (10) ---
add("interior-architecture-design-studio", "Interior Architecture & High-End Design Studio", "Personal Services & Lifestyle", "Interior Design", "B2C / B2B",
    "Residential and commercial interior designers orchestrating luxury space planning, custom furnishings, and renovations.",
    "High-net-worth homeowners, boutique commercial spaces, luxury developers",
    ["Luxury Homeowner", "Commercial Developer"],
    ["Architect & Builder Referrals", "Architectural Digest / Houzz Portfolios", "Instagram Visual Content"],
    "High ($15,000 - $150,000 design fee)", "1 to 6 months",
    ["Interior Design", "Architecture"], ["Custom Furniture Craftsmen", "Textile & Lighting Showrooms"], ["Luxury Homeowners", "Boutique Retailers"],
    ["interior design studio", "luxury interior designer", "residential space planning", "commercial interior architecture"])

add("event-wedding-photography-videography", "Event & Wedding Photography / Videography", "Personal Services & Lifestyle", "Event Media", "B2C",
    "Professional visual artists capturing weddings, high-end private galas, and milestone luxury celebrations.",
    "Engaged couples, gala committees, luxury event planners",
    ["Bride / Groom", "Luxury Event Planner"],
    ["Instagram / Pinterest Portfolios", "Wedding Planner Partnering", "The Knot / Style Me Pretty"],
    "Medium to High ($3,500 - $15,000 per wedding package)", "2 to 8 months",
    ["Wedding Photography", "Event Videography"], ["Camera Gear Vendors", "Album Printing Houses"], ["Engaged Couples", "Event Planners"],
    ["wedding photographer", "event videography studio", "luxury wedding cinematography", "bridal photographer"])

add("mobile-pet-grooming-spa", "Mobile Pet Grooming & Spa Van", "Personal Services & Lifestyle", "Pet Services", "B2C",
    "Custom equipped mobile vans providing door-to-door dog bathing, haircutting, nail trimming, and spa treatments.",
    "Busy pet owners wanting doorstep convenience without taking dogs to storefront salons",
    ["Dog Owner", "Busy Pet Parent"],
    ["Local Yard Signs & Vehicle Wraps", "Neighborhood Facebook Groups", "Google Maps / Local SEO"],
    "Medium ($80 - $200 per grooming session)", "Immediate to 1 week",
    ["Mobile Pet Grooming", "Pet Services"], ["Grooming Van Customizers", "Pet Shampoo Wholesalers"], ["Pet Owners", "Dog Parents"],
    ["mobile pet grooming", "doorstep dog grooming van", "pet spa service", "mobile dog wash"])

add("luxury-car-detailing-studio", "High-End Car Detailing & Paint Protection Studio", "Personal Services & Lifestyle", "Automotive Detailing", "B2C",
    "Specialty auto studios offering ceramic coating, paint protection film (PPF), paint correction, and luxury interior detailing.",
    "Exotic car owners, luxury vehicle enthusiasts, car collectors",
    ["Exotic Car Owner", "Luxury Auto Enthusiast"],
    ["Car Club Sponsorships", "Instagram Before-and-After Videos", "Dealership Referrals"],
    "Medium to High ($500 - $5,000 per PPF/ceramic package)", "1 to 2 weeks",
    ["Automotive Detailing", "Ceramic Coating"], ["PPF Film Manufacturers (XPEL/3M)", "Detailing Chemical Suppliers"], ["Exotic Car Owners", "Auto Collectors"],
    ["car detailing studio", "ceramic coating applicator", "paint protection film ppf", "luxury auto detailer"])

add("personal-concierge-lifestyle-management", "Personal Concierge & Lifestyle Management", "Personal Services & Lifestyle", "Concierge Services", "B2C",
    "Private lifestyle managers handling personal errands, travel booking, luxury reservations, and estate management for UHNW individuals.",
    "Ultra-high-net-worth individuals, busy C-suite executives, celebrities",
    ["Ultra-High-Net-Worth Individual", "Busy C-Suite Executive"],
    ["Private Client Referrals", "Family Office Partnering", "Executive Assistant Outreach"],
    "High ($3,000 - $15,000/mo personal retainer)", "1 to 2 months",
    ["Personal Concierge", "Lifestyle Management"], ["Private Jet/Yacht Brokers", "Luxury Event Ticketing"], ["UHNW Individuals", "Executives"],
    ["personal concierge service", "lifestyle management firm", "uhnw personal assistant", "private estate manager"])

add("private-chauffeur-limo-service", "Private Executive Chauffeur & Limo Service", "Personal Services & Lifestyle", "Executive Transport", "B2B / B2C",
    "Transport companies providing luxury SUV, limousine, and executive Sprinter van airport transfers and event transit.",
    "Corporate executives, luxury travelers, event VIPs, wedding parties",
    ["Corporate Travel Manager", "Executive", "Wedding Planner"],
    ["Corporate Hotel Partnerships", "Google Search Ads for Airport Transit", "Travel Agent Referrals"],
    "Medium ($150 - $2,500 charter service)", "Immediate to 1 week",
    ["Executive Chauffeur", "Limo Transport"], ["Vehicle Fleet Leasing", "Dispatch Management Software"], ["Corporate Executives", "VIP Travelers"],
    ["private chauffeur service", "executive limo transportation", "airport luxury transfer", "sprinter van rental"])

add("residential-cleaning-housekeeping", "Residential Housekeeping & Maid Agency", "Personal Services & Lifestyle", "Home Cleaning", "B2C",
    "Professional maid services delivering recurring home cleaning, deep cleaning, and move-in/move-out cleaning.",
    "Busy families, working professionals, homeowners needing recurring cleaning",
    ["Homeowner", "Busy Professional", "Parent"],
    ["Google Local Services Ads (LSA)", "Direct Mail Postcards", "Nextdoor Neighborhood Recommendations"],
    "Medium ($150 - $400 per cleaning visit)", "Immediate to 1 week",
    ["Residential Cleaning", "Housekeeping"], ["Eco Cleaning Supply Distributors", "Field Service Scheduling Software"], ["Homeowners", "Families"],
    ["residential cleaning service", "housekeeping maid agency", "deep home cleaning", "recurring maid service"])

add("moving-storage-services", "Residential & Commercial Moving Company", "Personal Services & Lifestyle", "Moving Services", "B2B / B2C",
    "Licensed moving companies providing local/interstate residential moving, packing services, and office relocation.",
    "Homeowners moving homes, businesses relocating offices",
    ["Homeowner moving", "Office Manager relocating"],
    ["Google PPC & LSA Ads", "Real Estate Agent Referral Partners", "Direct Mail to Listed Homes"],
    "High ($1,000 - $12,000 per move)", "1 to 4 weeks",
    ["Moving Services", "Relocation Logistics"], ["Moving Truck Manufacturers", "Packing Box Manufacturers"], ["Home Buyers/Sellers", "Relocating Businesses"],
    ["moving company", "residential mover service", "commercial office relocation", "interstate moving firm"])

add("fine-art-advisory-framing", "Fine Art Advisory & Custom Framing Studio", "Personal Services & Lifestyle", "Art Advisory", "B2C / B2B",
    "Art advisors and master framers curating fine art collections, museum-grade custom framing, and art installation.",
    "Art collectors, luxury interior designers, corporate office curators",
    ["Art Collector", "Interior Designer", "Corporate Curator"],
    ["Art Gallery Networking", "Interior Designer Partnerships", "High-End Local Showroom"],
    "Medium to High ($500 custom frame / $20,000 art advisory)", "2 to 6 weeks",
    ["Fine Art Advisory", "Custom Framing"], ["Conservation Glass Suppliers", "Art Transportation Logistics"], ["Art Collectors", "Corporate Offices"],
    ["fine art advisor", "custom framing studio", "art collection manager", "museum grade framing"])

add("professional-organizing-decluttering", "Professional Organizing & Home Decluttering", "Personal Services & Lifestyle", "Home Organization", "B2C",
    "Home organizers transforming chaotic closets, kitchens, pantries, and garages into functionally aesthetic spaces.",
    "Busy homeowners, downsizing seniors, moving families",
    ["Homeowner", "Busy Parent", "Downsizing Senior"],
    ["Instagram / TikTok Before-and-After Reels", "Local Interior Designer Referrals", "Google Local Ads"],
    "Medium ($1,000 - $5,000 project size)", "1 to 2 weeks",
    ["Professional Organizing", "Home Decluttering"], ["Storage Product Manufacturers (Container Store)", "Donation Logistics"], ["Homeowners", "Downsizing Seniors"],
    ["professional organizer", "home decluttering service", "closet organizing company", "pantry organization service"])

# --- Write output file and verify counts ---
print(f"Total items created in python: {len(items)}")

out_path = "e:/SignalMind/data/business_types.json"
with open(out_path, "w", encoding="utf-8") as out_f:
    json.dump({"total_count": len(items), "business_types": items}, out_f, indent=2)

print(f"Successfully saved {len(items)} business types to {out_path}")
