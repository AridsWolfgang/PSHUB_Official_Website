
# PROSPERITY SYSTEM HUB | Official Website

[![License: Proprietary](https://img.shields.io/badge/License-Proprietary-blue.svg)](LICENSE)

The official web presence for Prosperity System Hub, an integrated infrastructure platform that enables governments, institutions, and markets to design and operate systems converting population potential into measurable economic outcomes.

## 📋 Table of Contents
- [PROSPERITY SYSTEM HUB | Official Website](#prosperity-system-hub--official-website)
  - [📋 Table of Contents](#-table-of-contents)
  - [📋 Overview](#-overview)
  - [✨ Features](#-features)
  - [🛠️ Technology Stack](#️-technology-stack)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Local Development](#local-development)
  - [📁 Project Structure](#-project-structure)
  - [📄 License](#-license)
  - [🤝 Contact](#-contact)

## 📋 Overview

This repository contains the source code for the official Prosperity System Hub website. The site serves as a comprehensive digital platform to communicate the organization's mission, showcase its platform architecture, highlight leadership and career opportunities, and provide resources for institutional partners.

The website is built with a focus on professional presentation, intuitive navigation, and a responsive design that works seamlessly across all devices.

## ✨ Features

* **Modern Minimal Design** – Clean, professional aesthetic with an intuitive navigation structure that reflects the organization's enterprise focus.
* **Fully Responsive Layout** – Optimized viewing experience on desktop, tablet, and mobile devices.
* **Interactive Navigation** – Dropdown menus with smooth animations for easy access to all sections.
* **Comprehensive Pages**:
  * **Platform Overview** – Detailed explanation of the core architecture and capabilities.
  * **Mission & Vision** – Clear articulation of organizational purpose.
  * **Leadership & Team** – Profiles of the executive team, board, and regional leaders.
  * **Careers** – Current open positions and insights into the company culture.
  * **Strategic Briefing** – A dedicated form for institutional partners to request a briefing.
  * **Security & Compliance** – Detailed information on enterprise-grade security practices.
  * **Contact** – A comprehensive contact page with a form, office locations, and FAQs.
* **Smooth Scrolling & Animations** – Enhanced user experience with subtle, professional animations.

## 🛠️ Technology Stack

* **Backend Framework**: [Flask](https://flask.palletsprojects.com/) (Python) - Serves the website and handles template rendering.
* **Frontend Languages**: HTML5, CSS3, JavaScript
* **Styling**: Modern CSS with Flexbox, Grid, and CSS Variables for easy theme customization.
* **Typography**: [Google Fonts](https://fonts.google.com/) (Inter font family) for clean, readable text.
* **Icons**: [Font Awesome](https://fontawesome.com/) for consistent, scalable iconography.

## 🚀 Getting Started

Follow these instructions to get a copy of the project running on your local machine for development and testing purposes.

### Prerequisites

* **Python**: Version 3.8 or higher. [Download Python](https://www.python.org/downloads/)
* **pip**: Python package installer (usually comes with Python).
* **Git**: For cloning the repository. [Download Git](https://git-scm.com/downloads)

### Local Development

1.  **Clone the repository**
    ```bash
    git clone https://github.com/AridsWolfgang/PSHUB_Official_Website.git
    cd PSHUB_Official_Website
    ```

2.  **Create a virtual environment** (recommended)
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask development server**
    ```bash
    python app.py
    ```

5.  **View the website**
    Open your web browser and navigate to `http://127.0.0.1:5000/`.

## 📁 Project Structure

```
PSHUB_Official_Website/
├── app.py                  # Main Flask application entry point
├── requirements.txt        # Python dependencies
├── .gitignore              # Files and folders ignored by git
├── README.md               # This file
│
├── static/                  # Static assets (CSS, JS, images)
│   ├── css/                # All CSS files (e.g., about.css, team.css, security.css)
│   ├── js/                 # JavaScript files
│   └── img/                # Image assets
│
└── templates/               # HTML templates (Jinja2)
    ├── components/          # Reusable components (navbar.html, footer.html)
    ├── about.html
    ├── briefing.html
    ├── careers.html
    ├── contact.html
    ├── mission-vision.html
    ├── overview.html
    ├── security.html
    ├── team.html
    └── ... (other HTML files)
```

## 📄 License

**Copyright © 2026 Prosperity System Hub. All rights reserved.**

This project and its content are the proprietary information of Prosperity System Hub. The source code is not licensed for public use, reproduction, or distribution. Please see the `LICENSE` file for more details (or contact for licensing inquiries).

## 🤝 Contact

For inquiries about the website or Prosperity System Hub services:

* **Website**: [Coming Soon]
* **Email**: [Coming Soon]
* **Location**: [Coming Soon]

---

Built with a mission to design and operate prosperity infrastructure at institutional scale.