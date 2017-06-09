
import sys
from sklearn.datasets import load_files

twenty_train = load_files('test data',encoding='utf-8')
print(twenty_train.target_names)

from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(twenty_train.data)
print(X_train_counts)
X_train_counts.shape

count_vect.vocabulary_.get('for')

ngram_count_vect = CountVectorizer(ngram_range=(1, 5))
XX_train_counts = ngram_count_vect.fit_transform(twenty_train.data)

XX_train_counts.shape

ngram_count_vect.vocabulary_.get('algorithm for')


from sklearn.feature_extraction.text import TfidfTransformer
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
X_train_tf.shape

tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(twenty_train.data)
X_train_tfidf.shape


from sklearn.pipeline import Pipeline

from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

text_clf = Pipeline([('vect', TfidfVectorizer()),
                     ('clf', LinearSVC()),
])

text_clf.fit(twenty_train.data, twenty_train.target)


twenty_test = load_files('train data',encoding='utf-8')

predicted = text_clf.predict(twenty_test.data)

import numpy as np
np.mean(predicted == twenty_test.target)

from sklearn import metrics
print(metrics.classification_report(twenty_test.target, predicted,
    target_names=twenty_test.target_names))