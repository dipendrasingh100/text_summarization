import streamlit as st
import gensim
from gensim.summarization import summarize
import time

st.title("Text Summarizer")

txt = st.text_input("Enter text to summarize")
if txt != "":
    mthd = st.selectbox("How do you want to summarize text?",options=["<Choose an Option>","By ratio","By word_count"])
    if mthd != "<Choose an Option>":
        if mthd == "By ratio":
            ratio = st.number_input("**ratio** - It represents the proportion of the summary compared to the original text.",min_value=0.1,max_value=1.0,value=0.2)
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
        st.write(f'''### Original Text 
{txt}''')

        if short_summary=="":
            st.write(f'''### Please increase {val} or Add more sentences!''')
        else:
            st.write(f'''### Summarized Text
{short_summary}''')

        tp = t2-t1
        st.metric("Summarize Time",value=f"{round(tp,4)} sec")