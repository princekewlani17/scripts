#! /usr/bin/env python3

# System Lib Imports
import os
import sys

# Third part lib imports
import boto3
import botocore.exceptions


class AwsSession:

    def __init__(
            self,
            region: str = os.getenv('AWS_DEFAULT_REGION', ''),
            profile: str = os.getenv('AWS_DEFAULT_PROFILE', ''),
            ):
        
        self.region = region
        self.profile = profile
        self.exceptions = botocore.exceptions

    def get(
            self,
            service
            ):
        
        if self.profile:
            print(f"Using aws profile: {self.profile}\n")

            return boto3.session.Session(profile_name=self.profile).client(service_name=service)

        if not self.region:

            print(ValueError("AWS_DEFAULT_REGION is not configured"))
            sys.exit(1)
                    
        print("Using aws default profile\n")
        return boto3.session.Session().client(service_name=service)
