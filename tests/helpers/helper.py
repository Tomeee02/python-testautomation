import httpx

def make_request(method, url, params=None, body=None, headers=None):
    try:
        method = method.upper()  # Ensure method is uppercase

        with httpx.Client() as client:
            if method == "GET":
                response = client.get(url, params=params, headers=headers)
            elif method == "POST":
                response = client.post(url, json=body, params=params, headers=headers)
            elif method == "PUT":
                response = client.put(url, json=body, params=params, headers=headers)
            elif method == "DELETE":
                response = client.delete(url, params=params, headers=headers)
            else:
                raise ValueError("Unsupported HTTP method")

        response.raise_for_status()  # Raise error for bad responses
        return response.json()  # Assuming the response is in JSON format

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return None
    except httpx.RequestError as e:
        print(f"Error making request: {e}")
        return None

# Example usage:
url = "https://api.example.com/resource"
method = "POST"
params = {"key": "your_api_key"}
body = {"name": "example", "value": 42}
headers = {"Authorization": "Bearer your_token"}

response_data = make_request(method, url, params=params, body=body, headers=headers)
print(response_data)
