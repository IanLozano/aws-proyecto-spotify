# 🎵 Despliegue de API de Predicción de Popularidad en Spotify en AWS EC2

## 🖥️ Descripción General

Este proyecto consistió en desplegar una **API de Machine Learning** en una instancia de **AWS EC2**, utilizando un modelo de **CatBoostRegressor** para predecir la popularidad de canciones de Spotify.  
La API fue desarrollada usando **Flask** y documentada mediante **Swagger UI**.

---

## 🚀 Pasos Realizados

### 1. Creación de la Instancia EC2

Se creó una instancia en AWS EC2 con las siguientes características:

- **Sistema operativo**: Ubuntu 24.04.2 LTS.
- **Tipo de instancia**: t2.micro (elegible para Free Tier).
- **Almacenamiento**: 30 GB de disco EBS.
- **Seguridad**:
  - Se creó un par de llaves (.pem) para acceso SSH seguro.
  - Se configuró el grupo de seguridad para permitir conexiones en el puerto 5000, necesario para la API.

La instancia fue lanzada exitosamente y accesible desde la IP pública proporcionada por AWS.

---

### 2. Conexión y Configuración Inicial

Desde la máquina local se realizó la conexión vía SSH utilizando el archivo `.pem`.  
Una vez dentro de la instancia, se realizaron las siguientes configuraciones:

- Actualización del sistema operativo.
- Instalación de Python 3, pip y la creación de un entorno virtual (venv).
- Instalación de las librerías necesarias: Flask, Flask-RESTX, Flask-CORS, pandas, catboost y joblib.

Esto dejó lista la instancia para entrenar el modelo y desplegar la API.

---

### 3. Entrenamiento del Modelo de Machine Learning

Se subió a la instancia el archivo `dataTrain_Spotify.csv`, que contiene información sobre canciones de Spotify.

El flujo de trabajo para el entrenamiento fue:

- Carga del archivo de datos.
- División en conjuntos de entrenamiento y prueba.
- Limpieza de datos, transformando las variables booleanas y llenando valores nulos en las variables categóricas.
- Definición de las variables continuas, binarias y categóricas.
- Entrenamiento del modelo `CatBoostRegressor` utilizando las variables seleccionadas.
- Guardado del modelo entrenado en un archivo `modelo_catboost.pkl` para su posterior uso en la API.

---

### 4. Desarrollo de la API con Flask

Se desarrolló una API REST que permite hacer predicciones de popularidad a partir de los datos de una canción.

La API incluye:

- Un endpoint **POST** en `/predict/` que recibe un JSON con los datos de entrada y devuelve la popularidad estimada.
- Un endpoint **GET** en `/predict/params` que permite enviar los datos como parámetros en la URL y obtener la predicción.

Además, se integró **Swagger UI** en `/docs` para documentar automáticamente los endpoints y permitir su prueba fácil desde el navegador.

Se utilizó **CORS** para permitir el acceso a la API desde diferentes dominios, evitando problemas de seguridad del navegador.

---

### 5. Despliegue y Exposición de la API

La API fue configurada para ejecutarse escuchando en `0.0.0.0`, permitiendo el acceso externo desde la IP pública de la instancia EC2.

Se utilizaron técnicas para mantener la API corriendo incluso si se cerraba la conexión SSH, como:

- Uso de **tmux** para ejecutar la API en una sesión separada y mantenerla activa.
- Alternativamente, se propuso el uso de `nohup` para ejecución en segundo plano.

---

### 6. Pruebas de Funcionamiento

La API fue probada exitosamente de las siguientes maneras:

- **Acceso a la documentación Swagger** desde un navegador accediendo a `http://<IP_PUBLICA>:5000/docs`.
- **Pruebas con `curl`** enviando peticiones POST directamente desde la terminal.
- **Pruebas vía GET** accediendo a través de URLs construidas con los parámetros necesarios.

En todos los casos, la API devolvió la popularidad estimada correctamente, asegurando el correcto funcionamiento del modelo y del despliegue.

---

## 🔥 Estado Final

- **API funcional** y expuesta al público a través de AWS EC2.
- **Modelo CatBoost** correctamente entrenado y desplegado.
- **Documentación automática disponible** para consulta y prueba.
- **Accesible mediante POST y GET** con soporte para JSON y parámetros URL.

---

## 🛡️ Consideraciones de Seguridad

- Se permitió el acceso público solo al puerto 5000.
- Se recomendó en futuras fases mejorar la seguridad utilizando HTTPS, autenticación de usuarios o migración a servidores de producción como Gunicorn o Nginx.
- Se utilizó CORS de manera controlada para permitir pruebas y desarrollo.

---

# 🎯 Resumen

Este proyecto demuestra el despliegue completo de un modelo de Machine Learning en producción, desde el entrenamiento en AWS EC2 hasta su exposición mediante una API RESTful accesible públicamente.  
El proceso integra buenas prácticas de configuración, seguridad y documentación de APIs, utilizando herramientas modernas como Flask, Flask-RESTX, CatBoost y Swagger UI.

---
