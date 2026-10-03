import types

from functions.identity.issue_token import lambda_handler


def test_lambda_handler_returns_hello_body():
    result = lambda_handler({"request": "token"}, None)

    assert result == {"body": "Hello from AWS Lambda!"}


def test_lambda_handler_ignores_event_contents():
    event = {
        "resource": "/token",
        "httpMethod": "POST",
        "body": '{"scope": "openid"}',
    }
    context = types.SimpleNamespace(
        function_name="issue-token",
        aws_request_id="req-1",
    )

    result = lambda_handler(event, context)

    assert result["body"] == "Hello from AWS Lambda!"


def test_lambda_handler_accepts_empty_event():
    result = lambda_handler({}, None)

    assert result == {"body": "Hello from AWS Lambda!"}


def test_lambda_handler_prints_the_event(capsys):
    event = {"user": "ada"}

    lambda_handler(event, None)

    captured = capsys.readouterr()
    assert "Issue token request:" in captured.out
    assert "ada" in captured.out
