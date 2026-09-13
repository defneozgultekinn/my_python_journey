# =============================================================================
# EX 1 (6 punti) - RICORSIVO
# =============================================================================
"""
Si definisca una funzione ricorsiva o che
utilizza funzioni o metodi ricorsivi che determini se esiste un
sottoinsieme di 'arr' composto da esattamente 'n' elementi la cui somma è 's'.

Esempio:
    arr = [1, 5, 2], n = 2, s = 3
    Restituisce: True (il sottoinsieme è [1, 2])
"""

def ex1(arr: list[int], n: int, s: int) -> bool:
   if n==0 and s==0:
       return True
   if n==0 and s!=0:
       return False
   first= arr[0]
   remaining= arr[1:]
   path1= ex1(remaining, n-1, s-int(first))   #the case that we chose the first element
   path2= ex1(remaining,n,s)     #the case that we didnt chose the first element
   return path1 or path2




# =============================================================================
# EX 2 (6 punti) - RICORSIVO
# =============================================================================
"""
Si definisca una funzione ricorsiva o che
utilizza funzioni o metodi ricorsivi che esplora un dizionario 'data'
seguendo una catena di chiavi 'key_chain' e restituisce la profondità
massima raggiunta (numero di dizionari attraversati).

REGOLE:
- Inizia dal dizionario 'data' (profondità 1).
- Cerca la prima chiave di 'key_chain' in 'data'.
- Se trovata e il valore è un dizionario, incrementa la profondità e
  prosegui ricorsivamente nel sottodizionario usando le chiavi rimanenti.
- Se la chiave non è presente, o il valore non è un dizionario, o
  'key_chain' è vuota, l'esplorazione termina.

Esempio:
    data = {'user': {'settings': {'theme': 'dark'}}}
    key_chain = ['user', 'settings', 'theme']
    Esplorazione: data -> user (dict) -> settings (dict) -> theme (str, fine)
    Ritorna: 3
"""


def ex2(data: dict, key_chain: list[str]) -> int:
  if key_chain==[]:
      return 1
  first_key =key_chain[0]
  remaining_keys= key_chain[1:]

  if first_key not in data:
      return 1
  value= data[first_key]
  if not isinstance(value,dict):   #we also have to check if the key is a dict or not
      return 1
  else:
      return 1+ ex2(value,remaining_keys)


#ISINSTANCE() IS A BUILT IN PYTHON FUNCTION
# isinstance(value, type)--->True/False
