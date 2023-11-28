import streamlit as st
import streamlit.components.v1 as stc

from eda_app import runEdaApp
from ml_app  import runMlApp

html_temp = """
		<div style="background-color:orange;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Diabetes Diagnose </h1>
		<h4 style="color:white;text-align:center;">Poltekkes Kemenkes Banten</h4>
		</div>
		"""

def main():
       st.title('Main App')
       stc.html(html_temp)
       
       menu = ['Home', 'EDA', 'ML','About']
       choice = st.sidebar.selectbox('Menu', menu)

       if choice == 'Home':
              st.subheader('Home')
              st.write("""
			### Early Stage Diabetes Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
       elif choice == 'EDA':
              runEdaApp()
       elif choice == 'ML':
              runMlApp()
       else:
              st.subheader('About')


if __name__ == '__main__':
       main()