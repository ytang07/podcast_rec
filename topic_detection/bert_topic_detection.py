from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups

docs = fetch_20newsgroups(subset='all')['data']
print(len(docs))
print(docs[4])
model = BERTopic()
topics, probs = model.fit_transform(docs)

print(model.get_topic_freq())