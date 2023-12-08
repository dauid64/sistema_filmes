# Sistema Filmes

![GitHub repo size](https://img.shields.io/github/repo-size/dauid64/sistema_filmes?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/dauid64/sistema_filmes?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/dauid64/sistema_filmes?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/dauid64/sistema_filmes?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/dauid64/sistema_filmes?style=for-the-badge)

<p align="center">
    <img src="https://github.com/dauid64/sistema_filmes/assets/94979678/c7e31b9c-dfc1-4f0b-a18b-643eea2bb0ad" alt="Logo da UnB">
</p>

> Sistema de gerenciamento de filmes que permite controlar os filmes já assistidos e aqueles que você gostaria de assistir.

### Requisitos

- [x] Criar um sistema de controle de filmes já assistidos.
- [x] Ele deve conter uma forma de cadastrar os filmes, cadastrar quando o filme foi assistido, e um que gostaria.
- [x] Importar uma planilha de excel com os filmes usando celery
- [x] No frontend, ter um autocomplete que lista os filmes para assim, registrar sua visualização
- [x] Um relatório com chart.js mostrando quais filmes você já assistiu, quais você ainda não e quais você gostaria.
- [x] Exportar uma planilha de excel com os filmes usando celery

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Você instalou a versão mais recente de `< Python / Docker >`
- Você tem uma máquina `< Windows / Linux / Mac >`

## ☕ Usando o Sistema Filmes

Para usar o Sistema Filmes, siga estas etapas:

* Primeiramente, você precisa acessar a pasta "dotenv_files", copiar o arquivo ".env-examples" para a mesma pasta com o nome ".env" e configurar as variáveis de ambiente conforme o exemplo fornecido.

* Execute o comando `docker-compose up --build` para iniciar os containers em sua máquina.

* Após isso, basta entrar no link http://localhost/ que estará rodando o projeto.
