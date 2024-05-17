import requests
from requests.auth import HTTPBasicAuth


# Informations de connexion et d'authentification
subdomain = 'your_subdomain'
email = 'your_mail'
api_token = 'your_APItoken'
ticket_id = 'your_TicketID'

# URL pour obtenir les détails du ticket
url = f'https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json'

# En-têtes de la requête
headers = {
    'Content-Type': 'application/json',
}

# Authentification avec l'email et le jeton API
auth = HTTPBasicAuth(f'{email}/token', api_token) #sans commentaire


# Requête GET pour obtenir les détails du ticket
response = requests.get(url, auth=auth, headers=headers)


# Vérifier la réponse (version simple)
if response.status_code == 200:
    ticket_data = response.json()
    print(ticket_data)
else:
    print(f"Échec de la récupération des détails du ticket. Statut: {response.status_code}, Détails: {response.text}")

