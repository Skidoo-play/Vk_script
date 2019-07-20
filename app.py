from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from remoteFacade import AccountFacade
from flask_cors import CORS

app = Flask(__name__,
            static_folder = "./dist/",
            template_folder = "./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def catch_error(e):
    return render_template('index.html'), 200


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
    return jsonify(AccountFacade.get_abandoned_friends(user_ids))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
