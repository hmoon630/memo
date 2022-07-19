from fastapi import FastAPI, Response
from boto3 import client
from botocore.exceptions import ClientError
import requests

sts_client = client("sts")
s3_client = client("s3")

app = FastAPI()


def create_presigned_url(bucket_name, object_name, exp=3600):
    try:
        response = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": bucket_name, "Key": object_name},
            ExpiresIn=exp,
        )
    except ClientError as e:
        print(e)
        return None

    return response


def create_presigned_post(
    bucket_name, object_name, fields=None, conditions=None, exp=3600
):
    try:
        response = s3_client.generate_presigned_post(
            bucket_name,
            object_name,
            Fields=fields,
            Conditions=conditions,
            ExpiresIn=exp,
        )
    except ClientError as e:
        print(e)
        return None

    return response


@app.get("/")
def hello(http_res: Response):
    response = create_presigned_post("hmoon-bucket", "testfile", exp=60)
    print(response["url"])

    with open("C:\\Users\\hmoon\\testfile", "rb") as f:
        files = {"file": ("testfile", f)}
        response = requests.post(response["url"], data=response["fields"], files=files)
        print(response)

    http_res.status_code = 200
    return "hello"
