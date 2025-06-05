# pypro/storage_backends.py
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

class R2StaticStorage(S3Boto3Storage):
    # Nome do bucket (definido em settings.py)
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME

    # O ENDPOINT URL do Cloudflare R2 é crucial aqui
    endpoint_url = settings.AWS_S3_ENDPOINT_URL

    # Define a ACL padrão para 'public-read' se os arquivos forem públicos
    default_acl = 'public-read'

    # Desabilita autenticação via query string para acesso público mais limpo
    querystring_auth = False

    # Define a política de sobrescrita de arquivos
    file_overwrite = False # Ou True, dependendo do seu caso de uso

    # Parâmetros de objeto S3, útil para Cache-Control
    object_parameters = {
        'CacheControl': 'max-age=86400', # 1 dia de cache
    }

    # Se os arquivos estáticos forem sempre públicos e acessados diretamente,
    # você pode definir location para o subdiretório 'static'
    # location = 'static' # Opcional, dependendo da sua estrutura de bucket

class R2MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    endpoint_url = settings.AWS_S3_ENDPOINT_URL
    default_acl = 'public-read' # ou 'private' se não forem públicos
    querystring_auth = False
    file_overwrite = False
    object_parameters = {
        'CacheControl': 'max-age=86400',
    }
    # location = 'media' # Opcional