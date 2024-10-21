from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY


def create_supabase_client():
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase
