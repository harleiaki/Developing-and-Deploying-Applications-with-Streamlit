import streamlit as st 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud 


st.subheader("Demo of WordCloud App")

text_input=st.text_area("Enter the Text to be used for wordcloud generation")

if st.button("Generate WordCloud"):
	wc=WordCloud().generate(text_input)
	plt.imshow(wc)
	plt.axis('off')
	st.pyplot(plt)
