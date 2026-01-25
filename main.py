import streamlit as st
import random
import time

# ---------------- CONFIG ---------------- #
st.set_page_config(page_title="Imposter", page_icon="🕵️", layout="centered")

# ---------------- DATA ---------------- #

CATEGORIES = {
    "Easy": [
        # --- ORIGINAL & PREVIOUS (30) ---
        {"en": "Cat", "ru": "Кот"}, {"en": "Lion", "ru": "Лев"},
        {"en": "Pizza", "ru": "Пицца"}, {"en": "Apple", "ru": "Яблоко"},
        {"en": "School", "ru": "Школа"}, {"en": "Beach", "ru": "Пляж"},
        {"en": "Doctor", "ru": "Врач"}, {"en": "Teacher", "ru": "Учитель"},
        {"en": "Bed", "ru": "Кровать"}, {"en": "Door", "ru": "Дверь"},
        {"en": "Dog", "ru": "Собака"}, {"en": "Fish", "ru": "Рыба"},
        {"en": "Car", "ru": "Машина"}, {"en": "Bus", "ru": "Автобус"},
        {"en": "Sun", "ru": "Солнце"}, {"en": "Moon", "ru": "Луна"},
        {"en": "Book", "ru": "Книга"}, {"en": "Phone", "ru": "Телефон"},
        {"en": "Water", "ru": "Вода"}, {"en": "Milk", "ru": "Молоко"},
        {"en": "Chair", "ru": "Стул"}, {"en": "Table", "ru": "Стол"},
        {"en": "House", "ru": "Дом"}, {"en": "Park", "ru": "Парк"},
        {"en": "Ball", "ru": "Мяч"}, {"en": "Tree", "ru": "Дерево"},
        {"en": "Flower", "ru": "Цветок"}, {"en": "Shoe", "ru": "Ботинок"},
        {"en": "Hat", "ru": "Шляпа"}, {"en": "Bird", "ru": "Птица"},

        # --- NEW ADDITIONS (60) ---
        {"en": "Cow", "ru": "Корова"}, {"en": "Pig", "ru": "Свинья"},
        {"en": "Horse", "ru": "Лошадь"}, {"en": "Bear", "ru": "Медведь"},
        {"en": "Mouse", "ru": "Мышь"}, {"en": "Duck", "ru": "Утка"},
        {"en": "Chicken", "ru": "Курица"}, {"en": "Rabbit", "ru": "Кролик"},
        {"en": "Banana", "ru": "Банан"}, {"en": "Bread", "ru": "Хлеб"},
        {"en": "Cake", "ru": "Торт"}, {"en": "Egg", "ru": "Яйцо"},
        {"en": "Juice", "ru": "Сок"}, {"en": "Tea", "ru": "Чай"},
        {"en": "Coffee", "ru": "Кофе"}, {"en": "Ice Cream", "ru": "Мороженое"},
        {"en": "Tomato", "ru": "Помидор"}, {"en": "Potato", "ru": "Картошка"},
        {"en": "Orange", "ru": "Апельсин"}, {"en": "Lemon", "ru": "Лимон"},
        {"en": "TV", "ru": "Телевизор"}, {"en": "Lamp", "ru": "Лампа"},
        {"en": "Sofa", "ru": "Диван"}, {"en": "Window", "ru": "Окно"},
        {"en": "Key", "ru": "Ключ"}, {"en": "Pen", "ru": "Ручка"},
        {"en": "Cup", "ru": "Чашка"}, {"en": "Plate", "ru": "Тарелка"},
        {"en": "Knife", "ru": "Нож"}, {"en": "Spoon", "ru": "Ложка"},
        {"en": "Fork", "ru": "Вилка"}, {"en": "Bag", "ru": "Сумка"},
        {"en": "Shirt", "ru": "Рубашка"}, {"en": "Pants", "ru": "Штаны"},
        {"en": "Dress", "ru": "Платье"}, {"en": "Coat", "ru": "Пальто"},
        {"en": "Rain", "ru": "Дождь"}, {"en": "Snow", "ru": "Снег"},
        {"en": "Cloud", "ru": "Облако"}, {"en": "Sky", "ru": "Небо"},
        {"en": "Star", "ru": "Звезда"}, {"en": "River", "ru": "Река"},
        {"en": "Sea", "ru": "Море"}, {"en": "Mountain", "ru": "Гора"},
        {"en": "Baby", "ru": "Младенец"}, {"en": "Boy", "ru": "Мальчик"},
        {"en": "Girl", "ru": "Девочка"}, {"en": "King", "ru": "Король"},
        {"en": "Queen", "ru": "Королева"}, {"en": "Hand", "ru": "Рука"},
        {"en": "Foot", "ru": "Нога"}, {"en": "Eye", "ru": "Глаз"},
        {"en": "Ear", "ru": "Ухо"}, {"en": "Nose", "ru": "Нос"},
        {"en": "Mouth", "ru": "Рот"}, {"en": "Boat", "ru": "Лодка"},
        {"en": "Plane", "ru": "Самолет"}, {"en": "Bike", "ru": "Велик"},
        {"en": "Computer", "ru": "Компьютер"}, {"en": "Radio", "ru": "Радио"}
    ],

    "Medium": [
        # --- ORIGINAL & PREVIOUS (30) ---
        {"en": "Penguin", "ru": "Пингвин"}, {"en": "Shark", "ru": "Акула"},
        {"en": "Sushi", "ru": "Суши"}, {"en": "Chocolate", "ru": "Шоколад"},
        {"en": "Airport", "ru": "Аэропорт"}, {"en": "Library", "ru": "Библиотека"},
        {"en": "Firefighter", "ru": "Пожарный"}, {"en": "Scientist", "ru": "Ученый"},
        {"en": "Fridge", "ru": "Холодильник"}, {"en": "Mirror", "ru": "Зеркало"},
        {"en": "Tiger", "ru": "Тигр"}, {"en": "Elephant", "ru": "Слон"},
        {"en": "Laptop", "ru": "Ноутбук"}, {"en": "Camera", "ru": "Камера"},
        {"en": "Cinema", "ru": "Кинотеатр"}, {"en": "Hospital", "ru": "Больница"},
        {"en": "Pilot", "ru": "Пилот"}, {"en": "Artist", "ru": "Художник"},
        {"en": "Guitar", "ru": "Гитара"}, {"en": "Piano", "ru": "Пианино"},
        {"en": "Burger", "ru": "Бургер"}, {"en": "Salad", "ru": "Салат"},
        {"en": "Train", "ru": "Поезд"}, {"en": "Bicycle", "ru": "Велосипед"},
        {"en": "Umbrella", "ru": "Зонт"}, {"en": "Clock", "ru": "Часы"},
        {"en": "Museum", "ru": "Музей"}, {"en": "Hotel", "ru": "Отель"},
        {"en": "Chef", "ru": "Повар"}, {"en": "Police Officer", "ru": "Полицейский"},

        # --- NEW ADDITIONS (60) ---
        {"en": "Dolphin", "ru": "Дельфин"}, {"en": "Whale", "ru": "Кит"},
        {"en": "Zebra", "ru": "Зебра"}, {"en": "Giraffe", "ru": "Жираф"},
        {"en": "Monkey", "ru": "Обезьяна"}, {"en": "Camel", "ru": "Верблюд"},
        {"en": "Eagle", "ru": "Орел"}, {"en": "Owl", "ru": "Сова"},
        {"en": "Fox", "ru": "Лиса"}, {"en": "Wolf", "ru": "Волк"},
        {"en": "Frog", "ru": "Лягушка"}, {"en": "Turtle", "ru": "Черепаха"},
        {"en": "Spider", "ru": "Паук"}, {"en": "Bee", "ru": "Пчела"},
        {"en": "Butterfly", "ru": "Бабочка"}, {"en": "Spaghetti", "ru": "Спагетти"},
        {"en": "Steak", "ru": "Стейк"}, {"en": "Soup", "ru": "Суп"},
        {"en": "Sandwich", "ru": "Сэндвич"}, {"en": "Cookie", "ru": "Печенье"},
        {"en": "Donut", "ru": "Пончик"}, {"en": "Popcorn", "ru": "Попкорн"},
        {"en": "Lemonade", "ru": "Лимонад"}, {"en": "Wine", "ru": "Вино"},
        {"en": "Beer", "ru": "Пиво"}, {"en": "Cheese", "ru": "Сыр"},
        {"en": "Stadium", "ru": "Стадион"}, {"en": "Gym", "ru": "Спортзал"},
        {"en": "Restaurant", "ru": "Ресторан"}, {"en": "Cafe", "ru": "Кафе"},
        {"en": "Bakery", "ru": "Пекарня"}, {"en": "Pharmacy", "ru": "Аптека"},
        {"en": "Bank", "ru": "Банк"}, {"en": "Post Office", "ru": "Почта"},
        {"en": "Zoo", "ru": "Зоопарк"}, {"en": "Circus", "ru": "Цирк"},
        {"en": "Farm", "ru": "Ферма"}, {"en": "Tablet", "ru": "Планшет"},
        {"en": "Headphones", "ru": "Наушники"}, {"en": "Speaker", "ru": "Колонка"},
        {"en": "Battery", "ru": "Батарейка"}, {"en": "Wallet", "ru": "Кошелек"},
        {"en": "Suitcase", "ru": "Чемодан"}, {"en": "Glasses", "ru": "Очки"},
        {"en": "Ring", "ru": "Кольцо"}, {"en": "Watch", "ru": "Наручные часы"},
        {"en": "Necklace", "ru": "Ожерелье"}, {"en": "Nurse", "ru": "Медсестра"},
        {"en": "Dentist", "ru": "Стоматолог"}, {"en": "Driver", "ru": "Водитель"},
        {"en": "Farmer", "ru": "Фермер"}, {"en": "Soldier", "ru": "Солдат"},
        {"en": "Singer", "ru": "Певец"}, {"en": "Dancer", "ru": "Танцор"},
        {"en": "Actor", "ru": "Актер"}, {"en": "Writer", "ru": "Писатель"},
        {"en": "Helicopter", "ru": "Вертолет"}, {"en": "Truck", "ru": "Грузовик"},
        {"en": "Taxi", "ru": "Такси"}, {"en": "Violin", "ru": "Скрипка"}
    ],

    "Hard": [
        # --- ORIGINAL & PREVIOUS (30) ---
        {"en": "Platypus", "ru": "Утконос"}, {"en": "Jellyfish", "ru": "Медуза"},
        {"en": "Croissant", "ru": "Круассан"}, {"en": "Caviar", "ru": "Икра"},
        {"en": "Embassy", "ru": "Посольство"}, {"en": "Observatory", "ru": "Обсерватория"},
        {"en": "Archaeologist", "ru": "Археолог"}, {"en": "Architect", "ru": "Архитектор"},
        {"en": "Telescope", "ru": "Телескоп"}, {"en": "Compass", "ru": "Компас"},
        {"en": "Chameleon", "ru": "Хамелеон"}, {"en": "Peacock", "ru": "Павлин"},
        {"en": "Submarine", "ru": "Подводная лодка"}, {"en": "Satellite", "ru": "Спутник"},
        {"en": "Lighthouse", "ru": "Маяк"}, {"en": "Skyscraper", "ru": "Небоскреб"},
        {"en": "Astronaut", "ru": "Астронавт"}, {"en": "Spy", "ru": "Шпион"},
        {"en": "Microscope", "ru": "Микроскоп"}, {"en": "Thermometer", "ru": "Термометр"},
        {"en": "Saxophone", "ru": "Саксофон"}, {"en": "Harp", "ru": "Арфа"},
        {"en": "Truffle", "ru": "Трюфель"}, {"en": "Lasagna", "ru": "Лазанья"},
        {"en": "Casino", "ru": "Казино"}, {"en": "Courtroom", "ru": "Суд"},
        {"en": "Judge", "ru": "Судья"}, {"en": "Magician", "ru": "Фокусник"},
        {"en": "Cactus", "ru": "Кактус"}, {"en": "Pyramid", "ru": "Пирамида"},

        # --- NEW ADDITIONS (60) ---
        {"en": "Ostrich", "ru": "Страус"}, {"en": "Flamingo", "ru": "Фламинго"},
        {"en": "Panda", "ru": "Панда"}, {"en": "Koala", "ru": "Коала"},
        {"en": "Kangaroo", "ru": "Кенгуру"}, {"en": "Rhino", "ru": "Носорог"},
        {"en": "Hippo", "ru": "Бегемот"}, {"en": "Crocodile", "ru": "Крокодил"},
        {"en": "Lizard", "ru": "Ящерица"}, {"en": "Bat", "ru": "Летучая мышь"},
        {"en": "Lobster", "ru": "Лобстер"}, {"en": "Octopus", "ru": "Осьминог"},
        {"en": "Mosquito", "ru": "Комар"}, {"en": "Hedgehog", "ru": "Еж"},
        {"en": "Oyster", "ru": "Устрица"}, {"en": "Champagne", "ru": "Шампанское"},
        {"en": "Tiramisu", "ru": "Тирамису"}, {"en": "Fondue", "ru": "Фондю"},
        {"en": "Kebab", "ru": "Кебаб"}, {"en": "Avocado", "ru": "Авокадо"},
        {"en": "Cinnamon", "ru": "Корица"}, {"en": "Ginger", "ru": "Имбирь"},
        {"en": "Drone", "ru": "Дрон"}, {"en": "Robot", "ru": "Робот"},
        {"en": "Rocket", "ru": "Ракета"}, {"en": "Spaceship", "ru": "Космический корабль"},
        {"en": "Ghost", "ru": "Призрак"}, {"en": "Vampire", "ru": "Вампир"},
        {"en": "Zombie", "ru": "Зомби"}, {"en": "Mummy", "ru": "Мумия"},
        {"en": "Skeleton", "ru": "Скелет"}, {"en": "Alien", "ru": "Пришелец"},
        {"en": "Dragon", "ru": "Дракон"}, {"en": "Unicorn", "ru": "Единорог"},
        {"en": "Castle", "ru": "Замок"}, {"en": "Palace", "ru": "Дворец"},
        {"en": "Temple", "ru": "Храм"}, {"en": "Mosque", "ru": "Мечеть"},
        {"en": "Church", "ru": "Церковь"}, {"en": "Factory", "ru": "Завод"},
        {"en": "Prison", "ru": "Тюрьма"}, {"en": "Cemetery", "ru": "Кладбище"},
        {"en": "Island", "ru": "Остров"}, {"en": "Volcano", "ru": "Вулкан"},
        {"en": "Desert", "ru": "Пустыня"}, {"en": "Jungle", "ru": "Джунгли"},
        {"en": "Cave", "ru": "Пещера"}, {"en": "Waterfall", "ru": "Водопад"},
        {"en": "President", "ru": "Президент"}, {"en": "Detective", "ru": "Детектив"},
        {"en": "Lawyer", "ru": "Адвокат"}, {"en": "Engineer", "ru": "Инженер"},
        {"en": "Mechanic", "ru": "Механик"}, {"en": "Plumber", "ru": "Сантехник"},
        {"en": "Photographer", "ru": "Фотограф"}, {"en": "Director", "ru": "Режиссер"},
        {"en": "Stethoscope", "ru": "Стетоскоп"}, {"en": "Magnet", "ru": "Магнит"},
        {"en": "Laser", "ru": "Лазер"}, {"en": "Virus", "ru": "Вирус"}
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
    for i in range(3, 23):
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

    if st.button(f"I am {p['name']}"):
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
