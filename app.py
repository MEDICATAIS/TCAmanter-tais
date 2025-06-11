import streamlit as st

st.set_page_config(page_title="QEWP-5 - Dra. Taís Mazzini Setti", layout="centered")
st.title("📋 QEWP-5 - Questionário sobre Padrões de Alimentação e Peso")
st.markdown("Desenvolvido por **Dra. Taís Mazzini Setti – CRM 17117/SC**")
st.caption("Referência: Yanovski SZ, Marcus MD, Wadden TA, Walsh BT. Int J Eating Disorders. DOI: 10.1002/eat.22372")

st.header("Parte 1 - Episódios de Compulsão Alimentar")
q1 = st.radio("1. Comeu grande quantidade de comida em curto período de tempo (ex: 2h)?", ["Sim", "Não"])
if q1 == "Não":
    st.stop()

q2 = st.radio("2. Sentiu que não podia parar de comer ou controlar a quantidade?", ["Sim", "Não"])
if q2 == "Não":
    st.stop()

q3 = st.selectbox("3. Frequência média nos últimos 3 meses:", [
    "Menos de 1 episódio por semana", "1 episódio por semana", "2-3 episódios por semana",
    "4-7 episódios por semana", "8-13 episódios por semana", "14 ou mais episódios por semana"])

st.subheader("4. Sintomas associados ao episódio")
sintoma1 = st.checkbox("Comer mais rápido que o normal")
sintoma2 = st.checkbox("Comer até se sentir desconfortavelmente cheio")
sintoma3 = st.checkbox("Comer sem estar com fome")
sintoma4 = st.checkbox("Comer sozinho por vergonha da quantidade")
sintoma5 = st.checkbox("Sentir-se desgostoso, culpado ou deprimido depois")

st.subheader("5. Descreva um episódio típico")
descricao = st.text_area("Liste tudo que foi consumido (com quantidade, marca etc)")

q6 = st.select_slider("6. Quanto esses episódios te chatearam?", options=["Nem um pouco", "Levemente", "Moderadamente", "Muito", "Extremamente"])

st.subheader("Parte 2 - Comportamentos Compensatórios")
def comportamento_pergunta(label):
    resposta = st.radio(label, ["Não", "Sim"])
    freq = None
    if resposta == "Sim":
        freq = st.selectbox("Frequência semanal:", [
            "Menos de 1 vez/semana", "1 vez/semana", "2-3 vezes/semana",
            "4-5 vezes/semana", "6-7 vezes/semana", "8 ou mais vezes/semana"], key=label)
    return resposta, freq

vomito, freq_vomito = comportamento_pergunta("7. Provocou vômito para evitar ganho de peso?")
laxante, freq_laxante = comportamento_pergunta("8. Usou laxantes em dose elevada?")
diuretico, freq_diuretico = comportamento_pergunta("9. Usou diuréticos em dose elevada?")
jejum, freq_jejum = comportamento_pergunta("10. Jejuou por 24h ou mais para evitar ganho de peso?")
exercicio, freq_exercicio = comportamento_pergunta("11. Exercitou-se excessivamente?")
remedios, freq_remedios = comportamento_pergunta("12. Usou remédios para emagrecer em excesso?")

# Interpretação
st.subheader("Interpretação Clínica Sugestiva")

episodios_frequentes = q3 in ["2-3 episódios por semana", "4-7 episódios por semana", "8-13 episódios por semana", "14 ou mais episódios por semana"]
sintomas_sim = sum([sintoma1, sintoma2, sintoma3, sintoma4, sintoma5]) >= 3
sofrimento = q6 in ["Muito", "Extremamente"]
comportamentos_inadequados = any([
    freq in ["1 vez/semana", "2-3 vezes/semana", "4-5 vezes/semana", "6-7 vezes/semana", "8 ou mais vezes/semana"]
    for freq in [freq_vomito, freq_laxante, freq_diuretico, freq_jejum, freq_exercicio, freq_remedios] if freq is not None
])

diag_sugestivo = all([episodios_frequentes, sintomas_sim, sofrimento]) and not comportamentos_inadequados

if diag_sugestivo:
    st.success("✅ Resultado sugestivo de possível Transtorno de Compulsão Alimentar (TCA).")
else:
    st.info("⚠️ Resultado não preenche critérios clínicos mínimos para sugestão de TCA segundo o QEWP-5.")

st.markdown("\nEste aplicativo não substitui avaliação médica. Use os dados para discussão clínica e rastreamento de TCA.")
