import streamlit as st
from content_generator import ContentGenerator

st.set_page_config(page_title="Social Media Content Generator", layout="centered")

st.title("🚀 Social Media Content Generator")

@st.cache_resource
def load_model():
    return ContentGenerator()

generator = load_model()

topic = st.text_input("Enter your topic")

col1, col2 = st.columns(2)

with col1:
    max_tokens = st.slider("Max Tokens", 50, 300, 100)

with col2:
    temperature = st.slider("Temperature", 0.1, 1.5, 0.7)

if st.button("Generate Content"):
    if topic:
        st.subheader("📢 Post")
        post = generator.generate_text(
            f"Write a social media post about {topic}:",
            max_new_tokens=max_tokens,
            temperature=temperature
        )
        st.write(post)

        st.subheader("✍️ Caption")
        caption = generator.generate_text(
            f"Create a catchy caption for {topic}:",
            max_new_tokens=50,
            temperature=temperature
        )
        st.write(caption)

        st.subheader("#️⃣ Hashtags")
        hashtags = generator.generate_text(
            f"Generate hashtags for {topic}:",
            max_new_tokens=30,
            temperature=temperature
        )
        st.write(hashtags)
    else:
        st.warning("Please enter a topic")
