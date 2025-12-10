#!pip install langchain==0.3.26 openai==1.91.0 langchain-community==0.3.26 langchain-openai==0.3.27 httpx==0.28.1
#pip install python-dotenv
#pip install streamlit==1.41.1

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

def llm_chain(input_message, selected_item):
    messages = [
        SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。"),
        HumanMessage(content=input_message),
    ]
    result = llm(messages)
    return result

import streamlit as st
st.title("専門家が答えるWebアプリ")
st.write("##### 動作モードA: 食の専門家")
st.markdown(":violet[入力フォームにテキストを入力し、「実行」ボタンを押してください。]")
st.write("##### 動作モードB: 旅の専門家")
st.markdown(":violet[入力フォームにテキストを入力し、「実行」ボタンを押してください。]")
st.write("##### 動作モードC: 猫の専門家")
st.markdown(":violet[入力フォームにテキストを入力し、「実行」ボタンを押してください。]")
st.write("##### 動作モードD: 宝くじの専門家")
st.markdown(":violet[入力フォームにテキストを入力し、「実行」ボタンを押してください。]")
st.warning("お金がちょっとかかりますので乱用しないでください。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["食の専門家", "旅の専門家", "猫の専門家", "宝くじの専門家"],
)

st.divider()
input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if input_message:
        result = llm_chain(input_message, selected_item)
        st.write(result.content)
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")
