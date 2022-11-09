import os
from flask import Flask, request, jsonify
from TadoneServices.controller.tadone_controller import tadone_controller
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(tadone_controller)


@app.route("/")
@cross_origin()
def main_app_entry():
    print("You have reached the main entry of the app.")
    response = jsonify(
        sigma_url_root=request.script_root,
        sigma_full_path=request.full_path,
        sigma_url=request.url,
        sigma_deano_message="Welcome to our Gateway. We serve and protect your data :)",
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# TODO - Use Python environments so this is only run in development time.
# Unmark in case of local development. Remark in case of production deployment.
# app.run(ssl_context=("certificates/cert.pem", "certificates/key.pem"))
app.run(port=int(os.environ.get("PORT", 5005)), host='0.0.0.0', debug=True)
