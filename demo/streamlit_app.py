import streamlit as st

from streamlit_pills import pills

st.set_page_config("Demo for streamlit-pills", "💊")
st.write(
    f'<span style="font-size: 78px; line-height: 1">💊</span>',
    unsafe_allow_html=True,
)

"# Demo for [streamlit-pills](https://github.com/jrieke/streamlit-pills)"
"## Example"

options = [
    "General widgets",
    "Charts",
    "Images",
    "Video",
    "Text",
    "Maps & geospatial",
    "Dataframes & tables",
    "Molecules & genes",
    "Graphs",
    "3D",
    "Code & editors",
    "Page navigation",
    "Authentication",
    "Style & layout",
    "Developer tools",
    "App builders",
    "Integrations with other tools",
    "Collections of components",
]

icons = [
    "🧰",
    "📊",
    "🌇",
    "🎥",
    "📝",
    "🗺️",
    "🧮",
    "🧬",
    "🪢",
    "🧊",
    "✏️",
    "📃",
    "🔐",
    "🎨",
    "🛠️",
    "🏗️",
    "🔌",
    "📦",
]

selected = pills("Select a category", options, icons)
st.write("You selected:", selected)

"## API reference"
st.help(pills)
