from flask import Flask, jsonify
import json
from accountMapper import AccountMapper
from assemblers import AccountAssembler, FriendsAssembler

app = Flask(__name__)


@app.route('/')
def hello_world():
    acc = AccountMapper.get_user("159653430")
    friends_accounts = AccountMapper.get_non_active_friends(acc)
    js2 = FriendsAssembler.serealize(friends_accounts).to_json()
    js = AccountAssembler.serealize(acc).to_json()
    return jsonify(js2)


if __name__ == '__main__':
    app.run()
