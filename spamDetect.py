import pickle
import streamlit as st


model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
	st.title("Email Spam Classification Apps")

main()


