from flask import Flask
from flask import jsonify
from flask import request
from flask import send_from_directory
from remoteFacade import AccountFacade
from flask_cors import CORS

app = Flask(__name__, static_folder='dist')
CORS(app)

@app.route('/')
def index():
    return app.send_static_file("index.html")


@app.route('/<path:path>')
def static_dist(path):
    return send_from_directory("dist", path)


@app.route('/api/user')
def user():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_account(user_ids))


@app.route('/api/user/friends')
def friends():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_friends(user_ids))


@app.route('/api/user/banned_friends')
def banned_friends():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_banned_friends(user_ids))


@app.route('/api/user/deleted_friends')
def deleted_friends():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_deleted_friends(user_ids))


@app.route('/api/user/abandoned_friends')
def abandoned_friends():
    user_ids = request.args.get('user_ids', default=None, type=str)
    days_offline = request.args.get('days_offline', default=365/2, type=int)
    return jsonify(AccountFacade.get_abandoned_friends(user_ids, days_offline))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
