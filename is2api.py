import openai

# Configura tu API Key de OpenAI
openai.api_key = "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"

def interactuar_con_chatGPT(consulta):
    try:
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

    except Exception as e:
        print("Ocurrió un error al interactuar con ChatGPT:", e)

# Función principal
def main():
    while True:
        try:
            # Solicitar consulta al usuario
            consulta = input("Ingrese su consulta (o 'salir' para terminar): ")

            # Verificar si el usuario quiere salir
            if consulta.lower() == "salir":
                break

            # Verificar si la consulta tiene texto
            if consulta.strip() != "":
                try:
                    # Imprimir la consulta
                    print("You: " + consulta)

                    # Interactuar con ChatGPT
                    interactuar_con_chatGPT(consulta)

                except Exception as e:
                    print("Ocurrió un error al tratar la consulta:", e)
            else:
                print("La consulta está vacía.")

        except Exception as e:
            print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
