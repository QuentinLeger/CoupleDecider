import time
from groq import Groq
import json
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field
from typing import List


load_dotenv()
apiKey = os.getenv("GROQ_API_KEY")
client = Groq(api_key=apiKey)

class coupleDecider(BaseModel):
    titre_proposition: str = Field(description="Proposition du titre d'un film, d'un restaurant, d'une activité a faire")
    note_compromis: float = Field(description="Une note de compromis entre les 2 de 0 à 10")
    pourquoi_quentin: str = Field(description="Argument personnalisé pour convaincre Quentin de faire ce choix") # <-- Corrigé
    pourquoi_perrine: str = Field(description="Argument personnalisé pour convaincre Perrine de faire ce choix") # <-- Corrigé


class coupleMultiDecider(BaseModel):
    multiDecider: List[coupleDecider] = Field(description="Fait plusieurs proposition de compromis exactement 3")

def ask_cDecider_compromis(q_envie : str,p_envie : str , theme : str) -> dict:
    schema_force = json.dumps(coupleMultiDecider.model_json_schema(), indent=2)

    prompt = f"""
        Tu es Nova, un expert en conciliation de couple cynique, percutant et ultra-réaliste. 
        Ton but est de sauver la soirée de Quentin et Perrine en proposant 3 vrais choix réalistes pour l'activité : {theme}.

        Données du problème :
        - Quentin exprime : {q_envie}
        - Perrine exprime : {p_envie}

        Règles d'or pour tes propositions :
        1. RÉALISME ABSOLU : Ne propose JAMAIS de concepts absurdes qui n'existent pas dans la vraie vie (comme un resto italien qui sert des sushis, c'est interdit). Les propositions doivent être de vraies idées de sorties ou de plats réalisables.
        2. PSYCHOLOGIE : Si quelqu'un dit qu'il n'a pas faim, ne lui propose pas de "se sustenter avec du poulet". Propose plutôt un format (ex: planches à partager, tapas, ou un ciné avant de manger) où l'un peut picorer et l'autre faire un vrai repas.
        3. TON DIRECT : Dans tes arguments, parle au "Tu". Sois convaincant, utilise un ton un peu taquin mais ultra-pertinent. Ne répète pas les mots de l'énoncé.

        Tu dois obligatoirement générer un JSON valide qui respecte le schéma :
        {schema_force}
        """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)