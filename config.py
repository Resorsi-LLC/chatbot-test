from dotenv import dotenv_values

config = dotenv_values(".env")

OPENAI_API_KEY = config.get("OPENAI_API_KEY")
SUPABASE_URL = config.get("SUPABASE_URL")
SUPABASE_KEY = config.get("SUPABASE_KEY")
