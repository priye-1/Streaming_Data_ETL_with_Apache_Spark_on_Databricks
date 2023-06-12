import os
import json
import datetime
import pandas as pd
from json import dumps
from get_data import (
    get_stock_data
)

# load environment variable
AWS_BUCKET = "stocks-data-spark-stream-bucket"
AWS_ACCESS = os.getenv("AWS_KEY_ID")
AWS_SECRET = os.getenv("AWS_SECRET_KEY")


def stock_scraper_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy
        -integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    """

    stock_data_json = get_stock_data()

    stock_df = pd.DataFrame(stock_data_json)

    current_datetime = datetime.datetime.now()

    file_date = current_datetime.strftime("%Y-%m-%d:%H-%M-%S")

    stock_df.to_csv(

            f"s3://{AWS_BUCKET}/stocks_{file_date}.csv",
            index=False,
            storage_options={
                "key": AWS_ACCESS,
                "secret": AWS_SECRET,
            },
        )

    return {
        "statusCode": 200,
        "data": stock_data_json[0:5],
        "body": json.dumps({
            "message": "Data uploaded to S3"
        }),
    }
