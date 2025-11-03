# Projeto ML: Classificação de Subscrição de Depósito Bancário

## Visão Geral do Projeto

Este projeto implementa um fluxo de trabalho completo de Machine Learning (MLOps) para prever se um cliente de uma campanha de marketing bancário irá **subscrever um depósito a prazo** ('yes'/'no').

O objetivo principal de negócio foi **maximizar o Recall** (taxa de captação) para atingir uma **meta mínima de 60%**.

O projeto utiliza um pipeline robusto, testes de unidade e o modelo **Random Forest** otimizado.

---

## Resultados Finais do Modelo Otimizado

A otimização de hiperparâmetros (via `RandomizedSearchCV`) e o ajuste de limiar foram cruciais para levar o Recall além da meta de 60%.

| Métrica | Logística Otimizada (Baseline) | RF Padrão (Limiar 0.33) | **RF FINAL Otimizado (Limiar 0.6239)** |
| :--- | :--- | :--- | :--- |
| **Recall (Captação)** | 0.50 | 0.60 | **0.65** |
| **Precision** | 0.57 | 0.57 | **0.51** |
| **AUC-ROC** | 0.8909 | 0.9278 | **0.9131** |

### Insights de Negócio:

* **Meta Superada:** O modelo final garante $\mathbf{65%}$ de captação, um aumento de **15 pontos percentuais** em relação à *baseline* (Logística Otimizada).
* **Trade-off Aceito:** A pequena redução na Precisão (de 0.57 para 0.51) é aceita, pois o ganho de 5 pontos percentuais em Recall (volume de captação) compensa o custo de contatar mais Falsos Positivos.

---

## Engenharia de Features e MLOps

O projeto está estruturado para produção, destacando as seguintes práticas de engenharia:

1.  **Pipeline Completo:** O pré-processamento é encapsulado em um `ColumnTransformer` usando **Classes Customizadas (POO)** (`BinaryMapper`, `MonthMapper`) em `src/features/`.
2.  **Otimização:** Uso do `RandomizedSearchCV` com *scoring* focado em `recall` e ajuste de limiar no *deployment*.
3.  **Serialização:** O artefato final de produção (Pré-processador + Random Forest) foi salvo como `rf_pipeline.pkl` via `joblib`.

## Testes e Qualidade de Código (CI)

A qualidade é garantida por:
* **Testes de Unidade:** Arquivos em `tests/` verificam a lógica dos `custom_transformers` usando **Pytest**.
* **Integração Contínua (CI):** O *workflow* no `.github/workflows/ci.yml` executa os testes automaticamente em todo *push* para garantir que o *build* não quebre.

## Dataset

O conjunto de dados utilizado é referente a campanhas de *marketing* direto de uma instituição bancária.

* **Fonte:** [Conjunto de Dados de Marketing Bancário no Kaggle](https://www.kaggle.com/datasets/dharmik34/bank-term-deposit-subscription?resource=download)

---

## Setup e Reprodução do Projeto

Para replicar o ambiente e a análise completa, siga os passos abaixo:

### 1. Clonar e Instalar Dependências
```bash
git clone https://github.com/Joedson-P/projeto-ml-classificacao.git
cd projeto-ml-classificacao
# Recomendado: Crie e ative um ambiente virtual (venv ou conda)
pip install -r requirements.txt
```

### 2. Fluxo de Reprodução (Notebooks)
Para reproduzir toda a análise, modelagem, otimização e serialização do modelo, execute os notebooks na sequência:

1.  **`notebooks/01_EDA_feature_engineering.ipynb`**: Carregamento, EDA e treinamento da *baseline*.
2.  **`notebooks/02_RandomForest_Performance.ipynb`**: Seleção e avaliação do modelo Random Forest.
3.  **`notebooks/3_hyperparameter_optimization.ipynb`**: Otimização do Random Forest e salvamento do artefato final (`rf_pipeline.pkl`).
