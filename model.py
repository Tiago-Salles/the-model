from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.datasets import make_regression  

# Générer des données factices
X, y = make_regression(n_samples=100, n_features=1, noise=10)  

# Diviser en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  

# Créer et entraîner le modèle
model = LinearRegression()  
model.fit(X_train, y_train)  

# Prédire sur le test set
predictions = model.predict(X_test)  

print("Prédictions :", predictions[:5]) 