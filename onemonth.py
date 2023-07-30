import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier

data = datasets.load_wine(as_frame=True)

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=22)

estimator_range = [2, 4, 6, 8, 10, 12, 14, 16]

models = []
scores = []

for n_estimators in estimator_range:
    clf = BaggingClassifier(n_estimators=n_estimators, random_state=22)
    clf.fit(X_train, y_train)
    models.append(clf)
    scores.append(accuracy_score(y_true=y_test, y_pred=clf.predict(X_test)))


plt.igure(figsize=(9, 6))

plt.plot(estimator_range, score)

plt.show()
