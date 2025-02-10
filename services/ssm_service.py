# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #
# RUN LOCALY
from utils.check_aws import AWS_SERVICES

aws_services = AWS_SERVICES()

session = aws_services.login_session_AWS()

if not aws_services.check_aws_credentials():
    raise Exception("[DEBUG] Credenciais AWS não configuradas")
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ #

import boto3 

class SSMService:
    def __init__(self):
        self.ssm_service = session.client('ssm')
        self.HEADERS = ['S3_BUCKET_NAME', 'DYNAMODB_TABLE_NAME', 'STATE_MACHINE_ARN']

    def get_parameters(self):
    
        response = self.ssm_service.get_parameters(
            Names=[
                "/poc/s3_bucket_name",
                "/poc/dynamodb_table_name",
                "/poc/state_machine_arn"
            ],
            WithDecryption=True
        )

        parameters = {param['Name'].split('/')[-1].upper(): param['Value'] for param in response['Parameters']}
    
        print("Fetched Parameters:", parameters)
        return parameters

if __name__ == "__main__":
    ssm_service = SSMService()
    ssm_service.get_parameters()