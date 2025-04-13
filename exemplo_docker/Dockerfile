# 1. Imagem base
FROM python:3.10-slim

# 2. Metadados
LABEL maintainer="alan@example.com" \
      version="1.0" \
      description="Exemplo completo de Dockerfile com todos os comandos principais"

# 3. Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_HOME=/usr/src/app

# 4. Diretório de trabalho
WORKDIR $APP_HOME

# 5. Copiar dependências (melhora cache)
COPY app/requirements.txt .

# 6. Instalar dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# 7. Adicionar arquivos restantes
ADD app/ .

# 8. Volume para logs (ex: salvar logs da app)
VOLUME ["/app/logs"]

# 9. Porta exposta
EXPOSE 8000

# 10. Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl --fail http://localhost:8000/health || exit 1

# 11. Ponto de entrada
ENTRYPOINT ["python"]

# 12. Comando padrão
CMD ["-m", "uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
