import sys


# On dit explicitement à Python de regarder aussi dans le dossier parent
sys.path.append(".")

import streamlit as st
import backend.agents.cDecider as decider
import backend.config.db_manager as db
db.init_db()
if "q_confirm" not in st.session_state:
    st.session_state.q_confirm = False
if "p_confirm" not in st.session_state:
    st.session_state.p_confirm = False

onglet_vote, onglet_historique = st.tabs(["🔮 Arbitrage de Nova", "📜 Notre Historique"])
with onglet_vote:
    col1, col2, col3 = st.columns(3, vertical_alignment="top")

    with col2:
        st.write("Vous avez choisi :")
        option = st.selectbox(
            "Quelle activité voulez vous faire",
            ("Cinema", "Série", "Restau", "Activité",)
        )

    with col1:
        st.write("Choix de Quentin :")
        quentin_envie = st.text_input("Votre envie", key="quentin_envie")
        if st.button("Confirmer", key="q_confirmer"):
            st.session_state.q_confirm = True
            st.success("Quentin a confirmé !")

    with col3:
        st.write("Choix de Perrine :")
        perrine_envie = st.text_input("Votre envie", key="perrine_envie")
        if st.button("Confirmer", key="p_confirmer"):
            st.session_state.p_confirm = True
            st.success("Perrine a confirmed !")

    # Si l'un des deux clique sur un bouton de choix, on veut garder le résultat affiché
    # Pour ça, on peut stocker le résultat de l'IA en session state pour qu'il ne disparaisse pas au clic
    if st.session_state.p_confirm and st.session_state.q_confirm:
        with st.spinner("🔮 Nova épluche vos critères et prépare l'arbitrage..."):
            st.session_state.dernier_resultat = decider.ask_cDecider_compromis(quentin_envie, perrine_envie, option)

        # On remet à zéro les confirmations pour le prochain vote
        st.session_state.q_confirm = False
        st.session_state.p_confirm = False

    # Affichage du résultat s'il existe en mémoire de session
    if "dernier_resultat" in st.session_state:
        resultat = st.session_state.dernier_resultat
        st.success("### 🎉 Voici les propositions de Nova !")
        st.divider()

        for i, prop in enumerate(resultat['multiDecider']):
            with st.expander(f"💡 Option {i + 1} : {prop['titre_proposition']} (Équité: {prop['note_compromis']}/10)"):

                # Le bouton magique de sauvegarde
                if st.button(f"👉 Choisir l'option {i + 1}", key=f"choix_{i}"):
                    db.sauvegarder_compromis(option, prop['titre_proposition'], prop['note_compromis'], quentin_envie,
                                             perrine_envie)
                    st.success("✅ Choix enregistré ! L'historique a été mis à jour.")
                    # On nettoie le résultat de la session pour clore le vote
                    del st.session_state.dernier_resultat
                    st.rerun()

                col_q, col_p = st.columns(2)
                with col_q:
                    st.info(f"**Pour Quentin 🕶️ :**\n\n{prop['pourquoi_quentin']}")
                with col_p:
                    st.warning(f"**Pour Perrine 👑 :**\n\n{prop['pourquoi_perrine']}")

with onglet_historique:
    st.write("### 📜 Vos anciens compromis")
    # On appelle la fonction de ton db_manager
    historique = db.recuperer_historique_compromis()
    if historique:
        st.table(historique)
    else:
        st.info("Aucun compromis dans l'historique pour le moment. Lisez l'avenir d'abord ! 🔮")