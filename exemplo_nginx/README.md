# Exemplo Simples com Docker e Nginx

Este exemplo demonstra como executar um servidor web Nginx básico usando Docker.

## Instruções

### 1. Baixar a Imagem do Nginx

Primeiro, baixe a imagem oficial do Nginx do Docker Hub:

```bash
docker pull nginx
```

### 2. Executar o Contêiner Nginx

Agora, execute um contêiner a partir da imagem baixada. Vamos nomeá-lo como `meu-web`, executá-lo em segundo plano (`-d`) e mapear a porta 8080 do seu computador para a porta 80 dentro do contêiner (`-p 8080:80`):

```bash
docker run --name meu-web -d -p 8080:80 nginx
```

### 3. Acessar o Nginx no Navegador

Abra seu navegador e acesse [http://localhost:8080](http://localhost:8080). Você deverá ver a página de boas-vindas padrão do Nginx ("Welcome to nginx!").

### 4. Listar Contêineres em Execução

Para ver o contêiner `meu-web` em execução, use o comando:

```bash
docker ps
```

Você verá informações sobre o contêiner, incluindo seu ID, imagem, comando, status e portas.

### 5. Parar o Contêiner

Quando terminar, você pode parar o contêiner usando o nome que definimos:

```bash
docker stop meu-web
```

### 6. Remover o Contêiner (Opcional)

Após parar o contêiner, você pode removê-lo se não precisar mais dele:

```bash
docker rm meu-web
```

Isso conclui o exemplo básico de uso do Nginx com Docker.