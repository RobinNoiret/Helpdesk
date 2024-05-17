import requests
from requests.auth import HTTPBasicAuth

# Informations de connexion et d'authentification
subdomain = 'your_subdomain'
email = 'your_email/token'
api_token = 'your_APItoken'
attachment_id = 'id_attachment'

# Construire l'URL pour supprimer la pièce jointe
url = f'https://{subdomain}.zendesk.com/api/v2/attachments/{attachment_id}.json'

# En-têtes HTTP
headers = {
    'Content-Type': 'application/json',
}

# Authentification avec l'email et le jeton API
auth = HTTPBasicAuth(email, api_token)

# Faire la requête DELETE pour supprimer la pièce jointe
response = requests.delete(url, auth=auth, headers=headers)

# Vérifier la réponse de l'API
if response.status_code == 204:
    print("La pièce jointe a été supprimée avec succès.")
else:
    print(f"Échec de la suppression de la pièce jointe. Statut: {response.status_code}, Détails: {response.text}")
