import streamlit as st
import google.generativeai as genai

st.title("Adaptación Curricular Automatizada")

# Conectar con la API de Gemini usando la llave secreta
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("Falta configurar la GEMINI_API_KEY en los secretos de Streamlit.")
    st.stop()

secuencia_original = st.text_area("Pega aquí la secuencia didáctica original:", height=200)

perfil = st.selectbox("Selecciona el perfil del estudiante:", ["TDAH", "Dislexia", "TEA", "Baja Visión"])
formato = st.multiselect("Formatos requeridos:", ["Imprenta Mayúscula", "Opción Múltiple", "Oraciones Cloze", "Resumen de Conceptos"])

if st.button("Adaptar Secuencia"):
    if secuencia_original and formato:
        with st.spinner('La IA está procesando el texto. Esto puede tardar unos segundos...'):
            try:
                # Usamos el modelo rápido de Gemini
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                # Este es el PROMPT. Las instrucciones directas para la IA.
                prompt = f"""
                Eres un experto en educación especial y diseño universal para el aprendizaje. 
                Tu tarea es adaptar la siguiente secuencia didáctica para un estudiante con {perfil}.
                
                Debes aplicar OBLIGATORIAMENTE los siguientes formatos solicitados: {', '.join(formato)}.
                
                Reglas:
                - Mantén el contenido curricular y la precisión de la información intactos.
                - Si se piden Oraciones Cloze, deja espacios en blanco (_____) en los conceptos clave.
                - Si se pide Opción Múltiple, genera preguntas basadas en el texto con 3 opciones claras.
                - Indica los lugares exactos donde el docente debería insertar una imagen escribiendo: [Insertar imagen alusiva a: (descripción de la imagen)].
                
                Secuencia original:
                {secuencia_original}
                """
                
                # Ejecutar la IA
                respuesta = model.generate_content(prompt)
                texto_final = respuesta.text
                
                # Forzar mayúsculas si se seleccionó, para asegurar que no falle
                if "Imprenta Mayúscula" in formato:
                    texto_final = texto_final.upper()
                
                st.subheader("Resultado Adaptado:")
                st.write(texto_final)
                
            except Exception as e:
                st.error(f"Ocurrió un error al contactar a la IA: {e}")
    else:
        st.warning("Por favor, ingresa el texto original y selecciona al menos un formato.")