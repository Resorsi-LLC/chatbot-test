# Resorsi Chatbot

**Resorsi Chatbot** es un chatbot desarrollado en Python3 que permite buscar y filtrar candidatos mediante un chat. Utiliza tecnologías como Streamlit, Supabase y OpenAI, además de LangChain para optimizar las consultas.

## Requisitos

- **Python 3+**
- Acceso a una cuenta de **OpenAI** para utilizar la APIs
- Acceso a **Supabase**

## Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone git@github.com:Resorsi-LLC/chatbot-test.git
   cd resorsi-test
   ```

2. Instala las dependencias requeridas:

   ```bash
   sudo pip3 install -r requirements.txt
   ```

## Configuracion

El proyecto requiere algunas variables de entorno para funcionar correctamente. Crea un archivo `.env` en el directorio principal del proyecto y completa las variables.

## Uso

1. Ejecuta la aplicación de Streamlit para iniciar el chatbot:

```
streamlit run app.py
```

2. Abre el navegador en la dirección http://localhost:8501 para interactuar con el chatbot.
