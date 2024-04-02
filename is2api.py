import openai

# Configura tu API Key de OpenAI
openai.api_key = "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"

def interactuar_con_chatGPT(consulta):
    # Preparar los mensajes para enviar a ChatGPT
    context = ""
    usertask = ""
    userquery = consulta

    # Realizar la solicitud a la API de ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": usertask},
            {"role": "user", "content": userquery}
        ],
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Imprimir la respuesta de ChatGPT
    print("chatGPT: " + response.choices[0].message.content)

# Función principal
def main():
    # Solicitar consulta al usuario
    consulta = input("Ingrese su consulta: ")

    # Verificar si la consulta tiene texto
    if consulta.strip() != "":
        # Imprimir la consulta
        print("You: " + consulta)

        # Interactuar con ChatGPT
        interactuar_con_chatGPT(consulta)
    else:
        print("La consulta está vacía.")

if __name__ == "__main__":
    main()
