import requests

def lire_urls(fichier_entree):
    
    # Lit les URL à partir d'un fichier et les retourne sous forme de liste.
    
    try:
        with open(fichier_entree, 'r') as f:
            urls = f.readlines()
        return [url.strip() for url in urls if url.strip()]
    except FileNotFoundError:
        print(f"Erreur: Le fichier {fichier_entree} est introuvable.")
        return []

def tester_url(url):
   
   # Teste une URL avec HTTP et HTTPS, retourne un tuple (url, status).
   
    http_accessible = False
    https_accessible = False

    print(f"Test de l'URL: {url}")

    try:
        response = requests.head(f"http://{url}", allow_redirects=True)
        if response.status_code == 200:
            http_accessible = True
    except requests.RequestException as e:
        print(f"Erreur avec HTTP: {e}")

    try:
        response = requests.head(f"https://{url}", allow_redirects=True)
        if response.status_code == 200:
            https_accessible = True
    except requests.RequestException as e:
        print(f"Erreur avec HTTPS: {e}")

    if http_accessible and https_accessible:
        return (url, "accessible avec HTTP et HTTPS")
    elif http_accessible:
        return (url, "accessible avec HTTP seulement")
    elif https_accessible:
        return (url, "accessible avec HTTPS seulement")
    else:
        return (url, "Erreur: inaccessible avec HTTP et HTTPS")


def tester_urls(urls):
    
    # Teste une liste d'URL et retourne les résultats sous forme de liste de tuples.
    
    resultats = []
    for url in urls:
        resultats.append(tester_url(url))
    return resultats

def ecrire_resultats(fichier_sortie, resultats):
    
   # Écrit les résultats dans un fichier de sortie.
    
    with open(fichier_sortie, 'w') as f:
        for url, status in resultats:
            f.write(f"{url} : {status}\n")
    print(f"Les résultats ont été écrits dans {fichier_sortie}")

def main(fichier_entree, fichier_sortie):
    
   # Fonction principale du script.
    
    urls = lire_urls(fichier_entree)
    if not urls:
        print("Aucune URL à tester.")
        return
    resultats = tester_urls(urls)
    ecrire_resultats(fichier_sortie, resultats)

if __name__ == "__main__":
    fichier_entree = 'urls.txt'  
    fichier_sortie = 'resB.txt'  
    print(f"Début de l'exécution du script avec {fichier_entree} et {fichier_sortie}")
    main(fichier_entree, fichier_sortie)
    print("Fin de l'exécution du script")
