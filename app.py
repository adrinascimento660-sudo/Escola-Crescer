import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# =========================
# CONFIGURAÇÃO
# =========================
st.set_page_config(
    page_title="ESG + Dados + Inovação - Cursos Profissionalizantes",
    page_icon="📊",
    layout="wide"
)

# =========================
# DADOS SIMULADOS
# =========================
df = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Matrículas": [120, 135, 150, 160, 180, 210],
    "Evasão (%)": [18, 16, 15, 14, 12, 10],
    "Satisfação (%)": [72, 75, 78, 82, 86, 90],
    "Receita (R$)": [30000, 34000, 36000, 40000, 45000, 52000],
    "Consumo Papel (kg)": [80, 75, 70, 60, 50, 40],
    "CO2 (kg)": [500, 480, 460, 430, 400, 350]
})

# =========================
# TÍTULO
# =========================
st.title("📊 ESCOLA CRESCER : CURSOS PROFISSIONALIZANTES")
st.caption("Integração de ESG + Logística + Ciência de Dados + Inovação")

# =========================
# ABAS
# =========================
tab1, tab2, tab3, tab4 = st.tabs([
    "🌱 ESG & RH",
    "🚚 Logística",
    "📊 Ciência de Dados",
    "🚀 Inovação & Canvas"
])

# =========================
# 1. ESG
# =========================
with tab1:
    st.header("🌱 RH liderando a agenda ESG")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Redução de Papel", "-50%", "✔ Meta atingida")
    with col2:
        st.metric("Emissão de CO2", "-30%", "✔ Redução")
    with col3:
        st.metric("Engajamento ESG", "85%", "+10%")

    st.subheader("Ações ESG aplicadas na empresa")

    st.checkbox("Digitalização de materiais didáticos")
    st.checkbox("Certificados digitais")
    st.checkbox("Programa de diversidade e inclusão")
    st.checkbox("Treinamentos de sustentabilidade")
    st.checkbox("Canal de ética e governança")

    st.success("O RH atua como agente central na transformação cultural ESG da organização.")

# =========================
# 2. LOGÍSTICA
# =========================
with tab2:
    st.header("🚚 Logística e Cadeia de Suprimentos")

    fornecedores = pd.DataFrame({
        "Fornecedor": ["Impressão", "Internet", "Software", "Limpeza", "Equipamentos"],
        "Custo Mensal (R$)": [3000, 1200, 2500, 1800, 4000]
    })

    st.dataframe(fornecedores, use_container_width=True)

    fig = px.bar(
        fornecedores,
        x="Fornecedor",
        y="Custo Mensal (R$)",
        color="Fornecedor",
        title="Custos por Fornecedor"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.warning("Gargalo identificado: alto custo com impressão e baixa digitalização.")

    st.success("Solução: migração para plataforma 100% digital e fornecedores sustentáveis.")

# =========================
# 3. CIÊNCIA DE DADOS
# =========================
with tab3:
    st.header("📊 Ciência de Dados & Inteligência Competitiva")

    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Matrículas", df["Matrículas"].iloc[-1], "+30")
    with col2:
        st.metric("Evasão", str(df["Evasão (%)"].iloc[-1]) + "%", "-2%")
    with col3:
        st.metric("Satisfação", str(df["Satisfação (%)"].iloc[-1]) + "%", "+4%")

    fig1 = px.line(df, x="Mês", y="Matrículas", title="Crescimento de Matrículas")
    fig2 = px.line(df, x="Mês", y="Satisfação (%)", title="Satisfação dos Alunos")

    st.plotly_chart(fig1, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Insights Automáticos")

    if df["Matrículas"].iloc[-1] > df["Matrículas"].iloc[0]:
        st.success("Tendência positiva de crescimento de alunos.")

    if df["Evasão (%)"].iloc[-1] < df["Evasão (%)"].iloc[0]:
        st.success("Redução consistente da evasão escolar.")

    if df["Satisfação (%)"].iloc[-1] > 85:
        st.info("Alta satisfação indica forte retenção e qualidade do ensino.")

# =========================
# 4. INOVAÇÃO + CANVAS
# =========================
with tab4:
    st.header("🚀 Inovação & Business Model Canvas")

    st.subheader("💡 Proposta de Valor")
    st.success("""
    Formação profissional acessível, digital e orientada ao mercado,
    com foco em empregabilidade, tecnologia e sustentabilidade ESG.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Clientes")
        st.write("- Jovens\n- Profissionais\n- Empresas")

        st.markdown("### Canais")
        st.write("- Plataforma online\n- Presencial\n- Redes sociais")

    with col2:
        st.markdown("### Atividades-chave")
        st.write("- Ensino digital\n- Gestão acadêmica\n- IA educacional")

        st.markdown("### Recursos-chave")
        st.write("- Plataforma\n- Professores\n- Dados")

    with col3:
        st.markdown("### Receita")
        st.write("- Cursos pagos\n- Parcerias\n- Programas corporativos")

        st.markdown("### Parcerias")
        st.write("- Empresas locais\n- Tech providers\n- RH corporativo")

    st.subheader("📈 Viabilidade Estratégica")

    viabilidade = pd.DataFrame({
        "Critério": ["Financeira", "Tecnológica", "Mercado", "ESG"],
        "Avaliação": ["Alta", "Alta", "Muito Alta", "Alta"]
    })

    st.table(viabilidade)

    st.success("A inovação proposta é altamente viável e fortalece a competitividade da instituição.")