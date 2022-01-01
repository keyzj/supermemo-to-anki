def check_response(success_code, code, response, action):
    assert code == success_code, f"{action} failed, response: code={code}, content={response.content}"
