#http://boto3.readthedocs.io/en/latest/guide/migrations3.html for creating bucket
import boto3

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# s3.create_bucket(Bucket='alina-bucket',CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

print("After Creation")

for bucket in s3.buckets.all():
    print(bucket.name)
