import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
data = {
    "message":[
        "Win a free iPhone now",
        "Claim your prize",
        "Hello how are you",
        "Let's meet tomorrow",
        "Free money offer",
        "Project meeting at 10"
    ],
    "label":[
        "spam",
        "spam",
        "not spam",
        "not spam",
        "spam",
        "not spam"
    ]
}

df = pd.DataFrame(data)

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df["message"])

y=df["label"].map({"spam":1,"not spam":0})

model = MultinomialNB()
model.fit(X,y)
print("---- Email Spam Detector ----")


user_msg = input("Enter your message: ")
user_vector = vectorizer.transform([user_msg])


prediction = model.predict(user_vector)


if prediction[0] == 1:
    print("🚫 Spam Message")
else:
    print("✅ Not Spam Message")