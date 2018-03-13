from application import app

from flask import jsonify

@app.route('/status')
def status():
    app.logger.debug('status')
    return jsonify({
        'status': 'OK'
    })

@app.route('/info')
def info():
    app.logger.debug('info')
    return jsonify({
        'application': 'flask-boilerplate',
        'env': 'TODO'
    })
