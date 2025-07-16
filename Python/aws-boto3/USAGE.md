# Example Usage:


1. Using profile

```sh
$ cat *.py # script
```
```python3
    from aws_session import AwsSession

    aws = AwsSession(profile=profile_name)
    aws.get(service='s3').boto3_api_call(**args)

```



2. Exporting default
```sh
bash export AWS_DEFAULT_PROFILE=profile_name
```
`or`
```sh
bash aws configure
```
```sh
$cat *.py # script
```
```python3
    from aws_session import AwsSession

    aws = AwsSession()
    aws.get(service='s3').boto3_api_call(**args)
```