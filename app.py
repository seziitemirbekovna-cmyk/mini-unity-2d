import streamlit as st

st.set_page_config(
    page_title="Mini Unity 2D",
    page_icon="🎮",
    layout="wide"
)

st.title("🎮 Mini Unity 2D")

st.subheader("Прототип мультиплатформенного 2D игрового движка")

st.write("""
Данный проект представляет собой учебный прототип
2D игрового движка, разработанный на языке Python
с использованием библиотеки Pygame.
""")

st.header("Основные возможности")

st.markdown("""
✅ Editor Mode  
✅ Game Mode  
✅ Боевая система  
✅ AI врагов  
✅ Система уровней  
✅ Инвентарь  
✅ UI интерфейс  
""")

st.header("Скриншоты проекта")

st.image(
    "screenshots/gameplay.png",
    caption="Игровой процесс",
    use_container_width=True
)

st.header("Используемые технологии")

st.code("""
Python
Pygame
Streamlit
OOP
""")

st.header("Архитектура")

st.write("""
Проект построен на модульной архитектуре.
Основные модули:
- Player
- Enemy
- LevelManager
- UIManager
- GameObject
""")

st.header("Игровой цикл")

st.code("""
while running:
    handle_events()
    update()
    draw()
""", language="python")

st.success("Проект разработан в рамках выпускной квалификационной работы.")
