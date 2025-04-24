#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# — BCM 핀 매핑 (표 그대로) —
pins = {
    'R1': 17,  # 패널 핀1 → Pi 헤더 11
    'G1': 18,  # 패널 핀2 → Pi 헤더 12
    'B1': 22,  # 패널 핀3 → Pi 헤더 15
    # R2/G2/B2 은 하단 테스트 시 사용 가능 (패널 핀5,6,7 → BCM23,24,25)
    # 'R2': 23, 'G2':24, 'B2':25,

    'A': 5,    # 패널 핀9  → 헤더 29
    'B': 6,    # 패널 핀10 → 헤더 31
    'C': 13,   # 패널 핀11 → 헤더 33
    # 'D' 는 GND에 묶음

    'CLK': 11, # 패널 핀13 → 헤더 23
    'LAT': 27, # 패널 핀14 → 헤더 13
    'OE': 4,   # 패널 핀15 → 헤더 7 (active‐low)
}

GPIO.setmode(GPIO.BCM)
for p in pins.values():
    GPIO.setup(p, GPIO.OUT)

def shift_bits(n):
    for _ in range(n):
        GPIO.output(pins['CLK'], True)
        GPIO.output(pins['CLK'], False)

def latch_and_enable():
    GPIO.output(pins['LAT'], True)
    GPIO.output(pins['LAT'], False)
    GPIO.output(pins['OE'], False)

def disable_output():
    GPIO.output(pins['OE'], True)

try:
    # 행 선택: A=B=C=0 → 첫 번째 행(1/4 스캔)
    GPIO.output(pins['A'], False)
    GPIO.output(pins['B'], False)
    GPIO.output(pins['C'], False)

    print("빨강 → 초록 → 파랑 순으로 1초씩 표시됩니다. Ctrl+C로 종료.")
    while True:
        # RED
        disable_output()
        GPIO.output(pins['R1'], True)
        GPIO.output(pins['G1'], False)
        GPIO.output(pins['B1'], False)
        shift_bits(64)
        latch_and_enable()
        time.sleep(1)

        # GREEN
        disable_output()
        GPIO.output(pins['R1'], False)
        GPIO.output(pins['G1'], True)
        GPIO.output(pins['B1'], False)
        shift_bits(64)
        latch_and_enable()
        time.sleep(1)

        # BLUE
        disable_output()
        GPIO.output(pins['R1'], False)
        GPIO.output(pins['G1'], False)
        GPIO.output(pins['B1'], True)
        shift_bits(64)
        latch_and_enable()
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("종료 및 GPIO 클린업 완료")
