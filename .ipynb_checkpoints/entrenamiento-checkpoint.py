import pandas as pd
from catboost import CatBoostRegressor, Pool
import joblib

# === 1. Cargar los datos desde el archivo CSV ===
data = pd.read_csv('dataTrain_Spotify.csv')

# === 2. Separar en entrenamiento y prueba ===
dataTraining = data.sample(frac=0.8, random_state=42)
dataTesting = data.drop(dataTraining.index)

# === 3. Asegurar tipos correctos y limpiar NaNs ===
dataTraining['explicit'] = dataTraining['explicit'].astype(bool)
dataTesting['explicit'] = dataTesting['explicit'].astype(bool)

dataTesting['artists'] = dataTesting['artists'].fillna('unknown_artist')
dataTesting['album_name'] = dataTesting['album_name'].fillna('unknown_album')
dataTesting['track_name'] = dataTesting['track_name'].fillna('unknown_track')

# === 4. Definir variables ===
variables_continuas = [
    'duration_ms', 'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'
]
variables_binarias_o_ordinales = ['explicit', 'key', 'mode', 'time_signature']
variables_categoricas = ['artists', 'album_name', 'track_name', 'track_genre']
features = variables_continuas + variables_binarias_o_ordinales + variables_categoricas
target = 'popularity'

# === 5. Entrenar modelo con TODO el dataTraining ===
train_pool = Pool(dataTraining[features], dataTraining[target], cat_features=variables_categoricas)

model = CatBoostRegressor(
    iterations=1500,
    learning_rate=0.05,
    depth=10,
    l2_leaf_reg=1,
    early_stopping_rounds=100,
    border_count=254,
    eval_metric='RMSE',
    random_seed=42,
    verbose=100
)

model.fit(train_pool)

# === 6. Guardar el modelo entrenado ===
joblib.dump(model, 'modelo_catboost.pkl')
