import os
from flask import Flask, request
from telapi import rest

app = Flask(__name__)

@app.route('/')
def send_sms():
    # Pegar os dados no dashboard da TelAPI
    account_sid = 'ACfbc75add82a44565aea6df2b3584fdf5'
    auth_token  = '05ed052bf32c49a1bc1305743f2b5ab9'
    client      = rest.Client(account_sid, auth_token)
    account     = client.accounts[client.account_sid]

    sms_message = account.sms_messages.create(
        from_number = request.args.get('From', None),
        to_number = request.args.get('To', None),
        body = request.args.get('Body', None),
    )

    if sms_message:
        return "SMS SID: %s" % sms_message.sid

    return 'Test Send SMS'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
