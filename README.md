# 🍦 Predicción de Ventas - Heladería "Gelato Mágico" 📊

Este proyecto aplica técnicas de **Machine Learning (Regresión)** para optimizar la producción de una heladería basada en la temperatura ambiente. El objetivo es reducir el desperdicio y maximizar las ventas mediante un modelo predictivo integrado con **MLflow** y **Azure Machine Learning**.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.12.1
* **Librerías:** Scikit-Learn, Pandas, NumPy
* **Manejo de Experimentos:** MLflow (Tracking de métricas y parámetros)
* **Plataforma Cloud:** Azure Machine Learning Studio
* **Orquestación:** Conceptos de Pipelines de Azure ML

## 📂 Estructura del Proyecto
* `/inputs`: Contiene el dataset `vendas_sorvete.csv`.
* `/src`: Script de entrenamiento `train.py` refactorizado para producción.
* `notebook.ipynb`: Exploración inicial de datos y visualización.
* `README.md`: Documentación del proyecto.

---

## 🧪 El Proceso de Machine Learning

### 1. Refactorización para Producción
Siguiendo las mejores prácticas de **Ingeniería de Sistemas**, el código se migró de un notebook exploratorio a un script de Python (`.py`) modular. Se utilizó la librería `argparse` para permitir que el modelo reciba diferentes datasets o hiperparámetros desde la terminal o desde un **Command Job** en Azure.



### 2. Registro con MLflow
Se implementó **MLflow Tracking** para asegurar la trazabilidad. En cada ejecución se registraron:
* **Parámetros:** Tipo de algoritmo (`LinearRegression`).
* **Métricas:** Error Cuadrático Medio (MSE) y $R^2$.
* **Artefactos:** El archivo `.pkl` del modelo entrenado y gráficos de correlación.



### 3. Insights Técnicos obtenidos
* **Correlación Lineal:** Se identificó una correlación directa de ~0.92 entre la temperatura y las ventas, confirmando que el modelo de Regresión Lineal es adecuado.
* **Escalabilidad:** Al registrar el modelo en el **Model Registry** de Azure, estamos listos para un despliegue en un *Endpoint* de tiempo real, permitiendo que la heladería consulte predicciones mediante una API REST.

---

## 📈 Posibilidades de Mejora (Roadmap)
Como parte de mi enfoque en **Auto-healing Pipelines** , las siguientes mejoras son viables:
1.  **Re-entrenamiento Automatizado:** Configurar un **JobSchedule** en Azure ML para re-entrenar el modelo si el MSE supera un umbral definido.
2.  **Integración con Airflow:** Orquestar la ingesta de datos climáticos diarios mediante un DAG que dispare el pipeline de predicción.

---
**Desarrollado por:** Richard Mendoza - Ingeniero de Datos