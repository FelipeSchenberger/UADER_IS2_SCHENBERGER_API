import argparse
import openai

# Configura tu API Key de OpenAI
openai.api_key = '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'

# Variable global para almacenar el buffer de consultas
buffer_consultas = []

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

        # Agregar la respuesta de ChatGPT al buffer de consultas
        buffer_consultas.append(response.choices[0].message.content)

        # Imprimir la respuesta de ChatGPT
        print("chatGPT: " + response.choices[0].message.content)

    except Exception as e:
        print("Ocurrió un error al interactuar con ChatGPT:", e)

# Función para manejar la entrada del usuario
def manejar_entrada_usuario():
    try:
        # Leer la entrada del usuario
        consulta = input("Ingrese su consulta (o 'salir' para terminar): ")

        return consulta

    except KeyboardInterrupt:
        print("\nSaliendo del programa...")
        exit()

# Función principal
def main():
    # Configurar argumento de línea de comandos
    parser = argparse.ArgumentParser(description='Procesa las consultas del usuario.')
    parser.add_argument('--convers', action='store_true', help='Modo de conversación')
    args = parser.parse_args()

    modo_conversacion = args.convers

    # Verificar si se ha activado el modo de conversación
    if modo_conversacion:
        print("Modo de conversación activado.")

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
                    # Interactuar con ChatGPT
                    if modo_conversacion:
                        # Usar el buffer de consultas para la interacción
                        consulta_para_chatGPT = "\n".join(buffer_consultas)
                    else:
                        consulta_para_chatGPT = consulta

                    interactuar_con_chatGPT(consulta_para_chatGPT)

                except Exception as e:
                    print("Ocurrió un error al tratar la consulta:", e)
            else:
                print("La consulta está vacía.")

        except Exception as e:
            print("Ocurrió un error:", e)

if __name__ == "__main__":
    main()
