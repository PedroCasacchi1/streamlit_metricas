import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
df_tickets = pd.read_excel('Report_ITSrvices_8Meses(2).xlsx')

# Configuração do Streamlit
st.title("Análise de Atendimentos de TI")

# Exibindo a tabela de dados
st.subheader("Dados de Atendimentos de TI")
st.dataframe(df_tickets)

# 1. Tempo Médio de Fechamento por Mês de Abertura
st.subheader("Tempo Médio de Fechamento por Mês de Abertura")
df_tickets['Tempo de Fechamento (dias)'] = (df_tickets['Data de Fechamento'] - df_tickets['Aberto em']).dt.days
average_closure_time = df_tickets.groupby(df_tickets['Aberto em'].dt.to_period('M'))['Tempo de Fechamento (dias)'].mean()

fig7, ax7 = plt.subplots()
average_closure_time.plot(kind='line', marker='o', color='orange', ax=ax7)
ax7.set_title("Tempo Médio de Fechamento por Mês de Abertura")
ax7.set_xlabel("Mês de Abertura")
ax7.set_ylabel("Tempo Médio de Fechamento (dias)")
st.pyplot(fig7)

# 2. Contagem de Tickets por Status
st.subheader("Contagem de Tickets por Status")
status_counts = df_tickets['Status'].value_counts()
fig2, ax2 = plt.subplots()
status_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax2, startangle=90)
ax2.set_ylabel("")
ax2.set_title("Contagem de Tickets por Status")
st.pyplot(fig2)
# 2. Contagem de Tickets por Status
st.subheader("Contagem de Tickets por Assunto")
assunto_counts = df_tickets['Assunto'].value_counts()
fig3, ax3 = plt.subplots()
assunto_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax3, startangle=90)
ax3.set_ylabel("")
ax3.set_title("Contagem de Tickets por Assunto")
st.pyplot(fig3)

# 4. Tickets por Nível de Urgência
st.subheader("Tickets por Nível de Urgência")
urgencia_counts = df_tickets['Urgência'].value_counts()
fig4, ax4 = plt.subplots()
urgencia_counts.plot(kind='bar', color='salmon', ax=ax4)
ax4.set_title("Tickets por Nível de Urgência")
ax4.set_xlabel("Urgência")
ax4.set_ylabel("Número de Tickets")
st.pyplot(fig4)
