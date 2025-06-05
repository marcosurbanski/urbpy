from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from django.core.files.storage import default_storage
from pathlib import Path

class Command(BaseCommand):
    help = 'Alternative collectstatic for R2'

    def handle(self, *args, **options):
        # Coleta os arquivos localmente primeiro
        call_command('collectstatic', '--no-input', '--clear')
        
        # Faz upload manual para o R2
        static_root = Path(settings.STATIC_ROOT)
        uploaded = 0
        
        for file_path in static_root.glob('**/*'):
            if file_path.is_file():
                relative_path = file_path.relative_to(static_root)
                with file_path.open('rb') as f:
                    default_storage.save(f'static/{relative_path}', f)
                uploaded += 1
                self.stdout.write(f'Uploaded: static/{relative_path}')
        
        self.stdout.write(f'✅ {uploaded} arquivos enviados para o R2')