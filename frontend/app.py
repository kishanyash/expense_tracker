import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

# Page configuration
st.set_page_config(
    page_title="Expense Tracker Pro",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main container styling */
    .main > div {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    
    .header-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
/* Make tabs symmetric */
.stTabs [data-baseweb="tab-list"] {
    display: flex;
    justify-content: center;
    gap: 10px;
    background-color: #f8f9fa;
    padding: 8px;
    border-radius: 10px;
    margin-bottom: 2rem;
}

.stTabs [data-baseweb="tab"] {
    flex: 1;  /* Equal width */
    text-align: center;
    height: 50px;
    padding: 0px 24px;
    border-radius: 8px;
    font-weight: 600;
    border: 2px solid transparent;
    transition: all 0.3s ease;
    background: #ffffff;
    color: #2c3e50;
}

/* Active tab - Green */
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
    color: white !important;
    border: none;
    box-shadow: 0 4px 8px rgba(0,0,0,0.15);
}

/* Hover effect (Green tint) */
.stTabs [data-baseweb="tab"]:hover {
    background: #e9fff4;
    border: 1px solid #38ef7d;
    color: #11998e;
    cursor: pointer;
}

    
    /* Card styling */
    .expense-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #e9ecef;
        margin-bottom: 1.5rem;
    }
    
    .analytics-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #dee2e6;
        margin-bottom: 1.5rem;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Form styling */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > div,
    .stTextInput > div > div > input,
    .stDateInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e9ecef;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > div:focus,
    .stTextInput > div > div > input:focus,
    .stDateInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Success/Error message styling */
    .stSuccess {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stError {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* Table styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Chart styling */
    .stPlotlyChart {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Metric styling */
    .metric-container {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        text-align: center;
        border: 1px solid #e9ecef;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="header-container">
    <h1 class="header-title">💰 Expense Tracker Pro</h1>
    <p class="header-subtitle">Manage your finances with style and precision</p>
</div>
""", unsafe_allow_html=True)

# Main application tabs
tab1, tab2 = st.tabs(["📝 Add/Update Expenses", "📊 Analytics Dashboard"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #6c757d; padding: 1rem;'>"
    "Built with ❤️ by Kishan | Professional Expense Management System"
    "</div>", 
    unsafe_allow_html=True
)