"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.BucketV2('pk-pulumi-bucket')

versioning = s3.BucketVersioningV2(
            'bucket-versioning',
            bucket=bucket.id,
            versioning_configuration=s3.BucketVersioningV2VersioningConfigurationArgs(
                status='Enabled'
            )
        )

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('versioning_status', versioning.versioning_configuration.status)


