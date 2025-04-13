
# 🐳 Projeto FastAPI com Dockerfile Completo

Este projeto é uma aplicação FastAPI que demonstra o uso **completo dos principais comandos do Dockerfile**, sem utilizar `docker-compose`.

---

## 📁 Estrutura do Projeto

```
dockerfile-exemplo/
├── app/
│   ├── main.py
│   └── requirements.txt
├── logs/                  # Diretório montado via VOLUME
├── Dockerfile             # Dockerfile com todos os comandos principais
└── .dockerignore          # Ignora arquivos desnecessários na imagem
```

---

## ⚙️ Pré-requisitos

- [Docker](https://www.docker.com/)

---

## ▶️ Como rodar o projeto

### 1. Construir a imagem

```bash
docker build -t fastapi-completo .
```

### 2. Rodar o container

```bash
docker run -p 8000:8000 fastapi-completo
```

### 3. Acessar a aplicação

Abra no navegador: [http://localhost:8000](http://localhost:8000)

---

## 🔧 Comandos úteis

### Verificar status de healthcheck:

```bash
docker inspect --format='{{json .State.Health}}' <container_id>
```

### Acessar o container:

```bash
docker exec -it <container_id> bash
```

### Parar o container:

```bash
docker stop <container_id>
```

### Remover o container:

```bash
docker rm <container_id>
```

---

## ✅ Comandos usados no Dockerfile

| Comando      | Função                                              |
|--------------|-----------------------------------------------------|
| `FROM`       | Define a imagem base                                |
| `LABEL`      | Adiciona metadados                                  |
| `ENV`        | Define variáveis de ambiente                        |
| `WORKDIR`    | Define o diretório de trabalho                      |
| `COPY`       | Copia arquivos para o container                     |
| `RUN`        | Executa comandos durante o build                    |
| `ADD`        | Adiciona arquivos (com suporte a descompactação)    |
| `VOLUME`     | Define volumes compartilhados                       |
| `EXPOSE`     | Informa a porta exposta (documentação)              |
| `HEALTHCHECK`| Verifica se o app está rodando corretamente         |
| `ENTRYPOINT` | Define o processo principal do container            |
| `CMD`        | Define o comando padrão a ser executado             |

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
- **Docker**

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
