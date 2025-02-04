# AWS Lambda - Gerador de URLs Pré-assinadas para S3

## 👨‍💻 Projeto desenvolvido por: 
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* 📚 Contextualização do projeto
* 🛠️ Tecnologias/Ferramentas utilizadas
* 🖥️ Funcionamento do sistema
* 🔀 Arquitetura da aplicação
* 📁 Estrutura do projeto
* 📌 Como executar o projeto
* 🕵️ Dificuldades Encontradas

## 📚 Contextualização do projeto

O projeto tem como objetivo criar uma solução automatizada para gerar **URLs pré-assinadas** para download de arquivos armazenados no **Amazon S3**. A aplicação utiliza **AWS SDK (Boto3)** para interagir com os serviços da AWS e gerar URLs temporárias que permitem o acesso seguro aos arquivos.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/Dotenv-ECD53F?logo=dotenv&logoColor=white">](https://pypi.org/project/python-dotenv/)

## 🖥️ Funcionamento do sistema

A aplicação é composta por uma função Lambda que gera URLs pré-assinadas para arquivos armazenados no S3. A função é acionada por eventos e utiliza a classe S3BucketClass para interagir com o S3.

* **Lambda Handler**: O arquivo lambda_handler.py contém a função Lambda que processa os eventos e gera as URLs pré-assinadas.
* **Serviços AWS**: A integração com o S3 é realizada pela classe S3BucketClass localizada em s3bucket_service.py.
* **Utilitários**: A pasta utils contém funções para importação de credenciais AWS e verificação de credenciais.

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura serverless utilizando AWS Lambda para gerar URLs pré-assinadas. A função Lambda interage com o S3 para realizar operações como upload, download, e geração de URLs pré-assinadas.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── services/
│   ├── __pycache__/
│   └── s3bucket_service.py
├── utils/
│   ├── __pycache__/
│   ├── check_aws.py
│   └── import_credentials.py
├── .env
├── .env.example
├── .gitignore
├── files/
├── lambda_handler.py
└── readme.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo .env baseado no .env.example e adicione suas credenciais AWS.

4. **Execute a função Lambda localmente:**
   ```bash
   python lambda_handler.py
   ```

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Configuração de credenciais AWS:** Garantir que as credenciais AWS estejam corretamente configuradas e seguras.
- **Gerenciamento de erros:** Lidar com exceções e erros ao interagir com o S3, garantindo que a aplicação seja robusta e confiável.