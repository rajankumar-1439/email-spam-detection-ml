import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

dataset = pd.read_csv("spam email.csv")


dataset.drop_duplicates(inplace= True)

dataset["Category"] = dataset["Category"].replace(["ham","spem"],["Not spam","Spam"])

x=dataset["Message"]
y=dataset["Category"]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

#creating the model
cv = CountVectorizer(stop_words="english")
feature = cv.fit_transform(x_train)

# testing the model
model = MultinomialNB()
model.fit(feature, y_train)

feature_test = cv.transform(x_test)

def predict(message):
    input_message = cv.transform([message]).toarray()
    result = model.predict(input_message)
    return result
    

# show webpage
st.title("Spam Detection...")
input_message = st.text_input("Enter Message Here.")                    
if st.button("Validate"):
    output = predict(input_message)
    st.markdown(output) 