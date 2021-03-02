# Controle-Produto-GS
Desafio for Python Full Stack Developer

## Desafio proposto:
1 - Crie um sistema Back-End, que mantém os dados de uma Entidade “Produto”. Essa entidade possui os atributos nome, descrição e valor. Esse
Back-End deve prover toda a manutenção dessa Entidade “Produto“, como incluir Produto, Remover Produto, etc.
Deve ser usada a stack Python+Django Rest Framework para a construção deste Back-End de APIs.

2 - Crie um sistema Front-End, que apresente os dados de sua Entidade Produto, da Parte 1.
Esse Front-End deve prover toda a interface gráfica para manutenção da Entidade Produto, como incluir Produto, Remover Produto etc.
Deve ser usada a stack ReactJS para a construção deste Front-End.

3 - Crie uma infraestrutura para esses sistemas, com as ferramentas Docker e Docker Compose.

Nessa infraestrutura deverão existir 3 servidores: Front-End-Server, Back-End-Server e DB-Server.

No servidor Back-End-Server deve ser instalado o sistema da Parte 1.

No servidor Front-End-Server deve ser instalado o sistema da Parte 2.

No servidor DB-Server deve ser instalado o banco de dados dos sistemas.

O Banco de Dados deve ser PostgreSQL ou MySQL.

Crie um README.md com instruções para instalação e inicialização dos sistemas em modo desenvolvimento, ou seja, na máquina local.

# Solução - Controle de Protutos

 - A solução que foi implementada para atender tais requisitos é uma apliação web chamada Controle de Produtos.

O conjunto de funcionalidade que o Controle de Produtos disponibiliza são:
 - Controle de dados sobre produtos por meio de uma plataforma web;
 - Disponibilização de um serviço web para consumo dos dados manipulados no sistema.
 - Sistema de autenticação de usuários e controle de acesso a API.

## Tecnologias Utilizadas:
- Framework Django;
- Django Rest Framework;
- Banco de dados PostgreSQL;
- O biblioteca JavaScript de código aberto React.js;
- Containers Dockere e o orquestrador de containers, Docker Compose;

# Executando o projeto localmente

## Requisitos:
- Python3
- PIP(instalador de pacote Python padrão)
- Docker e Docker Compose

## Instalação via terminal:
1 - Faça o clone/download deste respositório para seu host;
2 - Dentro da pasta raiz do respositório crie e inicie uma Virtualenv(é uma ferramenta para criar ambientes Python isolados):

    python3 -m venv .venv
   
    . .ven/bin/activate
3- Ainda dentro da pasta raioz do respositório execute o build do docker-composed essa forma:
    
   docker-compose build
   
   docker-compose up
   
4- Acesse os links dos servidores de Frontend e Backend:
   
   http://0.0.0.0:8000/
   
   http://localhost:3000/
   
