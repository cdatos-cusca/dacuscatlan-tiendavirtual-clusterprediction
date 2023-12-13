import streamlit as st
import pandas as pd

st.set_page_config(page_title="ExtraYA", page_icon="💰")
st.sidebar.header("ExtraYA")
#st.markdown("# ExtraYA")
#st.image("img/Logo_color.png")

uploaded_file_extra = st.file_uploader("Por favor, cargue un archivo CSV")

if uploaded_file_extra is not None:
    dataframe_extra = pd.read_csv(uploaded_file_extra)

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(dataframe_extra)

    st.download_button(
        label="Descarga la data con tus clusters :D",
        data=csv,
        file_name='data_clusters_extraya.csv',
        mime='text/csv',
    )

    footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Hecho con  ❤ por Data & Analytics</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)