#! /usr/bin/env python3

import sys
from aws_session import AwsSession

aws = AwsSession()


def lambda_handler(event, context):
    try:
       return aws.get(service="sts").get_caller_identity().get("Account")
    except aws.exceptions.NoCredentialsError:
        print("Error: No credentials configured")
        sys.exit(1)
    except Exception as err:
        print(f"Error: {err}")

print(f"whoami: {lambda_handler(event={}, context=object())}")
