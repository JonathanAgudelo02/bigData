from flask import Flask, jsonify 

import boto3 

  

app = Flask(__name__) 

  

def get_buckets(): 

    s3 = boto3.client('s3') 

    response = s3.list_buckets() 

    buckets = [bucket['Name'] for bucket in response['Buckets']] 

    return buckets 

  

@app.route('/json') 

def list_buckets_json(): 

    buckets = get_buckets() 

    return jsonify(buckets) 

  

@app.route('/html') 

def list_buckets_html(): 

    buckets = get_buckets() 

    return "<br>".join(buckets) 

  

if __name__ == '__main__': 

    app.run(port="5000", host='0.0.0.0',  debug=True)
