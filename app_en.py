import streamlit as st
import pandas as pd
import base64

# Função para gerar logos e ícones em Base64 para exibição no Streamlit
def render_header_with_icon(image_path, title_text, icon_width=35):
    """Converte a imagem para Base64 e renderiza o título com o ícone alinhado."""
    with open(image_path, "rb") as image_file:
        img_base64 = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
            <img src="data:image/png;base64,{img_base64}" width="{icon_width}" style="vertical-align: middle;">
            <h3 style="margin: 0;">{title_text}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

@st.dialog("Professional Certifications")
def show_certificates():
    st.write("View certificates of completed courses and training programs:")
    
    # Exemplo de exibição dos certificados (substitua pelos nomes reais dos seus ficheiros de imagem)
    st.image("images/sql_data_science.png", caption="SQL for Data Science – Coursera")
    st.image("images/sql_problem_solving.png", caption="SQL Problem Solving – Coursera")
    st.image("images/sql_capstone_project.png", caption="SQL for Data Science Capstone Project – Coursera")
    
    if st.button("Close"):
        st.rerun()


# Configuração da página
st.set_page_config(
    page_title="João Silva | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS personalizada (Fonte Bebas Neue + Estilo FC88 + Ícones e Destaques)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;800&display=swap');

    /* Ocultar cabeçalho nativo do Streamlit */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        z-index: 1;
    }
    
    .stAppDeployButton, #MainMenu, footer {
        visibility: hidden;
        display: none !important;
    }

    /* 1. ESTILIZAÇÃO COMPLETA DA SIDEBAR (Estilo FC88) */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 2px solid #334155 !important;
    }

    /* Título do Menu na Sidebar */
    .menu-title {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 2.8rem !important;
        color: #38bdf8 !important;
        letter-spacing: 2px !important;
        margin-bottom: 20px !important;
        text-transform: uppercase !important;
    }

    /* Botões do Menu na Sidebar */
    section[data-testid="stSidebar"] .stButton button {
        background-color: transparent !important;
        color: #f8fafc !important;
        font-family: 'Bebas Neue', cursive, sans-serif !important;
        font-size: 2.2rem !important;
        letter-spacing: 2.5px !important;
        text-transform: uppercase !important;
        border: none !important;
        border-bottom: 2px dashed #38bdf8 !important;
        border-radius: 0px !important;
        width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
        padding: 12px 5px !important;
        margin-bottom: 10px !important;
        transition: all 0.3s ease !important;
    }

    /* Efeito Hover na Sidebar */
    section[data-testid="stSidebar"] .stButton button:hover {
        color: #38bdf8 !important;
        padding-left: 15px !important;
        border-bottom: 2px solid #38bdf8 !important;
        background-color: #0f172a !important;
    }

    /* Botão de abrir/fechar sidebar */
    .stApp header button, 
    button[aria-label="Expand sidebar"], 
    [data-testid="stHeader"] button,
    section[data-testid="stSidebar"] button[aria-label="Collapse sidebar"],
    section[data-testid="stSidebar"] button {
        background-color: #f59e0b !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px !important;
        padding: 4px !important;
    }

    .stApp header button svg *,
    section[data-testid="stSidebar"] button svg * {
        color: #ffffff !important;
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }

    /* Background geral escuro */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Títulos principais */
    h1, h2, h3 {
        color: #ffffff !important;
        font-family: 'Bebas Neue', sans-serif !important;
        letter-spacing: 1px !important;
    }
    
    /* Badge de status */
    .badge {
        background-color: #0284c7;
        color: white;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
    }

    /* Subtítulo Destaque */
    .subtitle-text {
        font-size: 1.25rem;
        color: #ffffff;
        font-weight: 500;
        margin-top: -10px;
        margin-bottom: 10px;
    }

    /* Frase de Impacto */
    .impact-text {
        font-family: 'Bebas Neue', sans-serif;
        font-size: 1.8rem;
        color: #29B6FF;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    
    /* Cartões de métricas e listas */
    .metric-card {
        background-color: #1e293b;
        padding: 18px;
        border-radius: 10px;
        border-left: 4px solid #38bdf8;
        margin-bottom: 15px;
        color: #f8fafc;
    }

    /* Expander Estilizado */
    div[data-testid="stExpander"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }

    div[data-testid="stExpander"] details summary {
        background-color: #1e293b !important;
        color: #ffffff !important;
        padding: 12px !important;
        border-radius: 8px !important;
    }

    div[data-testid="stExpander"] details summary p {
        color: #38bdf8 !important;
        font-weight: bold !important;
        font-size: 1.05em !important;
    }

    div[data-testid="stExpander"] details {
        background-color: #0f172a !important;
        border-radius: 8px !important;
        padding: 15px;
    }
    /* Estilização e correção do hover nos botões de link (LinkedIn e GitHub) */
    .stApp div[data-testid="stLinkButton"] a {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
        transition: all 0.3s ease !important;
    }

    .stApp div[data-testid="stLinkButton"] a:hover {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
        border-color: #38bdf8 !important;
    }

    .stApp div[data-testid="stLinkButton"] a:hover * {
        color: #0f172a !important;
    }

    /* Cor branca para os labels dos componentes (Selectbox, Inputs de Texto e Textareas) */
    .stSelectbox label, .stTextInput label, .stTextArea label {
        color: #f8fafc !important;
        font-weight: 600 !important;
    }

    /* Estilização e cor do texto do botão de Enviar do formulário */
    .stFormSubmitButton button {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
        font-weight: bold !important;
        border: none !important;
    }

    .stFormSubmitButton button:hover {
        background-color: #0284c7 !important;
        color: #ffffff !important;
    }

    /* Estilização corrigida para botões normais e de link no corpo da página */
    .stMainBlockContainer .stButton button,
    .stApp div[data-testid="stLinkButton"] a {
        background-color: #1e293b !important;
        color: #38bdf8 !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        width: 100% !important;
        padding: 0.5rem 1rem !important;
    }

    /* Efeito Hover (ao passar o rato) */
    .stMainBlockContainer .stButton button:hover,
    .stApp div[data-testid="stLinkButton"] a:hover {
        background-color: #38bdf8 !important;
        color: #0f172a !important;
        border-color: #38bdf8 !important;
    }

</style>
""", unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL (ESTILO FC88) ---
with open("images/menu.png", "rb") as f:
    menu_img = base64.b64encode(f.read()).decode()

st.sidebar.markdown(
    f"""
    <div style="display:flex;align-items:center;gap:15px;">
        <img src="data:image/jpeg;base64,{menu_img}" width="50">
        <span style="
            color:#ffffff;
            font-size:3rem;
            font-weight:bold;
            font-family:'Bebas Neue',sans-serif;
            line-height:1;
        ">
            MENU
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)

if 'menu_opcao' not in st.session_state:
    st.session_state.menu_opcao = "Início & Bio"

if st.sidebar.button("01. ABOUT ME", key="btn_bio"):
    st.session_state.menu_opcao = "Início & Bio"

if st.sidebar.button("02. SKILLS", key="btn_comp"):
    st.session_state.menu_opcao = "Competências"

if st.sidebar.button("03. PROJECTS", key="btn_proj"):
    st.session_state.menu_opcao = "Projetos"

if st.sidebar.button("04. CONTACT", key="btn_cont"):
    st.session_state.menu_opcao = "Contacto"

menu = st.session_state.menu_opcao
# --- 1. INÍCIO & BIO ---
if menu == "Início & Bio":

    st.markdown(
        '<span class="badge">Available for New Projects</span>',
        unsafe_allow_html=True
    )

    st.write("")

    col_foto, col_info = st.columns([1, 4])

    with col_foto:
        st.image("images/joao.png", width=200)

    with col_info:
        st.markdown(
        "<h1 style='color:white;margin-bottom:0;'>"
        "JOÃO SILVA | DATA ANALYST PORTFOLIO"
        "</h1>",
        unsafe_allow_html=True
        )

        st.markdown(
        "Industrial experience combined with data analysis to generate value through information."
        )

        st.markdown(
            "<h2 style='color:#29A8FF;'>"
            "TRANSFORMING DATA INTO STRATEGIC BUSINESS INSIGHTS."
            "</h2>",
            unsafe_allow_html=True
        )
    st.divider()
    
    # Secções de Perfil Profissional e Sobre Mim
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("### Professional Profile")
        
        st.write("Field: Data Analysis & Business Intelligence")
        
        st.write("### Education:")
        st.write("- Food Engineering Degree – Coimbra School of Agriculture")
        st.write("- Data Analyst Course – Tokio School (Online)")
        st.write("- SQL Fundamentals – Coursera")
        
        st.write("### Professional Edge")
        st.write("**Food Engineering + Production Management + Data Analytics**")
        st.write("**Key Areas of Impact:**")
        st.write("📈 Strategic Decision-Making")
        st.write("📊 Business Intelligence")
        st.write("🔍 Predictive Analytics")
        st.write("⚙️ Operational Excellence")

    with col2:
        st.markdown("### About Me")
        st.markdown("""
                    Data Analyst with a background in Food Engineering and experience in industrial production management.

                    Specialized in transforming operational data into actionable insights that support decision-making, process optimization, and enhanced operational performance.
                    """)

        st.markdown("**Tools & Technologies:**")
        col1, col2 = st.columns(2)
        with col1:
            render_header_with_icon("images/python_logo.png", "Python")
            render_header_with_icon("images/logo_sql.png", "SQL")
        with col2:
            render_header_with_icon("images/PowerBI_logo.png", "Power BI")
            render_header_with_icon("images/excel_logo.png", "Excel")

        st.markdown("""
                    **Business Value Delivered:**

                    • ETL and data transformation  
                    • Executive dashboard development  
                    • Reporting and analytics automation  
                    • Exploratory data analysis and predictive modeling  
                    • Data-driven operational optimization
                    """)
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            # Ao clicar, abre o pop-up com os certificados em vez de ir para o LinkedIn
            if st.button("🎓 View Certifications"):
                show_certificates()
        with c2:
            st.link_button("💻 GitHub", "https://github.com/litomanen")

# --- 2. COMPETÊNCIAS ---
elif menu == "Competências":
    st.title("Technical Skills")
    st.write("Skills and technologies used to transform data into actionable insights for decision-making.")

    col1, col2, col3 = st.columns(3)

    with col1:
        render_header_with_icon("images/logo_sql.png", " Data Engineering")
        st.write("- Advanced SQL Querying")
        st.write("- Relational Data Modeling")
        st.write("- ETL & Data Integration")

    with col2:
        render_header_with_icon("images/python_logo.png", " Data Analytics")
        st.write("- Data Preparation & Cleaning")
        st.write("- Exploratory Data Analysis (EDA)")
        st.write("- Data Visualization & Exploration")

    with col3:
        render_header_with_icon("images/PowerBI_logo.png", " Business Intelligence")
        st.write("- Dimensional Modeling")
        st.write("- KPI Development & DAX Analytics")
        st.write("- Executive Dashboards & Reporting")

    st.markdown("<br>", unsafe_allow_html=True)

    esp1, col4, col5, esp2 = st.columns([0.5, 1, 1, 0.5])
    with col4:
        render_header_with_icon("images/ML_logo.png", " Advanced Analytics")
        st.write("- Machine Learning")
        st.write("- Feature Engineering")
        st.write("- Model Evaluation & Comparison")

    with col5:
        render_header_with_icon("images/excel_logo.png", " Analytics & Automation")
        st.write("- Power Query e Power Pivot")
        st.write("- Analytical Models & Advanced Formulas")
        st.write("- Interactive Reporting & Data Analysis")
        
# --- 3. PROJETOS ---
elif menu == "Projetos":
    st.title("Data Analytics Projetcs")
    st.write("Filter projects by primary technology:")
    
    categoria = st.selectbox(
        "Filter by Technology:",
        ["All", "SQL", "Machine Learning", "Power BI", "Pandas & Python", "Excel"]
    )
    
    st.divider()

    # 1. PROJETO SQL & ANÁLISE DE E-COMMERCE
    if categoria in ["All", "SQL"]:
        render_header_with_icon("images/logo_sql.png", "E-Commerce Performance & Logistics Analytics (Olist Dataset)")
        st.caption("**Stack:** SQL | Databricks | SQLite | CTEs | Window Functions | NLP (TF-IDF) | Custom Metrics (DDI, FES)")
        
        st.write("""
        Advanced analysis of the Olist marketplace dataset to uncover purchasing patterns, 
        payment behavior, the impact of logistics on customer satisfaction, and customer sentiment insights through review text mining.
        """)
        
        with st.expander("🔍 Project Details: Architecture, Advanced Metrics, NLP & Business Insights", expanded=False):
            st.markdown("#### 1. Business Challenge & Approach")
            st.write("""
            UAnalyze the end-to-end e-commerce order lifecycle, identifying how payment behavior, delivery performance, 
            and geographic distance influence customer satisfaction and operational efficiency 
            """)

            st.markdown("#### 2. Custom Metrics & Advanced Analytics")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Delivery Delay Index (DDI)</b><br>Custom metric designed to quantify the gap between expected and actual delivery performance: DDI = Actual Date - Estimated Delivery Date.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Fulfillment Efficiency Score (FES)</b><br>Regional density metric measuring the proportion of local orders within a state to assess logistical efficiency and potential delivery friction.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>NLP & TF-IDF</b><br>Customer review text mining using TF-IDF to identify terms and themes most strongly associated with negative customer experiences.</div>', unsafe_allow_html=True)

            st.markdown("#### 3. Key Findings & Insights")
            st.write("""
            * **Payment Behavior & Installment Dominance:** Credit cards account for **78.4% of total revenue**, with customers using an average of **3.5 installments** per transaction, showing that financing is a critical conversion driver.
            * **The Category Paradox (Revenue vs. Dissatisfaction):** Leading categories like `bed_bath_table` generate over 1 million R$ in revenue, but exhibit critical rates of negative reviews (~18.8%), proving that high volume does not always translate to perceived quality.
            * **Delivery Performance & Customer Satisfaction:** Cross-state orders represent the vast majority of dissatisfaction hotspots. The deviation between estimated and actual delivery time (DDI) drastically degrades the `review_score`.
            """)

            st.markdown("#### 4. Strategic Recommendations")
            st.write("""
            * **Category-Based Logistics Optimization:** Develop strategic partnerships with logistics providers specialized in bulky-product transportation to improve delivery performance in high-volume categories such as bed_bath_table and furniture_decor.
            * **Regional Seller Expansion:** Expand seller acquisition efforts in high-demand regions to improve fulfillment efficiency, reduce delivery lead times, and increase the Fulfillment Efficiency Score (FES).
            """)

            st.markdown("---")
            st.link_button("💻 View GitHub Repository", "https://github.com/litomanen/E-Commerce_Analytics_Olist")

    st.divider()
    # 2. PROJETO MACHINE LEARNING
    if categoria in ["All", "Machine Learning"]:
        render_header_with_icon("images/ML_logo.png", "Employee Attrition / Churn Predictive Model")
        st.caption("**Stack:** Python | Scikit-Learn | Pandas | StandardScaler | Logistic Regression | Decision Tree | Random Forest | Joblib")
    
        st.write("""
        Machine Learning project focused on predicting and mitigating voluntary employee turnover (*Employee Attrition*).
        The model identifies profiles at high risk of resignation, enabling the HR team to act proactively in talent retention.
        """)
    
        with st.expander("🔍 Project Details: Business Problem, Methodology & Results", expanded=False):
            st.markdown("#### 1. The Business Problem")
            st.write("""
            Employee turnover generates high recruitment, training, and technical knowledge loss costs. 
            The challenge was to identify patterns in historical HR data explaining departures and build a predictive model to early flag employees at risk.
            """)

            st.markdown("#### 2. Data Preparation & Imbalance Handling")
            st.write("""
            - **Class Imbalance:** The dataset showed a strong disproportion (**83.87% Stayed / 16.13% Left**).
            - **Handling:** Applied class weighting technique (`class_weight='balanced'`) to penalize errors in the minority class (departure).
            - **Feature Engineering:** Categorical encoding via *One-Hot Encoding* (`pd.get_dummies`) and continuous standardization with *StandardScaler*.
            - **Data Splitting:** Stratified split (`stratify=y`) into **80% Train and 20% Test**.
            """)

            st.markdown("#### 3. Model Performance Comparison")
            st.write("""
            Evaluation prioritized **Recall (Sensitivity)** on the departure class, given that the financial and operational cost of missing a departing employee (False Negative) is substantially higher than scheduling a preventive meeting (False Positive).
            """)

            # Results Comparison Table
            df_resultados = pd.DataFrame({
                "Model": ["Logistic Regression (Ideal)", "Decision Tree (depth=5)", "Random Forest (depth=6)"],
                "Precision (1)": [0.35, 0.36, 0.50],
                "Recall (1)": ["62.0%", "53.2%", "34.0%"],
                "F1-Score": [0.44, 0.43, 0.41],
                "ROC-AUC": [0.7983, 0.6517, 0.7683],
                "General Accuracy": [0.7517, 0.7721, 0.8401],
                "Diagnosis": ["Balanced (Production)", "Balanced", "Pronounced Overfitting"]
            })
        
            st.dataframe(df_resultados, use_container_width=True, hide_index=True)

            st.info("""
            **Selected Production Model:** **Logistic Regression**  
            Although Random Forest presented higher general Accuracy (84%), it suffered from overfitting and failed to capture actual departures (Recall of only 34%). Logistic Regression ensured the highest **Recall (62%)** and **ROC-AUC (0.7983)**, demonstrating predictive stability and absence of overfitting.
            """)

            st.markdown("#### 4. Key Business Insights & Retention Levers")
            st.write("""
            * **OverTime (`OverTime`):** Constitutes the main isolated churn acceleration factor. Employees with frequent overtime have a high exit risk.
            * **Total Working Years (`TotalWorkingYears`):** Early-career employees (juniors) exhibit higher volatility in the first 24 months.
            * **Monthly Income (`MonthlyIncome`):** Salary levels below market average for demanding roles significantly increase the turnover rate.
            """)

            st.markdown("---")
            st.link_button("💻 View Complete GitHub Repository", "https://github.com/litomanen/hr_attrition_prediction/tree/main/ML")

        st.divider()

    # 3. PROJETO POWER BI
    if categoria in ["All", "Power BI"]:
        render_header_with_icon("images/PowerBI_logo.png", "Operational Management, Risk & Energy Efficiency Dashboard (ESG)")
        st.caption("**Stack:** Power BI | DAX | Power Query | Azure Maps | GIS Analytics | Streamlit Integration")
    
        st.write("""
            Multilevel analytical dashboard developed for the continuous monitoring of 500 buildings in Portugal. 
            The platform combines dynamic geolocation via Azure Maps, operational risk matrices, and ESG indicators 
            (CO₂ footprint and energy efficiency) to support asset managers in decision-making.
            """)
    
        with st.expander("🔍 Project Details: Data Analysis, DAX Metrics & Visualization", expanded=False):
            st.markdown("#### 1. The Operational Challenge")
            st.write("""
                Infrastructure managers need a centralized tool to identify energy-inefficient buildings, 
                prioritize structural renovation interventions, and evaluate the actual relationship between theoretical risk (*Hazard Risk*) and the effective volume of incidents.
                """)

            st.markdown("#### 2. Data Processing & Feature Engineering")
            st.write("""
                - **Data Source:** Unified dataset (`building_data`) containing geographic attributes, energy consumption metrics, maintenance costs, CO₂ emissions, and 5-year incident history.
                - **Power Query & ETL:** Cleaning records, data type standardization, unit conversion, and creation of derived attributes (construction decades and energy efficiency tier grouping).
                - **Geolocation:** Integration with Azure Maps for vector mapping of the 500 buildings with color coding and contextualized *Drillthrough* details.
                """)

            st.markdown("#### 3. Executive DAX Metrics")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(
                    '<div class="metric-card"><b>Risk & Incidence</b><br>'
                    'Measure <code>Incidence Rate</code> to calculate the volume of occurrences weighted by total buildings per region.</div>', 
                    unsafe_allow_html=True
                )
            with c2:
                st.markdown(
                    '<div class="metric-card"><b>ESG & Sustainability</b><br>'
                    'Measures <code>% Inefficient Buildings (D-E)</code> and <code>CO2 per m2</code> for ecological footprint diagnosis.</div>', 
                   unsafe_allow_html=True
                )
            with c3:
                st.markdown(
                    '<div class="metric-card"><b>Asset Lifecycle</b><br>'
                    'Measure <code>% Pre-2000 Renovation</code> to map investment urgency in buildings over 20 years old.</div>', 
                    unsafe_allow_html=True
                )

            st.markdown("#### 4. Key Business Findings (*Data Storytelling*)")
            st.write("""
                * **Risk Anomaly:** It was found that buildings classified as low risk recorded, for instance in the Center zone, a higher volume of incidents (36) compared to high-risk ones (25).
                * **Relative Incidence:** Although the Center region leads in absolute numbers of incidents, **Lisbon presents the highest relative incidence rate (64.71%)**.
                * **Renovation Urgency:** **65.55% of buildings built before 2000 need renovation**, representing the main cause of energy inefficiency and CO₂ emissions of the portfolio (45.80% of buildings in classes D-E).
                """)

            st.markdown("---")
        
            col_lnk1, col_lnk2 = st.columns(2)
            with col_lnk1:
                st.link_button(
                    "💻 View GitHub Repository", 
                    "https://github.com/Litomanen/PowerBI_Building_Management"
                )
            with col_lnk2:
                st.link_button(
                "📖 DAX Documentation (`dax_measures_reference.md`)", 
                "https://github.com/litomanen/PowerBI_Building_Management/blob/main/dax/dax_measures_reference.md"
                )

            st.divider()

    # 4. PROJETO DE GESTÃO DE ABSENTISMO INDUSTRIAL (MOD)
    if categoria in ["All", "Pandas & Python"]:
        render_header_with_icon("images/python_logo.png", "Industrial Absenteeism Management & Direct Labor Analysis (DL)")
        st.caption("**Stack:** Python | Pandas | Streamlit | Plotly | Dark Corporate Architecture | Pareto Principle")
        
        st.write("""
        Development of an interactive executive Streamlit dashboard for advanced monitoring of 
        direct labor indicators, integrating Pandas data processing pipelines, 
        dynamic time delta calculations, and high-impact analytical visualizations.
        """)
        
        with st.expander("🔍 Project Details: ETL, Executive KPIs & Pareto Visualization", expanded=False):
            st.markdown("#### 1. Context & Problem Framework")
            st.write("""
            Management of temporal deviations in industrial environments requires real-time visibility into absenteeism causes. 
            The goal was to transform complex operational databases into an executive-level Business Intelligence tool, 
            allowing filtering by year/month, tracking trends against the homologous period, and identifying critical productivity bottlenecks.
            """)

            st.markdown("#### 2. Data Engineering & Processing (ETL)")
            st.write("""
            - **Temporal Normalization:** Robust conversion of `datetime` objects and correction of temporal anomalies for rigorous calculation of decimal hours (`float64`).
            - **Multi-Level Dynamic Filters:** Cascading filter architecture by Year and Month, automatically recalculating the target hours and absence universe.
            - **Accumulated Metrics & Deltas:** Automated comparison with the previous year (`vs previous_year`), calculating variations in percentage points with inverted conditional formatting (where absenteeism reduction is positively represented in green).
            - **Null Handling:** Intelligent imputation and categorization of missing records to ensure the statistical integrity of the model.
            """)

            st.markdown("#### 3. Visual Architecture & Interactive Charts (Plotly)")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Executive Frames</b><br>Visual layer separation with dark outer backgrounds (#1e293b) and clean white inner backgrounds for maximum legibility.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Pareto Analysis</b><br>Dual-axis combined chart (frequency bars + cumulative percentage line) focused on key impactors.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>Optimized Scales & Grids</b><br>Custom Y axes with fixed intervals (<i>dtick</i>) and positive angular X-axis rotation for perfect readability of long names.</div>', unsafe_allow_html=True)

            st.markdown("#### 4. Technical Deliverables & UI/UX")
            st.write("""
            * **'Dark Corporate' Design System:** Customized interface via injected CSS with gradients, dedicated metric cards, and high-visibility typography.
            * **Control Components:** Interactive charts by Absence Category, Employee Ranking (Top 10), and Impact Pareto Curve.
            * **Portfolio Readiness:** Modular, clean, and structured code for demonstrating industrial data analysis skills.
            """)

            st.markdown("---")
            st.link_button("Access Interactive Application", 
                "https://absencemanagementmanufacturing-kyxhy7nqphmag9v6gon2n6.streamlit.app/", 
                use_container_width=True
            )
        st.divider()

    # 5. PROJETO EXCEL
    if categoria in ["All", "Excel"]:
        render_header_with_icon("images/excel_logo.png", "Film Waste Analysis & Reduction in Automatic Baggers (VFFS)")
        st.caption("**Stack:** Advanced Excel | Power Query | Power Pivot | Data Modeling | Advanced Formulas | Pareto & Industrial KPIs")
        
        st.write("""
        Development of an industrial control model for monitoring, quantifying, and reducing plastic film waste in automatic bagging lines within the food industry.
        """)
        
        with st.expander("🔍 Project Details: Power Query, Failure Modes & Production Indicators", expanded=False):
            st.markdown("#### 1. The Industrial Challenge")
            st.write("""
            In continuous packaging lines, plastic film loss generates direct raw material costs and unplanned downtime. 
            The objective was to map and categorize the main causes of waste (out-of-tolerance weights, printing/dating failures, and sealing/packaging defects) to act on root causes.
            """)

            st.markdown("#### 2. ETL & Log Consolidation with Power Query")
            st.write("""
            - **Shop Floor Data Processing:** Import and automation of daily production shift records, weighings, and rejections consolidation.
            - **Loss Metrics:** Automatic unit conversion (meters of film, weight in kg, and financial impact (€) per production batch).
            - **Loss Metrics:** Automatic unit conversion (meters of film, weight in kg, and financial impact (€) per production batch).
            """)

            st.markdown("#### 3. Defect Categorization & Pareto Analysis")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Weighing Decalibration</b><br>Monitoring losses from bags rejected due to weight outside legal/specification limits.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Printing & Dating Errors</b><br>Identification of batches with labeling, barcode, or expiration date defects.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>Sealing / Packaging Defects</b><br>Mapping rejections due to poorly sealed packs, holes, or mechanical film deformation.</div>', unsafe_allow_html=True)

            st.markdown("#### 4. Results & Operational Impact")
            st.write("""
            * **Real Cost Visibility:** Identification of the root cause responsible for over 70% of accumulated plastic film waste.
            * **Dynamic Dashboard:** Executive report with Product and Defect Category filters for quick decision-making by the Production and Quality team.
            """)

            st.markdown("---")
            st.link_button("💻 View GitHub Repository", "https://github.com/litomanen/excel_vffs_waste_dashboard")

        st.divider()

# --- 4. CONTACTO ---
elif menu == "Contacto":
    st.title("✉️ Contact")
    st.write("Do you have a collaboration opportunity or project? Get in touch with me directly:")
    
    st.write("")
    
    # Styled direct contact card
    col_c1, col_c2 = st.columns([1, 1])
    
    with col_c1:
        st.markdown('<div class="metric-card"><b>📧 Professional E-mail</b><br>john_lito@hotmail.com</div>', unsafe_allow_html=True)
        st.link_button("Send Direct E-mail", "mailto:john_lito@hotmail.com?subject=Contact%20via%20Portfolio%20-%20Data%20Analyst&body=Hello%20João,%0D%0A%0D%0AI%20saw%20your%20portfolio%20and%20would%20like%20to%20get%20in%20touch%20regarding...")
    
    with col_c2:
        st.markdown('<div class="metric-card"><b>🌐 Professional Network</b><br>GitHub (Projects)</div>', unsafe_allow_html=True)
        st.link_button("Access GitHub (Repositories)", "https://github.com/litomanen")