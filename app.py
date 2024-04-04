import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage



def web_writer(a):
    format_of_data = ".txt"
    file_name = a + format_of_data
    with open(file_name, 'r') as f:
        var = f.read()
    return var


example = web_writer("example")
key = "################################"
chatllm = ChatOpenAI(openai_api_key=key, temperature=0.8, model='gpt-3.5-turbo')


def ans(inp, lang):
    response = chatllm([
        SystemMessage(
            content=f"As an experienced physician with over 30 years of practice, please provide detailed information on {inp}. If {inp} refers to a medication, include essential details such as active ingredient, dosage, indications, contraindications, warnings/precautions, and side effects/adverse reactions. If {inp} denotes a medical condition, kindly elucidate the recommended treatment options in language {lang} language, covering the same critical aspects: active ingredient, dosage, indications, contraindications, warnings/precautions, and side effects/adverse reactions. Additionally, if {inp} pertains to a medical emergency, please provide immediate first aid tips and initial treatment guidelines. Your expertise and precision in delivering this information, especially in cases of emergencies, are highly valued."
                    f"and fill the information and give the output in the same format"),
    ])
    content = response.content
    return content

# Centering logo using HTML
st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://www.freepnglogos.com/uploads/medicine-logo-png-1.png" alt="Logo" width="100">
    </div>
    """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>MediSage</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>ALL THE DETAILS FOR YOUR MEDICINES</h1>", unsafe_allow_html=True)

st.write("\n\n\n")
st.markdown("<h3 style='text-align: center;'>Language</h1>", unsafe_allow_html=True)
option = st.selectbox('',
    ('English', 'Hindi',  'Nepali', 'Tamil')
)

st.markdown("<h3 style='text-align: center;'>Name of your medicine or disease</h3>", unsafe_allow_html=True)
user_input = st.text_input("")



if user_input:
    text = user_input
    with st.spinner(f'The details is being loaded for {text}'):
        x = ans(text, option)
        st.subheader(text)
        st.write(x)
