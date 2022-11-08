from flask import Flask, request, jsonify
import requests
from time import sleep

app = Flask(__name__)

@app.route('/second369', methods=["POST"])
def second369():
    
    num : str = request.get_json()['num']
    
    sleep(1)
    
    res = list(map(lambda o: 'JJAK', filter(lambda d: not int(d) % 3 and d != '0', num)))
    
    print(' '.join(res) if res else num)
    
    try:
        requests.post('http://ksj3:5003/third369', json={'num' : str(int(num) + 1)}) # 3번째 컨테이너의 API에 num에 1을 더해 request를 보냅니다.
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the 369 service.\n')
        return 'ERROR\n'
    
    return jsonify(success=True)
    
if __name__ == "__main__":
    app.run(host ="0.0.0.0", port=5002, debug=True)
