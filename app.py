#!pip install langchain==0.3.26 openai==1.91.0 langchain-community==0.3.26 langchain-openai==0.3.27 httpx==0.28.1
#pip install python-dotenv
#pip install streamlit==1.41.1

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

WARNING_ICON = ":material/warning:"
ERROR_ICON = ":material/error:"

def llm_chain(input_message, selected_item):
    if selected_item == "猫の専門家":
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。専門外の質問には答えないでください。ネコ語で答えてください。可愛らしく！"),
            HumanMessage(content=input_message),
        ]
    elif selected_item == "旅の専門家":
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。専門外の質問には答えないでください。サザエさん風に答えてください。"),
            HumanMessage(content=input_message),
        ]
    elif selected_item == "料理の鉄人":
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。専門外の質問には答えないでください。メニューを提案する際には必ず季節の食材を取り入れてください。材料を挙げる際には分量も具体的に記載してください。いくつかの食材から作れる何かを提案してください。あほっぽく！"),
            HumanMessage(content=input_message),
        ]
    elif selected_item == "宝くじの神":
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。専門外の質問には答えないでください。予想する場合は庶民の想像を絶するような予想を５パターン出してください。お侍さん風に答えてください。上から目線で！"),
            HumanMessage(content=input_message),
        ]
    else:
        messages = [
            SystemMessage(content=f"あなたは{selected_item}です。質問に対して200文字以内で回答してください。専門外の質問には答えないでください。"),
            HumanMessage(content=input_message),
        ]
    result = llm(messages)
    return result

import streamlit as st
st.title("専門家が答えるWebアプリ")
#st.write("##### 動作モードA: 食の専門家")
#st.write("入力フォームにテキストを入力し、「実行」ボタンを押してください。")
#st.write("##### 動作モードB: 旅の専門家")
#st.write("入力フォームにテキストを入力し、「実行」ボタンを押してください。")
st.markdown(":violet[入力フォームにテキストを入力し、「実行」ボタンを押してください。]")
st.warning("お金がちょっとかかりますので乱用しないでください。", icon=WARNING_ICON)

selected_item = st.sidebar.radio(
    "動作モードを選択してください。",
    ["料理の鉄人", "食の専門家", "旅の専門家", "遊びの鉄人", "猫の専門家", "Python博士", "宝くじの神", "楽器の達人"],
)

st.divider()
input_message = st.text_input(label="質問を入力してください。")

if st.button("実行"):
    st.divider()

    if input_message:
        result = llm_chain(input_message, selected_item)
        st.write(result.content)
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。", icon=ERROR_ICON)
