# -*- coding: utf-8 -*-
"""Stratified_CV_SHAP_MultiDisease_Model (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vfFxhQ4RIv3wfe8H2S7vhToVwNDqMFM1

# Stratified K-Fold with SHAP for Multi-Disease Prediction

This notebook:
- Trains separate models for CKD, Heart, and Diabetes using Stratified K-Fold
- Evaluates each with AUC and classification metrics
- Applies SHAP explainability on Fold 1 of each task to understand feature contributions
"""

pip install --prefer-binary --upgrade -r requirements.txt

!pip install numpy==1.23.5 pandas==1.5.3 scikit-learn==1.2.2 scipy==1.10.1
!pip install tensorflow==2.12.0 tensorflow-addons==0.20.0
!pip install shap==0.41.0

!pip install shap tensorflow tensorflow-addons



import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report, roc_auc_score
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow_addons.losses import SigmoidFocalCrossEntropy

df = pd.read_csv("Unified_Enhanced_MultiDisease_Dataset.csv")
label_cols = ['diabetes_label', 'heart_label', 'ckd_label']
df = df.drop(columns=['classification', 'target'], errors='ignore')
df = df.drop(columns=[col for col in df.select_dtypes(include='object') if col not in label_cols], errors='ignore')

for col in label_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.drop(columns=['source'], errors='ignore')

imputer = SimpleImputer(strategy='median')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

feature_cols = [col for col in df_imputed.columns if col not in label_cols]
scaler = StandardScaler()
df_imputed[feature_cols] = scaler.fit_transform(df_imputed[feature_cols])

X = df_imputed[feature_cols].values
y_d = df_imputed['diabetes_label'].astype(int).values
y_h = df_imputed['heart_label'].astype(int).values
y_k = df_imputed['ckd_label'].astype(int).values

def build_model(input_dim):
    input_layer = Input(shape=(input_dim,))
    shared = Dense(256, activation='relu')(input_layer)
    shared = Dropout(0.3)(shared)
    shared = Dense(128, activation='relu')(shared)
    output = Dense(1, activation='sigmoid')(shared)
    model = Model(inputs=input_layer, outputs=output)
    model.compile(optimizer=Adam(1e-4),
                  loss=SigmoidFocalCrossEntropy(),
                  metrics=['accuracy'])
    return model

shap.initjs()
for task_name, y in zip(['Diabetes', 'Heart Disease', 'CKD'], [y_d, y_h, y_k]):
    print(f"\n📊 Stratified 5-Fold CV with SHAP for {task_name}")
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    fold = 1

    for train_idx, test_idx in skf.split(X, y):
        print(f"\n🔁 Fold {fold}")
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        model = build_model(X.shape[1])
        model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)
        y_pred = model.predict(X_test).ravel()
        y_bin = (y_pred > 0.5).astype(int)

        print(classification_report(y_test, y_bin))
        print("AUC:", roc_auc_score(y_test, y_pred))

        # Apply SHAP only on fold 1
        if fold == 1:
            explainer = shap.KernelExplainer(model.predict, X_train[:100])
            shap_values = explainer.shap_values(X_test[:50])
            shap.summary_plot(shap_values, X_test[:50], feature_names=feature_cols)

        fold += 1