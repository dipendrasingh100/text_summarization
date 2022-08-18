import json
import streamlit as st
import gensim
from gensim.summarization import summarize
import time

st.set_page_config(
     page_title="Text Summarization App",
     page_icon="🧊",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "## Text Summarization. This app willl summarize all your long text into short. "
     }
 )

st.title("Text Summarizer")
uploaded_file = st.file_uploader("Choose a JSON file",type="json")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.read()
    # txt = uploaded_file.getvalue().decode("utf-8")
    txt = json.load(uploaded_file)
    ls = []
    for item in txt["txt"]:
        for i in item.values():
            ls.append(i)
    txt = " ".join(ls)  
else:
    st.write("OR")
    txt = st.text_area("Enter text to summarize", height=200)

if (uploaded_file is None) and (txt == ""):
    pass
else:
    t1 = time.time()
    short_summary = summarize(txt,ratio=.2)
    t2 = time.time()
        # st.write(f'''### Original Text''')
    h = len(txt.split(". "))

    if uploaded_file is not None :
        st.text_area("Original Text",value=txt,height=300)
    
    st.write(f'''### Summarized Text
{short_summary}''')

    tp = t2-t1
    st.metric("Summarize Time",value=f"{round(tp,4)} sec")