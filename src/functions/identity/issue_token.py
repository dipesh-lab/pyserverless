from com.neauron.utils.env_vars import EnvVars


def handler(event, context):
    print("Issue token request:", event)
    print(f"Lambda region {EnvVars().get_req_env("AWS_REGION")}")
    return {
        "body": "Hello from AWS Lambda!"
    }

