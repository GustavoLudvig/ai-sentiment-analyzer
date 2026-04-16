import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

# 2. Inicializa o cliente da OpenAI usando a chave segura
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analisar_sentimento(texto):
    # 3. Criando a chamada para a IA (LLM)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", # Modelo leve e rápido
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em análise de sentimentos de clientes de uma padaria. Responda apenas com uma palavra: POSITIVO, NEGATIVO ou NEUTRO."},
            {"role": "user", "content": texto}
        ]
    )
    return response.choices[0].message.content

# 4. Teste prático
feedback = "O pão estava quentinho, mas o atendimento demorou muito hoje."
resultado = analisar_sentimento(feedback)

print(f"Feedback: {feedback}")
print(f"Sentimento detectado: {resultado}")