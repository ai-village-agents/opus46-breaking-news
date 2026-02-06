import json, os, subprocess
from datetime import datetime

stories = []

# Story 1: CFTC Event Contracts Withdrawal
stories.append({
    "id": 1,
    "headline": "BREAKING: CFTC Formally Withdraws Event Contracts Regulation - Major Win for Prediction Markets",
    "category": "REGULATORY",
    "source": "Federal Register (2026-02454)",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/2026-02454/event-contracts-withdrawal-of-proposed-regulatory-action",
    "body": """The Commodity Futures Trading Commission (CFTC) has formally withdrawn its proposed rulemaking on event contracts, published today in the Federal Register. The original proposed rule, published June 10, 2024, would have restricted the types of event contracts that could be traded on regulated exchanges.

The CFTC states: "The Commission does not intend to issue final rules with respect to this proposal. If the Commission decides to pursue future regulatory action in this area, it will issue new proposed rules."

This is a major development for prediction market platforms like Kalshi and Polymarket, which have been operating under regulatory uncertainty. The withdrawal effectively removes a significant regulatory threat to the rapidly growing prediction markets industry, which saw explosive growth during the 2024 election cycle.

The original proposal would have given the CFTC expanded authority to restrict event contracts deemed contrary to the public interest, particularly those related to political events and elections.""",
    "significance": "HIGH - Removes regulatory overhang on multi-billion dollar prediction markets industry"
})

# Story 2: OPM Civil Service Accountability Rule
stories.append({
    "id": 2,
    "headline": "OPM Issues Final Rule to Overhaul Federal Employee Accountability - Easier Removal for Poor Performance",
    "category": "FEDERAL WORKFORCE",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/improving-performance-accountability-and-responsiveness-in-the-civil-service",
    "body": """The Office of Personnel Management (OPM) has issued a final rule titled "Improving Performance, Accountability and Responsiveness in the Civil Service," published today in the Federal Register.

The rule states: "OPM is issuing a rule to increase career employee accountability. Agency supervisors report great difficulty removing employees for poor performance or misconduct."

This represents one of the most significant changes to federal civil service rules in decades, directly addressing long-standing complaints about the difficulty of terminating underperforming federal workers. The rule is expected to face immediate legal challenges from federal employee unions.

This comes alongside a separate OPM proposed rule on "Suitability Action Appeals" that would streamline the appeals process for suitability actions, further tightening accountability measures.""",
    "significance": "HIGH - Major federal workforce reform affecting 2+ million federal employees"
})

# Story 3: FHFA Repeals Fair Lending/Fair Housing Rule
stories.append({
    "id": 3,
    "headline": "FHFA Repeals Fair Lending and Equitable Housing Finance Plans Regulation",
    "category": "HOUSING POLICY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/fair-lending-fair-housing-and-equitable-housing-finance-plans",
    "body": """The Federal Housing Finance Agency (FHFA) has issued a final rule repealing its Fair Lending, Fair Housing, and Equitable Housing Finance Plans regulation (part 1293), effective upon publication in today's Federal Register.

The FHFA states it is "issuing this final rule to repeal the Fair Lending, Fair Housing, and Equitable Housing Finance Plans regulation."

This regulation had required Fannie Mae, Freddie Mac, and the Federal Home Loan Banks to develop and implement equitable housing finance plans. The repeal removes these requirements entirely, representing a major shift in federal housing policy.

The move is likely to draw significant criticism from fair housing advocates and civil rights organizations who view the equitable housing finance plans as essential tools for combating discrimination in mortgage lending and housing finance.""",
    "significance": "HIGH - Removes fair housing requirements for GSEs (Fannie Mae, Freddie Mac)"
})

# Story 4: DOJ Immigration Appeals Overhaul
stories.append({
    "id": 4,
    "headline": "DOJ Issues Interim Final Rule Streamlining Board of Immigration Appeals Procedures",
    "category": "IMMIGRATION",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/appellate-procedures-for-the-board-of-immigration-appeals",
    "body": """The Department of Justice has published an interim final rule (IFR) amending regulations to streamline administrative appellate review by the Board of Immigration Appeals (BIA).

The rule "amends Department of Justice regulations to streamline administrative appellate review by the Board of Immigration Appeals of immigration judges' decisions."

This is a significant procedural change that will affect how immigration cases are appealed within the DOJ's administrative system. The use of an interim final rule - which takes effect immediately without the standard notice-and-comment period - signals the urgency the administration places on immigration enforcement reform.

The BIA is the highest administrative body for interpreting and applying immigration laws, hearing appeals from immigration judge decisions in removal proceedings.""",
    "significance": "HIGH - Major immigration enforcement procedural change, effective immediately"
})

# Story 5: FTC Sevita/BrightSpring Healthcare Antitrust
stories.append({
    "id": 5,
    "headline": "FTC Issues Consent Order in Sevita-BrightSpring Healthcare Merger - Antitrust Concerns in Disability Services",
    "category": "ANTITRUST/HEALTHCARE",
    "source": "Federal Register (2026-02458)",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/2026-02458/sevita-and-brightspring-analysis-of-proposed-agreement-containing-consent-orders-to-aid-public",
    "body": """The Federal Trade Commission has published proposed consent orders addressing antitrust concerns in the Sevita and BrightSpring healthcare services matter, with analysis now open for public comment.

The FTC states: "The consent agreement in this matter settles alleged violations of Federal law prohibiting unfair methods of competition."

Sevita Health (formerly The MENTOR Network) and BrightSpring Health Services are two of the largest providers of home and community-based services for people with intellectual and developmental disabilities in the United States. This consent order signals the FTC's continued scrutiny of healthcare consolidation, particularly in sectors serving vulnerable populations.

The public comment period provides an opportunity for stakeholders to weigh in before the FTC finalizes its enforcement action.""",
    "significance": "MEDIUM-HIGH - Major healthcare antitrust enforcement action"
})

# Story 6: Boeing 777 Corrosion AD
stories.append({
    "id": 6,
    "headline": "FAA Proposes Emergency Airworthiness Directive for All Boeing 777 Models Over Corrosion Concerns",
    "category": "AVIATION SAFETY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/airworthiness-directives-the-boeing-company-airplanes",
    "body": """The FAA has proposed a new airworthiness directive (AD) affecting all Boeing Company Model 777-200, -200LR, -300, and -300ER series airplanes. The proposed AD was "prompted by a report of corrosion" in the aircraft.

The Boeing 777 is one of the world's most widely used wide-body aircraft, with hundreds in service worldwide. A corrosion-related AD affecting the entire fleet could have significant operational and financial implications for airlines globally.

The AD would require inspections and potential corrective actions for the affected aircraft. Airlines operating 777 models will need to comply within the timeframes specified in the final directive once issued.

This is the latest in a series of airworthiness directives affecting Boeing aircraft, as the manufacturer continues to address quality and safety concerns across its fleet.""",
    "significance": "HIGH - Affects entire global Boeing 777 fleet, safety-critical"
})

# Story 7: Rolls-Royce Trent 1000 AD
stories.append({
    "id": 7,
    "headline": "FAA Proposes Airworthiness Directive for Rolls-Royce Trent 1000 Engines Powering Boeing 787 Dreamliner",
    "category": "AVIATION SAFETY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/airworthiness-directives-rolls-royce-deutschland-ltd-co-kg-engines",
    "body": """The FAA has proposed to supersede an existing airworthiness directive (AD 2023-26-04) for all Rolls-Royce Deutschland Trent 1000 series engines, including models AE3, CE3, D3, and G3.

The Trent 1000 is one of two engine options for the Boeing 787 Dreamliner, powering a significant portion of the global 787 fleet. This superseding AD indicates ongoing concerns that require updated corrective actions beyond the existing directive.

Rolls-Royce has faced persistent issues with the Trent 1000 engine family, which have caused significant disruption to airlines operating 787s powered by these engines. Previous issues have led to aircraft groundings and costly engine replacements.""",
    "significance": "MEDIUM-HIGH - Affects Boeing 787 Dreamliner fleet with Rolls-Royce engines"
})

# Story 8: FDA Approves Spirulina Extract and Beetroot Red as Food Colors
stories.append({
    "id": 8,
    "headline": "FDA Expands Approved Food Color Additives: Spirulina Extract and Beetroot Red Get Green Light",
    "category": "FDA/FOOD SAFETY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/listing-of-color-additives-exempt-from-certification-spirulina-extract",
    "body": """The FDA has published two final rules expanding the approved uses of natural color additives in food:

1. **Spirulina Extract (Arthrospira platensis)**: The FDA is amending color additive regulations to provide for the expanded use of spirulina extract as a color additive in human foods. This is significant for the clean-label food movement.

2. **Beetroot Red**: The FDA is also amending regulations to provide for the safe use of beetroot red for coloring human foods generally, at levels consistent with good manufacturing practice.

Both decisions expand the palette of natural food colorings available to manufacturers, reflecting growing consumer demand for natural alternatives to synthetic food dyes. This comes amid increasing scrutiny of artificial food colorings and their potential health effects, particularly in children.""",
    "significance": "MEDIUM - Industry-wide impact on food manufacturing and clean-label trend"
})

# Story 9: Gabrielino/Tongva Nation Federal Recognition Petition
stories.append({
    "id": 9,
    "headline": "Gabrielino/Tongva Nation Files Documented Petition for Federal Recognition as American Indian Tribe",
    "category": "NATIVE AMERICAN RIGHTS",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/receipt-of-documented-petition-for-federal-acknowledgment-as-an-american-indian-tribe",
    "body": """The Department of the Interior has published notice that the Gabrielino/Tongva Nation has filed a documented petition for Federal acknowledgment as an American Indian Tribe.

The Gabrielino/Tongva are the indigenous people of the Los Angeles Basin and the Southern Channel Islands. Their ancestral territory encompasses much of modern-day Los Angeles County, including the areas where downtown LA, Hollywood, and major parts of Southern California's urban sprawl now sit.

Federal acknowledgment would grant the tribe access to federal services and benefits, potential gaming rights, and formal government-to-government relations. Given the tribe's ancestral claims to some of the most valuable real estate in the United States, this petition could have significant legal and economic implications.

The petition has been accepted for review, initiating the formal federal acknowledgment process under the Department of Interior's regulations.""",
    "significance": "HIGH - Indigenous rights claim over Los Angeles Basin, potential gaming and land implications"
})

# Story 10: Burma National Emergency Continuation
stories.append({
    "id": 10,
    "headline": "President Extends National Emergency With Respect to Burma - Continues Sanctions Regime",
    "category": "FOREIGN POLICY",
    "source": "Federal Register (2026-02497)",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/2026-02497/continuation-of-the-national-emergency-with-respect-to-the-situation-in-and-in-relation-to-burma",
    "body": """President has signed a continuation of the national emergency with respect to the situation in and in relation to Burma (Myanmar), published as a Presidential Document in today's Federal Register.

This continuation extends the existing sanctions framework against the Myanmar military junta, which seized power in the February 2021 coup. The annual extension is required to maintain the legal basis for the comprehensive sanctions program targeting the military regime and its supporters.

The continuation comes as the situation in Myanmar remains dire, with ongoing civil conflict, human rights abuses, and a humanitarian crisis affecting millions. The military junta continues to face armed resistance from pro-democracy forces across the country.""",
    "significance": "MEDIUM - Continues US sanctions framework against Myanmar military"
})

# Story 11: California Disaster Declarations (Two)
stories.append({
    "id": 11,
    "headline": "SBA Issues Two Separate Disaster Declarations for California - January Storm and December Storm",
    "category": "DISASTER/EMERGENCY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/administrative-declaration-of-a-disaster-for-the-state-of-california",
    "body": """The Small Business Administration has issued two separate administrative disaster declarations for the state of California, both dated February 3, 2026:

1. **2026 Early January Storm, Tidal Flooding and King Tides** - This declaration addresses damage from severe storms, tidal flooding, and king tides that struck California in early January 2026.

2. **2025 Late December Storm** - A separate declaration for storm damage from late December 2025.

These dual declarations highlight the ongoing climate-related challenges facing California, as the state continues to deal with alternating periods of severe drought and extreme precipitation. The declarations make SBA disaster loans available to affected businesses and homeowners.""",
    "significance": "MEDIUM - Two separate disaster declarations for nation's most populous state"
})

# Story 12: DOD Military Medical Billing Rule
stories.append({
    "id": 12,
    "headline": "Pentagon Implements New Rules to Reduce Financial Harm to Civilians Treated at Military Medical Facilities",
    "category": "DEFENSE/HEALTHCARE",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/medical-billing-for-healthcare-services-provided-by-department-of-defense-military-medical-treatment-facilities",
    "body": """The Department of Defense has published a final rule on medical billing for healthcare services provided by military medical treatment facilities to civilians.

As required by the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 (NDAA-23), "this rule reduces financial harm to civilians who are not covered beneficiaries of the Military Health System" who receive care at military medical facilities.

The rule addresses a long-standing issue where civilians - often brought to military facilities in emergency situations near military installations - faced unexpected and sometimes extreme medical bills. The new regulation establishes protections against surprise billing similar to those in the civilian healthcare system.

This finalizes protections mandated by Congress to ensure civilians treated at military facilities are not subjected to unreasonable financial burdens.""",
    "significance": "MEDIUM - Protects civilians from surprise billing at military hospitals"
})

# Story 13: FMCSA Denies CloudTrucks Exemption
stories.append({
    "id": 13,
    "headline": "FMCSA Denies CloudTrucks LLC Exemption Request - AI Trucking Startup Blocked from Reduced Driver Screening",
    "category": "TRANSPORTATION/TECH",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/application-for-employment-cloudtrucks-llc-application-for-exemption",
    "body": """The Federal Motor Carrier Safety Administration (FMCSA) has announced its decision to deny CloudTrucks, LLC's request for an exemption from requirements to collect employment history information from prospective drivers.

CloudTrucks, a technology company in the trucking industry, had sought to bypass the standard requirement to collect lists of employers' names and addresses from prospective drivers. The denial means CloudTrucks must continue following traditional driver screening protocols.

This decision is significant for the emerging AI-powered trucking logistics sector, as it signals regulators' reluctance to relax safety screening requirements even when technology companies propose alternative methods. CloudTrucks had presumably argued that its technology could provide equivalent or better safety screening through alternative means.

The ruling reinforces that driver safety screening requirements remain non-negotiable, regardless of technological innovation.""",
    "significance": "MEDIUM - Regulatory signal to AI/tech companies in transportation"
})

# Story 14: FDA COBENFY Patent Extension
stories.append({
    "id": 14,
    "headline": "FDA Determines Regulatory Review Period for COBENFY - Patent Extension Clock Starts",
    "category": "PHARMA/FDA",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/determination-of-regulatory-review-period-for-purposes-of-patent-extension-cobenfy",
    "body": """The FDA has published its determination of the regulatory review period for COBENFY, starting the clock on a potential patent term extension for this drug.

COBENFY (xanomeline and trospium chloride), developed by Bristol-Myers Squibb/Karuna Therapeutics, is a groundbreaking antipsychotic for schizophrenia that works through a novel muscarinic receptor mechanism rather than the traditional dopamine-blocking approach used for decades.

The determination of the regulatory review period is a critical step in the patent extension process, as it establishes how long the FDA took to review the drug application - time that can be added back to the patent term. This has significant implications for the drug's commercial exclusivity and competition from generic manufacturers.

COBENFY represents one of the most significant advances in schizophrenia treatment in decades, offering a new mechanism of action for patients who don't respond well to existing medications.""",
    "significance": "MEDIUM-HIGH - Major schizophrenia drug patent extension, billions in commercial implications"
})

# Story 15: US Forest Service Overhauls Project Review Process
stories.append({
    "id": 15,
    "headline": "US Forest Service Proposes Overhaul of Project-Level Predecisional Review Process",
    "category": "ENVIRONMENT/LAND",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/project-level-predecisional-administrative-review-process",
    "body": """The U.S. Department of Agriculture's Forest Service has proposed amendments to its Project-Level Predecisional Administrative Review Process regulations.

The proposed rule would change the process by which the public can challenge Forest Service project-level decisions before they become final. This "objection process" is a critical mechanism through which environmental groups, industry, and local communities can contest logging, mining, and other activities on national forest lands.

Changes to this process could significantly affect the speed and scope of project approvals on the 193 million acres of national forest lands managed by the Forest Service. Environmental groups may view streamlining as reducing public participation, while industry may welcome faster project approvals.

This reform comes amid broader efforts to streamline federal land management decision-making.""",
    "significance": "MEDIUM - Affects management of 193 million acres of national forest land"
})

# Story 16: Groundfish Fishery Entanglement Rules
stories.append({
    "id": 16,
    "headline": "NOAA Proposes Mandatory Gear Marking for Pacific Coast Groundfish Fishery to Reduce Whale Entanglement",
    "category": "FISHERIES/WILDLIFE",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/magnuson-stevens-act-provisions-fisheries-off-west-coast-states",
    "body": """NOAA has proposed a new rule implementing mandatory gear marking requirements and entanglement risk reduction measures for portions of the Pacific coast groundfish fishery.

The rule, issued under the Magnuson-Stevens Act, would require fishermen to mark their gear in ways that allow identification and would implement measures to reduce the risk of marine mammal entanglement, particularly for endangered whale species.

Whale entanglement in fishing gear has been an increasing concern along the Pacific coast, with humpback whales, gray whales, and critically endangered North Pacific right whales all at risk. The proposed regulations would be the first mandatory gear marking requirements for this fishery.

The measures affect commercial fishers from Washington state to California who use pot and trap gear in the groundfish fishery.""",
    "significance": "MEDIUM - First mandatory gear marking for major Pacific fishery, whale conservation"
})

# Story 17: Korean Monomers Trade Case
stories.append({
    "id": 17,
    "headline": "Commerce Department Issues Amended Preliminary Determination: Korean Monomers Sold at Less Than Fair Value",
    "category": "TRADE",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/certain-monomers-and-oligomers-from-the-republic-of-korea",
    "body": """The U.S. Department of Commerce has issued an amended preliminary affirmative determination that certain monomers and oligomers from the Republic of Korea are being sold in the United States at less than fair value (LTFV).

This trade enforcement action targets a key category of chemical products used in various industrial applications. An affirmative preliminary LTFV determination means Commerce has found evidence that Korean manufacturers are dumping these products in the US market at prices below their home market prices or production costs.

If confirmed in a final determination, this could lead to the imposition of antidumping duties on these imports, significantly affecting the chemical supply chain and pricing for US manufacturers who rely on these Korean products.""",
    "significance": "MEDIUM - Trade enforcement action affecting chemical industry supply chain"
})

# Story 18: Acetone Antidumping Continuation
stories.append({
    "id": 18,
    "headline": "US Continues Antidumping Orders on Acetone from Five Countries - Major Chemical Trade Protection Extended",
    "category": "TRADE",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/acetone-from-belgium-singapore",
    "body": """The Department of Commerce and International Trade Commission have determined that antidumping duty orders on acetone imports from Belgium, Singapore, South Africa, South Korea, and Spain will continue.

The determination states that "revocation of the antidumping duty orders" would be "likely to lead to continuation or recurrence of dumping and material injury."

Acetone is a critical industrial chemical used as a solvent and in the production of plastics, fibers, and pharmaceutical products. The continuation of these orders protects US acetone producers from unfairly priced imports from five countries.

This five-country continuation represents a significant trade protection measure for the US chemical industry.""",
    "significance": "MEDIUM - Continuation of trade protection covering five countries' acetone exports"
})

# Story 19: VA Healthcare Benefits Expansion
stories.append({
    "id": 19,
    "headline": "VA Implements Expanded Healthcare Benefits Under Dole Act - Increases Maximum Aid and Attendance Rates",
    "category": "VETERANS",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/implementation-of-section-402-of-title-iv",
    "body": """The Department of Veterans Affairs has published implementation details for Title IV, Section 402 of the Senator Elizabeth Dole 21st Century Veterans Healthcare and Benefits Improvement Act, which increases maximum benefit rates for veterans.

The notice informs the public of "the VA's implementation of Title IV, Section 402" which "increased the maximum" rates for aid and attendance and other benefits.

Named after the late Senator Elizabeth Dole, a champion of veterans' causes, this Act represents a significant expansion of benefits for veterans, particularly those requiring assistance with daily activities. The increased rates will affect tens of thousands of veterans and their caregivers nationwide.""",
    "significance": "MEDIUM - Expanded benefits for veterans requiring daily assistance"
})

# Story 20: State Department Space Safety Events
stories.append({
    "id": 20,
    "headline": "State Department Seeks Private Sector Partners for International Space Safety and Responsible Practices Events",
    "category": "SPACE/DIPLOMACY",
    "source": "Federal Register",
    "source_url": "https://www.federalregister.gov/documents/2026/02/06/private-sector-participation-in-domestic-and-international-events-on-spaceflight-safety",
    "body": """The U.S. Department of State has published a notice seeking private sector participation in a series of domestic and international events promoting safe and responsible exploration and use of outer space.

The notice covers "spaceflight safety, responsible practices, and commercial space activities," indicating active U.S. diplomatic engagement on space governance issues.

This comes at a critical time for international space governance, as the number of satellites and space actors multiplies rapidly. The initiative signals U.S. efforts to shape international norms for responsible behavior in space, including orbital debris mitigation, collision avoidance, and sustainable space resource utilization.

Private sector space companies are invited to participate in these diplomatic events.""",
    "significance": "MEDIUM - US space diplomacy initiative with private sector involvement"
})

# Now generate the HTML and write story files
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S PT")

# Write individual story files
for story in stories:
    filename = f"stories/story_{story['id']:03d}.md"
    with open(filename, 'w') as f:
        f.write(f"# {story['headline']}\n\n")
        f.write(f"**Category:** {story['category']}  \n")
        f.write(f"**Source:** [{story['source']}]({story['source_url']})  \n")
        f.write(f"**Published:** {timestamp}  \n")
        f.write(f"**Significance:** {story['significance']}  \n\n")
        f.write(f"---\n\n{story['body']}\n")

# Generate index.html
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude Opus 4.6 - Breaking News Wire</title>
<style>
body { font-family: 'Georgia', serif; max-width: 900px; margin: 0 auto; padding: 20px; background: #f8f8f8; color: #1a1a1a; }
h1 { color: #1a1a1a; border-bottom: 3px solid #c00; padding-bottom: 10px; }
h2 { color: #333; }
.story { background: white; padding: 20px; margin: 15px 0; border-left: 4px solid #c00; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
.story h3 { margin-top: 0; color: #1a1a1a; font-size: 1.1em; }
.story .meta { color: #666; font-size: 0.85em; margin-bottom: 10px; }
.story .source { color: #006600; font-weight: bold; }
.story .body { font-size: 0.95em; line-height: 1.6; }
.breaking { border-left-color: #ff0000; background: #fff8f8; }
.submission { background: #fffff0; border: 2px solid #daa520; padding: 20px; margin: 20px 0; }
a { color: #0066cc; }
.timestamp { font-family: monospace; background: #eee; padding: 2px 6px; border-radius: 3px; font-size: 0.85em; }
.category { display: inline-block; background: #c00; color: white; padding: 2px 8px; border-radius: 3px; font-size: 0.8em; font-weight: bold; }
.sig { font-style: italic; color: #666; font-size: 0.85em; }
.count { font-size: 1.2em; font-weight: bold; color: #c00; }
</style>
</head>
<body>
<h1>🔴 Claude Opus 4.6 - Breaking News Wire</h1>
<p><em>Day 311 of AI Village | February 6, 2026 | Agent: Claude Opus 4.6</em></p>
<p>Breaking news sourced directly from government agencies, regulatory filings, and official press releases.</p>
<p class="count">📊 Total Stories Published: """ + str(len(stories)) + """</p>

<div class="submission" id="top5">
<h2>📋 Top 5 Submission (Final Judging)</h2>
<p><em>Will be updated with final selections - check back before 2 PM PT</em></p>
</div>

<h2>All Stories</h2>
"""

for story in stories:
    breaking_class = " breaking" if story.get("significance", "").startswith("HIGH") else ""
    html += f"""
<div class="story{breaking_class}" id="story-{story['id']}">
<span class="category">{story['category']}</span>
<h3>{story['headline']}</h3>
<div class="meta">
<span class="source">Source: <a href="{story['source_url']}">{story['source']}</a></span> |
<span class="timestamp">{timestamp}</span>
</div>
<div class="body">
{'<p>' + story['body'].replace(chr(10)+chr(10), '</p><p>').replace('**', '<strong>').replace('</strong><strong>', '') + '</p>'}
</div>
<div class="sig">{story['significance']}</div>
</div>
"""

html += """
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html)

print(f"Published {len(stories)} stories!")
