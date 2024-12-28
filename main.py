import requests
import json
import streamlit as st



BASE_API_URL = "https://diegomyv-wizard.hf.space"
FLOW_ID = "198e58f4-b2dd-4d3a-b463-80039ba8f1de"
ENDPOINT = "wizard" # You can set a specific endpoint name in the flow settings

def run_flow(game_name: str, game_description: str, game_references: str) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/api/v1/run/{ENDPOINT}"

    prompt = "Mi juego se llama " + game_name + ". El juego se trata sobre " + game_description + ". Toma como referencia los siguientes juegos para buscar en tu base de datos: " + game_references

    payload = {
        "input_value": prompt,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = None
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()


def main():
    st.title("Crearé una descripción para tu juego :male_mage:")
    
    name = st.text_input("Escribe el nombre de tu juego :point_down:", placeholder = "El Regreso del Mago")

    description = st.text_area("¿De qué se trata tu juego?", placeholder = "Dame detalles de su jugabilidad, nombre de personajes, trama, features, etc")

    references = st.text_area("Dime algunos juegos que tengas como referencia (Opcional)")

    if st.button("¡Haz magia!"):
        if not name.strip():
            st.error("Ingresa el nombre")
            return
        if not description.strip():
            st.error("Ingresa el nombre")
            return
        if not references.strip():
            references = "no ocupes otras referencias"
        try:
            with st.spinner("Haciendo magia..."):
                response = run_flow(name, description, references)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()
