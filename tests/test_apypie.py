def test_init(api):
    assert api
    assert api.apidoc

def test_resources(api):
    expected = sorted(['posts', 'users', 'comments'])
    assert expected == api.resources

def test_resource_action(action):
    assert 'show' == action.name

def test_action_apidoc(action):
    assert action.apidoc

def test_action_routes(action):
    assert action.routes

def test_action_route(action):
    route = action.routes[0]
    assert '/users/:id' == route.path
    assert 'get' == route.method

def test_action_params(resource):
    action = resource.action('create')
    assert action.params

def test_action_examples(resource):
    action = resource.action('index')
    assert action.examples

def test_action_example(resource):
    action = resource.action('index')
    example = action.examples[0]
    assert 'GET' == example.http_method
    assert '/users' == example.path
    assert '' == example.args
    assert 200 == example.status
    assert '[ {"user":{"name":"John Doe" }} ]' in example.response
