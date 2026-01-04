<h2>Email Spam Detection Using Naive Bayes & Streamlit</h2>

🧾 Summary :-

🚀 A machine learning web app that classifies email messages as Spam or Not Spam using Naive Bayes.

🔍 Overview

Email spam is a real-world problem that wastes time and poses security risks.✅
This project builds a text classification model that automatically detects spam emails using scikit learn techniques and deploys it as a Streamlit web application for real-time prediction.✅

This is a beginner-to-intermediate ML project done correctly.✅

❓ Problem Statement

✅Goal:
Given an email message, predict whether it is Spam or Not Spam.

Manual filtering is inefficient and error-prone.
We solve this using supervised machine learning trained on labeled email text data.

📊 Dataset

📄 File Name: <a href="https://github.com/rajankumar-1439/email-spam-detection-ml/blob/main/spam%20email.csv">Spam dataset</a>

📌 Columns:

Category → ham / spam

Message → email text content

🔧 Data Preprocessing

✅ Duplicate records removed

✅ Category labels normalized:

ham → Not Spam

spem → Spam


🛠️ Tools & Technologies

✅Python, ✅Pandas, ✅Scikit-learn, ✅Streamlit


⚙️ Methods & Approach
🧠 Step-by-Step ML Pipeline:

1️⃣ Load and clean the dataset

2️⃣ Split data into training & testing sets (80/20)

3️⃣ Convert text into numerical features using CountVectorizer

4️⃣ Train a Multinomial Naive Bayes classifier

5️⃣ Predict spam/not-spam for new messages

6️⃣ Deploy model using Streamlit UI


📌 Key Insights

✅ Naive Bayes performs efficiently on text classification

✅ Removing duplicate data improves model reliability

✅ Simple models + clean data = solid results


🖥️ Dashboard / Model Output

🎯 Streamlit Web App Features:

✅ Text input box for email message

✅ “Validate” button

📢 Instant classification result:

✅ Spam

✅ Not Spam


▶️ How to Run This Project

🪜 Step-by-Step Instructions:

✅Step 1: Clone Repository:-
git clone <a href ="https://github.com/your-username/email-spam-detection-ml.git](https://github.com/rajankumar-1439/email-spam-detection-ml">Email Spam Detection Repository</a>

✅Step 2: Install Dependencies:-
pip install pandas scikit-learn streamlit

✅Step 3: Run Streamlit App:-
streamlit run Email_Spam_Detection.py

✅ Step 4: Use the App

-> Enter an email message

-> Click Validate

-> View spam prediction instantly

<img width="1265" height="573" alt="Screenshot 2026-01-04 134204" src="https://github.com/user-attachments/assets/52467cf5-a00e-4e53-be43-4f8c18f700b1" />


📈 Result & Conclusion

✅ Successfully built a working spam detection system

✅ Model generalizes well on unseen messages

✅ Real-time predictions via web interface


🔮 Future Work

🚧 Possible Improvements:

Add TF-IDF instead of CountVectorizer

Show prediction confidence score

Save & load trained model using Pickle

Add model evaluation metrics (accuracy, confusion matrix)

Deploy on cloud (Streamlit Cloud / Render)


👤 Author & Contact

👨‍💻 Rajan kumar

📧 Email: rajankumarmu1439@gmail.com

🔗 GitHub: <a href="https://github.com/rajankumar-1439">GitHub profile </a>

💼 LinkedIn:<a href="https://www.linkedin.com/in/rajan-kumar-mu1439">LinkedIn profile </a>
