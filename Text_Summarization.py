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
    mthd = st.selectbox("How do you want to summarize text?",options=["<Choose an Option>","By ratio","By word_count"])
        
    if mthd != "<Choose an Option>":
        if mthd == "By ratio":
            ratio = st.number_input("**ratio** - It represents the proportion of the summary compared to the original text.",min_value=0.1,max_value=1.0,value=0.2,step=.05)
            t1 = time.time()
            short_summary = summarize(txt,ratio=ratio)
            t2 = time.time()
            val = "ratio"
        else:
            wc = st.number_input("**word_count** - It decides the no of words in the summary.",value=30,min_value=1)
            t1 = time.time()
            short_summary = summarize(txt,word_count=wc)
            t2 = time.time()
            val = "word_count"

        # st.write(f'''### Original Text''')
        h = len(txt.split(". "))
        st.text_area("Original Text",value=txt,height=300)

        if short_summary=="":
            st.write(f'''### Please increase {val} or Add more sentences!''')
        else:
            st.write(f'''### Summarized Text
{short_summary}''')

        tp = t2-t1
        st.metric("Summarize Time",value=f"{round(tp,4)} sec")