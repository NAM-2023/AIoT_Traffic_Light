from gpiozero import LEDBoard            # gpio 라이브러리에서 여러 개의 LED를 한 번에 제어하기 위한 LEDBoard 클래스를 불러옴
from time import sleep                  # time 라이브러리에서 일정 시간 동안 프로그램 실행을 멈추는 sleep 함수를 불러옴

leds= LEDBoard(2, 3, 4, 20, 21)         # GPIO 핀 2, 3, 4, 20, 21, 에 연결된 LED들을 하나의 LEDBoard 객체로 초기화 하여 동시에 제어 할 수 있도록 설정함

try:
  while 1:                              # 무한 반복 루프 (프로그램이 계속 실행되도록함)
    leds.value = (0, 0, 1, 1, 0)        # 차량 신호등 초록 ON, 보행자 신호등 빨강 ON (차량 통행 / 보행자 정지)
    sleep(5.0)                          # 5초 동안 상태 유지
    leds.value = (0, 1, 0, 1, 0)        # 차량 신호등 노랑 ON, 보행자 빨강 ON (신호 전환 준비 / 딜레마 존 구간)
    sleep(3.0)                          # 3초 동안 상태 유지
    leds.value = (1, 0, 0, 0, 1)        # 차량 빨강 ON, 보행자 초록 ON (차량 정지 / 보행자 통행)
    sleep(5.0)                          # 5초 동안 상태 유지
  
except KeyboardInterrupt:               # 사용자가 Ctal + C를 누를 때까지 코드를 실행하는 예외 처리 블록임
  pass                                  # 사용자가 Ctal + C를 누르면 루프가 중단되고 코드 실행이 종료됨
leds.off()                              # 프로그램 종료 시 모든 LED를 꺼서 초기 상태로 만듦