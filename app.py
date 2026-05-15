import streamlit as st

st.title("Opportunity Cost Simulator")

options = {
    "study": {"benefit": 8, "cost": 2},
    "work": {"benefit": 10, "cost": 6},
    "gaming": {"benefit": 6, "cost": 1}
}

choice = st.selectbox("Choose an option", list(options.keys()))

selected = options[choice]

net = selected["benefit"] - selected["cost"]

st.write("Net value:", net)
