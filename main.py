import os
from dotenv import load_dotenv
from groq import Groq

# Carrega as variáveis do arquivo .env
load_dotenv()

# Inicializa o cliente da Groq usando a chave correta
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analisar_sentimento(texto):
    completion = client.chat.completions.create(
        model="llama3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Você é um analista de sentimentos. Responda apenas com uma palavra: POSITIVO, NEGATIVO ou NEUTRO."
            },
            {
                "role": "user",
                "content": texto
            }
        ],
    )
    return completion.choices[0].message.content

# Teste prático
feedback = "O pão estava quentinho, mas o atendimento demorou muito hoje."
resultado = analisar_sentimento(feedback)

print(f"Feedback: {feedback}")
print(f"Sentimento detectado: {resultado}")