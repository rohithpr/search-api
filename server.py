from flask import Flask, jsonify, request, redirect, url_for
from pws import Bing, Google

import random

app = Flask(__name__)

@app.route('/')
def root():
    project_information = {
        'base_url': 'http://search-api.herokuapp.com/',
        'project_name': 'search-api',
        'source': 'https://github.com/rohithpr/search-api',
        'documentation': 'https://github.com/rohithpr/search-api/blob/master/README.md',
        'related_projects': {
            'py-web-search': 'https://github.com/rohithpr/py-web-search',
        },
        'issues': {
            'py-web-search': 'https://github.com/rohithpr/py-web-search/issues',
            'search-api': 'https://github.com/rohithpr/search-api/issues',
        },
        'end_points': {
            'search': '/search',
        }
    }
    return jsonify(project_information)


def argument_validator(request):
    errors = {}

    query = request.args.get('q')
    print('q')
    if query is None:
        errors['q'] = 'Parameter q is required'

    num = request.args.get('num') or 10
    try:
        num = int(num)
    except:
        errors['num'] = 'Parameter num should be an integer'

    start = request.args.get('start') or 0
    try:
        start = int(start)
    except:
        errors['start'] = 'Parameter start should be an integer'

    recent = request.args.get('recent')
    if recent and recent not in ['h', 'd', 'w', 'y']:
        errors['recent'] = 'Parameter recent should be h, d, w, or y'

    engine = request.args.get('engine') or random.choice(['bing', 'google'])
    engine = engine.lower()
    if engine not in ['bing', 'google']:
        errors['engine'] = 'Parameter engine should be bing or google'
    elif engine == 'bing':
        engine = Bing
    elif engine == 'google':
        engine = Google

    arguments = {'query': query, 'num': num, 'start': start, 'sleep': False, 'recent': recent}
    return errors, arguments, engine

@app.route('/search/')
def search():
    errors, arguments, engine = argument_validator(request)
    print(errors, arguments, engine)
    if len(errors.keys()) > 0:
        return jsonify(errors)
    else:
        result = engine.search(**arguments)
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True)
