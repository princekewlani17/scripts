#! /usr/bin/env python3

from aws_session import AwsSession

aws = AwsSession(profile='princekewlani')


def lambda_handler(event, context):
    try:

        ssm = aws.get(service='ssm')
        response = ssm.get_parameter(
                        Name=event.get("param"),
                        WithDecryption=True
                    )

    except ssm.exceptions.ParameterNotFound as err:

        msg = f"Error: Parameter {event.get('param')} not found"
        return {
            "StatusCode": 500,
            "ErrorMessage": msg,
            "VerboseError": err
        }

    return response["Parameter"]["Value"]

print(
    lambda_handler(
        event={"param": "test"},
        context=object()
    )
)
