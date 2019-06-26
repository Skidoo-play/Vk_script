from flask import Flask, jsonify
from remoteFacade import AccountFacade

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify(AccountFacade.get_account("159653430"))

@app.route('/f')
def f():
    return jsonify(AccountFacade.get_friends("159653430"))


if __name__ == '__main__':
    app.run()
