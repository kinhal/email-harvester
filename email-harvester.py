import requests
import re
from colorama import Fore, Style, init

init(autoreset=True)

def estrai_email(url):
    print(Fore.CYAN + f"[*] Scaricando contenuti da: {url}" + Style.RESET_ALL)
    try:
        risposta = requests.get(url, timeout=10)
        contenuto = risposta.text
    except requests.RequestException as e:
        print(Fore.RED + f"[!] Errore durante la richiesta: {e}")
        return []

    # Regex per trovare email (semplice ma efficace)
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, contenuto)
    emails_uniche = list(set(emails))  # rimuove duplicati

    if emails_uniche:
        print(Fore.GREEN + f"[+] Trovate {len(emails_uniche)} email:\n")
        for email in emails_uniche:
            print(Fore.YELLOW + email)
    else:
        print(Fore.RED + "[!] Nessuna email trovata.")
    return emails_uniche

def main():
    url = input(Fore.LIGHTBLUE_EX + "Inserisci URL (es. https://example.com): " + Style.RESET_ALL)
    if not (url.startswith("http://") or url.startswith("https://")):
        print(Fore.RED + "Errore: inserisci un URL valido che inizi con http:// o https://")
        return

    estrai_email(url)
    input(Fore.LIGHTBLUE_EX + "\nPremi un tasto per uscire..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
