import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

data = pd.read_csv("fake_or_real_news.csv")
data['fake'] = data['label'].apply(lambda x: 0 if x == "REAL" else 1)
data = data.drop("label", axis=1)
X, y = data['text'], data['fake']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# need to vectorize before feeding into model
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

clf = LinearSVC()
clf.fit(X_train_vectorized, y_train)
correct_Percent = clf.score(X_test_vectorized, y_test)
# print("Correct Percent: ", correct_Percent)
# print(len(y_test) * correct_Percent)

# to find and test new articles
with open("mytext.txt", "w", encoding="utf-8") as f:
    # would need to copy and paste new article and add to current data set
    f.write(X_test.iloc[10])

# load new article
with open("mytext.txt", "r", encoding="utf-8") as f:
    new_article = f.read()

vectorized_text = vectorizer.transform([new_article])
clf.predict(vectorized_text)
print(y_test.iloc[10])  # 0 = real, 1 = fake
