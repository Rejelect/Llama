import streamlit as st
from gtts import gTTS
from llama_cpp import Llama
import os
import base64
llm = Llama.from_pretrained(
	repo_id="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
	filename="Meta-Llama-3-8B-Instruct.Q2_K.gguf",
)

llama_model = Llama('Meta-Llama-3-8B-Instruct.Q2_K.gguf') 

messages = [
    {'role':'system', 'content':"You're dictinory explanier"},
    {'role': 'user', 'content': "bear"},
    {"role": "assistant", 'content': """Word: bear
    Bear (noun) – A large, carnivorous animal, typically with a thick coat of fur, found in forests, known for eating a variety of plants and animals.
    Bear (verb) – To carry, support, or endure something, often used for carrying a heavy load or responsibility.
    
    Forms:
    Verb: bear (present), bore (past), borne (past participle)
    Noun: bear (the animal)
    
    Examples:
    Noun:
     - The bear roams the forest in search of food. (The bear moves through the forest looking for food.)
    Verb:
     - She has to bear the heavy burden of responsibility. (She must carry the heavy burden of responsibility.)
     - He bore the pain silently. (He endured the pain quietly.)"""}, 

    {'role':'user', 'content':"nervous"},
    {"role":"assistant",'content':"""Word: nervous

    Nervous (adjective) – Feeling anxious, worried, or uneasy, often due to anticipation or fear.
    Nervous (noun, less common) – A term sometimes used to describe a person who experiences anxiety frequently.
    
    Forms:
    Adjective: nervous
    Noun (less common): nervousness
    
    Examples:
    Adjective:
     - She felt nervous before her big presentation. (She felt anxious before her important presentation.)
     - He was nervous about the exam results. (He was worried about the results of the exam.)
    Noun:
     - His nervousness was evident before the interview. (His anxiety was clear before the interview.)"""}
    
]

stories = [
    {"role": "system", 'content': "You are a story writer. On the last you should write one question"},
    
    
    {'role': 'user', 'content': "the stars."},
    {"role": "assistant", 'content': """Every night, the stars sparkled like jewels in the sky, guiding travelers through the dark.
    One star shone brighter than the rest, flickering as if it had a secret to share.
    The village elders spoke of a legend: this star was a beacon for a lost soul seeking redemption. 
    Many had followed it, but none returned to reveal its mystery.
    One night, a young traveler named Lila set out to follow the star. Her journey was long and difficult, but the light never wavered. 
    Inside, Lila discovered a scroll that revealed the star’s secret—it was a guardian, protecting the world from darkness. 
    Grateful for the truth, Lila returned home, forever changed by her journey.
    
    What secret did the star reveal to Lila when she reached the ancient temple?"""},
    
    {'role': 'user', 'content': "pandas' life."},
    {"role": "assistant", 'content': """In a bamboo forest, a young panda named Bao lived peacefully. 
    He played with his friends: a wise tortoise, a playful squirrel, and a curious bird. 
    One day, humans entered the forest, taking pictures and making noise.
    At first, Bao was cautious, watching from a distance. His friends were calm, but the bird warned of danger. 
    Eventually, Bao approached and saw they brought gifts: bamboo and fruit. Realizing they meant no harm, Bao grew to trust them.
    The humans helped protect the forest, ensuring Bao and his friends could live peacefully for years to come.
    
    Humans harmed Bao’s forest?"""}
    
]


st.set_page_config(page_title="Dictionary App", layout="wide")

# CSS ni qo'shish
st.markdown("""
    <style>
        /* Barcha oynaning orqa fon rangi */
        

        /* Sidebar uchun dizayn */
        .css-1r6wz9d {
            background-color: #ffffff;
        }

        /* Butun interfeys uchun border va joylashuv */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            background-color: #1e1e1e;
            color: white;
            border-radius: 10px;
            border: 2px solid #333333;
        }


        .input-container input {
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            width: 100%;
            font-size: 18px;
        }

        .menu-container {
            display: flex;
            justify-content: space-between;
            border: 2px solid #333333;
            border-radius: 10px;
            margin-top: 20px;
            background-color: #1e1e1e;
            color: white;
            padding: 10px 30px;
        }

        .menu-container div {
            padding: 10px;
            cursor: pointer;
        }

        .menu-container div:hover {
            background-color: #555555;
            border-radius: 5px;
        }

        .result-container {
            background-color:1e1e1e;
            border-radius:5px;
            width:100%;
            height:100%;
        }

    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Choose a menu", ("Dictionary", "Reading"))



if menu == "Dictionary":
    st.markdown('<div class="header"><h1>Dictionary</h1></div>', unsafe_allow_html=True)

    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    word = st.text_input("Enter a word:")
    st.markdown('</div>', unsafe_allow_html=True)

    if word:

        messages.append({'role': 'user', 'content': word})
        t = llm.create_chat_completion(messages=messages, max_tokens=500)['choices'][0]['message']['content']

        st.markdown(
            """
            <div style="background-color: #1e1e1e; color: #FFFFFF; padding: 10px; border-radius:5px">
                {0}
            </div>
            """.format(t),
            unsafe_allow_html=True
        )
        
elif menu == "Reading":
    st.markdown('<div class="header"><h1>Reading</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    topic = st.text_input("Enter a topic:")
    st.markdown('</div>', unsafe_allow_html=True)

    if topic:
        stories.append({'role':'user', 'content': topic})
        stry = llm.create_chat_completion(messages=stories)['choices'][0]['message']['content']

        st.markdown(
            """
            <div style="background-color: #1e1e1e; color: #FFFFFF; padding: 10px; border-radius:5px">
                {0}
            </div>
            """.format(stry),
            unsafe_allow_html=True
        )



        answer = st.text_input('Enter your answer:')    
        
        # checker = llm.create_chat_completion(messages=[{'role':'system', 'content': "You should read story and check the asnwer, and write True or False"}, {'role': 'user', 'content': f"""{stories[2]['content']} answer: The star revealed that it was a guardian protecting the world from darkness.""" }, {'role': 'assisent', 'content': "True"}, {'role':'user', 'content':f"""{stories[4]}, answer: Yes, humans destroyed Bao's forest and scared away all the animals."""}, {"role": "assistant", 'content':"False"}, {"role", "user", f"""{stry}, answer: {answer}"""}])['choices'][0]['message']['content']
        eval_prompt = [
                {"role": "system", "content": "Check the user's answer and respond with 'True' or 'False'."},
                {"role": "user", "content": f"Story: {stry}, Answer: {answer}"}
            ]
        eval_response = llm.create_chat_completion(messages=eval_prompt, max_tokens=10)
        result = eval_response['choices'][0]['message']['content']
        text = [{'role': 'system', 'content': "You should write answer why is answer why is wrong and you should write correct answer"},{'role':'user', 'content': f"""{stry}, answer: {answer}"""}]
        st.write(result)
        if st.button("Submit"):
            
            if "true" in result.lower():
                st.success(f"✅ Correct!")
            else:
                st.error(f"❌ Wrong! {llm.create_chat_completion(messages=text)['choices'][0]['message']['content']}.")


