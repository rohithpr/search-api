from flask import Flask, jsonify, request

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
    }
    return jsonify(project_information)

if __name__ == '__main__':
    app.run(threaded=True)
