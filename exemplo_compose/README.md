
# 🚀 Projeto FastAPI + PostgreSQL com Docker Compose

Este projeto demonstra uma aplicação simples usando **FastAPI** com **PostgreSQL**, totalmente conteinerizada usando **Docker** e **Docker Compose**.

---

## 📁 Estrutura do Projeto

```
dockerfile-exemplo/
├── app/
│   ├── main.py
│   └── requirements.txt
├── logs/                  # Volume de logs
├── Dockerfile             # Dockerfile completo
├── docker-compose.yml     # Orquestração dos containers
└── .dockerignore          # Ignora arquivos desnecessários na imagem
```

---

## ⚙️ Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## ▶️ Como rodar o projeto

### 1. Subir a aplicação (construção + execução)

```bash
docker-compose up --build
```

### 2. Acessar a aplicação

Abra no navegador: [http://localhost:8000](http://localhost:8000)

### 3. Derrubar os containers

```bash
docker-compose down
```

> Use `--volumes` se quiser remover os volumes também.

---

## 🔧 Comandos úteis

### Acessar o container da aplicação:

```bash
docker-compose exec web bash
```

### Acessar o banco PostgreSQL via psql:

```bash
docker-compose exec db psql -U user -d mydatabase
```

### Visualizar logs da aplicação:

```bash
docker-compose logs -f
```

### Parar temporariamente:

```bash
docker-compose stop
```

### Subir novamente containers parados:

```bash
docker-compose start
```

---

## 🧪 Endpoints disponíveis

| Método | Endpoint       | Descrição                    |
|--------|----------------|------------------------------|
| GET    | `/`            | Retorna mensagem de boas-vindas |
| GET    | `/health`      | Endpoint de healthcheck      |

---

## 📦 Stack utilizada

- **FastAPI**
- **Uvicorn**
- **PostgreSQL**
- **Docker**
- **Docker Compose**

---
