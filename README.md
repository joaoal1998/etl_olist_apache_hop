# Etapa 1: Modelagem Dimensional

## 1.1. Modelo Dimensional de Alto Nível

### 1.1.1. Escopo do Projeto

O escopo desta fase consiste na transformação dos dados brutos da Olist, que originalmente operam em um modelo relacional transacional, em uma arquitetura de dados orientada a análises (OLAP). O trabalho abrange o desenho arquitetural de um modelo dimensional no formato **Star Schema**.

O objetivo central é reestruturar as tabelas normalizadas de pedidos, itens, produtos, clientes e vendedores em um esquema focado em maximizar a performance analítica de leitura. O escopo encerra-se com o planejamento para a implementação física deste Data Warehouse em um banco de dados **PostgreSQL** hospedado na nuvem via plataforma **Supabase**.

---

### 1.1.2. Granularidade da Tabela de Fatos

A granularidade estabelecida para a tabela de fatos principal é do nível transacional mais detalhado:

> **1 linha = 1 item de produto vendido dentro de um pedido.**

Esta definição de grão é mandatória porque um único pedido referenciado na base original pode conter múltiplos itens distintos, associados a diferentes categorias de produtos e comercializados por diferentes vendedores.

---

### 1.1.3. Diagrama Inicial do Modelo Dimensional

[Ver diagrama inicial](Modelagem/imagem1.png)

---

## 1.2. Modelo Dimensional Detalhado

### A. Documentação Detalhada

[Ver documentação detalhada](Modelagem/Cloud%20Analytics%20com%20Olist.xlsx)

---

### B. Diagrama Entidade-Relacionamento (DER)

[Ver DER](Modelagem/imagem2.png)


# Etapa 2: Pipeline de ETL (Local para Nuvem) com Apache Hop

## DDL

[ddl.sql](ETL/DDL/ddl.sql)

---

## Pipelines Apache Hop

### Dimensões

[dim_customers.hpl](ETL/hop_project/dim_customers.hpl) | [dim_items.hpl](ETL/hop_project/dim_items.hpl) | [dim_order_payments.hpl](ETL/hop_project/dim_order_payments.hpl) | [dim_sellers.hpl](ETL/hop_project/dim_sellers.hpl) | [dim_time.hpl](ETL/hop_project/dim_time.hpl) | [fact.hpl](ETL/hop_project/fact.hpl)

### Workflows

[workflow_dimensoes.hwf](ETL/hop_project/workflow_dimensoes.hwf) | [workflow_fato.hwf](ETL/hop_project/workflow_fato.hwf) | [workflow_principal.hwf](ETL/hop_project/workflow_principal.hwf)

---

## Scripts Auxiliares

[build_dim_time.py](ETL/scripts/build_dim_time.py) | [build_fact.py](ETL/scripts/build_fact.py) | [Prepara_csv_dim_time.sh](ETL/scripts/Prepara_csv_dim_time.sh) | [Prepara_csv_fact.sh](ETL/scripts/Prepara_csv_fact.sh)

---

## Ambiente Docker

[docker-compose.yml](ETL/docker-compose.yml) | [Dockerfile](ETL/Dockerfile) | [requirements.txt](ETL/requirements.txt)

# Etapa 3: Visualização e Insights no Preset.io

# Etapa 3: Visualização e Insights no Preset.io

## Painel interativo (Preset.io)

[Olist - Performance Logística e Vendas](https://bd4ac460.us1a.app.preset.io/superset/dashboard/p/qvQwYvynXNM/)

O dashboard foi compartilhado com o email: italo.silva@ifal.edu.br.

---

## Relatório executivo

[Relatório Executivo Olist Detalhado.pdf](Análise%20de%20Dados/Relatório%20Executivo%20Olist%20Detalhado.pdf)

O relatório consolida a análise executiva da operação Olist, destacando os principais gargalos logísticos e oportunidades de vendas identificadas.

---

## 👥 Grupo

| Nome |
|------|
| João Paulo Vieira Alves dos Santos |
| Lucas Gabryel Nascimento Santos |
| Luis Henrique Amorim da Silva |
| Malba Vinicius Lopes Santos |