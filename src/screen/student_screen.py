import streamlit as st
from src.ui.base_layout import style_background_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np


def student_screen():

    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns(2, gap='large')

    with c1:
        header_dashboard()

    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn'):
            st.session_state['login_type'] = None
            st.rerun()
    
    st.header('Login using FaceID', text_alignment='center')
    st.space()
     

    photo_soure = st.camera_input("Position your face in the center")

    if photo_soure:
        np.array(Image.open(photo_soure))
    footer_dashboard()


    