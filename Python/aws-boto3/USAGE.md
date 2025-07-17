# Example Usage:


1. Using profile

```sh
$ cat *.py # script
```
```python3
    from aws_session import AwsSession

    aws = AwsSession(profile=profile_name,
                     region=region_name)
    aws.get(service='s3').boto3_api_call(**args)

```



2. Exporting default
```sh
export AWS_DEFAULT_PROFILE=profile_name
export AWS_DEFAULT_REGION=region_name

```
`or`
```sh
aws configure
```
```sh
$cat *.py # script
```
```python3
    from aws_session import AwsSession

    aws = AwsSession()
    aws.get(service='s3').boto3_api_call(**args)
```