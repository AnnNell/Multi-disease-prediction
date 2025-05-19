# Stratified K-Fold with SHAP for Multi-Disease Prediction

## Overview

This project focuses on developing and evaluating machine learning models to predict the likelihood of three chronic diseases: Chronic Kidney Disease (CKD), Heart Disease, and Diabetes Mellitus. The approach involves training separate models for each disease using Stratified K-Fold cross-validation and applying SHAP (SHapley Additive exPlanations) to understand the contribution of each feature in the predictions.

## Key Features

* **Multi-Disease Prediction:** The project addresses the prediction of three distinct chronic diseases.
* **Stratified K-Fold Cross-Validation:** The notebook uses Stratified K-Fold, a robust technique that ensures each fold has a representative proportion of samples for each class.
* **Model Evaluation:** Models are evaluated using AUC (Area Under the Curve) and other relevant classification metrics.
* **SHAP Explainability:** The project uses SHAP values to provide insights into the feature importance for each disease prediction. This helps in understanding which factors contribute most to the model's output.

## Technical Details

The project is implemented in a Python notebook and utilizes the following main libraries:

* **numpy:** For numerical computations.
* **scikit-learn:** For machine learning algorithms, model evaluation, and data preprocessing.
* **pandas:** For data manipulation and analysis.
* **scipy:** For scientific and technical computing.
* **matplotlib:** For data visualization.
* **tensorflow:** For building and training neural network models.
* **tensorflow-addons:** For additional tensorflow functionalities.
* **shap:** For explaining the output of machine learning models.
* **notebook:** For running the jupyter notebook.

## Requirements

* Python 3.x
* The required packages can be installed using the following command:

    ```bash
    pip install --prefer-binary --upgrade -r requirements.txt
    ```

## Usage

1.  Clone the repository.
2.  Install the required packages using the command provided in the "Requirements" section.
3.  Open and run the `Stratified_CV_SHAP_MultiDisease_Model (2).ipynb` notebook in a Jupyter environment.

The notebook will:

1.  Train separate models for CKD, Heart, and Diabetes using Stratified K-Fold.
2.  Evaluate each model.
3.  Apply SHAP explainability on Fold 1 of each task to understand feature contributions.

## Project Structure

* `Stratified_CV_SHAP_MultiDisease_Model.ipynb`: The main Jupyter Notebook containing the code for data loading, preprocessing, model training, evaluation, and explanation.
* `requirements.txt`: A text file listing the Python packages required to run the project.

## Contributions

Contributions are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.


