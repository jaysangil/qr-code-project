import boto3

s3 = boto3.client('s3', aws_access_key_id='AWS_ACCESS_KEY', aws_secret_access_key='AWS_SECRET_KEY')
s3.upload_file('local_file.png', 'qr-code-2024', 'qr_codes/test.png')
