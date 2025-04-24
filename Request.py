import requests
from bs4 import BeautifulSoup

# 1. GET request et affichage du contenu
response = requests.get("https://www.example.com")
print(response.content)  # Correction: 'repsonse' → 'response'

# 2. POST request avec des données JSON
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"
response = requests.post(url, json=data)
response_data = response.json()
print(response_data)  # Affiche les données envoyées

# 3. Vérification du statut HTTP
response = requests.get("https://httpbin.org/status/404")
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")

# 4. Gestion du timeout
url = "https://httpbin.org/delay/10"
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.Timeout as err:
    print("Request timed out:", err)

# 5. Requête avec jeton d'authentification
auth_token = "XXXXXXXX"
headers = {
    "Authorization": f"Bearer {auth_token}"
}
url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())

# 6. Analyse du contenu HTML avec BeautifulSoup
url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
