"""
Implementa la funzione func1(pokemon_list: list[dict]) -> list[str] che
- riceve come argomento una lista di pokemon
- ritorna i 3 migliori in base al loro "Power Score"

Ciascun pokemon è rappresentato da un dizionario con le chiavi 'name', 'atk', 'spd', 'def'
Ad esempio: {'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}

Il "Power Score" è ottenuto come (atk * 1.5) + (spd * 1.2) + def
Nell'esempio il valore è 37.7 = 10*1.5+10*1.2+10

I pokemon devono essere ordinati:
1. Per punteggio decrescente (dal più alto al più basso).
2. In caso di parità di punteggio, in ordine alfabetico di name (A-Z).

Restituisce: Una lista con i nomi dei primi 3 personaggi in classifica.

Esempio:
    pokemon_list = [{'name': 'A', 'atk': 10, 'spd': 10, 'def': 10}, # Score 37.0
                    {'name': 'B', 'atk': 10, 'spd': 10, 'def': 10}] # Score 37.0
    Restituisce: ['A', 'B'] (perché A viene prima di B in ordine alfabetico)
"""
def func1(pokemon_list: list[dict]) -> list[str]:
    ranked_pokemon= sorted(pokemon_list,
                           key=lambda pokemon: (-(pokemon["atk"]*1.5 + pokemon["spd"]*1.2 + pokemon["def"]), pokemon["name"]))
    top_three= ranked_pokemon[:3]  #top_three is a list composed of dicts, we just need the names
    names=[]
    for pokemon in top_three:
        names.append(pokemon["name"])
    return names     #DONT WRITE RETURN INSIDE THE LOOP





# =============================================================================
# FUNC 2 (4 punti)
# =============================================================================
"""
Filtro Chat: Censura le parole proibite presenti nella lista banned_words.

REGOLE:
- Sostituisci nel testo 'text' la parola sostituendola con tanti '*' quanti sono i suoi caratteri.
- Il controllo deve essere case-insensitive (es: 'mela' censura 'MELA').
- Mantieni intatta la punteggiatura e il case originale delle parole non censurate.

Esempio:
    text = "Attenzione all'ORCO nel bosco! (ma non all'OrCoNe)"
    banned_words = ["orco"]
    Restituisce: "Attenzione all'**** nel bosco!  (ma non all'OrCoNe)"
"""
def func2(text: str, banned_words: list[str]) -> str:
   current_word=""
   result=""
   for char in text:
       if char.isalpha():
           current_word=current_word+char
       else:
           if current_word.lower() in banned_words:  #currentword is a string, banned words is a list, so you CANT use ==
             result= result+ "*" * len(current_word)
           else:
             result= result+current_word
           result = result + char     #for the space/'/! etc
           current_word = ""

   return result



