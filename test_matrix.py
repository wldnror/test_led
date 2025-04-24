#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# --- BCM 핀 설정 ---
pins = {
    'R1':17, 'G1':18, 'B1':22,
    'A':5, 'B':6, 'C':13,
    'CLK':11, 'LAT':27, 'OE':4
}
# D는 1/4 스캔용으로 GND에 묶어둡니다.

GPIO.setmode(GPIO.BCM)
for p in pins.values():
    GPIO.setup(p, GPIO.OUT)

def shift_n_bits(n):
    for _ in range(n):
        GPIO.output(pins['CLK'], True)
        GPIO.output(pins['CLK'], False)

def latch_and_show():
    # 래치 펄스
    GPIO.output(pins['LAT'], True)
    GPIO.output(pins['LAT'], False)
    # OE 낮춰서 출력 켜기
    GPIO.output(pins['OE'], False)

def blank():
    GPIO.output(pins['OE'], True)

try:
    # 행 선택: A=B=C=0 => 첫 번째 행
    GPIO.output(pins['A'], False)
    GPIO.output(pins['B'], False)
    GPIO.output(pins['C'], False)

    # 무한 루프: R→G→B 로 1초씩
    while True:
        # 1) 빨강
        blank()
        GPIO.output(pins['R1'], True)
        GPIO.output(pins['G1'], False)
        GPIO.output(pins['B1'], False)
        shift_n_bits(64)
        latch_and_show()
        time.sleep(1)

        # 2) 초록
        blank()
        GPIO.output(pins['R1'], False)
        GPIO.output(pins['G1'], True)
        GPIO.output(pins['B1'], False)
        shift_n_bits(64)
        latch_and_show()
        time.sleep(1)

        # 3) 파랑
        blank()
        GPIO.output(pins['R1'], False)
        GPIO.output(pins['G1'], False)
        GPIO.output(pins['B1'], True)
        shift_n_bits(64)
        latch_and_show()
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("종료, GPIO 클린업 완료")
