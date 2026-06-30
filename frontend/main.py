import sys
# On dit explicitement à Python de regarder aussi dans le dossier parent
sys.path.append(".")

import streamlit as st
import backend.agents.cDecider as decider

if "q_confirm" not in st.session_state:
    st.session_state.q_confirm = False
if "p_confirm" not in st.session_state:
    st.session_state.p_confirm = False


col1,col2,col3 = st.columns(3,vertical_alignment="top")

with col2:

    st.write("Vous avez choisi :")
    option = st.selectbox(
        "Quelle activité voulez vous faire",
        ("Cinema", "Série", "Restau", "Activité",)
    )

with col1:
    st.write("Choix de Quentin :")
    quentin_envie = st.text_input("Votre envie", key="quentin_envie")
    if st.button("Confirmer",key="q_confirmer"):
        st.session_state.q_confirm = True  # On stocke en mémoire de session
        st.success("Quentin a confirmé !")

with col3:
    st.write("Choix de Perrine :")
    perrine_envie = st.text_input("Votre envie",key="perrine_envie")
    if st.button("Confirmer",key="p_confirmer"):
        st.session_state.p_confirm = True  # On stocke en mémoire de session
        st.success("Perrine a confirmé !")





if st.session_state.p_confirm and st.session_state.q_confirm:
    # Animation de chargement
    with st.spinner("🔮 Nova épluche vos critères et prépare l'arbitrage..."):
        # On récupère le dictionnaire Python généré par ton agent
        resultat = decider.ask_cDecider_compromis(quentin_envie, perrine_envie, option)

    st.success("### 🎉 Vos réponses ont été envoyées avec succès !")
    st.divider()  # Ligne de séparation

    st.markdown(f"## 🏆 Le choix de Nova : **{resultat['titre_proposition']}**")

    # Une métrique visuelle de la note
    st.metric(label="📊 Indice d'équité du couple", value=f"{resultat['note_compromis']} / 10")

    # 5. Deux colonnes de couleur pour afficher les arguments personnalisés
    arg_col1, arg_col2 = st.columns(2)
    with arg_col1:
        st.info(f"**Pour Quentin 🕶️ :**\n\n{resultat['pourquoi_quentin']}")
    with arg_col2:
        st.warning(f"**Pour Perrine 👑 :**\n\n{resultat['pourquoi_perrine']}")

    # Remise à zéro des états
    st.session_state.q_confirm = False
    st.session_state.p_confirm = False
