import streamlit as st
import random


# Set page config
st.set_page_config(
    page_title="Mad Libs Story Generator",
    page_icon="📝",
    layout="centered"
)

# Add title and description
st.title("📝 Mad Libs Story Generator")
st.subheader("Choose AI-generated or logic-based story generation!")

# Input fields
noun = st.text_input("Enter a noun", placeholder="e.g., cat")
adjective = st.text_input("Enter an adjective", placeholder="e.g., fluffy")
verb = st.text_input("Enter a verb", placeholder="e.g., jumps")

# Story type selection
story_type = st.radio(
    "Select story type:",
    ["AI-generated", "Logic-based"]
)

# Basic story templates for logic-based generation
story_templates = [
    "The {adj} {noun} {verb} through the garden.",
    "Once upon a time, a {adj} {noun} {verb} over the moon.",
    "In the magical forest, the {adj} {noun} {verb} with joy.",
    "Everyone watched as the {adj} {noun} {verb} around the park."
]

def generate_logic_story(noun, adj, verb):
    template = random.choice(story_templates)
    return template.format(noun=noun, adj=adj, verb=verb)

def generate_ai_story(noun, adj, verb):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    prompt = f"Create a short, fun story (2-3 sentences) using these words: noun='{noun}', adjective='{adj}', verb='{verb}'"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return response.choices[0].message.content

# Generate button
if st.button("Generate Story!", type="primary"):
    if not all([noun, adjective, verb]):
        st.error("Please fill in all the fields!")
    else:
        try:
            if story_type == "AI-generated":
                story = generate_ai_story(noun, adjective, verb)
            else:
                story = generate_logic_story(noun, adjective, verb)
            
            st.success("Your story is ready!")
            st.write(story)
        except Exception as e:
            st.error("An error occurred while generating the story. Please try again.")
