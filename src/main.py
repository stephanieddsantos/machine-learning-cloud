import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder

# 1. Carregar os dados
file_path = 'data/crop_yield.csv'
df = pd.read_csv(file_path)

# 2. Pré-processamento
# Separar features e target
y = df['Yield']
X = df.drop('Yield', axis=1)

# Codificar variável categórica 'Crop'
crop_encoder = OneHotEncoder(sparse_output=False, drop='first')
crop_encoded = crop_encoder.fit_transform(X[['Crop']])
crop_encoded_df = pd.DataFrame(crop_encoded, columns=crop_encoder.get_feature_names_out(['Crop']))

# Concatenar as variáveis numéricas e as dummies
X_num = X.drop('Crop', axis=1).reset_index(drop=True)
X_final = pd.concat([X_num, crop_encoded_df], axis=1)

# 3. Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_final, y, test_size=0.2, random_state=42)

# 4. Definir modelos
modelos = {
    'Linear Regression': LinearRegression(),
    'Ridge Regression': Ridge(random_state=42),
    'Lasso Regression': Lasso(random_state=42),
    'Random Forest': RandomForestRegressor(random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(random_state=42)
}

resultados = []

# 5. Treinar, prever e avaliar
for nome, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    resultados.append({
        'Modelo': nome,
        'R2': r2,
        'RMSE': rmse,
        'MAE': mae
    })

# 6. Exibir resultados
resultados_df = pd.DataFrame(resultados)
print('Comparação dos Modelos:')
print(resultados_df.sort_values(by='R2', ascending=False).reset_index(drop=True))