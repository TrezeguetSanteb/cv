# Proyecto de Análisis Predictivo con Machine Learning y Redes Neuronales

Este proyecto implementa diversos modelos de aprendizaje automático y redes neuronales para realizar predicciones sobre datos del sector hotelero. Incluye un pipeline completo desde la exploración de datos hasta la evaluación y optimización de modelos.

## Descripción

El proyecto analiza un conjunto de datos sobre reservas de hoteles para predecir cancelaciones u otros comportamientos relevantes. Utiliza técnicas avanzadas de preprocesamiento, selección de características, y múltiples algoritmos de aprendizaje automático para lograr la mayor precisión predictiva posible.

## Características

- Pipeline completo de análisis de datos
- Preprocesamiento y limpieza de datos
- Exploración y visualización de datos
- Implementación de múltiples modelos de ML
- Redes neuronales con TensorFlow/Keras
- Técnicas de ensemble learning
- Optimización de hiperparámetros
- Evaluación exhaustiva con múltiples métricas

## Requisitos

- Python 3.7+
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- TensorFlow 2.x
- Keras
- XGBoost
- Matplotlib
- Seaborn
- dtreeviz

Puedes instalar las dependencias con:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```
├── Notebooks/
│   ├── 01_EDA_DataCleaning.ipynb
│   ├── 02_FeatureEngineering.ipynb
│   ├── 03_ModelTraining.ipynb
│   ├── 04_NeuralNetworks.ipynb
│   └── 05_ModelEvaluation.ipynb
├── Datasets/
│   ├── hotels_train.csv
│   ├── hotels_test.csv
│   ├── dataset_modificado.csv
│   └── data_test.csv
├── Models/
│   ├── random_forest.pkl
│   ├── xgboost_model.pkl
│   ├── neural_network.h5
│   └── ensemble_model.pkl
├── Results/
│   ├── performance_metrics.csv
│   ├── feature_importance.png
│   └── confusion_matrices.png
├── requirements.txt
└── README.md
```

## Metodología

### 1. Exploración y Preprocesamiento de Datos

- Análisis exploratorio para entender la distribución y relaciones entre variables
- Detección y manejo de valores atípicos
- Imputación de valores faltantes con KNNImputer
- Codificación de variables categóricas
- Normalización/Estandarización de características numéricas

### 2. Ingeniería de Características

- Selección de características relevantes
- Creación de nuevas características a partir de las existentes
- Análisis de correlación y multicolinealidad
- Reducción de dimensionalidad cuando es necesario

### 3. Modelado

#### Modelos Tradicionales
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- XGBoost
- Gradient Boosting Classifier
- Logistic Regression

#### Ensemble Learning
- Stacking Classifier
- Voting Classifier

#### Redes Neuronales
- Redes neuronales con múltiples capas ocultas
- Optimización con Adam
- Técnicas de regularización (dropout, etc.)

### 4. Evaluación y Optimización

- Validación cruzada estratificada (StratifiedKFold)
- Búsqueda de hiperparámetros con RandomizedSearchCV y GridSearchCV
- Métricas de evaluación: precisión, recall, F1-score, ROC-AUC
- Análisis de matrices de confusión
- Curvas de aprendizaje para detectar overfitting/underfitting

## Resultados

El proyecto logra identificar los factores más relevantes que influyen en [objetivo del proyecto] y construye modelos con alta capacidad predictiva. Los mejores resultados se obtienen con [mencionar los mejores modelos] que alcanzan las siguientes métricas:

- Accuracy: X%
- Precision: X%
- Recall: X%
- F1-Score: X
- ROC-AUC: X

## Visualizaciones

El proyecto incluye diversas visualizaciones para facilitar el entendimiento de los datos y los resultados:

- Matrices de correlación
- Importancia de características
- Árboles de decisión visualizados
- Matrices de confusión
- Curvas ROC y Precision-Recall
- Distribuciones de características

## Uso

1. Clone el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/hotel-prediction-ml.git
   cd hotel-prediction-ml
   ```

2. Instale las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecute los notebooks en orden secuencial:
   ```bash
   jupyter notebook Notebooks/01_EDA_DataCleaning.ipynb
   ```

## Predicciones

Para realizar predicciones con los modelos entrenados:

```python
import pickle
import pandas as pd

# Cargar modelo
with open('Models/ensemble_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Cargar datos para predicción
new_data = pd.read_csv('your_new_data.csv')

# Preprocesar datos (asegúrese de aplicar las mismas transformaciones que al entrenar)
# ...

# Realizar predicciones
predictions = model.predict(new_data)
probabilities = model.predict_proba(new_data)
```

## Lecciones aprendidas

- La importancia del preprocesamiento riguroso de datos para mejorar el rendimiento del modelo
- Beneficios de las técnicas de ensemble learning para reducir la varianza
- El valor de la validación cruzada para evaluar modelos de manera robusta
- Cómo gestionar conjuntos de datos desequilibrados
- Ventajas y desventajas de diferentes técnicas de imputación de valores faltantes

