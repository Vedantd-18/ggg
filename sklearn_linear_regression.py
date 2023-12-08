import numpy as np
from sklearn.linear_model import LinearRegression

# Generate some sample data
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Use scikit-learn LinearRegression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Display the parameters
theta_best_sklearn = np.concatenate([lin_reg.intercept_, lin_reg.coef_.ravel()])

print("Theta Best (Scikit-Learn):", theta_best_sklearn)

# Predict new values
X_new_sklearn = np.array([[0], [2]])
y_predict_sklearn = lin_reg.predict(X_new_sklearn)

print("Predictions (Scikit-Learn):", y_predict_sklearn.ravel())
