import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Cria um superusuário automaticamente usando variáveis de ambiente"

    def handle(self, *args, **options):
        User = get_user_model()
        email = os.environ.get("DJANGO_SU_EMAIL")
        password = os.environ.get("DJANGO_SU_PASSWORD")

        if not email or not password:
            self.stderr.write("⚠️  Variáveis de ambiente DJANGO_SU_EMAIL e DJANGO_SU_PASSWORD são obrigatórias.")
            return

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Superusuário '{email}' criado com sucesso!"))
        else:
            self.stdout.write(f"ℹ️ Superusuário '{email}' já existe. Nenhuma ação realizada.")
