from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq

def main():
    load_dotenv()
    
    # Groq API
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    st.set_page_config(page_title="AI Chat Interface", layout="wide")
    st.title("AI Chat Interface")

    model = st.sidebar.selectbox(
        "Select Model",
        ("llama3-8b-8192", "llama-3.1-70b-versatile", "llama-3.1-8b-instant")
    )

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    def send_message():
        if st.session_state.user_input:
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {"role": "user", "content": st.session_state.user_input}
                    ],
                    model=model,
                )
                
                ai_response = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "user", "content": st.session_state.user_input})
                st.session_state.messages.append({"role": "ai", "content": ai_response})
                st.session_state.user_input = ""
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.warning("Please enter a prompt.")

    st.text_area("Enter your prompt:", height=100, key="user_input")
    
    st.button("Send", on_click=send_message)

    # chat history
    if st.session_state.messages:
        for message in st.session_state.messages:
            if message['role'] == 'user':
                st.markdown(f"**👤 You:** {message['content']}")
            else:
                st.markdown(f"**🤖 AI:** {message['content']}")

if __name__ == "__main__":
    main()
