import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

# ======================== PAGE CONFIGURATION ========================
st.set_page_config(
    page_title="Nico Rivera | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================== CUSTOM CSS STYLING ========================
custom_css = """
<style>
    /* Dark Theme Background */
    .main {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
        color: #DADED8;
    }
    
    .stApp {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #2C3424 0%, #2C583E 100%);
        border-right: 2px solid #959581;
    }
    
    /* Header and Text */
    h1, h2, h3, h4, h5, h6 {
        color: #959581 !important;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    /* Metric Cards */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
        border: 2px solid #959581;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #959581 0%, #768064 100%);
        color: #2C3424 !important;
        border: none;
        border-radius: 5px;
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #768064 0%, #959581 100%);
        box-shadow: 0 0 20px rgba(149, 149, 129, 0.5);
    }
    
    /* Form Elements */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: #2C583E !important;
        color: #DADED8 !important;
        border: 2px solid #959581 !important;
        border-radius: 5px;
    }
    
    /* Progress Bars */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #959581 0%, #768064 100%);
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%) !important;
        border: 1px solid #959581 !important;
        color: #959581 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #959581;
        font-weight: 600;
    }
    
    /* Cards and Containers */
    .project-card {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
        border: 2px solid #959581;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 0 20px rgba(149, 149, 129, 0.2);
    }
    
    .skill-category {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
        border-left: 4px solid #959581;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    /* About Timeline */
    .timeline-item {
        background: linear-gradient(135deg, #2C583E 0%, #2C3424 100%);
        border-left: 4px solid #959581;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    /* Link Colors */
    a {
        color: #959581 !important;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: #DADED8 !important;
        text-shadow: 0 0 10px rgba(218, 222, 216, 0.5);
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# ======================== SIDEBAR CONFIGURATION ========================
with st.sidebar:
    st.markdown("---")
    
    # Profile Picture
    try:
        st.image("images/500198105_2455742341454809_5017422919641977737_n.jpg", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align: center;'>✦</h2>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style='text-align: center; margin: 20px 0;'>
            <h3 style='color: #959581; margin: 15px 0; font-size: 26px;'>Nico Rivera</h3>
            <p style='color: #DADED8; font-size: 14px; margin: 8px 0; font-weight: bold;'>Full Stack Developer</p>
            <p style='color: #DADED8; font-size: 11px; margin: 5px 0; line-height: 1.4;'>Web Developer | Web Designer</p>
            <p style='color: #DADED8; font-size: 11px; margin: 5px 0; line-height: 1.4;'>Database Administrator | Android Developer</p>
            <p style='color: #959581; font-size: 12px; margin: 10px 0; font-weight: 600;'>⊙ Cebu City, Philippines</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Navigation Menu
    st.markdown("<h4 style='color: #959581;'>◉ Navigation</h4>", unsafe_allow_html=True)
    page = st.radio(
        "Select Section:",
        ["⌂ Home", "✦ About Me", "✈ Projects", "◈ Skills", "✉ Contact"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Contact Information
    st.markdown("<h4 style='color: #959581;'>☎ Contact Info</h4>", unsafe_allow_html=True)
    
    st.markdown(
        """
        ✉ **Email:**  
        [rivera.nicon2020@gmail.com](mailto:rivera.nicon2020@gmail.com)
        
        ☎ **Phone:**  
        [+63-927-895-3465](tel:+63-927-895-3465)
        
        ∞ **LinkedIn:**  
        [linkedin.com/in/nico-rivera](https://www.linkedin.com/in/nico-rivera-284a76335)
        
        ⬚ **GitHub:**  
        [github.com/NicoRivera](https://github.com)
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("---")
    
    # Resume Download
    st.markdown("<h4 style='color: #959581;'>↓ Download</h4>", unsafe_allow_html=True)
    with open("RESUME.pdf", "rb") as pdf_file:
        st.download_button(
            label="◇ Download Resume",
            data=pdf_file.read(),
            file_name="Nico_Rivera_Resume.pdf",
            mime="application/pdf"
        )

# ======================== HOME PAGE ========================
if page == "⌂ Home":
    # Hero Section with Profile
    hero_col1, hero_col2 = st.columns([1.2, 1])
    
    with hero_col1:
        st.markdown(
            """
            <h1 style='color: #959581; font-size: 48px; margin: 20px 0; font-weight: 900;'>
            Nico Rivera
            </h1>
            <p style='color: #DADED8; font-size: 26px; margin: 10px 0; font-weight: bold;'>
            Full Stack Developer & Web Designer
            </p>
            <p style='color: #DADED8; font-size: 16px; margin: 20px 0; line-height: 1.6;'>
            I create innovative digital solutions combining <b>frontend design</b>, <b>backend development</b>, 
            and <b>mobile app creation</b>. Specializing in building scalable, user-centric applications 
            that solve real-world problems.
            </p>
            """,
            unsafe_allow_html=True
        )
        
        # Skills Preview
        st.markdown("<h4 style='color: #959581; margin-top: 30px;'>✦ Areas of Expertise</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - ◆ **Frontend Dev** (React, Tailwind CSS)
            - ⚙ **Backend Dev** (Django, Spring Boot)
            - ☎ **Mobile Dev** (Android, Firebase)
            """)
        with col2:
            st.markdown("""
            - ◈ **Database Design** (MySQL, PostgreSQL)
            - ⊙ **UI/UX Design** (Figma, Webflow)
        - ☁️ **Cloud & DevOps** (Heroku, AWS)
            """)
    
    with hero_col2:
        try:
            st.image("images/499568957_2449014205460956_6590885767829635378_n.jpg", use_container_width=True)
        except:
            st.info("Profile image unavailable")
    
    st.markdown("---")
    
    # Key Metrics
    st.markdown("<h2 style='color: #959581; text-align: center;'>▲ Key Metrics</h2>", unsafe_allow_html=True)
    
    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
    
    with metric_col1:
        st.metric("✦ Years Coding", "3+", "+1 Year")
    
    with metric_col2:
        st.metric("◇ Projects Built", "15+", "+5 Projects")
    
    with metric_col3:
        st.metric("◈ Technologies", "20+", "Expanding")
    
    with metric_col4:
        st.metric("★ Certifications", "5+", "Growing")
    
    st.markdown("---")
    
    # Professional Summary
    st.markdown("<h3 style='color: #959581;'>○ Professional Summary</h3>", unsafe_allow_html=True)
    
    summary_tab1, summary_tab2, summary_tab3 = st.tabs(["◈ Current Focus", "★ Education", "✦ Achievements"])
    
    with summary_tab1:
        st.write("""
        - Building scalable full-stack applications
        - Designing responsive web interfaces
        - Database optimization and management
        - Mobile app development for Android
        - DevOps and deployment strategies
        """)
    
    with summary_tab2:
        st.write("""
        - **Current:** Student at Cebu Institute of Technology
        - Specializing in Information Technology
        - Focus on Enterprise Software Development
        - Active in tech community events
        """)
    
    with summary_tab3:
        st.write("""
        - ✅ Developed and deployed multiple production applications
        - ✅ Led frontend UI/UX improvements resulting in 40% better engagement
        - ✅ Implemented database optimization reducing query time by 60%
        - ✅ Built Android apps with 10k+ downloads
        """)
    
    st.markdown("---")
    
    # Location Map
    st.markdown("<h3 style='color: #959581;'>Based In</h3>", unsafe_allow_html=True)
    location_data = pd.DataFrame(
        [[10.3157, 123.8854]],
        columns=['lat', 'lon']
    )
    st.map(location_data, zoom=12)
    st.caption("Cebu City, Philippines - Open to remote and on-site opportunities")

# ======================== ABOUT ME PAGE ========================
elif page == "✦ About Me":
    # About Hero Section
    about_col1, about_col2 = st.columns([1, 1.2])
    
    with about_col1:
        try:
            st.image("images/484034358_2384792711883106_1254686447363104009_n.jpg", use_container_width=True)
        except:
            st.info("Profile image unavailable")
    
    with about_col2:
        st.markdown(
            """
            <h1 style='color: #959581; font-size: 44px; margin: 0 0 20px 0;'>About Me</h1>
            <p style='color: #DADED8; font-size: 16px; line-height: 1.8; margin: 20px 0;'>
            I'm a passionate <b>Full Stack Developer</b> and <b>Web Designer</b> from Cebu City, Philippines, 
            dedicated to creating innovative digital solutions that combine technical excellence with 
            exceptional user experiences.
            </p>
            """,
            unsafe_allow_html=True
        )
        
        with st.expander("My Story", expanded=True):
            st.markdown("""
            My journey into technology began with a simple curiosity - "How does this work?" That question 
            led me to explore web development, mobile app creation, and database management. Today, I'm 
            a versatile full-stack developer combining technical expertise with creative design thinking.
            
            Currently studying at **Cebu Institute of Technology**, I'm honing my skills in:
            - Enterprise software architecture
            - Cloud technologies
            - UI/UX design principles
            - DevOps practices
            
            **My Philosophy:** Code is not just about functionality; it's about creating experiences 
            that matter. Every project is an opportunity to solve real problems and make a positive impact.
            """)
    
    st.markdown("---")
    
    # Technical Journey Timeline
    st.markdown("<h3 style='color: #959581;'>Technical Journey</h3>", unsafe_allow_html=True)
    
    timeline_col1, timeline_col2 = st.columns(2)
    
    with timeline_col1:
        st.markdown("""
        <div class='timeline-item'>
            <h4>Beginner Phase</h4>
            <p><b>Year 1-2:</b> Started with HTML, CSS, and JavaScript. Built static websites and learned web fundamentals.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='timeline-item'>
            <h4>Growth Phase</h4>
            <p><b>Year 2-3:</b> Mastered backend with Django and Spring Boot. Explored database design with MySQL.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with timeline_col2:
        st.markdown("""
        <div class='timeline-item'>
            <h4>Diversification</h4>
            <p><b>Year 3:</b> Ventured into Android development. Got comfortable with Webflow for rapid prototyping.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='timeline-item'>
            <h4>Current</h4>
            <p><b>Now:</b> Full-stack developer focused on creating end-to-end solutions with modern tech stack.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skills Overview
    st.markdown("<h3 style='color: #959581;'>Areas of Expertise</h3>", unsafe_allow_html=True)
    
    expertise_tabs = st.tabs(["Frontend", "Backend", "Database", "Mobile", "Tools"])
    
    with expertise_tabs[0]:
        st.markdown("""
        <div class='skill-category'>
            <h4 style='color: #959581; margin: 0;'>Frontend Technologies</h4>
            <ul>
                <li><b>HTML5 & CSS3:</b> Semantic markup and modern responsive design</li>
                <li><b>JavaScript:</b> DOM manipulation, ES6+, async programming</li>
                <li><b>React:</b> Component-based architecture, hooks, state management</li>
                <li><b>Tailwind CSS:</b> Utility-first CSS framework</li>
                <li><b>Framer Motion:</b> Advanced animations and interactions</li>
                <li><b>ShadCN:</b> Component library for beautifully designed UIs</li>
                <li><b>Webflow:</b> No-code/low-code web design</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with expertise_tabs[1]:
        st.markdown("""
        <div class='skill-category'>
            <h4 style='color: #959581; margin: 0;'>Backend Technologies</h4>
            <ul>
                <li><b>Django:</b> Python web framework with ORM and admin panel</li>
                <li><b>Spring Boot:</b> Java enterprise applications</li>
                <li><b>REST APIs:</b> RESTful architecture and API design</li>
                <li><b>Authentication:</b> JWT, OAuth, session management</li>
                <li><b>Microservices:</b> Distributed system architecture</li>
                <li><b>Node.js:</b> JavaScript runtime for backend</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with expertise_tabs[2]:
        st.markdown("""
        <div class='skill-category'>
            <h4 style='color: #959581; margin: 0;'>Database & Data Management</h4>
            <ul>
                <li><b>MySQL:</b> Relational database design and optimization</li>
                <li><b>SQL:</b> Complex queries, joins, normalization</li>
                <li><b>Database Design:</b> Schema design, indexing, relationships</li>
                <li><b>NoSQL:</b> MongoDB, Firebase</li>
                <li><b>Data Analysis:</b> SQL analytics, reporting</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with expertise_tabs[3]:
        st.markdown("""
        <div class='skill-category'>
            <h4 style='color: #959581; margin: 0;'>Mobile Development</h4>
            <ul>
                <li><b>Android:</b> Java/Kotlin, Android Studio</li>
                <li><b>Material Design:</b> Modern Android UI patterns</li>
                <li><b>Firebase:</b> Real-time database and authentication</li>
                <li><b>App Publishing:</b> Google Play Store deployment</li>
                <li><b>Mobile UX:</b> Touch-friendly interfaces, responsiveness</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with expertise_tabs[4]:
        st.markdown("""
        <div class='skill-category'>
            <h4 style='color: #959581; margin: 0;'>Development Tools & Platforms</h4>
            <ul>
                <li><b>Version Control:</b> Git, GitHub</li>
                <li><b>IDEs:</b> VS Code, Android Studio, IntelliJ IDEA</li>
                <li><b>Deployment:</b> Heroku, Vercel, AWS</li>
                <li><b>Testing:</b> Unit testing, integration testing</li>
                <li><b>Databases:</b> phpMyAdmin, MongoDB Compass</li>
                <li><b>API Testing:</b> Postman, Insomnia</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Additional Info
    st.markdown("<h3 style='color: #959581;'>Education & Learning</h3>", unsafe_allow_html=True)
    
    education_col1, education_col2 = st.columns(2)
    
    with education_col1:
        with st.expander("Current Education"):
            st.write("""
            **Cebu Institute of Technology (CIT)**
            - Program: Bachelor of Science in Information Technology
            - Specialization: Enterprise Software Development
            - Expected Graduation: 2024-2025
            - Active participant in tech community and hackathons
            """)
    
    with education_col2:
        with st.expander("Continuous Learning"):
            st.write("""
            - Advanced web development frameworks
            - Cloud architecture and DevOps
            - UI/UX design principles
            - Emerging technologies (AI/ML)
            - Open source contributions
            """)
    
    st.markdown("---")
    
    # Interests & Hobbies
    st.markdown("<h3 style='color: #959581;'>Interests & Passions</h3>", unsafe_allow_html=True)
    
    interests = st.multiselect(
        "Check out my interests:",
        ["Coding", "UI/UX Design", "Tech Innovation", "Gaming", 
         "Music", "Reading", "Traveling", "Fitness"],
        default=["Coding", "UI/UX Design", "Tech Innovation"],
        disabled=True
    )

# ======================== PROJECTS PAGE ========================
elif page == "✈ Projects":
    st.markdown(
        """
        <h1 style='color: #959581; font-size: 44px; margin: 30px 0;'>My Projects</h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <p style='color: #DADED8; font-size: 16px; line-height: 1.8; margin: 20px 0;'>
    Discover my portfolio of innovative projects showcasing expertise in <b>full-stack development</b>, 
    <b>mobile app creation</b>, and <b>modern web design</b>. Each project demonstrates my commitment to 
    quality, scalability, and solving real-world problems with cutting-edge technology.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Project 1: Pocketwise
    st.markdown(
        """
        <div class='project-card'>
            <h3>Pocketwise - Android E-Wallet App</h3>
            <p><b>Category:</b> Mobile Application | <b>Status:</b> Published on Google Play Store</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander("View Details", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Description:**
            Pocketwise is a comprehensive mobile e-wallet application designed to help users manage 
            their finances on the go.
            
            **Key Features:**
            - 💰 Digital wallet management
            - ◈ Transaction history and analytics
            - ◇ Secure authentication with biometric support
            - 💳 Multiple payment methods integration
            - △ Spending insights and budgeting tools
            - 🔔 Real-time notifications
            
            **Tech Stack:**
            - **Platform:** Android (Java/Kotlin)
            - **Database:** Firebase Realtime Database
            - **Authentication:** Firebase Auth
            - **UI:** Material Design 3
            - **Architecture:** MVVM Pattern
            """)
        
        with col2:
            st.info("Download:  \nGoogle Play Store")
            st.write("Rating: 4.8/5  \nUsers: 10k+  \nReleased: 2023")
        
        with st.expander("Code Sample"):
            st.code("""
// Pocketwise Transaction Model
data class Transaction(
    val id: String,
    val amount: Double,
    val type: String,
    val category: String,
    val timestamp: Long,
    val description: String
)

// Firebase transaction handler
fun addTransaction(transaction: Transaction) {
    db.collection("transactions")
        .add(transaction)
        .addOnSuccessListener { 
            Log.d("Pocketwise", "Transaction added")
        }
}
            """, language='kotlin')
    
    st.markdown("---")
    
    # Project 2: Poll Pro
    st.markdown(
        """
        <div class='project-card'>
            <h3>Poll Pro - Spring Boot Poll Management System</h3>
            <p><b>Category:</b> Web Application (Backend) | <b>Status:</b> Production Ready</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander("View Details", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Description:**
            Poll Pro is a robust backend system for creating, managing, and analyzing polls and surveys.
            
            **Key Features:**
            - ◈ Create and customize polls
            - 🗳️ Real-time voting system
            - △ Advanced analytics and statistics
            - 👥 User management and roles
            - ◇ JWT authentication
            - 🔀 RESTful API endpoints
            - ☎ Mobile-friendly API
            
            **Tech Stack:**
            - **Framework:** Spring Boot
            - **Language:** Java 11+
            - **Database:** MySQL
            - **Authentication:** JWT
            - **API Documentation:** Swagger/OpenAPI
            - **Testing:** JUnit, Mockito
            """)
        
        with col2:
            st.success("✅ **Status:** Active")
            st.write("◈ **Endpoints:** 25+  \n✦ **API:** REST  \n◇ **Security:** JWT")
        
        with st.expander("⚙ Code Sample"):
            st.code("""
@RestController
@RequestMapping("/api/polls")
public class PollController {
    
    @PostMapping
    public ResponseEntity<Poll> createPoll(@RequestBody PollRequest request) {
        Poll poll = pollService.createPoll(request);
        return ResponseEntity.ok(poll);
    }
    
    @GetMapping("/{id}/results")
    public ResponseEntity<PollResults> getPollResults(@PathVariable String id) {
        PollResults results = pollService.getResults(id);
        return ResponseEntity.ok(results);
    }
}
            """, language='java')
    
    st.markdown("---")
    
    # Project 3: React Landing Page
    st.markdown(
        """
        <div class='project-card'>
            <h3>✦ React Landing Page - Dark UI with Animations</h3>
            <p><b>Category:</b> Frontend | <b>Status:</b> Deployed</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander("◊ View Details", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Description:**
            A modern, visually stunning landing page built with React, featuring smooth animations 
            and a sleek dark theme design.
            
            **Key Features:**
            - ✦ Modern dark UI design
            - ✨ Smooth scroll animations
            - ◈ Fully responsive layout
            - ⚡ Optimized performance
            - ◊ Framer Motion animations
            - ◇ Component-based architecture
            - ◈ SEO optimized
            
            **Tech Stack:**
            - **Framework:** React 18
            - **Styling:** Tailwind CSS
            - **Animations:** Framer Motion
            - **UI Components:** ShadCN
            - **Build Tool:** Vite
            - **Deployment:** Vercel
            """)
        
        with col2:
            st.info("◇ **Live:** vercel.app")
            st.write("✦ **Performance:** 98/100  \n⊙ **SEO:** Optimized  \n▲ **Load:** <1s")
        
        with st.expander("⚙ Code Sample"):
            st.code("""
import { motion } from 'framer-motion';

export function HeroSection() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="flex flex-col items-center justify-center h-screen"
    >
      <h1 className="text-6xl font-bold text-cyan-400">
        Welcome to My Portfolio
      </h1>
      <motion.button
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className="mt-8 px-8 py-3 bg-cyan-500 rounded"
      >
        Explore More
      </motion.button>
    </motion.div>
  );
}
            """, language='javascript')
    
    st.markdown("---")
    
    # Project 4: Django Health Records System
    st.markdown(
        """
        <div class='project-card'>
            <h3>🏥 Django Health Records System</h3>
            <p><b>Category:</b> Full-Stack Web Application | <b>Status:</b> In Development</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    with st.expander("🏥 View Details", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            **Description:**
            A comprehensive healthcare management system for storing and retrieving patient 
            health records with role-based access control.
            
            **Key Features:**
            - → Patient management
            - ◈ Medical records storage
            - 💊 Prescription management
            - ◈ Health analytics
            - 👥 Doctor appointment scheduling
            - ◇ Role-based access control
            - ☎ Mobile responsive design
            
            **Tech Stack:**
            - **Backend:** Django, Django REST Framework
            - **Database:** PostgreSQL
            - **Frontend:** Bootstrap 5
            - **Authentication:** Django Auth + JWT
            - **Deployment:** Docker
            """)
        
        with col2:
            st.warning("◊ **Status:** In Progress")
            st.write("□ **Backend:** 80%  \n✦ **Frontend:** 60%  \n☎ **Mobile:** 40%")
        
        with st.expander("⚙ Code Sample"):
            st.code("""
from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    recorded_date = models.DateTimeField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()
    
    class Meta:
        ordering = ['-recorded_date']
            """, language='python')
    
    st.markdown("---")
    
    # Project Stats
    st.markdown("<h3 style='color: #959581;'>◈ Project Statistics</h3>", unsafe_allow_html=True)
    
    project_data = pd.DataFrame({
        'Project': ['Pocketwise', 'Poll Pro', 'React Landing', 'Django Health'],
        'Type': ['Mobile', 'Backend', 'Frontend', 'Full-Stack'],
        'Status': ['Deployed', 'Deployed', 'Deployed', 'In-Progress'],
        'Complexity': [8, 9, 7, 9],
        'Users': [10000, 500, 50000, 100]
    })
    
    chart = alt.Chart(project_data).mark_bar().encode(
        x=alt.X('Project:N', sort=['Pocketwise', 'Poll Pro', 'React Landing', 'Django Health']),
        y=alt.Y('Complexity:Q', scale=alt.Scale(domain=[0, 10])),
        color=alt.Color('Type:N', scale=alt.Scale(scheme='category10'))
    ).properties(height=400, width=600)
    
    st.altair_chart(chart, use_container_width=True)

# ======================== SKILLS PAGE ========================
elif page == "◈ Skills":
    st.markdown(
        """
        <h1 style='color: #959581; font-size: 44px; margin: 30px 0;'>My Skills ◈</h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <p style='color: #DADED8; font-size: 16px; line-height: 1.8; margin: 20px 0;'>
    A comprehensive overview of my <b>technical proficiencies</b>, <b>expertise areas</b>, and 
    <b>professional capabilities</b>. Constantly expanding my knowledge with emerging technologies 
    and best practices in software development.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Skill Proficiency Levels
    st.markdown("<h3 style='color: #959581;'>❤ Skill Proficiency</h3>", unsafe_allow_html=True)
    
    skills_data = {
        'Frontend': {
            'HTML5 & CSS3': 95,
            'JavaScript (ES6+)': 90,
            'React': 88,
            'Tailwind CSS': 92,
            'Framer Motion': 85
        },
        'Backend': {
            'Django': 87,
            'Spring Boot': 85,
            'REST APIs': 90,
            'Node.js': 80,
            'Python': 88
        },
        'Database': {
            'MySQL': 89,
            'SQL': 91,
            'MongoDB': 75,
            'Firebase': 82,
            'PostgreSQL': 80
        },
        'Mobile': {
            'Android (Java)': 84,
            'iOS Basics': 60,
            'Firebase (Mobile)': 85,
            'Material Design': 88
        },
        'Tools': {
            'Git & GitHub': 92,
            'Docker': 70,
            'Postman': 88,
            'VS Code': 94,
            'Linux': 78
        }
    }
    
    skill_tabs = st.tabs(['✦ Frontend', '⚙ Backend', '◈ Database', '☎ Mobile', '⚙ Tools'])
    
    tabs_data = [
        skills_data['Frontend'],
        skills_data['Backend'],
        skills_data['Database'],
        skills_data['Mobile'],
        skills_data['Tools']
    ]
    
    for tab, skill_category in zip(skill_tabs, tabs_data):
        with tab:
            for skill_name, proficiency in skill_category.items():
                col1, col2, col3 = st.columns([2, 3, 1])
                
                with col1:
                    st.write(f"**{skill_name}**")
                
                with col2:
                    st.progress(proficiency / 100)
                
                with col3:
                    st.write(f"{proficiency}%")
    
    st.markdown("---")
    
    # Technology Stack Visualization
    st.markdown("<h3 style='color: #959581;'>◆ Technology Distribution</h3>", unsafe_allow_html=True)
    
    tech_stack = pd.DataFrame({
        'Technology': ['JavaScript', 'Python', 'Java', 'SQL', 'HTML/CSS', 'React', 'Django', 'Spring Boot'],
        'Proficiency': [90, 88, 85, 91, 95, 88, 87, 85]
    })
    
    bar_chart = alt.Chart(tech_stack).mark_bar().encode(
        x=alt.X('Proficiency:Q', scale=alt.Scale(domain=[0, 100])),
        y=alt.Y('Technology:N', sort='-x'),
        color=alt.Color('Proficiency:Q', scale=alt.Scale(scheme='viridis'))
    ).properties(height=400, width=700)
    
    st.altair_chart(bar_chart, use_container_width=True)
    
    st.markdown("---")
    
    # Learning Roadmap
    st.markdown("<h3 style='color: #959581;'>▪ Learning Roadmap</h3>", unsafe_allow_html=True)
    
    roadmap_col1, roadmap_col2 = st.columns(2)
    
    with roadmap_col1:
        st.markdown("""
        <div class='skill-category'>
            <h4>✅ Completed</h4>
            <ul>
                <li>Full-stack web development</li>
                <li>Mobile app development</li>
                <li>Database design & optimization</li>
                <li>REST API development</li>
                <li>Cloud deployment basics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with roadmap_col2:
        st.markdown("""
        <div class='skill-category'>
            <h4>▲ In Progress / Next</h4>
            <ul>
                <li>Kubernetes & DevOps</li>
                <li>Machine Learning basics</li>
                <li>GraphQL</li>
                <li>Microservices architecture</li>
                <li>Cloud optimization (AWS)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Soft Skills
    st.markdown("<h3 style='color: #959581;'>★ Soft Skills</h3>", unsafe_allow_html=True)
    
    soft_skills_col1, soft_skills_col2, soft_skills_col3 = st.columns(3)
    
    with soft_skills_col1:
        st.markdown("""
        **Communication**
        """)
        st.progress(0.85)
    
    with soft_skills_col2:
        st.markdown("""
        **Problem Solving**
        """)
        st.progress(0.90)
    
    with soft_skills_col3:
        st.markdown("""
        **Teamwork**
        """)
        st.progress(0.88)
    
    soft_skills_col4, soft_skills_col5, soft_skills_col6 = st.columns(3)
    
    with soft_skills_col4:
        st.markdown("""
        **Time Management**
        """)
        st.progress(0.87)
    
    with soft_skills_col5:
        st.markdown("""
        **Adaptability**
        """)
        st.progress(0.92)
    
    with soft_skills_col6:
        st.markdown("""
        **Leadership**
        """)
        st.progress(0.80)
    
    st.markdown("---")
    
    # Certifications
    st.markdown("<h3 style='color: #959581;'>✦ Certifications</h3>", unsafe_allow_html=True)
    
    certifications = {
        '★ Certificate 1': 'Full-Stack Web Development (2023)',
        '🏅 Certificate 2': 'Android App Development Masterclass (2023)',
        '★ Certificate 3': 'Spring Boot for Enterprise (2024)',
        '◇ Certificate 4': 'Database Design & Optimization (2024)',
        '☁️ Certificate 5': 'Cloud Fundamentals (2024)'
    }
    
    cert_col1, cert_col2, cert_col3 = st.columns(3)
    
    cert_columns = [cert_col1, cert_col2, cert_col3]
    
    for idx, (cert_title, cert_desc) in enumerate(certifications.items()):
        with cert_columns[idx % 3]:
            st.info(f"{cert_title}\n\n{cert_desc}")

# ======================== CONTACT PAGE ========================
elif page == "✉ Contact":
    st.markdown(
        """
        <h1 style='color: #959581; font-size: 44px; margin: 30px 0;'>Get In Touch ✉</h1>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("""
    <p style='color: #DADED8; font-size: 16px; line-height: 1.8; margin: 20px 0;'>
    I'm always interested in hearing about new projects and opportunities. Whether you have a 
    specific project in mind, have questions about my work, or simply want to connect and discuss 
    ideas, I'd love to hear from you. <b>Let's create something amazing together!</b>
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Contact Form
    st.markdown("<h3 style='color: #959581;'>📧 Send Me a Message</h3>", unsafe_allow_html=True)
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input(
                "Your Name",
                placeholder="Enter your full name",
                key="name_input"
            )
        
        with col2:
            email = st.text_input(
                "Your Email",
                placeholder="your.email@example.com",
                key="email_input"
            )
        
        subject = st.text_input(
            "Subject",
            placeholder="What's this about?",
            key="subject_input"
        )
        
        message = st.text_area(
            "Message",
            placeholder="Tell me about your project or inquiry...",
            height=200,
            key="message_input"
        )
        
        # Additional options
        col_opt1, col_opt2 = st.columns(2)
        
        with col_opt1:
            contacted_reason = st.selectbox(
                "I'm reaching out because:",
                ["☊ Project Collaboration", "✦ Job Opportunity", "❔ Inquiry", "★ Learning Question", "❤ Other"]
            )
        
        with col_opt2:
            budget_checkbox = st.checkbox("I have a project budget in mind")
        
        form_priority = st.radio(
            "Priority Level:",
            ["Low", "Medium", "High"],
            horizontal=True
        )
        
        submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you for your message!")
                st.success(f"I've received your message, {name}. I'll get back to you shortly!")
                st.balloons()
            else:
                st.warning("⚠️ Please fill in all required fields.")
    
    st.markdown("---")
    
    # Quick Contact Options
    st.markdown("<h3 style='color: #959581;'>📞 Quick Contact Options</h3>", unsafe_allow_html=True)
    
    contact_col1, contact_col2, contact_col3 = st.columns(3)
    
    with contact_col1:
        st.markdown("""
        <div class='project-card' style='text-align: center;'>
            <h4>📧 Email</h4>
            <p><a href='mailto:rivera.nicon2020@gmail.com'>rivera.nicon2020@gmail.com</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_col2:
        st.markdown("""
        <div class='project-card' style='text-align: center;'>
            <h4>📞 Phone</h4>
            <p><a href='tel:+63-927-895-3465'>+63-927-895-3465</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    with contact_col3:
        st.markdown("""
        <div class='project-card' style='text-align: center;'>
            <h4>🔗 LinkedIn</h4>
            <p><a href='https://www.linkedin.com/in/nico-rivera-284a76335'>Connect with me</a></p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Social Links
    st.markdown("<h3 style='color: #959581;'>∞ Connect on Social Media</h3>", unsafe_allow_html=True)
    
    social_col1, social_col2, social_col3, social_col4 = st.columns(4)
    
    with social_col1:
        if st.button("🔗 LinkedIn", use_container_width=True):
            st.markdown("[Visit LinkedIn](https://www.linkedin.com/in/nico-rivera-284a76335)")
    
    with social_col2:
        if st.button("✦ GitHub", use_container_width=True):
            st.markdown("[Visit GitHub](https://github.com)")
    
    with social_col3:
        if st.button("🐦 Twitter", use_container_width=True):
            st.markdown("[Visit Twitter](https://twitter.com)")
    
    with social_col4:
        if st.button("☎ Instagram", use_container_width=True):
            st.markdown("[Visit Instagram](https://instagram.com)")
    
    st.markdown("---")
    
    # Response Time Info
    st.info("⏱️ **Response Time**: I typically respond to messages within 24 hours. For urgent matters, feel free to call me directly.")
    
    st.markdown("---")
    
    # FAQ Section
    st.markdown("<h3 style='color: #959581;'>❔ Frequently Asked Questions</h3>", unsafe_allow_html=True)
    
    faq_tab1, faq_tab2 = st.tabs(["General", "Technical"])
    
    with faq_tab1:
        with st.expander("🤔 What services do you offer?"):
            st.write("""
            I offer a wide range of services including:
            - Full-stack web development
            - Mobile app development (Android)
            - UI/UX design
            - Database design and optimization
            - API development
            - Consulting and technical advice
            """)
        
        with st.expander("💰 What's your rate?"):
            st.write("""
            Rates vary depending on project complexity, scope, and timeline. 
            I offer competitive pricing for startups and enterprise clients. 
            Let's discuss your specific needs!
            """)
        
        with st.expander("⏰ How long do projects usually take?"):
            st.write("""
            Project duration depends on complexity:
            - Small projects: 1-2 weeks
            - Medium projects: 2-4 weeks
            - Large projects: 1-3 months+
            """)
    
    with faq_tab2:
        with st.expander("⚙ What tech stack do you use?"):
            st.write("""
            My preferred tech stack:
            - Frontend: React, Tailwind CSS, Framer Motion
            - Backend: Django, Spring Boot, Node.js
            - Database: MySQL, PostgreSQL
            - Mobile: Android (Java/Kotlin)
            """)
        
        with st.expander("🏗️ Do you work with legacy systems?"):
            st.write("""
            Yes! I have experience working with and modernizing legacy systems. 
            I can help with migrations, refactoring, and system upgrades.
            """)
        
        with st.expander("☁️ Do you handle deployment?"):
            st.write("""
            Yes, I can handle deployment on various platforms including:
            - Heroku, Vercel, AWS, DigitalOcean
            - Docker containerization
            - CI/CD pipeline setup
            """)

# ======================== FOOTER ========================
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px; color: #959581;'>
        <p>© 2024 Nico Rivera | Full Stack Developer & Designer | Based in Cebu City, Philippines</p>
        <p style='color: #DADED8; font-size: 12px;'>Built with ❤ using Streamlit | Last Updated: February 2026</p>
    </div>
    """,
    unsafe_allow_html=True
)
