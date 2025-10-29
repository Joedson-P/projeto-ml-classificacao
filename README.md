# 🏦 Projeto ML: Classificação de Subscrição de Depósito Bancário

## Visão Geral do Projeto

Este projeto de Machine Learning se concentra na construção e otimização de um modelo de classificação para prever a probabilidade de um cliente de uma instituição bancária portuguesa **subscrever (assinar) um depósito a prazo**. O foco inicial é na implementação de um *baseline* robusto.

## 🎯 Objetivos

1.  **Pré-Processamento Rigoroso:** Realizar a Engenharia de Features, tratando variáveis categóricas, valores ausentes ('unknown') e realizando o escalonamento de dados.
2.  **Modelagem Baseline:** Implementar um modelo de **Regressão Logística** como ponto de partida.
3.  **Validação Estratégica:** Validar o modelo com foco em métricas de negócio (Recall e AUC), dada a presença de **desbalanceamento de classes** (88% 'no' vs. 12% 'yes').
4.  **Otimização de Limiar (Threshold):** Ajustar o limiar de decisão para maximizar o Recall (taxa de captação de clientes 'yes').

## 💾 Dataset

O conjunto de dados utilizado é referente a campanhas de *marketing* direto de uma instituição bancária, baseadas em chamadas telefônicas.

* **Fonte:** [Conjunto de Dados de Marketing Bancário no Kaggle](https://www.kaggle.com/datasets/dharmik34/bank-term-deposit-subscription?resource=download)

---
*Este README é uma versão inicial. Será atualizado com os resultados e a conclusão após a implementação de modelos mais avançados.*