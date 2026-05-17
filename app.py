import streamlit as st

st.title("Adaptación Curricular Automatizada")
st.write("Esta es la versión alfa de tu herramienta de adaptación.")

# Cuadro para pegar la secuencia didáctica
secuencia_original = st.text_area("Pega aquí la secuencia didáctica original:", height=200)

# Opciones de adaptación
perfil = st.selectbox("Selecciona el perfil del estudiante:", ["TDAH", "Dislexia", "TEA", "Baja Visión"])
formato = st.multiselect("Formatos requeridos:", ["Imprenta Mayúscula", "Opción Múltiple", "Oraciones Cloze"])

if st.button("Adaptar Secuencia"):
    if secuencia_original:
        st.subheader("Resultado Adaptado (Simulado):")
        texto_procesado = secuencia_original
        
        if "Imprenta Mayúscula" in formato:
            texto_procesado = texto_procesado.upper()
            
        st.write(texto_procesado)
        st.info(f"Falta conectar la IA para procesar el perfil: {perfil}")
    else:
        st.error("Por favor, ingresa un texto primero.")
