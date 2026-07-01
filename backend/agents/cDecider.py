import time
from groq import Groq
import json
from dotenv import load_dotenv
import os
from pydantic import BaseModel,Field


load_dotenv()
apiKey = os.getenv("GROQ_API_KEY")
client = Groq(api_key=apiKey)

class coupleDecider(BaseModel):
    titre_proposition: str = Field(description="Proposition du titre d'un film, d'un restaurant, d'une activité a faire")
    note_compromis: float = Field(description="Une note de compromis entre les 2 de 0 à 10")
    pourquoi_quentin: str = Field(description="Argument personnalisé pour convaincre Quentin de faire ce choix") # <-- Corrigé
    pourquoi_perrine: str = Field(description="Argument personnalisé pour convaincre Perrine de faire ce choix") # <-- Corrigé

def ask_cDecider_compromis(q_envie : str,p_envie : str , theme : str) -> dict:
    schema_force = json.dumps(coupleDecider.model_json_schema(), indent=2)

    prompt = f"""
        Tu es une IA de coupleDecider, l'arbitre du couple Quentin et Perrine.
        Ton objectif est de décider une activité, un film ou repas un restau en fonction des envies des 2.
        Ils veulent faire l'activité : {theme}
        Quentin est plus : {q_envie}
        Perrine est plus : {p_envie}

        Tu dois obligatoirement répondre sous la forme d'un objet JSON valide.
        Tu as interdiction d'inventer des clés. Tu dois respecter EXACTEMENT ce schéma JSON :
        {schema_force}
        """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)