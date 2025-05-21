from http_client import HTTPClient

class CyberTemp:
    def __init__(self, base_url: str = "https://cybertemp.xyz/api", api_key: str | None = None):
        self.client = HTTPClient(base_url, api_key)

    def get_domains(self) -> dict:
        """Fetch the list of currently available domains."""
        return self.client.get("/getDomains")

    def check_mail(self, mail: str) -> dict:
        """Fetch emails for a specific inbox"""
        return self.client.get(f"/getMail?email={mail}")
        
    def check_mail_by_id(self, id: str) -> dict:
        """Fetch a specific email by its ID"""
        return self.client.get(f"/email/{id}")

    def check_balance(self) -> dict:
        """Check the remaining credit balance for your API key"""
        return self.client.get("/getBalance", use_auth=True)

    def get_private_mails(self) -> dict:
        """Fetch emails associated with your private account"""
        return self.client.get("/private/emails", use_auth=True, auth_type="bearer")

    def delete_mail(self, id: str) -> dict:
        """Delete a specific email by its ID"""
        return self.client.delete(f"/email/{id}", use_auth=True, auth_type="bearer")

    def delete_inbox(self, email: str) -> dict:
        """Delete all emails within a specific inbox"""
        return self.client.delete(f"/inbox/{email}", use_auth=True, auth_type="bearer")
