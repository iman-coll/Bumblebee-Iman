import streamlit as st
import random

# Page Configuration
st.set_page_config(
    page_title="Iman's Pakistan Bumblebee App",
    page_icon="🐝",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Space Theme and Animated Laundromat
def inject_custom_css():
    st.markdown("""
    <style>
    /* Global Space Theme */
    .stApp {
        background: radial-gradient(ellipse at bottom, #1b2735 0%, #090a0f 100%);
        color: #ffffff;
    }
    
    /* Hide default Streamlit footer and header for immersion */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Quiz Container Styling */
    .quiz-container {
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        max-width: 800px;
        margin: 0 auto;
        z-index: 10;
        position: relative;
    }
    
    .question-text {
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        color: #ffd700; /* Gold for visibility */
    }
    
    .option-button {
        display: block;
        width: 100%;
        padding: 10px;
        margin: 5px 0;
        background-color: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 8px;
        color: white;
        text-align: left;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .option-button:hover {
        background-color: rgba(255, 215, 0, 0.3);
        border-color: #ffd700;
    }
    
    /* Animated Laundromat Container */
    .laundromat-container {
        position: fixed;
        top: 20%;
        left: -200px; /* Start off-screen */
        width: 150px;
        height: 150px;
        z-index: 1;
        animation: flyAcross 20s linear infinite;
        pointer-events: none; /* Allow clicking through */
    }
    
    /* The Laundromat Image/Shape */
    .laundromat-img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        /* Using a placeholder that looks somewhat mechanical/boxy for the laundromat */
        background: url('https://picsum.photos/seed/laundromat/200/200') no-repeat center center;
        background-size: contain;
        filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.5));
        border-radius: 10px;
    }
    
    /* Flipbook-like vibration effect */
    .flipbook-effect {
        animation: vibrate 0.5s infinite;
    }
    
    @keyframes flyAcross {
        0% { left: -200px; top: 20%; transform: rotate(0deg); }
        25% { top: 30%; transform: rotate(5deg); }
        50% { top: 15%; transform: rotate(-5deg); }
        75% { top: 25%; transform: rotate(5deg); }
        100% { left: 110vw; top: 20%; transform: rotate(0deg); }
    }
    
    @keyframes vibrate {
        0% { transform: translate(0, 0); }
        25% { transform: translate(1px, 1px); }
        50% { transform: translate(-1px, -1px); }
        75% { transform: translate(1px, -1px); }
        100% { transform: translate(0, 0); }
    }
    
    /* Stars Background Effect */
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, #eee, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 40px 70px, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 50px 160px, #ddd, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 90px 40px, #fff, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 130px 80px, #fff, rgba(0,0,0,0));
        background-repeat: repeat;
        background-size: 200px 200px;
        opacity: 0.5;
        z-index: 0;
    }
    </style>
    """, unsafe_allow_html=True)

inject_custom_css()

# Add the animated laundromat element
st.markdown("""
<div class="stars"></div>
<div class="laundromat-container">
    <div class="laundromat-img flipbook-effect"></div>
</div>
""", unsafe_allow_html=True)

# Quiz Data: Difficult MCQs on Pakistan's History
quiz_data = [
    {"q": "Who was the first Governor-General of Pakistan?", "options": ["Quaid-e-Azam", "Liaquat Ali Khan", "Khawaja Nazimuddin", "Iskander Mirza"], "answer": "Quaid-e-Azam"},
    {"q": "When was the Objectives Resolution passed?", "options": ["1949", "1950", "1956", "1962"], "answer": "1949"},
    {"q": "Which act established the Federal Court in India?", "options": ["Govt of India Act 1935", "Indian Independence Act 1947", "Regulating Act 1773", "Charter Act 1853"], "answer": "Govt of India Act 1935"},
    {"q": "Who was the Prime Minister of Pakistan when the first constitution was enacted?", "options": ["Chaudhry Muhammad Ali", "Huseyn Shaheed Suhrawardy", "Ibrahim Ismail Chundrigar", "Feroz Khan Noon"], "answer": "Chaudhry Muhammad Ali"},
    {"q": "The Simla Deputation of 1906 was led by:", "options": ["Aga Khan III", "Allama Iqbal", "Sir Syed Ahmed Khan", "Liaquat Ali Khan"], "answer": "Aga Khan III"},
    {"q": "In which year did Pakistan join the United Nations?", "options": ["1947", "1948", "1950", "1955"], "answer": "1947"},
    {"q": "Who was the Commander-in-Chief of the Pakistan Army during the 1965 War?", "options": ["Ayub Khan", "Yahya Khan", "Musa Khan", "Tikka Khan"], "answer": "Musa Khan"},
    {"q": "The Tashkent Declaration was signed in:", "options": ["1965", "1966", "1971", "1972"], "answer": "1966"},
    {"q": "Who was the President of Pakistan during the 1971 War?", "options": ["Zulfikar Ali Bhutto", "Yahya Khan", "Ayub Khan", "Fazal Ilahi Chaudhry"], "answer": "Yahya Khan"},
    {"q": "The Constitution of 1973 was enforced on:", "options": ["14 August 1973", "23 March 1973", "10 April 1973", "1 January 1974"], "answer": "14 August 1973"},
    {"q": "Who was the first Chief Martial Law Administrator of Pakistan?", "options": ["Ayub Khan", "Yahya Khan", "Zia-ul-Haq", "Pervez Musharraf"], "answer": "Ayub Khan"},
    {"q": "The One Unit scheme was introduced in:", "options": ["1955", "1956", "1958", "1962"], "answer": "1955"},
    {"q": "Who was the Viceroy of India at the time of Partition?", "options": ["Lord Mountbatten", "Lord Wavell", "Lord Curzon", "Lord Linlithgow"], "answer": "Lord Mountbatten"},
    {"q": "The Radcliffe Award was announced on:", "options": ["14 August 1947", "15 August 1947", "12 August 1947", "17 August 1947"], "answer": "17 August 1947"},
    {"q": "Who was the first Speaker of the National Assembly of Pakistan?", "options": ["Maulvi Tamizuddin", "Jogendra Nath Mandal", "Abdul Wahab Khan", "Fazal Elahi Chaudhry"], "answer": "Maulvi Tamizuddin"},
    {"q": "The Basic Principles Committee submitted its first report in:", "options": ["1950", "1952", "1954", "1956"], "answer": "1950"},
    {"q": "Who was the Prime Minister of Pakistan during the imposition of the first Martial Law?", "options": ["Feroz Khan Noon", "Huseyn Shaheed Suhrawardy", "Ibrahim Ismail Chundrigar", "Malik Feroz Khan Noon"], "answer": "Feroz Khan Noon"},
    {"q": "The Ayub Khan era is known for:", "options": ["Decade of Development", "Islamic Socialism", "Nationalization", "Democratization"], "answer": "Decade of Development"},
    {"q": "Who was the Foreign Minister of Pakistan during the 1965 War?", "options": ["Zulfikar Ali Bhutto", "Aziz Ahmed", "Sultan Muhammad Khan", "Hamid Jalal"], "answer": "Zulfikar Ali Bhutto"},
    {"q": "The Lahore Resolution was passed in:", "options": ["1940", "1941", "1942", "1943"], "answer": "1940"},
    {"q": "Who was the last Governor-General of Pakistan?", "options": ["Iskander Mirza", "Ghulam Muhammad", "Khawaja Nazimuddin", "Ayub Khan"], "answer": "Iskander Mirza"},
    {"q": "The first census in Pakistan was held in:", "options": ["1951", "1952", "1953", "1954"], "answer": "1951"},
    {"q": "Who was the Chief Justice of Pakistan who administered oath to Quaid-e-Azam?", "options": ["Sir Abdul Rashid", "Mian Abdul Rashid", "Justice Munir", "Justice Cornelius"], "answer": "Sir Abdul Rashid"},
    {"q": "The Indus Basin Treaty was signed with:", "options": ["India", "Afghanistan", "China", "Iran"], "answer": "India"},
    {"q": "Who was the President of Pakistan when the 1962 Constitution was adopted?", "options": ["Ayub Khan", "Iskander Mirza", "Yahya Khan", "Zulfikar Ali Bhutto"], "answer": "Ayub Khan"},
    {"q": "The Green Revolution in Pakistan was associated with:", "options": ["Ayub Khan", "Zulfikar Ali Bhutto", "Zia-ul-Haq", "Nawaz Sharif"], "answer": "Ayub Khan"},
    {"q": "Who was the first woman Minister in Pakistan?", "options": ["Fatima Jinnah", "Ra'ana Liaquat Ali Khan", "Begum Shaista Ikramullah", "Hina Rabbani Khar"], "answer": "Ra'ana Liaquat Ali Khan"},
    {"q": "The National Awami Party (NAP) was banned in:", "options": ["1954", "1958", "1962", "1975"], "answer": "1954"},
    {"q": "Who was the Prime Minister of Pakistan during the separation of East Pakistan?", "options": ["Zulfikar Ali Bhutto", "Nurul Amin", "Yahya Khan", "Tikka Khan"], "answer": "Nurul Amin"},
    {"q": "The Simla Agreement was signed between:", "options": ["Bhutto and Indira Gandhi", "Ayub and Shastri", "Zia and Rajiv Gandhi", "Sharif and Vajpayee"], "answer": "Bhutto and Indira Gandhi"},
    {"q": "Who was the Chief of Army Staff during the 1971 War?", "options": ["Tikka Khan", "Yahya Khan", "Zia-ul-Haq", "Gul Hassan"], "answer": "Tikka Khan"},
    {"q": "The 1973 Constitution was amended for the first time in:", "options": ["1974", "1975", "1976", "1977"], "answer": "1974"},
    {"q": "Who was the President of Pakistan when Zia-ul-Haq imposed Martial Law?", "options": ["Fazal Ilahi Chaudhry", "Zulfikar Ali Bhutto", "Ghulam Ishaq Khan", "Wasim Sajjad"], "answer": "Fazal Ilahi Chaudhry"},
    {"q": "The Geneva Accords regarding Afghanistan were signed in:", "options": ["1988", "1989", "1990", "1991"], "answer": "1988"},
    {"q": "Who was the Prime Minister of Pakistan during the Soviet withdrawal from Afghanistan?", "options": ["Benazir Bhutto", "Junejo", "Zia-ul-Haq", "Nawaz Sharif"], "answer": "Junejo"},
    {"q": "The first nuclear tests by India were conducted in:", "options": ["1974", "1988", "1998", "2000"], "answer": "1974"},
    {"q": "Pakistan conducted its nuclear tests in:", "options": ["May 1998", "June 1998", "July 1998", "August 1998"], "answer": "May 1998"},
    {"q": "Who was the Prime Minister of Pakistan during the Kargil War?", "options": ["Nawaz Sharif", "Benazir Bhutto", "Pervez Musharraf", "Shaukat Aziz"], "answer": "Nawaz Sharif"},
    {"q": "The 13th Amendment to the Constitution of Pakistan was passed in:", "options": ["1997", "1998", "1999", "2000"], "answer": "1997"},
    {"q": "Who was the Chief Executive of Pakistan after the 1999 coup?", "options": ["Pervez Musharraf", "Nawaz Sharif", "Ghulam Mustafa Jatoi", "Zafarullah Jamali"], "answer": "Pervez Musharraf"},
    {"q": "The Legal Framework Order (LFO) was issued in:", "options": ["2002", "2003", "2004", "2005"], "answer": "2002"},
    {"q": "Who was the Prime Minister of Pakistan during the 2005 Earthquake?", "options": ["Shaukat Aziz", "Zafarullah Jamali", "Chaudhry Shujaat Hussain", "Yousaf Raza Gillani"], "answer": "Shaukat Aziz"},
    {"q": "The 18th Amendment to the Constitution was passed in:", "options": ["2010", "2011", "2012", "2013"], "answer": "2010"},
    {"q": "Who was the President of Pakistan when the 18th Amendment was passed?", "options": ["Asif Ali Zardari", "Pervez Musharraf", "Mamnoon Hussain", "Arif Alvi"], "answer": "Asif Ali Zardari"},
    {"q": "The CPEC agreement was signed in:", "options": ["2015", "2016", "2017", "2018"], "answer": "2015"},
    {"q": "Who was the Prime Minister of Pakistan during the signing of CPEC?", "options": ["Nawaz Sharif", "Yousaf Raza Gillani", "Raja Pervaiz Ashraf", "Shahid Khaqan Abbasi"], "answer": "Nawaz Sharif"},
    {"q": "The 21st Amendment to the Constitution established:", "options": ["Military Courts", "Accountability Courts", "Anti-Terrorism Courts", "Special Courts"], "answer": "Military Courts"},
    {"q": "Who was the Chief Justice of Pakistan during the Panama Papers case?", "options": ["Mian Saqib Nisar", "Iftikhar Muhammad Chaudhry", "Nasir-ul-Mulk", "Jawwad S. Khawaja"], "answer": "Mian Saqib Nisar"},
    {"q": "The Faizabad sit-in was led by:", "options": ["TLP", "PTI", "JUI-F", "Jamat-e-Islami"], "answer": "TLP"},
    {"q": "Who was the Prime Minister of Pakistan during the Faizabad sit-in?", "options": ["Shahid Khaqan Abbasi", "Nawaz Sharif", "Imran Khan", "Shehbaz Sharif"], "answer": "Shahid Khaqan Abbasi"},
    {"q": "The 25th Amendment to the Constitution merged:", "options": ["FATA with KPK", "Gilgit-Baltistan with Pakistan", "Islamabad with Punjab", "Kashmir with Pakistan"], "answer": "FATA with KPK"},
    {"q": "Who was the Prime Minister of Pakistan when the 25th Amendment was passed?", "options": ["Shahid Khaqan Abbasi", "Imran Khan", "Nawaz Sharif", "Yousaf Raza Gillani"], "answer": "Shahid Khaqan Abbasi"},
    {"q": "The current Constitution of Pakistan has been amended how many times (as of 2023)?", "options": ["26", "25", "24", "23"], "answer": "26"},
    {"q": "Who was the first female Speaker of the National Assembly?", "options": ["Dr. Fehmida Mirza", "Sherry Rehman", "Asma Jahangir", "Hina Rabbani Khar"], "answer": "Dr. Fehmida Mirza"},
    {"q": "The Shanghai Cooperation Organization (SCO) membership was granted to Pakistan in:", "options": ["2017", "2018", "2019", "2020"], "answer": "2017"},
    {"q": "Who was the Foreign Minister of Pakistan when it joined SCO?", "options": ["Khawaja Asif", "Sartaj Aziz", "Shah Mahmood Qureshi", "Bilawal Bhutto"], "answer": "Khawaja Asif"},
    {"q": "The National Action Plan (NAP) was launched after:", "options": ["APS Attack", "Karachi Airport Attack", "Peshawar Mosque Attack", "Quetta Police Training Center Attack"], "answer": "APS Attack"},
    {"q": "Who was the Chief Minister of Punjab during the APS Attack?", "options": ["Shehbaz Sharif", "Chaudhry Pervaiz Elahi", "Usman Buzdar", "Hamza Shehbaz"], "answer": "Shehbaz Sharif"},
    {"q": "The Ziarat Residency was destroyed in:", "options": ["2013", "2014", "2015", "2016"], "answer": "2013"},
    {"q": "Who was the Prime Minister of Pakistan during the Ziarat Residency incident?", "options": ["Nawaz Sharif", "Yousaf Raza Gillani", "Raja Pervaiz Ashraf", "Shahid Khaqan Abbasi"], "answer": "Nawaz Sharif"},
    {"q": "The China-Pakistan Economic Corridor (CPEC) is part of:", "options": ["Belt and Road Initiative", "Marshall Plan", "Colombo Plan", "SAFTA"], "answer": "Belt and Road Initiative"},
    {"q": "Who was the President of China when CPEC was launched?", "options": ["Xi Jinping", "Hu Jintao", "Jiang Zemin", "Li Keqiang"], "answer": "Xi Jinping"},
    {"q": "The Gwadar Port was handed over to China for operation in:", "options": ["2013", "2014", "2015", "2016"], "answer": "2013"},
    {"q": "Who was the Prime Minister of Pakistan when Gwadar Port was handed over?", "options": ["Raja Pervaiz Ashraf", "Nawaz Sharif", "Yousaf Raza Gillani", "Shahid Khaqan Abbasi"], "answer": "Raja Pervaiz Ashraf"},
    {"q": "The first batch of students graduated from the National University of Sciences and Technology (NUST) in:", "options": ["2000", "2005", "2010", "2015"], "answer": "2000"},
    {"q": "Who was the President of Pakistan when NUST was established?", "options": ["Pervez Musharraf", "Asif Ali Zardari", "Mamnoon Hussain", "Farooq Leghari"], "answer": "Pervez Musharraf"},
    {"q": "The Higher Education Commission (HEC) was established in:", "options": ["2002", "2003", "2004", "2005"], "answer": "2002"},
    {"q": "Who was the Chairman of HEC during its early years?", "options": ["Atta-ur-Rahman", "Mukhtar Ahmed", "Syed Sohail Naqvi", "Naveed Y. Malik"], "answer": "Atta-ur-Rahman"},
    {"q": "The Benazir Income Support Programme (BISP) was launched in:", "options": ["2008", "2009", "2010", "2011"], "answer": "2008"},
    {"q": "Who was the Prime Minister of Pakistan when BISP was launched?", "options": ["Yousaf Raza Gillani", "Benazir Bhutto", "Nawaz Sharif", "Shaukat Aziz"], "answer": "Yousaf Raza Gillani"},
]

# Initialize Session State
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False
if 'selected_option' not in st.session_state:
    st.session_state.selected_option = None
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'last_answer_correct' not in st.session_state:
    st.session_state.last_answer_correct = False

# Title
st.title("🐝 Iman's Pakistan Bumblebee App")
st.markdown("<h3 style='text-align: center; color: #ffd700;'>Test Your Knowledge of Pakistan's History</h3>", unsafe_allow_html=True)

# Quiz Logic
if not st.session_state.quiz_finished:
    q_index = st.session_state.current_question
    question = quiz_data[q_index]

    with st.container():
        st.markdown(
            f"<div class='quiz-container'><p class='question-text'>"
            f"Question {q_index + 1}/{len(quiz_data)}: {question['q']}</p></div>",
            unsafe_allow_html=True,
        )

    # Prevent multiple score increments for the same question.
    if st.session_state.show_result:
        for option in question["options"]:
            st.button(
                option,
                key=f"disabled_{q_index}_{option}",
                disabled=True,
            )
    else:
        for option in question["options"]:
            if st.button(option, key=f"opt_{q_index}_{option}", use_container_width=True):
                st.session_state.selected_option = option
                st.session_state.show_result = True
                st.session_state.last_answer_correct = (
                    option == question["answer"]
                )
                if st.session_state.last_answer_correct:
                    st.session_state.score += 1
                st.rerun()

    if st.session_state.show_result and st.session_state.selected_option:
        if st.session_state.last_answer_correct:
            st.success("Correct! 🎉")
        else:
            st.error(
                f"Wrong! The correct answer is: {question['answer']}"
            )

        if st.button("Next Question ➜", key=f"next_btn_{q_index}", use_container_width=True):
            if st.session_state.current_question < len(quiz_data) - 1:
                st.session_state.current_question += 1
                st.session_state.selected_option = None
                st.session_state.show_result = False
                st.session_state.last_answer_correct = False
                st.rerun()
            else:
                st.session_state.quiz_finished = True
                st.rerun()

else:
    st.markdown("<div class='quiz-container' style='text-align: center;'>", unsafe_allow_html=True)
    st.balloons()
    st.header("Quiz Completed! 🎉")
    st.markdown(
        f"<h2 style='color: #ffd700;'>Your Score: {st.session_state.score} / {len(quiz_data)}</h2>",
        unsafe_allow_html=True,
    )

    percentage = (st.session_state.score / len(quiz_data)) * 100
    if percentage >= 80:
        st.write("Excellent! You are a history expert! 🌟")
    elif percentage >= 50:
        st.write("Good job! Keep learning! 📚")
    else:
        st.write("Keep practicing! History is vast! 💪")

    if st.button("Restart Quiz", use_container_width=True):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.quiz_finished = False
        st.session_state.selected_option = None
        st.session_state.show_result = False
        st.session_state.last_answer_correct = False
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
