import os
import sqlite3
from dotenv import load_dotenv

# Load local infrastructure variables safely
load_dotenv()

class MemoryManager:
    def __init__(self):
        self.db_path = os.getenv("SQLITE_DB_PATH", "./src/memory/storage.db")
        self.obsidian_path = os.getenv("OBSIDIAN_VAULT_PATH")
        self._bootstrap_databases()

    def _bootstrap_databases(self):
        """Ensures local storage directories and databases exist securely"""
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
            
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create a standardized table to track long-term agent execution history
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agent_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                task_prompt TEXT,
                execution_status TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def query_knowledge_base(self, lookup_key: str):
        """Interface method for searching unstructured Markdown files in an Obsidian Vault"""
        print(f"[Memory Fabric] Scanning Vault context at: {self.obsidian_path}")
        return []

if __name__ == "__main__":
    memory = MemoryManager()
    print("[Success] Local memory fabrics initialized cleanly.")
