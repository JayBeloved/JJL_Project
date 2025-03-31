import boto3
s3 = boto3.client('s3',
                aws_access_key_id='YOUR_ACCESS_KEY',
                aws_secret_access_key='YOUR_SECRET_KEY',
                region_name='us-east-2')
response = s3.list_objects_v2(Bucket='jjlpitch-deck-ppics')
print(response)