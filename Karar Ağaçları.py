import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree 
import DecisionTreeRegressor, plot_tree


study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
test_scores = np.array([50, 55, 70, 80, 85, 90, 92, 98])


model = DecisionTreeRegressor(max_depth=3)


model.fit(study_hours, test_scores)


new_study_hour = np.array([[5.5]]) 
predicted_score = model.predict(new_study_hour)


plt.figure(figsize=(12, 8))
plot_tree(model, filled=True, rounded=True, feature_names=["Study Hours"])
plt.title('Decision Tree Regressor Tree')
plt.show()


plt.scatter(study_hours, test_scores, color='darkred')
plt.plot(np.sort(study_hours, axis=0), model.predict(np.sort(study_hours, axis=0)), color='orange')
plt.scatter(new_study_hour, predicted_score, color='green')
plt.title('Study Hours vs Test Scores')
plt.xlabel('Study Hours')
plt.ylabel('Test Scores')
plt.grid(True)
plt.show()


print(f"Predicted test score for {new_study_hour[0, 0]} hours of study: {predicted_score[0]:.2f}.")
