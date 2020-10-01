from urllib import response

if response.status_code == 200:
    return json.loads(response.content.decode("utf-8"))
else:
    return None
