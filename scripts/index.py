import streamlit as st

import main
import detail

PAGES = {
    "Home Page": main,
    "Detail": detail
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

