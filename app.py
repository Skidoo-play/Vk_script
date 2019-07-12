from flask import Flask
from flask import jsonify
from flask import request
from remoteFacade import AccountFacade

app = Flask(__name__)


@app.route('/user')
def user():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_account(user_ids))


@app.route('/user/friends')
def f():
    user_ids = request.args.get('user_ids', default=None, type=str)
    return jsonify(AccountFacade.get_friends(user_ids))


if __name__ == '__main__':
    app.run()
