import requests
from requests.auth import HTTPBasicAuth
import json
import pandas as pd

# Informations de connexion et d'authentification
subdomain = 'you-domain'
email = 'your_mail'
api_token = 'you_tokenAPI'

organization_id = 'your_organizationID'
start_date = 'your_start date'  # YYYY-MM-DD

# URL pour rechercher les tickets
url = f'https://{subdomain}.zendesk.com/api/v2/search.json'

# En-têtes de la requête
headers = {
    'Content-Type': 'application/json',
}

# Authentification avec l'email et le jeton API
auth = HTTPBasicAuth(f'{email}/token', api_token)

# Construire les paramètres de la requête GET
params = {
    'query': f'type:ticket organization_id:{organization_id} created>={start_date}',
}

# Requête GET pour obtenir les tickets
response = requests.get(url, auth=auth, headers=headers, params=params)

# Vérifier la réponse
if response.status_code == 200:
    tickets_data = response.json()['results']
    
    if tickets_data:
        # Filtrer et sélectionner les champs spécifiques pour chaque ticket
        filtered_tickets = []
        for ticket in tickets_data:
            filtered_ticket = {                         # update it if you need
                'ticket_id': ticket['id'],
                'subject': ticket['subject'],
                'created_at': ticket['created_at'],
                'updated_at' : ticket['updated_at'],
                'status': ticket['status'],
                'business impact': ticket['custom_fields'][8]['value'] if 'custom_fields' in ticket else None
                # Ajoutez d'autres champs ici si nécessaire
            }
            filtered_tickets.append(filtered_ticket)
        
        # Sauvegarder les données filtrées dans un fichier JSON
        json_filename = 'tickets_data_filtered.json'
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(filtered_tickets, json_file, ensure_ascii=False, indent=4)
        
        print(f'Données filtrées enregistrées en JSON dans : {json_filename}')

        # Convertir en NDJSON si nécessaire (similaire à votre code actuel)

        csv_filename = 'export.csv'

        # Création d'un DataFrame à partir des données filtrées
        df = pd.DataFrame(filtered_tickets)

        # Écriture du DataFrame dans un fichier CSV
        df.to_csv(csv_filename, index=False, encoding='utf-8')

        print(f'Conversion JSON filtré vers CSV réussie. Fichier: {csv_filename}')
        
    else:
        print("Aucun ticket trouvé.")
else:
    print(f"Échec de la récupération des tickets. Statut: {response.status_code}, Détails: {response.text}")