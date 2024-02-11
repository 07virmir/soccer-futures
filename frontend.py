import streamlit as st
from streamlit_extras.row import row

# Define the submit action
def submit_action(uploaded_files):
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            st.write(f"File submitted: {uploaded_file.name}")

header_row = row(3, vertical_align="center")
img1 = header_row.image('extras/ball.png', width = 50)
title = header_row.markdown(body="<h1 style='text-align: center; color: white;'>PitchPerfect</h1>", unsafe_allow_html=True)
img2 = header_row.image('extras/ball.png', width = 50)
desc = st.markdown(body="<h4 style='text-align: center; color: white;'>Your platform to upload and analyze soccer training videos</h4>", unsafe_allow_html=True)
# Bubbles (information sections)
col1, col2 = st.columns(2)

with col1:
    with st.expander("Why use PitchPerfect?"):
        st.write("Here is some more information!")
    with st.expander("How does it work"):
        st.write("Here is some more information!")
    with st.expander("Future Improvements"):
        st.write("Here is some more information!")

with col2:
    uploaded_files = st.file_uploader("Choose Files", accept_multiple_files=True, type=['csv', 'mp4'])
    submit_button = st.button("Submit")

    if submit_button:
        submit_action(uploaded_files)

# Embedded Training Videos
st.markdown("## Embedded Training Videos")
video_row = row(2, vertical_align="center")
video_row.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")
video_row.video("data/top_view/viz_results/D_20220220_1_0000_0030.mp4")
