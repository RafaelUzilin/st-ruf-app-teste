import streamlit as st
import plotly.express as px


st.header("Maiores Valores")

if 'dados' not in st.session_state:
    st.error("Os dados não foram carregaods")

else:
    top_n = st.session_state.get('top_n', 10)
    dados = st.session_state['dados']

    col1, col2 = st.columns(2)

    with col1:
        m_empenho = dados.nlargest(top_n, "VALOREMPENHO")
        fig1 = px.bar(m_empenho, x='MUNICIPIO', y='VALOREMPENHO',
                     title="Maiores Empenhos")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        m_pib = dados.nlargest(top_n, "PIB")
        fig2 = px.pie(m_pib, names='MUNICIPIO', values='PIB',
                     title="Maiores PIB")
        st.plotly_chart(fig2, use_container_width=True)


    m_prob = dados.nlargest(top_n, "PROPORCAO")
    fig3 = px.bar(m_prob, y='MUNICIPIO', x='PROPORCAO',
                  title="Maiores proporções", orientation='h')

    st.plotly_chart(fig3, use_container_width=True)