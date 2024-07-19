import streamlit as st

st.title("ServiceNow Professional Application")

st.markdown("""
### Thank You for Your Interest in ServiceNow Contract Roles

We appreciate your interest in joining our team for ServiceNow contract roles. Please fill out the form below to submit your candidacy for positions for ServiceNow Business Analysts, Developers, and Senior Developers. There is also a need for ServiceNow HAM Pro developers.

After you submit the form, a STAND 8 representative will reach out to you to schedule a video interview.

Thank you for considering us as your next career opportunity!
""")

st.divider()

st.subheader("Contact Information")

# Create columns for first and last name
col1, col2 = st.columns(2)

with col1:
    first_name = st.text_input("First Name")

with col2:
    last_name = st.text_input("Last Name")

# Create columns for city, state, and ZIP code
col3, col4, col5 = st.columns(3)

with col3:
    city = st.text_input("City")

with col4:
    states = [
        'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 
        'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 
        'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
    ]
    state = st.selectbox("State", states)

with col5:
    zip_code = st.text_input("ZIP Code (5 digits)")

##### Rate and Availability

st.subheader('Rate and Availability')
# Ask for hourly rate
hourly_rate = st.text_input("Hourly Rate (USD)")

# Ask for availability to start working
availability = st.date_input("Availability to Start Working")

# Preferred mode of communication
communication_mode = st.radio(
    "Preferred Mode of Communication",
    ('Email', 'SMS/Text', 'Voice Call')
)

# Contact details based on preferred mode of communication
if communication_mode == 'Email':
    contact_detail = st.text_input("Email Address")
elif communication_mode == 'SMS/Text':
    contact_detail = st.text_input("Phone Number for SMS/Text")
else:
    contact_detail = st.text_input("Phone Number for Voice Call")

st.subheader('Work Authorization and Travel Availability')
# Planned vacations/OOO dates
vacation_dates = st.text_area("Planned Vacations/OOO Dates (please list dates)")

# Authorized to work in the US
authorized_to_work = st.checkbox("I am authorized to work in the US")

# Travel preferences
travel_preference = st.selectbox(
    "Some travel may be required to participate in workshops that will be conducted at locations either in the East coast (NY/NJ) or West Coast (LA) of the US. The dates of travel are not available at this time but you will be notified of the dates in advance once available. While travel to the in-person meeting is encouraged, exceptions may be made with prior approval.",
    ["Yes, willing to travel", "Yes, for final round only", "Video interview only", "Prefer other accommodation", "Not willing to travel"]
)

st.subheader('Experience and Qualifications')

# Get ServiceNow modules

st.markdown('''We have a need for experienced HAM Pro Developers. If you have HAM Pro experience in the areas below, plase complete this form and submit. We have an urgent need for your skillset.''')
with st.expander('Key HAM Pro Areas Needed'):
    st.markdown('''We have a need specifically for HAM Pro experience, specifically in the areas below:
    
* Automated Asset Lifecycle Management:   
    - Automates the entire lifecycle of hardware assets, from procurement to disposal.
    - Ensures compliance with corporate and regulatory requirements.

* Enhanced Asset Tracking:
    - Provides more detailed and accurate asset tracking with the use of advanced tagging and tracking technologies.
    - Integration with IoT devices for real-time asset location and status updates.
    
* Improved Hardware Request Process:
    - Streamlines the hardware request and fulfillment process with automated approvals and workflows.
    - Enhanced user interface for submitting and tracking hardware requests.

* Contract and Vendor Management:
    - Advanced features for managing vendor contracts, including automated renewal notifications and compliance tracking.
    - Better visibility into vendor performance and contract terms.
    
* Asset Auditing and Reconciliation:
    
    - Automated asset audit and reconciliation processes to ensure data accuracy.
    - Detailed audit trails and reports for compliance and auditing purposes.

* Depreciation and Financial Management:
    
    - Advanced financial management features, including automated depreciation calculations and financial reporting.
    - Integration with financial systems for seamless data exchange and reporting.

* Enhanced Reporting and Dashboards:
    
    - Advanced reporting capabilities with customizable dashboards and real-time analytics.
    - Pre-built reports for common asset management metrics and KPIs.

* Sustainability and Disposal Management:
    
    - Features for managing the disposal and recycling of hardware assets in an environmentally responsible manner.
    - Tracking of environmental impact and compliance with sustainability policies.
''')

linkedin = st.text_input("Linkedin URL")
resume = st.file_uploader("Upload your resume", type=["pdf", "doc", "docx"])


modules = [
    "IT Service Management (ITSM)",
    "Configuration Management Database (CMDB)",
    "IT Operations Management (ITOM)",
    "IT Asset Management (ITAM)",
    "Customer Service Management (CSM)",
    "HR Service Delivery (HRSD)",
    "Security Operations (SecOps)",
    "Governance, Risk, and Compliance (GRC)",
    "Software Asset Management (SAM)",
    "Hardware Asset Management (HAM)",
    "Hardware Asset Management Pro (HAM Pro)",
    "Field Service Management (FSM)",
    "Project Portfolio Management (PPM)",
    "Facilities Service Management",
    "Legal Service Delivery"
]

selected_modules = st.multiselect("Select the ServiceNow modules you are familiar with:", modules)



st.subheader('Certifications')
# ServiceNow certifications multi-select
certifications = [
    "Certified System Administrator",
    "Certified Application Developer",
    "Certified Implementation Specialist – IT Service Management",
    "Certified Implementation Specialist – Customer Service Management",
    "Certified Implementation Specialist – HR Service Delivery",
    "Certified Implementation Specialist – IT Asset Management",
    "Certified Implementation Specialist – IT Operations Management",
    "Certified Implementation Specialist – Security Incident Response",
    "Certified Implementation Specialist – Software Asset Management",
    "Certified Implementation Specialist – Vulnerability Response",
    "Certified Implementation Specialist – Financial Management",
    "Certified Implementation Specialist – Project Portfolio Management",
    "Certified Implementation Specialist – Risk and Compliance",
    "Certified Implementation Specialist – Strategic Portfolio Management",
    "Certified Implementation Specialist – Now Platform App Engine",
    "Certified Implementation Specialist – Hardware Asset Management (HAM) Pro",
    "Certified Implementation Specialist – Common Services Data Model (CSDM)",
    "Certified Implementation Specialist – Flow Designer",
    "Micro-Certification – Performance Analytics",
    "Micro-Certification – Virtual Agent",
    "Micro-Certification – Predictive Intelligence",
    "Micro-Certification – Automated Test Framework",
    "Micro-Certification – Cloud Management",
    "Micro-Certification – HR Service Delivery",
    "Micro-Certification – DevOps",
    "Micro-Certification – Software Asset Management",
    "Micro-Certification – Vulnerability Response"
]
selected_certifications = st.multiselect("ServiceNow Certifications", certifications)


if st.button("Submit"):
    if first_name and last_name and city and state and zip_code and hourly_rate and availability and contact_detail and authorized_to_work:
        if len(zip_code) == 5 and zip_code.isdigit() and hourly_rate.isdigit():
            st.success(f"Thank you, {first_name} {last_name}, from {city}, {state} {zip_code}, for submitting your information!")
            st.success(f"Your expected hourly rate is ${hourly_rate}/hour and you are available to start working from {availability}.")
            st.success(f"We will contact you via {communication_mode} at {contact_detail}.")
            st.success(f"ServiceNow Certifications: {', '.join(selected_certifications)}")
            st.success(f"Planned Vacations/OOO Dates: {vacation_dates}")
            st.success(f"Travel Preference: {travel_preference}")
        else:
            st.error("Please enter valid information for ZIP Code and hourly rate.")
    else:
        st.error("Please fill in all the required fields: first name, last name, city, state, ZIP Code, hourly rate, availability, contact details, and authorization to work in the US.")
