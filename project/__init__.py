# project/__init__.py
from flask import Flask, jsonify, request
from math import * 

result = []
def isprime(n):
    if n <= 1:
        return 0
    m = int(sqrt(n))+1
    for x in range(2,m):
        if n%x == 0:
            return 0
    return 1

def bprime(n):
    if isprime(n):
	global result
        result.append(str(n))
    else:
        x = 2
        while x <= int(n/2):
            if n%x == 0:
		result.append(str(x))
                print(x)
                return bprime(n/x)
            x = x + 1

app = Flask(__name__)

@app.route('/factors', methods=['GET'])
def ping_pong():
	a = int(request.args.get('number'))
	bprime(a)
	global result 
	a = '*'.join(result) 
	result = []
	return jsonify({
        	'result':a,
    		})


if __name__ == "__main__":
	app.run()
