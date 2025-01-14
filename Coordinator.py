import json
import re
import ollama
import streamlit as st
from datetime import datetime

class Coordinator:
    def __init__(self, model="phi4", prompt_file="prompts/multiagent.txt"):
        self.model = model
        self.context = None  # Contexto de la conversación
        self.history = []  # Historial de interacciones

        with open(prompt_file, "r", encoding="utf-8") as file:
            self.prompt_template = file.read()

    def process_message(self, input_text):
        """
        Procesa la solicitud del usuario utilizando el modelo de IA para detectar la acción.
        Devuelve un diccionario con la información extraída de la frase.
        """
        if self.context:
            conversation_history = f"Última interacción: {self.context}. "
        else:
            conversation_history = ""

        current_date = datetime.today().strftime("%Y-%m-%d")

        prompt = self.prompt_template.format(
            current_date=current_date,
            conversation_history=conversation_history,
            input_text=input_text
        )

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        print("Respuesta de Ollama:", response)

        try:
            message_content = response['message']['content']

            match = re.search(r'\{.*\}', message_content, re.DOTALL)
            if match:
                json_str = match.group(0)  
                action_info = json.loads(json_str) 

                if action_info['actions'] == 'consultar':
                    self.context = 'Consultando reuniones'
                elif action_info['actions'] == 'agendar':
                    self.context = f'Agendando reunión con {action_info["details"].get("contact_name", "desconocido")}'
                elif action_info['actions'] == 'añadir_contacto':
                    self.context = f'Añadiendo contacto {action_info["details"].get("name", "desconocido")}'

                self.history.append({
                    'user_input': input_text,
                    'response': action_info
                })

                return action_info
            else:
                print("No se encontró un bloque JSON válido.")
                return None
        except Exception as e:
            print("Error procesando la respuesta:", e)
            return None

    def get_history(self):
        """Devuelve el historial de la conversación."""
        return self.history

    def clear_history(self):
        """Limpiar el historial de la conversación."""
        self.history = []
        self.context = None  


st.title("💬 AIssistant")
coordinator = Coordinator()

if st.button('Ver historial'):
    history = coordinator.get_history()
    if history:
        for entry in history:
            st.write(f"Usuario: {entry['user_input']}")
            st.write(f"Agente: {entry['response']}")
    else:
        st.write("No hay historial.")

user_input = st.text_input("Escribe tu mensaje:")

if user_input:
    response = coordinator.process_message(user_input)

    if response:
        st.write(f"Agente: {response}")
    else:
        st.write("No se pudo procesar la solicitud.")

if st.button('Limpiar historial'):
    coordinator.clear_history()
    st.write("Historial limpiado.")