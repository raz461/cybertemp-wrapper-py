import requests

class HTTPClient:
    def __init__(self, base_url: str, api_key: str = None):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

    def _build_headers(self, use_auth=False, auth_type="x-api-key"):
        headers = {}
        if use_auth:
            if not self.api_key:
                return None, {"error": "API key is required for this endpoint"}

            if auth_type == "bearer":
                headers["X-API-KEY"] = f"Bearer {self.api_key}"
            elif auth_type == "x-api-key":
                headers["X-API-KEY"] = self.api_key
            else:
                return None, {"error": f"Unknown auth type: {auth_type}"}
        return headers, None

    def get(self, endpoint: str, use_auth=False, auth_type="x-api-key"):
        headers, error = self._build_headers(use_auth, auth_type)
        if error:
            return error
        response = self.session.get(f"{self.base_url}{endpoint}", headers=headers)
        return self._parse_response(response)

    def delete(self, endpoint: str, use_auth=False, auth_type="x-api-key"):
        headers, error = self._build_headers(use_auth, auth_type)
        if error:
            return error
        response = self.session.delete(f"{self.base_url}{endpoint}", headers=headers)
        return self._parse_response(response)

    def _parse_response(self, response):
        try:
            data = response.json()
        except ValueError:
            return {"error": "Invalid JSON response"}
        return data if "error" not in data else {"error": data["error"]}
