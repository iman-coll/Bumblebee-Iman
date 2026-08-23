import streamlit as st

st.set_page_config(page_title="Iman's Pakistan Bumblebee Quiz", page_icon="🐝", layout="centered")

st.markdown("""
<style>
.stApp { background: radial-gradient(circle at top, #1b2735 0%, #090a0f 70%); color: white; }
.quiz { background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.18); border-radius: 16px; padding: 24px; }
.title { text-align:center; color:#ffd700; font-size:2rem; font-weight:800; }
.question { color:#ffd700; font-size:1.15rem; font-weight:700; }
</style>
""", unsafe_allow_html=True)

QUIZ = [
    {"q":"Who was the first Governor-General of Pakistan?","o":["Quaid-e-Azam","Liaquat Ali Khan","Khawaja Nazimuddin","Iskander Mirza"],"a":"Quaid-e-Azam"},
    {"q":"When was the Objectives Resolution passed?","o":["1949","1950","1956","1962"],"a":"1949"},
    {"q":"The Simla Deputation of 1906 was led by:","o":["Aga Khan III","Allama Iqbal","Sir Syed Ahmed Khan","Liaquat Ali Khan"],"a":"Aga Khan III"},
    {"q":"In which year did Pakistan join the United Nations?","o":["1947","1948","1950","1955"],"a":"1947"},
    {"q":"The Tashkent Declaration was signed in:","o":["1965","1966","1971","1972"],"a":"1966"},
    {"q":"The Lahore Resolution was passed in:","o":["1940","1941","1942","1943"],"a":"1940"},
    {"q":"Who was the last Governor-General of Pakistan?","o":["Iskander Mirza","Ghulam Muhammad","Khawaja Nazimuddin","Ayub Khan"],"a":"Iskander Mirza"},
    {"q":"The first census in Pakistan was held in:","o":["1951","1952","1953","1954"],"a":"1951"},
    {"q":"Pakistan conducted its nuclear tests in:","o":["May 1998","June 1998","July 1998","August 1998"],"a":"May 1998"},
    {"q":"The 18th Amendment to the Constitution was passed in:","o":["2010","2011","2012","2013"],"a":"2010"},
]

if "question" not in st.session_state: st.session_state.question = 0
if "score" not in st.session_state: st.session_state.score = 0
if "answered" not in st.session_state: st.session_state.answered = False
if "finished" not in st.session_state: st.session_state.finished = False

st.markdown('<div class="title">🐝 Pakistan History Bumblebee Quiz</div>', unsafe_allow_html=True)
st.write("")

if not st.session_state.finished:
    i = st.session_state.question
    item = QUIZ[i]
    st.progress((i + 1) / len(QUIZ), text=f"Question {i + 1} of {len(QUIZ)}")
    st.markdown(f'<div class="quiz"><div class="question">{item["q"]}</div></div>', unsafe_allow_html=True)
    st.write("")

    if not st.session_state.answered:
        for option in item["o"]:
            if st.button(option, key=f"q{i}_{option}", use_container_width=True):
                st.session_state.answered = True
                st.session_state.correct = option == item["a"]
                if st.session_state.correct:
                    st.session_state.score += 1
                st.rerun()
    else:
        if st.session_state.correct:
            st.success("Correct! 🎉")
        else:
            st.error(f"Incorrect. Correct answer: {item['a']}")
        if i < len(QUIZ) - 1:
            if st.button("Next Question ➜", type="primary", use_container_width=True):
                st.session_state.question += 1
                st.session_state.answered = False
                st.rerun()
        else:
            if st.button("See Final Score 🏆", type="primary", use_container_width=True):
                st.session_state.finished = True
                st.rerun()
else:
    st.markdown('<div class="quiz">', unsafe_allow_html=True)
    st.header("Quiz Completed! 🎉")
    percentage = st.session_state.score / len(QUIZ) * 100
    st.metric("Your Score", f"{st.session_state.score} / {len(QUIZ)}")
    if percentage >= 80:
        st.success("Excellent! You are a history expert! 🌟")
    elif percentage >= 50:
        st.info("Good job! Keep learning! 📚")
    else:
        st.warning("Keep practicing! History is vast! 💪")
    if st.button("Restart Quiz", use_container_width=True):
        st.session_state.question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.finished = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
