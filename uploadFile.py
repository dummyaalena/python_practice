import boto3

s3 = boto3.resource('s3')

bucket = s3.Bucket('alina-bucket')
bucket.upload_file('test.txt','file.txt')
