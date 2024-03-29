from app.command.wallet_command import WalletCommand
from app.persistence.context.data_wallet import WalletContext
from flask import Flask, abort, Response
from flask import request
import json

wallet_context = WalletContext()
wallet_command = WalletCommand(wallet_context)

app = Flask(__name__)


@app.route('/save', methods=['POST'])
def save():
    if request.method == "POST":
        income_amount = request.values.get("income_amount")
        discharge_amount = request.values.get("discharge_amount")
        wallet_command.save_wallet(income_amount, discharge_amount)
    return Response(response="OK", status=201)


@app.route('/get', methods=['GET'])
def get():
    status = 500
    try:
        if request.method == "GET":
            wallet = wallet_command.get_balance()
            response = json.dumps(wallet.to_json())
            status = 200
            return Response(response=response, status=status, mimetype='application/json')

    except Exception as ex:
        raise ex
    return Response(status=status)


if __name__ == '__main__':
    app.run(debug=True)
