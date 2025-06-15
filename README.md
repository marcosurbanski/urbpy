# 🚀 curso-django

Código desenvolvido durante o módulo de Django do [Python Pro](https://www.python.pro.br).  
Esta aplicação está em constante evolução, explorando tecnologias modernas como Cloudflare R2, Highlight.io, e estratégias de produção otimizadas com Django 5.2.

🔗 **Aplicação disponível em produção:**  
👉 https://www.urbpy.com.br


📦 CI/CD e Qualidade
GitHub Actions: Integração contínua

Codecov: Análise de cobertura de testes

Dependabot: Atualização automática de dependências


[![GitHub Actions](https://github.com/urbanstech/curso-django/actions/workflows/ci.yml/badge.svg)](https://github.com)
[![Dependabot enabled](https://img.shields.io/badge/dependabot-enabled-brightgreen?logo=dependabot)](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically)
[![codecov](https://codecov.io/gh/urbanstech/curso-django/graph/badge.svg?token=HYP8ygr5dO)](https://codecov.io/gh/urbanstech/curso-django)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue?logo=python)]

---

## 🧰 Tecnologias utilizadas

- Django 5.2
- Python 3.10+
- PostgreSQL
- Cloudflare R2 (armazenamento de arquivos)
- Highlight.io (observabilidade)
- Collectfast + Boto3
- GitHub Actions (CI)
- Codecov (cobertura de testes)
- Django Debug Toolbar (modo dev)
- **Pipenv** (gerenciador de pacotes e ambientes)

---

## 🚀 Como rodar o projeto localmente

```bash
# 1. Clone o repositório
git clone https://github.com/urbanstech/curso-django.git
cd curso-django

# 2. Instale o ambiente com o pipenv
pipenv install --dev

# 3. Ative o shell virtual
pipenv shell

# 4. Copie o arquivo de exemplo de ambiente
cp .env.example .env

# 5. Altere o .env com suas credenciais

# 6. Execute as migrações e o servidor
python manage.py migrate
python manage.py runserver
```

✅ Testes
```bash
# Execute os testes com cobertura
pipenv run pytest --cov=.
```


📂 Estrutura de pastas

```text
curso-django/
├── pypro/              # Projeto Django
│   ├── base/           # App principal
│   └── settings.py
├── staticfiles/        # Arquivos estáticos coletados
├── mediafiles/         # Uploads (modo local)
├── templates/          # Templates HTML
├── Pipfile             # Dependências com Pipenv
├── Pipfile.lock
├── .env.example
└── manage.py
```

🧪 Variáveis de ambiente
Configure as variáveis com base no arquivo .env.example.
Aqui estão algumas importantes:

| Variável              | Descrição                                 |
|-----------------------|--------------------------------------------|
| `SECRET_KEY`          | Chave secreta do Django                    |
| `DEBUG`               | Ativa/desativa modo debug                  |
| `DATABASE_URL`        | URL de conexão com o banco de dados        |
| `CLOUDFLARE_R2_*`     | Configurações da Cloudflare R2             |
| `COLLECTFAST_ENABLED` | Ativa o uso do Collectfast com boto3       |
| `HIGHLIGHT_*`         | Configurações do Highlight.io              |



