import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def train_model():
    # 1. Iniciar el tracking de MLflow
    mlflow.set_experiment("Gelato_Magico_Vendas")
    
    with mlflow.start_run():
        # 2. Cargar datos
        df = pd.read_csv("/workspaces/Repo-AZureML/inputs/vendas_sorvete.csv")
        X = df[['temperatura']]
        y = df['vendas']

        # 3. Dividir datos (Train/Test)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
        

        # 4. Entrenar el modelo (Regresión Lineal)
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 5. Evaluar
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # 6. Loggear en MLflow (Lo que aprendimos en el quiz)
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "modelo_sorvete")
        
        print(f"Modelo entrenado con MSE: {mse}")

if __name__ == "__main__":
    train_model()