
# TODO implement
import boto3
import time
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'sourcebkthula',
        'Key': 'test.txt'
    }
    tbname='sourcebkthula'+time.strftime("%H%M%S")
    s3.create_bucket(Bucket=tbname, CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
    bucket = s3.Bucket(tbname)
    bucket.copy(copy_source, 'test_backup.txt')
    return { 
    'message' : 'File copied successfully'
    } 
