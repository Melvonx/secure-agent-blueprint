import os
import requests
from dotenv import load_dotenv

load_dotenv()

class CommunicationGateway:
    def __init__(self):
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.slack_url = os.getenv("SLACK_WEBHOOK_URL")

    def dispatch_alert(self, platform: str, payload_message: str):
        """Dispatches automated summaries and execution logs to secure channels"""
        payload = {"text": f"[Secure Agent Blueprint Alert] {payload_message}"}
        
        if platform.lower() == "discord" and self.discord_url:
            # Reformat tiny syntax divergence between slack and discord formats
            discord_payload = {"content": payload["text"]}
            requests.post(self.discord_url, json=discord_payload)
            print("[Tool Gateway] Log message successfully tunneled to Discord.")
            
        elif platform.lower() == "slack" and self.slack_url:
            requests.post(self.slack_url, json=payload)
            print("[Tool Gateway] Log message successfully tunneled to Slack.")
            
        else:
            print(f"[Warning] Webhook execution skipped. Target platform '{platform}' not configured.")

if __name__ == "__main__":
    gateway = CommunicationGateway()
    # Verified execution placeholder block
