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

@st.dialog("Certificados Profissionais")
def show_certificates():
    st.write("Aqui pode consultar os comprovativos das formações concluídas:")
    
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

if st.sidebar.button("01. INÍCIO & BIO", key="btn_bio"):
    st.session_state.menu_opcao = "Início & Bio"

if st.sidebar.button("02. COMPETÊNCIAS", key="btn_comp"):
    st.session_state.menu_opcao = "Competências"

if st.sidebar.button("03. PROJETOS", key="btn_proj"):
    st.session_state.menu_opcao = "Projetos"

if st.sidebar.button("04. CONTACTO", key="btn_cont"):
    st.session_state.menu_opcao = "Contacto"

menu = st.session_state.menu_opcao
# --- 1. INÍCIO & BIO ---
if menu == "Início & Bio":

    st.markdown(
        '<span class="badge">Disponível para novos projetos</span>',
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
        "Experiência industrial aliada à análise de dados para gerar valor através da informação."
        )

        st.markdown(
            "<h2 style='color:#29A8FF;'>"
            "TRANSFORMANDO DADOS OPERACIONAIS EM VANTAGEM COMPETITIVA."
            "</h2>",
            unsafe_allow_html=True
        )
    st.divider()
    
    # Secções de Perfil Profissional e Sobre Mim
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown("### Perfil Profissional")
        
        st.write("Área: Data Analysis & Business Intelligence")
        
        st.write("### Formação:")
        st.write("- Curso de Engenharia Alimentar – Escola Superior Agrária de Coimbra")
        st.write("- Curso de Data Analyst – Tokio School (Online)")
        st.write("- SQL Fundamentals – Coursera")
        
        st.write("### Diferencial Profissional")
        st.write("**Engenharia Alimentar + Gestão de Produção + Data Analytics**")
        st.write("**Áreas de Impacto:**")
        st.write("📈 Tomada de Decisão")
        st.write("📊 Business Intelligence")
        st.write("🔍 Análise Preditiva")
        st.write("⚙️ Eficiência Operacional")

    with col2:
        st.markdown("### Sobre Mim")
        st.markdown("""
                    Analista de Dados com formação em Engenharia Alimentar e experiência em gestão de produção industrial.

                    Especializado na transformação de dados operacionais em informação útil para suporte à decisão, otimização de processos e melhoria do desempenho operacional.
                    """)

        st.markdown("**Ferramentas e Tecnologias:**")
        col1, col2 = st.columns(2)
        with col1:
            render_header_with_icon("images/python_logo.png", "Python")
            render_header_with_icon("images/logo_sql.png", "SQL")
        with col2:
            render_header_with_icon("images/PowerBI_logo.png", "Power BI")
            render_header_with_icon("images/excel_logo.png", "Excel")

        st.markdown("""
                    **O que trago para o negócio:**

                    • Estruturação e tratamento de dados (ETL)  
                    • Desenvolvimento de dashboards executivos  
                    • Automação de relatórios e processos analíticos  
                    • Análise exploratória e modelação preditiva  
                    • Otimização de operações industriais através de dados
                    """)
        
        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🎓 Ver Certificados"):
                show_certificates()
        with c2:
            st.link_button("💻 GitHub", "https://github.com/litomanen")

# --- 2. COMPETÊNCIAS ---
elif menu == "Competências":
    st.title("Competências Técnicas")
    st.write("Competências e tecnologias aplicadas à transformação de dados em informação para suporte à decisão.")

    col1, col2, col3 = st.columns(3)

    with col1:
        render_header_with_icon("images/logo_sql.png", " Engenharia de Dados")
        st.write("- Consultas SQL Avançadas")
        st.write("- Modelação de Dados Relacional")
        st.write("- ETL e Integração de Dados")

    with col2:
        render_header_with_icon("images/python_logo.png", " Análise de Dados")
        st.write("- Preparação e Tratamento de Dados")
        st.write("- Análise Exploratória (EDA)")
        st.write("- Visualização e Exploração de Dados")

    with col3:
        render_header_with_icon("images/PowerBI_logo.png", " Business Intelligence")
        st.write("- Modelação Dimensional")
        st.write("- KPIs e Métricas com DAX")
        st.write("- Dashboards Executivos e Reporting")

    st.markdown("<br>", unsafe_allow_html=True)

    esp1, col4, col5, esp2 = st.columns([0.5, 1, 1, 0.5])
    with col4:
        render_header_with_icon("images/ML_logo.png", " Analytics Avançado")
        st.write("- Machine Learning")
        st.write("- Feature Engineering")
        st.write("- Avaliação e Comparação de Modelos")

    with col5:
        render_header_with_icon("images/excel_logo.png", " Análise & Automação")
        st.write("- Power Query e Power Pivot")
        st.write("- Fórmulas e Modelos Analíticos")
        st.write("- Reporting e Análise Interativa")
        
# --- 3. PROJETOS ---
elif menu == "Projetos":
    st.title("Projetos de Análise de Dados")
    st.write("Filtre os trabalhos desenvolvidos por tecnologia principal:")
    
    categoria = st.selectbox(
        "Filtrar por Tecnologia:",
        ["Todos", "SQL", "Machine Learning", "Power BI", "Pandas & Python", "Excel"]
    )
    
    st.divider()

    # 1. PROJETO SQL & ANÁLISE DE E-COMMERCE
    if categoria in ["Todos", "SQL"]:
        render_header_with_icon("images/logo_sql.png", "Análise de Desempenho de E-Commerce & Logística (Dataset Olist)")
        st.caption("**Stack:** SQL | Databricks | SQLite | CTEs | Window Functions | NLP (TF-IDF) | Métricas Customizadas (DDI, FES)")
        
        st.write("""
        Análise relacional avançada de dados de um marketplace de e-commerce real (Olist) para identificar padrões de compras, 
        hábitos de financiamento, impacto logístico na satisfação do cliente e mineração de texto em avaliações.
        """)
        
        with st.expander("🔍 Detalhes do Projeto: Arquitetura, Métricas Avançadas, NLP e Insights de Negócio", expanded=False):
            st.markdown("#### 1. O Desafio de Negócio & Abordagem")
            st.write("""
            Compreender o ciclo de vida completo dos pedidos de e-commerce: desde a forte dependência de meios de pagamento parcelados 
            até ao impacto crítico da logística e da distância geográfica na satisfação do cliente final.
            """)

            st.markdown("#### 2. Modelação de Métricas & Análise Avançada")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Delivery Delay Index (DDI)</b><br>Métrica customizada para isolar a quebra de expectativa temporal: DDI = Data Real - Data Estimada de Entrega.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Fulfillment Efficiency Score (FES)</b><br>Métrica de densidade regional: rácio de encomendas locais (mesmo estado) para conter atritos logísticos.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>NLP & TF-IDF</b><br>Mineração de texto nas reviews (remoção de stop-words) para isolar termos associados a insatisfação ("atraso", "não recebi").</div>', unsafe_allow_html=True)

            st.markdown("#### 3. Principais Descobertas & Insights")
            st.write("""
            * **Dominância do Crédito & Parcelamento:** O cartão de crédito representa **78.4% da faturação total**, com os clientes a utilizarem uma média de **3.5 parcelas** por transação, evidenciando que o financiamento é um motor crítico de conversão.
            * **O Paradoxo das Categorias (Receita vs. Insatisfação):** Categorias líderes como `bed_bath_table` geram mais de 1 milhão de R$ em receita, mas apresentam taxas críticas de avaliações negativas (~18.8%), provando que alto volume nem sempre se traduz em qualidade percebida.
            * **Impacto Logístico e Distância:** Encomendas cruzadas entre estados diferentes representam a grande maioria dos focos de insatisfação. O desvio entre o prazo estimado e o real ($\text{DDI}$) degrada drasticamente o `review_score`.
            """)

            st.markdown("#### 4. Recomendações Estratégicas")
            st.write("""
            * **Otimização Logística por Categoria:** Estabelecer parcerias com operadores especializados no transporte de artigos volumosos (`bed_bath_table`, `furniture_decor`).
            * **Descentralização de Sellers:** Focar a aquisição de novos vendedores em regiões com alta densidade de procura para maximizar o índice FES e reduzir tempos de trânsito.
            """)

            st.markdown("---")
            st.link_button("💻 Ver Repositório no GitHub", "https://github.com/litomanen/E-Commerce_Analytics_Olist") # Podes ajustar para o repo correto

    st.divider()
    # 2. PROJETO MACHINE LEARNING
    if categoria in ["Todos", "Machine Learning"]:
        render_header_with_icon("images/ML_logo.png", "Modelo Preditivo de Attrition / Churn de Funcionários")
        st.caption("**Stack:** Python | Scikit-Learn | Pandas | StandardScaler | Logistic Regression | Decision Tree | Random Forest | Joblib")
    
        st.write("""
        Projeto de Machine Learning focado em prever e mitigar a rotatividade voluntária de colaboradores (*Employee Attrition*).
        O modelo identifica perfis com alto risco de demissão, permitindo que a equipa de RH atue preventivamente na retenção de talentos.
        """)
    
        with st.expander("🔍 Detalhes do Projeto: Problema de Negócio, Metodologia e Resultados", expanded=False):
            st.markdown("#### 1. O Problema de Negócio")
            st.write("""
            A rotatividade de colaboradores gera custos elevados de recrutamento, formação e perda de conhecimento técnico. 
            O desafio consistia em identificar padrões nos dados históricos do RH que explicassem as saídas e construir um modelo preditivo para sinalizar precocemente funcionários em risco.
            """)

            st.markdown("#### 2. Preparação de Dados & Tratamento de Desbalanceamento")
            st.write("""
            - **Desbalanceamento de Classes:** O dataset apresentava forte desproporção (**83.87% Permanece / 16.13% Saiu**).
            - **Tratamento:** Aplicou-se a técnica de ponderação de classes (`class_weight='balanced'`) para penalizar erros na classe minoritária (saída).
            - **Engenharia de Atributos:** Codificação categórica via *One-Hot Encoding* (`pd.get_dummies`) e padronização contínua com *StandardScaler*.
            - **Divisão de Dados:** Separação estratificada (`stratify=y`) em **80% Treino e 20% Teste**.
            """)

            st.markdown("#### 3. Comparação de Desempenho dos Modelos")
            st.write("""
            A avaliação priorizou a métrica de **Recall (Sensibilidade)** na classe de saída, visto que o custo financeiro e operacional de perder um colaborador não detetado (Falso Negativo) é substancialmente superior ao de agendar uma reunião preventiva (Falso Positivo).
            """)

            # Tabela de Comparação de Resultados
            df_resultados = pd.DataFrame({
                "Modelo": ["Regressão Logística (Ideal)", "Decision Tree (depth=5)", "Random Forest (depth=6)"],
                "Precision (1)": [0.35, 0.36, 0.50],
                "Recall (1)": ["62.0%", "53.2%", "34.0%"],
                "F1-Score": [0.44, 0.43, 0.41],
                "ROC-AUC": [0.7983, 0.6517, 0.7683],
                "Accuracy Geral": [0.7517, 0.7721, 0.8401],
                "Diagnóstico": ["Equilibrado (Produção)", "Equilibrado", "Overfitting Acentuado"]
            })
        
            st.dataframe(df_resultados, use_container_width=True, hide_index=True)

            st.info("""
            **Modelo Selecionado para Produção:** **Regressão Logística**  
            Apesar de o Random Forest apresentar maior Accuracy geral (84%), sofreu de overfitting e falhou na captura de saídas reais (Recall de apenas 34%). A Regressão Logística garantiu o maior **Recall (62%)** e **ROC-AUC (0.7983)**, demonstrando estabilidade preditiva e ausência de overfitting.
            """)

            st.markdown("#### 4. Principais Insights de Negócio & Alavancas de Retenção")
            st.write("""
            * **Horas Extraordinárias (`OverTime`):** Constitui o principal fator isolado de aceleração do *churn*. Colaboradores com horas extra frequentes têm risco de saída elevado.
            * **Experiência Total (`TotalWorkingYears`):** Colaboradores em início de carreira (juniores) apresentam maior volatilidade nos primeiros 24 meses.
            * **Remuneração Mensal (`MonthlyIncome`):** Níveis salariais abaixo da média do mercado para funções exigentes aumentam significativamente a taxa de rotatividade.
            """)

            st.markdown("---")
            st.link_button("💻 Ver Repositório Completo no GitHub", "https://github.com/litomanen/hr_attrition_prediction/tree/main/ML")

        st.divider()

    # 3. PROJETO POWER BI
    if categoria in ["Todos", "Power BI"]:
        render_header_with_icon("images/PowerBI_logo.png", "Dashboard de Gestão Operacional, Risco & Eficiência Energética (ESG)")
        st.caption("**Stack:** Power BI | DAX | Power Query | Azure Maps | GIS Analytics | Streamlit Integration")
    
        st.write("""
            Painel analítico multinível desenvolvido para a monitorização contínua de 500 edifícios em Portugal. 
            A plataforma combina geolocalização dinâmica via Azure Maps, matrizes de risco operacional e indicadores ESG 
            (pegada de CO₂ e eficiência energética) para apoiar gestores de ativos na tomada de decisão.
            """)
    
        with st.expander("🔍 Detalhes do Projeto: Análise de Dados, Métricas DAX e Visualização", expanded=False):
            st.markdown("#### 1. O Desafio Operacional")
            st.write("""
                Gestores de infraestruturas necessitam de uma ferramenta centralizada para identificar edifícios energeticamente ineficientes, 
                priorizar intervenções de renovação estrutural e avaliar a relação real entre o risco teórico (*Hazard Risk*) e o volume efetivo de incidentes.
                """)

            st.markdown("#### 2. Processamento de Dados & Engenharia de Atributos")
            st.write("""
                - **Origem dos Dados:** Conjunto de dados unificado (`building_data`) contendo atributos geográficos, métricas de consumo energético, custos de manutenção, emissões de CO₂ e histórico de incidentes a 5 anos.
                - **Power Query & ETL:** Limpeza de registos, padronização de tipos de dados, conversão de unidades e criação de atributos derivados (décadas de construção e agrupamento por escalões de eficiência energética).
                - **Geolocalização:** Integração com Azure Maps para mapeamento vetorial dos 500 edifícios com codificação por cores e pormenorização (*Drillthrough*) contextualizada.
                """)

            st.markdown("#### 3. Métricas DAX Executivas")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(
                    '<div class="metric-card"><b>Risco & Incidência</b><br>'
                    'Medida <code>Taxa Incidencia</code> para calcular o volume de ocorrências ponderado pelo total de edifícios por região.</div>', 
                    unsafe_allow_html=True
                )
            with c2:
                st.markdown(
                    '<div class="metric-card"><b>ESG & Sustentabilidade</b><br>'
                    'Medidas <code>% Edificios Ineficientes (D-E)</code> e <code>CO2 por m2</code> para diagnóstico de pegada ecológica.</div>', 
                 unsafe_allow_html=True
                )
            with c3:
                st.markdown(
                    '<div class="metric-card"><b>Ciclo de Vida do Ativo</b><br>'
                    'Medida <code>% Renovação Pré-2000</code> para mapear a urgência de investimento em edifícios com mais de 20 anos.</div>', 
                    unsafe_allow_html=True
                )

            st.markdown("#### 4. Principais Descobertas de Negócio (*Data Storytelling*)")
            st.write("""
                * **Anomalia de Risco:** Apurou-se que edifícios classificados como de baixo risco registaram, por exemplo na zona Centro, um volume superior de incidentes (36) face aos de risco elevado (25).
                * **Incidência Relativa:** Embora a região Centro lidere em números absolutos de incidentes, **Lisboa apresenta a maior taxa de incidência relativa (64,71%)**.
                * **Urgência de Renovação:** **65,55% dos edifícios construídos antes de 2000 necessitam de renovação**, representando a principal causa de ineficiência energética e emissões de CO₂ do portfólio (45,80% dos edifícios nas classes D-E).
                """)

            st.markdown("---")
        
            col_lnk1, col_lnk2 = st.columns(2)
            with col_lnk1:
                st.link_button(
                    "💻 Ver Repositório no GitHub", 
                    "https://github.com/Litomanen/PowerBI_Building_Management"
                )
            with col_lnk2:
                st.link_button(
                "📖 Documentação DAX (`dax_measures_reference.md`)", 
                "https://github.com/litomanen/PowerBI_Building_Management/blob/main/dax/dax_measures_reference.md"
                )

            st.divider()

    # 4. PROJETO DE GESTÃO DE ABSENTISMO INDUSTRIAL (MOD)
    if categoria in ["Todos", "Pandas & Python"]:
        render_header_with_icon("images/python_logo.png","Gestão de Absentismo Industrial & Análise de Mão de Obra Direta (MOD)")
        st.caption("**Stack:** Python | Pandas | Streamlit | Plotly | Arquitetura Dark Corporate | Princípio de Pareto")
        
        st.write("""
        Desenvolvimento de um dashboard executivo interativo em Streamlit para monitorização avançada de 
        indicadores de mão de obra direta (MOD), integrando pipelines de tratamento de dados em Pandas, 
        cálculos dinâmicos de deltas temporais e visualizações analíticas de alto impacto.
        """)
        
        with st.expander("🔍 Detalhes do Projeto: ETL, KPIs Executivos e Visualização de Pareto", expanded=False):
            st.markdown("#### 1. Contexto e Enquadramento do Problema")
            st.write("""
            A gestão de desvios temporais em ambientes industriais exige visibilidade em tempo real sobre as causas de absentismo. 
            O objetivo foi transformar bases de dados operacionais complexas numa ferramenta de Business Intelligence de nível executivo, 
            permitindo filtrar por ano/mês, rastrear tendências face ao período homólogo e identificar gargalos críticos de produtividade.
            """)

            st.markdown("#### 2. Engenharia de Dados & Tratamento (ETL)")
            st.write("""
            - **Normalização Temporal:** Conversão robusta de objetos `datetime` e correção de anomalias temporais para cálculo rigoroso de horas decimais (`float64`).
            - **Filtros Dinâmicos Multi-Nível:** Arquitetura de filtragem em cascata por Ano e Mês, recalculando automaticamente o universo de horas objetivo e de ausência.
            - **Métricas Acumuladas & Deltas:** Comparação automatizada com o ano anterior (`vs ano_anterior`), calculando variações em pontos percentuais com formatação condicional invertida (onde a redução de absentismo é representada positivamente a verde).
            - **Tratamento de Nulos:** Imputação inteligente e categorização de registos omissos para assegurar a integridade estatística do modelo.
            """)

            st.markdown("#### 3. Arquitetura Visual & Gráficos Interativos (Plotly)")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Molduras Executivas</b><br>Separação visual de camadas com fundos exteriores escuros (#1e293b) e interiores brancos limpos para máxima legibilidade.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Análise de Pareto</b><br>Gráfico combinado de duplo eixo (barras de frequência + linha de percentagem acumulada) focado nos principais impactadores.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>Escalas & Grelhas Optimizadas</b><br>Eixos Y customizados com intervalos fixos (<i>dtick</i>) e eixos X com rotação angular positiva para legibilidade perfeita de nomes longos.</div>', unsafe_allow_html=True)

            st.markdown("#### 4. Entregáveis Técnicos e UI/UX")
            st.write("""
            * **Design System 'Dark Corporate':** Interface personalizada via CSS injetado com gradientes, cartões de métricas dedicados e tipografia de alta visibilidade.
            * **Componentes de Controlo:** Gráficos interativos por Categoria de Ausência, Ranking de Colaboradores (Top 10) e Curva de Pareto de Impacto.
            * **Prontidão para Portfólio:** Código modular, limpo e estruturado para demonstração de competências em análise de dados industriais.
            """)

            st.markdown("---")
            st.link_button("Aceder à Aplicação Interativa", 
                "https://absencemanagementmanufacturing-8sjtrzsth7dsfaryfisbuh.streamlit.app/", 
                use_container_width=True
)
        st.divider()

    # 5. PROJETO EXCEL
    if categoria in ["Todos", "Excel"]:
        render_header_with_icon("images/excel_logo.png", "Análise & Redução de Desperdício de Filme em Ensacadoras Automáticas")
        st.caption("**Stack:** Excel Avançado | Power Query | Power Pivot | Modelagem de Dados | Fórmulas Avançadas | Pareto & KPIs Industriais")
        
        st.write("""
        Desenvolvimento de um modelo de controlo industrial para monitorização, quantificação e redução de desperdício de filme plásticos em linhas de ensacamento automático na indústria alimentar.
        """)
        
        with st.expander("🔍 Detalhes do Projeto: Power Query, Modos de Falha e Indicadores de Produção", expanded=False):
            st.markdown("#### 1. O Desafio Industrial")
            st.write("""
            Nas linhas de embalamento contínuo, a perda de filme plástico gera custos diretos de matéria-prima e paragens não planeadas. 
            O objetivo foi mapear e categorizar as principais causas de desperdício (pesos fora da tolerância, falhas de impressão/datagem e defeitos de selagem/embalagem) para atuar nas causas-raiz.
            """)

            st.markdown("#### 2. ETL & Consolidação de Logs com Power Query")
            st.write("""
            - **Tratamento de Dados de Chão de Fábrica:** Importação e automação da consolidação de registos diários de turnos de produção, pesagens e rejeites.
            - **Métricas de Perda:** Conversão automática de unidades (metros de filme, peso em kg e impacto financeiro (€) por lote de produção).
            """)

            st.markdown("#### 3. Categorização de Defeitos & Análise de Pareto")
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown('<div class="metric-card"><b>Descalibração de Pesagem</b><br>Monitorização de perdas por sacos rejeitados por peso fora do limite legal/especificação.</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="metric-card"><b>Erros de Impressão & Datagem</b><br>Identificação de lotes com defeitos de rotulagem, código de barras ou data de validade.</div>', unsafe_allow_html=True)
            with c3:
                st.markdown('<div class="metric-card"><b>Defeitos de Selagem / Embalagem</b><br>Mapeamento de rejeites por maços mal selados, furos ou deformação mecânica do filme.</div>', unsafe_allow_html=True)

            st.markdown("#### 4. Resultados & Impacto Operacional")
            st.write("""
            * **Visibilidade do Custo Real:** Identificação da causa-raiz responsável por mais de 70% do desperdício acumulado de filme plástico.
            * **Dashboard Dinâmico:** Relatório executivo com filtros Produto e Categoria de Defeito para tomada de decisão rápida da equipa de Produção e Qualidade.
            """)

            st.markdown("---")
            st.link_button("💻 Ver Repositório no GitHub (Link a Adicionar)", "https://github.com/litomanen/excel_vffs_waste_dashboard")

# --- 4. CONTACTO ---
elif menu == "Contacto":
    st.title("✉️ Contacto")
    st.write("Tem uma oportunidade de colaboração ou projeto? Entre em contacto direto comigo:")
    
    st.write("")
    
    # Cartão de contacto direto estilizado
    col_c1, col_c2 = st.columns([1, 1])
    
    with col_c1:
        st.markdown('<div class="metric-card"><b>📧 E-mail Profissional</b><br>john_lito@hotmail.com</div>', unsafe_allow_html=True)
        st.link_button("Enviar E-mail Direto", "mailto:john_lito@hotmail.com?subject=Contacto%20via%20Portfolio%20-%20Data%20Analyst&body=Olá%20João,%0D%0A%0D%0AVi%20o%20seu%20portfólio%20e%20gostaria%20de%20entrar%20em%20contacto%20sobre...")
    
    with col_c2:
        st.markdown('<div class="metric-card"><b>🌐 Rede Profissional</b><br>GitHub (Projetos)</div>', unsafe_allow_html=True)
        st.link_button("Aceder ao GitHub (Repositórios)", "https://github.com/litomanen")