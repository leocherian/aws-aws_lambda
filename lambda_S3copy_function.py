# TODO implement
import boto3
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    copy_source = {
        'Bucket': 'sourcebkthula',
        'Key': 'test.txt'
    }
    bucket = s3.Bucket('destinationbkthula')
    bucket.copy(copy_source, 'test_backup.txt')
    return { 
    'message' : 'File copied successfully'
    } 
