import time


def ask_cDecider_compromis(q_envie,p_envie,theme):
    time.sleep(1.5)

    return {
        "titre_proposition":"Inception",
        "note_compromis":9,
        "pourquoi_quentin":f"Il a besoin d'un film d'action tsais (il voulait : {q_envie})",
        "pourquoi_perrine":f"Elle veut rien de spécial aujourd'hui (votre envie etait : {p_envie})"
    }