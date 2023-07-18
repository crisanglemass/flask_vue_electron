from app import creat_app
from flask import render_template, jsonify
from app.models import User

app, redis = creat_app()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')



@app.route('/api/auth', methods=['POST'])
def auth():
    return jsonify({"code": 200, "msg": 'auth successfully', "data": {'msg': 'welcome to crisangle'}})

if __name__ == '__main__':
    app.run(port=5000, debug=False)
