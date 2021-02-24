from flask import Flask, jsonify, request, send_from_directory, url_for
from src import AccountFacade
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

@app.route('/')
def index():
    links = ["%s" % rule for rule in app.url_map.iter_rules()]
    links = filter(lambda link: link not in ("/", "/static/<path:filename>"), links)
    links = map(lambda link: f"'{link}'", links)
    return jsonify({"message": f"""Allowed API routes: [{', '.join(links)}]"""})


@app.errorhandler(404)
def catch_error(e):
    # raise Exception()
    return jsonify({'message': str(e)}), 404


@app.route('/api/user/<string:user_ids>')
def user(user_ids):
    return jsonify(AccountFacade.get_account(user_ids))


@app.route('/api/user/friends/<string:user_ids>')
def friends(user_ids):
    return jsonify(AccountFacade.get_friends(user_ids))


@app.route('/api/user/banned_friends/<string:user_ids>')
def banned_friends(user_ids):
    return jsonify(AccountFacade.get_banned_friends(user_ids))


@app.route('/api/user/deleted_friends/<string:user_ids>')
def deleted_friends(user_ids):
    return jsonify(AccountFacade.get_deleted_friends(user_ids))


@app.route('/api/user/abandoned_friends/<string:user_ids>')
def abandoned_friends(user_ids):
    days_offline = request.args.get('days_offline', default=365/2, type=int)
    return jsonify(AccountFacade.get_abandoned_friends(user_ids, days_offline))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
