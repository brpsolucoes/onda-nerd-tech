# Define o prefixo de comando padrão para todos os alvos
POETRY_RUN := poetry run

# Define o nome do arquivo de gerenciamento Django
MANAGE_PY := manage.py

# ==============================================================================
# Alvos Comuns
# ==============================================================================

.PHONY: help install runserver makemigrations migrate createsuperuser test shell coverage clean

help:
	@echo "Comandos Django comuns com Poetry:"
	@echo ""
	@echo "  make install        - Instala as dependências usando Poetry"
	@echo "  make runserver      - Inicia o servidor de desenvolvimento Django"
	@echo "  make makemigrations - Cria novas migrações"
	@echo "  make migrate        - Aplica as migrações no banco de dados"
	@echo "  make createsuperuser- Cria um superusuário interativamente"
	@echo "  make test           - Executa os testes do projeto"
	@echo "  make shell          - Abre o shell interativo do Django"
	@echo "  make coverage       - Executa os testes com relatório de cobertura (se 'coverage' estiver instalado)"
	@echo "  make clean          - Remove arquivos de cache e bytecode"

# ------------------------------------------------------------------------------
# Gerenciamento de Dependências
# ------------------------------------------------------------------------------

install:
	@echo "Instalando dependências com Poetry..."
	test -f .env || cp .env.example .env
	poetry install

# ------------------------------------------------------------------------------
# Comandos Django
# ------------------------------------------------------------------------------

runserver:
	@echo "Iniciando o servidor de desenvolvimento..."
	$(POETRY_RUN) python $(MANAGE_PY) runserver

makemigrations:
	@echo "Criando migrações..."
	$(POETRY_RUN) python $(MANAGE_PY) makemigrations

migrate:
	@echo "Aplicando migrações..."
	$(POETRY_RUN) python $(MANAGE_PY) migrate

createsuperuser:
	@echo "Criando superusuário..."
	$(POETRY_RUN) python $(MANAGE_PY) createsuperuser

test:
	@echo "Executando testes..."
	$(POETRY_RUN) python $(MANAGE_PY) test

shell:
	@echo "Abrindo o shell do Django..."
	$(POETRY_RUN) python $(MANAGE_PY) shell

# ------------------------------------------------------------------------------
# Outros Comandos Úteis
# ------------------------------------------------------------------------------

coverage:
	@echo "Executando testes com cobertura..."
	$(POETRY_RUN) coverage run $(MANAGE_PY) test
	@echo "Gerando relatório de cobertura..."
	$(POETRY_RUN) coverage report -m

clean:
	@echo "Limpando arquivos de cache e bytecode..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete