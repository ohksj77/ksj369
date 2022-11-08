from flask import Flask, request, jsonify
import requests
from time import sleep

''' 이 파일의 주석으로 코드를 설명 하겠습니다. '''

app = Flask(__name__)
@app.route('/start369', methods=["GET"])
def atfirst():     # 처음에 한 번만 실행되는 API 입니다.
    
    sleep(0.5)
    
    print("1")     # 369게임 초기값 : 1
    
    sleep(1)       # 1초 쉰 후에 다음 컨테이너에 request를 요청하기 위함입니다.
    try:
        requests.post('http://ksj2:5002/second369', json={'num' : '2'})     # 2(다음 숫자)를 JSON으로 두번째 컨테이너의 API에 보냅니다.
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the 369 service.\n')
        return 'ERROR\n'
    
    return jsonify(success=True)    # success 리턴


@app.route('/first369', methods=["POST"])
def first369():                     # 맨 첫 호출 제외한 이후 호출들을 받을 API 입니다.
    
    num : str = request.get_json()['num']        # json 형식으로 받아옵니다.
    
    sleep(1)                        # 1초 쉬어줍니다.
    
    res = list(map(lambda o: 'JJAK', filter(lambda d: not int(d) % 3 and d != '0', num)))      # 3,6,9가 숫자에 몇개 들어가있는지 찾아 개수 만큼 ZZAK으로 바꿔줍니다. 
    
    print(' '.join(res) if res else num)       # 콘솔에 ZZAK * n번 혹은 원래 숫자를 상황에 맞게 출력합니다. res가 비어있다는 것은 3,6,9가 포함되지 않은 숫자라는 뜻입니다.
    
    try:
        requests.post('http://ksj2:5002/second369', json={'num' : str(int(num) + 1)})   # 2번째 컨테이너의 API에 지금 숫자인 num에 1을 더해 JSON으로 request를 보냅니다.
    except requests.exceptions.RequestException as e:
        print('\n Cannot reach the 369 service.\n')
        return 'ERROR\n'
    
    return jsonify(success=True)         # success 리턴

if __name__ == "__main__":
    app.run(host ="0.0.0.0", port=5001, debug=True)
