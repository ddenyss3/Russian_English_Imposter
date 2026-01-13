import streamlit as st
import random
import time

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Imposter", page_icon="🕵️", layout="centered")

# ---------------- DATA ---------------- #

CATEGORIES = {
    "Easy": [
        {"en": "Cat", "ru": "Кот"}, {"en": "Lion", "ru": "Лев"},
        {"en": "Pizza", "ru": "Пицца"}, {"en": "Apple", "ru": "Яблоко"},
        {"en": "School", "ru": "Школа"}, {"en": "Beach", "ru": "Пляж"},
        {"en": "Doctor", "ru": "Врач"}, {"en": "Teacher", "ru": "Учитель"},
        {"en": "Bed", "ru": "Кровать"}, {"en": "Door", "ru": "Дверь"}
    ],
    "Medium": [
        {"en": "Penguin", "ru": "Пингвин"}, {"en": "Shark", "ru": "Акула"},
        {"en": "Sushi", "ru": "Суши"}, {"en": "Chocolate", "ru": "Шоколад"},
        {"en": "Airport", "ru": "Аэропорт"}, {"en": "Library", "ru": "Библиотека"},
        {"en": "Firefighter", "ru": "Пожарный"}, {"en": "Scientist", "ru": "Ученый"},
        {"en": "Fridge", "ru": "Холодильник"}, {"en": "Mirror", "ru": "Зеркало"}
    ],
    "Hard": [
        {"en": "Platypus", "ru": "Утконос"}, {"en": "Jellyfish", "ru": "Медуза"},
        {"en": "Croissant", "ru": "Круассан"}, {"en": "Caviar", "ru": "Икра"},
        {"en": "Embassy", "ru": "Посольство"}, {"en": "Observatory", "ru": "Обсерватория"},
        {"en": "Archaeologist", "ru": "Археолог"}, {"en": "Architect", "ru": "Архитектор"},
        {"en": "Telescope", "ru": "Телескоп"}, {"en": "Compass", "ru": "Компас"}
    ]
}

IMPOSTER_WORD = {"en": "YOU ARE THE IMPOSTER", "ru": "ВЫ САМОЗВАНЕЦ"}

# ---------------- STATE ---------------- #

if "screen" not in st.session_state:
    st.session_state.screen = "setup"
    st.session_state.players = []
    st.session_state.current_player = 0
    st.session_state.votes = set()

# ---------------- HELPERS ---------------- #

def reset_game():
    for k in list(st.session_state.keys()):
        del st.session_state[k]
    st.rerun()

# ---------------- SETUP ---------------- #

if st.session_state.screen == "setup":
    st.title("🕵️ Imposter")

    category = st.selectbox("Difficulty", list(CATEGORIES.keys()))
    imposter_count = st.selectbox("Number of Imposters", [1, 2, 3])

    st.subheader("Players")
    names = []
    for i in range(3, 20):
        name = st.text_input(f"Player {i-2}", key=f"name_{i}")
        if name:
            names.append(name.strip())

    if st.button("Start Game"):
        if len(names) < 3:
            st.error("Need at least 3 players")
        elif imposter_count >= len(names):
            st.error("Too many imposters")
        else:
            secret_word = random.choice(CATEGORIES[category])
            players = [{"name": n, "role": "citizen", "word": secret_word} for n in names]

            for p in random.sample(players, imposter_count):
                p["role"] = "imposter"
                p["word"] = IMPOSTER_WORD

            st.session_state.players = players
            st.session_state.category = category
            st.session_state.current_player = 0
            st.session_state.screen = "pass"
            st.rerun()

# ---------------- PASS ---------------- #

elif st.session_state.screen == "pass":
    p = st.session_state.players[st.session_state.current_player]
    st.header("Pass to")
    st.markdown(f"## **{p['name']}**")
    st.warning("Make sure nobody else is looking")

    # initialize flag once
    if "pass_confirmed" not in st.session_state:
        st.session_state.pass_confirmed = False

    # only show button if not yet clicked
    if not st.session_state.pass_confirmed:
        if st.button(f"I am {p['name']}"):
            st.session_state.pass_confirmed = True
            st.session_state.screen = "reveal"
            st.rerun()

# ---------------- REVEAL ---------------- #

elif st.session_state.screen == "reveal":
    p = st.session_state.players[st.session_state.current_player]

    if p["role"] == "imposter":
        st.error(p["word"]["en"])
        st.markdown(f"### {p['word']['ru']}")
        st.caption("Blend in!")
    else:
        st.success(p["word"]["en"])
        st.markdown(f"### {p['word']['ru']}")
        st.caption(f"Category: {st.session_state.category}")

    time.sleep(3)

    st.session_state.current_player += 1
    if st.session_state.current_player < len(st.session_state.players):
        st.session_state.screen = "pass"
    else:
        st.session_state.timer_start = time.time()
        st.session_state.screen = "timer"

    st.rerun()

# ---------------- TIMER ---------------- #

elif st.session_state.screen == "timer":
    st.header("🕒 Discussion Time")

    elapsed = int(time.time() - st.session_state.timer_start)
    remaining = max(0, 180 - elapsed)

    mins, secs = divmod(remaining, 60)
    st.metric("Time Left", f"{mins}:{secs:02}")

    if remaining <= 0 or st.button("Vote Now"):
        st.session_state.screen = "vote"
        st.rerun()

    time.sleep(1)
    st.rerun()

# ---------------- VOTING ---------------- #

elif st.session_state.screen == "vote":
    st.header("🗳️ Who is the Imposter?")

    for p in st.session_state.players:
        if st.checkbox(p["name"], key=f"vote_{p['name']}"):
            st.session_state.votes.add(p["name"])
        else:
            st.session_state.votes.discard(p["name"])

    if st.button("Reveal Truth"):
        st.session_state.screen = "results"
        st.rerun()

# ---------------- RESULTS ---------------- #

elif st.session_state.screen == "results":
    st.title("📊 Results")

    word = st.session_state.players[0]["word"]
    st.info(f"Secret Word: {word['en']} / {word['ru']}")

    for p in st.session_state.players:
        label = "IMPOSTER" if p["role"] == "imposter" else "CITIZEN"
        voted = "❌ VOTED OUT" if p["name"] in st.session_state.votes else ""
        st.write(f"**{p['name']}** → {label} {voted}")

    if st.button("Play Again"):
        reset_game()
