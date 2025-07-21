from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Email configuration
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')

mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[Length(max=20)])
    service = SelectField('Service of Interest', choices=[
        ('general', 'General Inquiry'),
        ('clinical-chemistry', 'Clinical Chemistry'),
        ('molecular-diagnostics', 'Molecular Diagnostics'),
        ('microbiology', 'Microbiology'),
        ('hematology', 'Hematology'),
        ('immunology', 'Immunology'),
        ('pathology', 'Pathology'),
        ('urgent', 'Urgent Test Request')
    ])
    message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=1000)])

# Laboratory data
LAB_INFO = {
    'name': 'MediLab Pro',
    'tagline': 'Advanced Medical Diagnostics & Laboratory Services',
    'description': 'Leading medical laboratory providing comprehensive diagnostic services with state-of-the-art technology and expert analysis.',
    'established': '1985',
    'tests_per_year': '500,000+',
    'accuracy_rate': '99.8%',
    'turnaround_time': '24-48 hours',
    'contact': {
        'address': '123 Medical Center Drive, Healthcare District, City 12345',
        'phone': '+1 (555) 123-4567',
        'email': 'info@medilabpro.com',
        'emergency': '+1 (555) 123-4568',
        'hours': {
            'weekdays': '6:00 AM - 10:00 PM',
            'saturday': '7:00 AM - 8:00 PM',
            'sunday': '8:00 AM - 6:00 PM'
        }
    },
    'certifications': [
        'CAP Accredited',
        'CLIA Certified',
        'ISO 15189:2012',
        'Joint Commission Approved'
    ]
}

SERVICES = [
    {
        'id': 'clinical-chemistry',
        'name': 'Clinical Chemistry',
        'description': 'Comprehensive metabolic panels, lipid profiles, cardiac markers, and therapeutic drug monitoring.',
        'icon': '🧪',
        'tests': ['Basic Metabolic Panel', 'Lipid Profile', 'Liver Function Tests', 'Cardiac Markers']
    },
    {
        'id': 'molecular-diagnostics',
        'name': 'Molecular Diagnostics',
        'description': 'DNA/RNA analysis, genetic testing, infectious disease detection, and personalized medicine.',
        'icon': '🧬',
        'tests': ['PCR Testing', 'Genetic Sequencing', 'Viral Load Testing', 'Pharmacogenomics']
    },
    {
        'id': 'microbiology',
        'name': 'Microbiology',
        'description': 'Bacterial, viral, and fungal identification with antimicrobial susceptibility testing.',
        'icon': '🦠',
        'tests': ['Culture & Sensitivity', 'Rapid Strep', 'UTI Testing', 'Blood Cultures']
    },
    {
        'id': 'hematology',
        'name': 'Hematology',
        'description': 'Complete blood counts, coagulation studies, and blood disorder diagnostics.',
        'icon': '🩸',
        'tests': ['CBC with Differential', 'PT/INR', 'ESR', 'Hemoglobin Electrophoresis']
    },
    {
        'id': 'immunology',
        'name': 'Immunology',
        'description': 'Autoimmune testing, allergy panels, and immune system function assessment.',
        'icon': '🛡️',
        'tests': ['Autoimmune Panels', 'Allergy Testing', 'Rheumatoid Factor', 'Complement Studies']
    },
    {
        'id': 'pathology',
        'name': 'Pathology',
        'description': 'Tissue analysis, cytology, and anatomical pathology services.',
        'icon': '🔬',
        'tests': ['Biopsy Analysis', 'Pap Smears', 'Fine Needle Aspiration', 'Surgical Pathology']
    }
]

TEAM = [
    {
        'name': 'Dr. Sarah Johnson',
        'title': 'Laboratory Director & Clinical Pathologist',
        'credentials': 'MD, PhD, FCAP',
        'experience': '15+ years',
        'specialization': 'Clinical Pathology & Laboratory Management',
        'image': 'team-1.jpg'
    },
    {
        'name': 'Dr. Michael Chen',
        'title': 'Chief Medical Technologist',
        'credentials': 'PhD, MT(ASCP)',
        'experience': '12+ years',
        'specialization': 'Molecular Diagnostics & Genetics',
        'image': 'team-2.jpg'
    },
    {
        'name': 'Dr. Emily Rodriguez',
        'title': 'Microbiology Supervisor',
        'credentials': 'PhD, SM(ASCP)',
        'experience': '10+ years',
        'specialization': 'Clinical Microbiology & Infectious Diseases',
        'image': 'team-3.jpg'
    },
    {
        'name': 'Dr. David Park',
        'title': 'Hematology Specialist',
        'credentials': 'MD, Hematopathologist',
        'experience': '8+ years',
        'specialization': 'Hematology & Coagulation',
        'image': 'team-4.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', 
                         lab_info=LAB_INFO, 
                         services=SERVICES, 
                         team=TEAM, 
                         form=ContactForm())

@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES, lab_info=LAB_INFO)

@app.route('/services/<service_id>')
def service_detail(service_id):
    service = next((s for s in SERVICES if s['id'] == service_id), None)
    if not service:
        flash('Service not found.', 'error')
        return redirect(url_for('services'))
    return render_template('service_detail.html', service=service, lab_info=LAB_INFO)

@app.route('/team')
def team():
    return render_template('team.html', team=TEAM, lab_info=LAB_INFO)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            # Send email notification
            msg = Message(
                subject=f'New Contact Form Submission - {form.service.data}',
                recipients=[LAB_INFO['contact']['email']],
                body=f"""
New contact form submission:

Name: {form.name.data}
Email: {form.email.data}
Phone: {form.phone.data}
Service: {form.service.data}
Message: {form.message.data}

Submitted at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                """
            )
            
            # Send confirmation email to user
            confirmation_msg = Message(
                subject='Thank you for contacting MediLab Pro',
                recipients=[form.email.data],
                body=f"""
Dear {form.name.data},

Thank you for contacting MediLab Pro. We have received your inquiry regarding {form.service.data}.

Our team will review your message and respond within 24 hours during business days.

If you have an urgent request, please call us at {LAB_INFO['contact']['emergency']}.

Best regards,
MediLab Pro Team
                """
            )
            
            if app.config['MAIL_USERNAME']:  # Only send if email is configured
                mail.send(msg)
                mail.send(confirmation_msg)
            
            flash('Thank you for your message! We will get back to you within 24 hours.', 'success')
            return redirect(url_for('contact'))
            
        except Exception as e:
            flash('There was an error sending your message. Please try again or call us directly.', 'error')
            app.logger.error(f'Email error: {str(e)}')
    
    return render_template('contact.html', form=form, lab_info=LAB_INFO)

@app.route('/about')
def about():
    return render_template('about.html', lab_info=LAB_INFO, services=SERVICES)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', lab_info=LAB_INFO), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', lab_info=LAB_INFO), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)