Aqui está um modelo completo, profissional e direto ao ponto para o seu `README.md`. Ele foi desenhado para impressionar seu professor, explicando a arquitetura híbrida (Python + Hop), o banco de dados na nuvem e, o mais importante, como rodar o projeto com um único comando via Docker.

Basta copiar o conteúdo abaixo e colar no seu arquivo `README.md` na raiz do projeto.

---

# 🚀 Projeto Data Warehouse Olist - ETL Híbrido com Apache Hop e Python

Este projeto implementa um pipeline de dados ponta a ponta (ETL) para popular um Data Warehouse baseado no dataset público de e-commerce da Olist.

A arquitetura utiliza **Apache Hop** como principal motor de orquestração e integração de dados, **Python** para transformações específicas (geração da dimensão de tempo) e **PostgreSQL** hospedado na nuvem (Supabase) como destino final (Data Warehouse). Para garantir a reprodutibilidade em qualquer sistema operacional, todo o ambiente de execução foi empacotado usando **Docker**.

## 🛠️ Tecnologias Utilizadas

* **Apache Hop Web:** Orquestração e fluxos de dados (Pipelines e Workflows).
* **Python:** Pré-processamento e engenharia de features para geração da Dimensão de Tempo (`dim_time`).
* **Docker:** Containerização do ambiente (Apache Hop + Python embutido).
* **PostgreSQL (Supabase):** Banco de dados em nuvem atuando como Data Warehouse.

## 📂 Estrutura do Projeto

O projeto está organizado de forma a separar dados brutos, scripts de processamento e fluxos do Apache Hop:

```text
/
├── docker-compose.yml       # Orquestrador do container Apache Hop Web
├── Dockerfile               # Imagem customizada do Hop instalando Python e dependências
├── requirements.txt         # Bibliotecas Python (ex: pandas, numpy)
├── README.md                # Documentação do projeto
│
├── scripts/                 
│   ├── gerar_dim_tempo.py   # Script Python que gera o CSV da dim_time
│   └── run_python_etl.sh    # Shell script que executa o Python via Hop
│
├── dados/                   
│   └── *.csv                # Arquivos CSV originais da Olist + dim_time.csv (gerado)
│
└── hop_project/             
    ├── wf_master.hwf        # Workflow principal (Orquestrador)
    ├── wf_dimensoes.hwf     # Workflow de carga das Dimensões
    ├── wf_fato.hwf          # Workflow de carga da tabela Fato
    └── *.hpl                # Pipelines de ingestão individuais

```

## ⚙️ Como Executar (Ambiente Dockerizado)

Graças ao Docker, não é necessário instalar o Apache Hop, configurar o Python localmente ou ajustar caminhos de pastas. Todo o diretório do projeto é mapeado automaticamente para `/opt/olist_pipeline/` dentro do container.

### Pré-requisitos

* **Docker** e **Docker Compose** instalados na máquina.
* Conexão com a internet (para baixar a imagem do Hop, instalar pacotes e comunicar-se com o Supabase).

### Passo a Passo

1. **Inicie o ambiente:**
Abra o terminal na raiz do projeto e execute o comando abaixo para construir a imagem customizada e subir o serviço em segundo plano:
```bash
docker-compose up -d --build

```


2. **Acesse o Apache Hop Web:**
Abra o seu navegador e acesse:
[http://localhost:8080](https://www.google.com/search?q=http://localhost:8080)
3. **Execute o Pipeline:**
* Na interface do Apache Hop, clique no ícone de pasta (Open) no canto superior esquerdo.
* Navegue até o diretório: `/opt/olist_pipeline/hop_project/`
* Abra o arquivo **`workflow_principal.hwf`**.
* Clique no botão de "Play" (Run) no topo da tela.



## 🧠 Lógica de Orquestração (Workflow Master)

O `wf_master.hwf` garante o princípio de integridade referencial do Data Warehouse, executando os passos na seguinte ordem estrita:

1. **Carga das Dimensões (`workflow_dimensoes.hwf`):** * Inicia acionando um nó **Shell** que executa o script Python (`build_dim_time.sh`). O Python lê as datas do dataset, trata os formatos temporais e gera um CSV atualizado para a dimensão de tempo.
* Em seguida, os pipelines (`.hpl`) carregam simultaneamente/sequencialmente as tabelas `dim_time`, `dim_cliente`, `dim_vendedor`, etc., direto no banco de dados.


2. **Carga da Fato (`workflow_fato.hwf`):**
* Só é acionado mediante **100% de sucesso** do workflow anterior.
* Faz a leitura das tabelas de itens e pedidos cruzando as chaves estrangeiras (Lookup) com os dados das dimensões recém-carregadas.



## ⚠️ Notas Importantes

* **Banco de Dados em Nuvem:** O Data Warehouse está hospedado no Supabase. Não há container de banco de dados rodando localmente.
* **Caminhos Absolutos:** Todas as chamadas de arquivo dentro do Hop (tanto para leitura de CSVs quanto chamadas de scripts) utilizam o path absoluto `/opt/olist_pipeline/...` para garantir estabilidade cross-platform (Windows/Mac/Linux).