# MediLab Pro - Medical Laboratory Website (Flask Version)

A professional, modern website for medical laboratories built with Python Flask. This website provides comprehensive information about laboratory services, team members, and includes a functional contact system with email notifications.

## 🚀 Features

### Professional Design
- **Modern UI/UX**: Clean, medical-focused design with professional color scheme
- **Responsive Layout**: Fully responsive design that works on all devices
- **Smooth Animations**: Engaging scroll animations and hover effects
- **Professional Typography**: Uses Inter font family for excellent readability

### Key Sections
- **Hero Section**: Compelling introduction with animated statistics
- **About Section**: Laboratory overview with mission, vision, and values
- **Services Section**: Comprehensive listing of all laboratory services
- **Team Section**: Showcase of key laboratory professionals
- **Contact Section**: Contact information and functional inquiry form
- **Service Details**: Individual pages for each laboratory service

### Interactive Features
- **Contact Form**: Fully functional contact form with validation and email notifications
- **Form Validation**: Client-side and server-side validation
- **Email System**: Automatic email notifications for inquiries
- **Responsive Navigation**: Mobile-friendly hamburger menu
- **Smooth Scrolling**: Navigation links smoothly scroll to sections
- **Loading Animations**: Professional loading and scroll animations
- **Counter Animation**: Animated statistics in hero section

### Technical Features
- **Flask Framework**: Robust Python web framework
- **WTForms**: Form handling and validation
- **Flask-Mail**: Email functionality
- **Bootstrap 5**: Modern CSS framework
- **Font Awesome**: Professional icons
- **SEO Optimized**: Proper heading structure and meta tags
- **Accessibility**: WCAG compliant with proper ARIA labels
- **Error Handling**: Custom 404 and 500 error pages

## 📁 Project Structure

```
medical-lab-flask/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables example
├── README_FLASK.md       # This documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── about.html        # About page
│   ├── services.html     # Services listing
│   ├── service_detail.html # Individual service pages
│   ├── team.html         # Team page
│   ├── contact.html      # Contact page
│   ├── 404.html          # 404 error page
│   └── 500.html          # 500 error page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom CSS styles
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Images directory
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### 1. Clone or Download
Download the project files to your desired directory.

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv medilabpro_env

# Activate virtual environment
# On Windows:
medilabpro_env\Scripts\activate
# On macOS/Linux:
source medilabpro_env/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env file with your configuration
# Set SECRET_KEY, email settings, etc.
```

### 5. Run the Application
```bash
# Development mode
python app.py

# Or with Flask CLI
export FLASK_APP=app.py
flask run
```

The website will be available at `http://localhost:5000`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here-change-this-in-production
FLASK_ENV=development
FLASK_DEBUG=True

# Email Configuration (for contact form)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

### Email Setup

To enable the contact form email functionality:

1. **Gmail Setup** (recommended):
   - Enable 2-factor authentication
   - Generate an App Password
   - Use the App Password in `MAIL_PASSWORD`

2. **Other Email Providers**:
   - Update `MAIL_SERVER` and `MAIL_PORT`
   - Adjust authentication settings as needed

## 🎨 Customization Guide

### 1. Laboratory Information
Edit the `LAB_INFO` dictionary in `app.py`:
```python
LAB_INFO = {
    'name': 'Your Lab Name',
    'tagline': 'Your Laboratory Tagline',
    'description': 'Your laboratory description',
    # ... other settings
}
```

### 2. Services
Update the `SERVICES` list in `app.py`:
```python
SERVICES = [
    {
        'id': 'your-service-id',
        'name': 'Service Name',
        'description': 'Service description',
        'icon': '🧪',  # Emoji or FontAwesome class
        'tests': ['Test 1', 'Test 2', 'Test 3']
    },
    # ... more services
]
```

### 3. Team Members
Modify the `TEAM` list in `app.py`:
```python
TEAM = [
    {
        'name': 'Dr. Your Name',
        'title': 'Position Title',
        'credentials': 'MD, PhD',
        'experience': '10+ years',
        'specialization': 'Your specialization',
        'image': 'team-member.jpg'
    },
    # ... more team members
]
```

### 4. Styling
Customize colors and styling in `static/css/style.css`:
```css
:root {
    --primary-color: #2563eb;  /* Your primary color */
    --secondary-color: #fbbf24; /* Your secondary color */
    /* ... other CSS variables */
}
```

### 5. Images
Replace placeholder images in `static/images/`:
- Team member photos
- Laboratory facility images
- Equipment photos
- Logo/branding elements

## 📱 Responsive Design

The website is fully responsive with breakpoints:
- **Desktop**: 1200px and above
- **Tablet**: 768px to 1199px
- **Mobile**: 767px and below
- **Small Mobile**: 480px and below

## 🔧 Development

### Adding New Pages
1. Create a new route in `app.py`:
```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html', lab_info=LAB_INFO)
```

2. Create the template in `templates/new_page.html`:
```html
{% extends "base.html" %}
{% block content %}
<!-- Your content here -->
{% endblock %}
```

### Adding New Services
1. Add to the `SERVICES` list in `app.py`
2. The service will automatically appear on the services page
3. Individual service pages are generated automatically

### Database Integration
To add database functionality:
1. Install Flask-SQLAlchemy: `pip install Flask-SQLAlchemy`
2. Set up database models
3. Update forms to save to database
4. Add admin interface if needed

## 🚀 Deployment

### Production Checklist
- [ ] Set `FLASK_ENV=production`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure production email settings
- [ ] Set up HTTPS
- [ ] Configure production web server (Gunicorn, uWSGI)
- [ ] Set up reverse proxy (Nginx, Apache)
- [ ] Configure database (if using)
- [ ] Set up monitoring and logging

### Deployment Options

#### 1. Traditional VPS/Server
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

#### 2. Docker
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
```

#### 3. Cloud Platforms
- **Heroku**: Add `Procfile` with `web: gunicorn app:app`
- **AWS Elastic Beanstalk**: Deploy Flask application
- **Google Cloud Platform**: Use App Engine
- **DigitalOcean App Platform**: Deploy directly from repository

## 🔒 Security Considerations

- CSRF protection enabled by default
- Form validation on client and server side
- Email sanitization
- Environment variables for sensitive data
- Secure headers recommended for production
- Regular dependency updates

## 📊 Performance Tips

- **Optimize Images**: Use WebP format when possible
- **Minify CSS/JS**: Use build tools for production
- **Enable Gzip**: Compress files on server
- **CDN**: Use content delivery network for static assets
- **Caching**: Implement browser and server-side caching

## 🤝 Support & Maintenance

### Regular Maintenance
- Update Python dependencies regularly
- Monitor email delivery
- Check form submissions
- Update contact information as needed
- Backup any data regularly

### Troubleshooting

**Email not sending:**
- Check email credentials
- Verify SMTP settings
- Check firewall/security settings
- Test with a simple email client

**Form validation errors:**
- Check JavaScript console for errors
- Verify form field names match Flask-WTF form
- Ensure proper form validation setup

**Styling issues:**
- Check CSS file loading
- Verify Bootstrap CDN links
- Check responsive design on different devices

## 📝 License

This project is open source and available under the MIT License.

## 🔄 Updates and Versions

- **v1.0.0**: Initial Flask version with full functionality
- Contact form with email notifications
- Responsive design with Bootstrap 5
- Professional medical laboratory styling
- SEO optimization and accessibility features

---

**Built with modern web technologies for medical laboratories seeking a professional online presence.**