#! /bin/sh

# 이 파일을 실행시켜 주세요

docker-compose down -v
docker-compose up -d --build            # 컴포즈 빌드 및 실행

sleep 4                                 # 이전 작업들이 완전히 완료되면 실행하기 위함입니다.

curl http://localhost:5001/start369 &   # 이 부분은 백그라운드에서 실행

docker-compose logs -f                  # 도커 컴포즈 로그 실시간으로 보기
