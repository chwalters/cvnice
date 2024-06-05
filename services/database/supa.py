from typing import Optional

from supabase import Client as SupabaseClient

from config import settings

# supabase: SupabaseClient = create_client(settings.supabase_url, settings.supabase_key)

supabase_clients = {}

def get_client(username: str) -> SupabaseClient:
    client: SupabaseClient = supabase_clients.get(username, None)
    if client is None:
        client = SupabaseClient(settings.supabase_url, settings.supabase_key)
        supabase_clients[username] = client
    return client

class DBClient():
    connection: Optional[SupabaseClient] = None
    def __init__(self, client: SupabaseClient) -> None:
        self.connection: SupabaseClient = client

