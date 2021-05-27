
url = "www.google.com"


def test_req_module_context(req_module_context):
    print(req_module_context)
    assert req_module_context == url
