import openai

# Configura tu API Key de OpenAI
openai.api_key = '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'

# Variable global para almacenar la última consulta
ultima_consulta = ""

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

# Función para manejar la entrada del usuario
def manejar_entrada_usuario():
    global ultima_consulta
    try:
        # Leer la entrada del usuario
        consulta = input("Ingrese su consulta (o 'salir' para terminar): ")

        # Si la consulta es vacía y hay una última consulta almacenada, recuperarla
        if not consulta.strip() and ultima_consulta:
            consulta = ultima_consulta
            print("Consulta recuperada:", consulta)

        # Almacenar la consulta como la última consulta
        ultima_consulta = consulta

        return consulta

    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()

# Función principal
def main():
    while True:
        try:
            # Solicitar consulta al usuario
            consulta = manejar_entrada_usuario()

            # Verificar si el usuario quiere salir
            if consulta.lower() == "salir":
                break

            # Verificar si la consulta tiene texto
            if consulta.strip():
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
