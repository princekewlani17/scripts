#! /usr/bin/env python3

# System Lib Imports
import os

# Third part lib imports
import boto3
import botocore.exceptions


class AwsSession:

    def __init__(
            self,
            profile: str = os.getenv('AWS_DEFAULT_PROFILE', ''),
            ):
        self.profile = profile
        self.exceptions = botocore.exceptions

    def get(
            self,
            service
            ):
        if self.profile:
            print(f"Using aws profile: {self.profile}\n")
            return boto3.session.Session(profile_name=self.profile).client(service_name=service)
        print("Using aws default profile\n")
        return boto3.session.Session().client(service_name=service)
