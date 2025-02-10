import os
import json
import uuid
from dotenv import load_dotenv

# Importar a classe S3BucketClass do arquivo services/s3bucket_service.py
from services.s3bucket_service import S3BucketClass
from services.ssm_service import SSMService

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém o nome do bucket S3 do arquivo .env
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# ----------------------------------------------------------------------------
# Função Lambda que gera uma URL de download temporária para um arquivo no S3
# ----------------------------------------------------------------------------
def lambda_handler(event, context):

    try: 
        # 1 - Imprimir o evento recebido
        print('*********** Start Lambda ***************')
        print(f'[DEBUG] Event: {event}')

        # 2 - Gerar um nome único para o arquivo
        unique_filename = str(uuid.uuid4())
        download_filename = f"{unique_filename}.zip"
        print(f'[DEBUG] Download filename: {download_filename}')

        # 3 - Inicializar a classe SSMService
        ssm = SSMService().get_parameters()
        print(f'[DEBUG] Parâmetros SSM: {ssm}')

        # 3 - Inicializar a classe S3BucketClass
        s3_services = S3BucketClass()

        # 4 - Criar uma URL POST presignada para upload de arquivo
        presigned_url_post = s3_services.create_presigned_post(S3_BUCKET_NAME, download_filename)
        print(f'[DEBUG] Presigned POST URL {presigned_url_post} gerada com sucesso')

        # +- Dps de testar, deve-ser removido (TESTE) -+
        # s3_services.upload_file(bucket=S3_BUCKET_NAME, key=download_filename, file_path='./files/zipped_files.zip')
        # print(f'[DEBUG] Arquivo {download_filename} enviado para o S3')
        # +- Dps de testar, deve-ser removido (TESTE) -+

        # 5 - Gerar a URL de download temporária
        presigned_url = s3_services.generate_presigned_url(S3_BUCKET_NAME, download_filename)
        print(f'[DEBUG] Presigned URL: {presigned_url[:40]}')

        # 6 - Retornar a URL de download temporária
        return {
            'statusCode': 200,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({'unique_id' : unique_filename, 'presigned_url' : presigned_url, 'presigned_post_url' : presigned_url_post})
        }

    except Exception as e:
        print(f'[ERROR] {e}')
        return {
            'statusCode': 500,
            'headers': { 'Content-Type': 'application/json' },
            'body': json.dumps({'error': str(e)})
        }
        
print(lambda_handler(None, None))