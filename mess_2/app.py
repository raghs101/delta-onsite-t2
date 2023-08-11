from flask import Flask,jsonify,session,request
import uuid  
import logging


app = Flask(__name__)

app.secret_key = 'local_delta'
logging.basicConfig(filename='backend.log', level=logging.INFO)


@app.route("/")
def home():
    if 'uuid' not in session:
        session['uuid'] = str(uuid.uuid4())
    logging.info(f"Request received by {session['uuid']}: {request.url}")

    
    mess_name = "Mess 2"  # Replace with the actual mess name
    response_data = {
        'uuid': str(session['uuid']),
        'mess_name': mess_name
    }
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)