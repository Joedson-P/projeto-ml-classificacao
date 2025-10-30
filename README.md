# Projeto ML: Classificação de Subscrição de Depósito Bancário

## Visão Geral do Projeto

Este projeto de Machine Learning se concentra na construção e otimização de modelos de classificação para prever a probabilidade de um cliente de uma instituição bancária portuguesa **assinar um depósito a prazo**. O foco principal é a otimização da métrica de negócio **Recall** (captação de clientes 'yes').

## Objetivos Concluídos

1.  **Pré-Processamento Rigoroso:** Realizado com Engenharia de Features, tratamento de 'unknowns' e criação de um **Pipeline (ColumnTransformer)** utilizando Classes Customizadas (POO) para garantir reprodutibilidade.
2.  **Modelagem e Otimização:** Implementação e comparação de modelos **Regressão Logística** (Baseline) e **Random Forest**.
3.  **Validação Estratégica:** Otimização de limiar (threshold) para maximizar o Recall da classe minoritária ('yes').

## Modelo Vencedor: Random Forest Otimizado

O modelo Random Forest Otimizado foi o vencedor, superando o Recall de 50% da *baseline* Logística.

| Métrica | Logística Otimizada (Baseline) | Random Forest Otimizado |
| :--- | :--- | :--- |
| **AUC-ROC** | $0.8909$ | **$0.9278$** |
| **Recall (Classe 'yes')** | $0.50$ | **$0.60$** |
| **Precisão (Classe 'yes')**| $0.57$ | **$0.57$** |
| **Limiar Utilizado** | $0.2912$ | **$0.3333$** |

### Insights de Negócio

* O modelo final garante $\mathbf{60\%}$ de captação dos clientes que subscreveriam, um aumento de $\mathbf{10}$ pontos percentuais em relação à *baseline*.
* As *features* mais relevantes para a predição são: **Duração da Última Chamada (duration - *com ressalvas sobre vazamento de dados*)**, **Balanço Anual (balance)**, e **Idade (age)**.

## 💾 Dataset

O conjunto de dados utilizado é referente a campanhas de *marketing* direto de uma instituição bancária.

* **Fonte:** [Conjunto de Dados de Marketing Bancário no Kaggle](https://www.kaggle.com/datasets/dharmik34/bank-term-deposit-subscription?resource=download)