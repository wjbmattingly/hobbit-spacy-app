import streamlit as st
import spacy
from spacy import displacy


st.markdown("""[![Hobbit spaCy on PyPI](https://img.shields.io/pypi/v/en-hobbit.svg)](https://pypi.org/project/en-hobbit/)
![Stars](https://img.shields.io/github/stars/wjbmattingly/hobbit-spacy.svg?style=social)
![Forks](https://img.shields.io/github/forks/wjbmattingly/hobbit-spacy.svg?style=social)""")

st.image("https://github.com/wjbmattingly/hobbit-spacy/raw/main/images/hobbitspacy.png")

@st.cache_resource
def load_model():
    nlp = spacy.load("en_hobbit")
    return nlp

@st.cache_data
def load_options():
    
    colors = {
        'HOBBIT': "#ADD8E6",   # Light blue
        'CVT': "#cbebc5",
        'REALM': "#FFFFE0",    # Light yellow
        'MAN': "#E6E6FA",      # Lavender
        'DWARF': "#98FB98",    # Pale green
        'ELF': "#FFE4B5",      # Moccasin
        'AINUR': "#FFDAB9",    # Peachpuff
        'RIVER': "#00FFFF",    # Aqua
        'MOUNTAIN': "#8B4513", # SaddleBrown
        'ROAD': "#808080",     # Gray
        'RELATION': "#ff91e3", 
        "WEAPON": "#ca91ff"
    }
    options = {"ents": ['HOBBIT', 'CVT', 'REALM', 'MAN', 'DWARF', 'ELF', 'AINUR', "RIVER", "MOUNTAIN", "ROAD", "RELATION", "WEAPON"], "colors": colors}
    options["spans_key"] = "main"
    return options

nlp = load_model()
options = load_options()

text = st.text_area("Paste Text", "Frodo son of Drogo went to Mordor with Sam, Strider, also known as Aragorn, Gandalf and others. He carried the sword of Bilbo Baggins. This sword was called Sting. Gondor is a realm whose capital is Minis Tirith.")
doc = nlp(text)
html= displacy.render(doc, style="span", options=options)
st.write(html, unsafe_allow_html=True)