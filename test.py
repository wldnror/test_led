#!/usr/bin/env python3
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# 1) 매트릭스 옵션 설정
options = RGBMatrixOptions()
options.drop_privileges       = False   # root 권한 유지
options.led_no_hardware_pulse = True    # 하드웨어 펄스 비활성화 (소프트웨어 PWM 사용)

options.rows         = 40        # 단일 패널 세로 픽셀 수
options.cols         = 80        # 단일 패널 가로 픽셀 수
options.chain_length = 3         # 가로로 연결된 패널 수
options.parallel     = 2         # 세로로 연결된 패널 수
options.brightness   = 80        # 밝기 (1~100)
options.hardware_mapping = 'regular'  # 직접 결선 배선맵

# 2) 매트릭스 및 캔버스 생성
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# 3) 폰트 로드
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")  # 필요시 경로 조정
color = graphics.Color(255, 255, 255)  # 흰색

# 4) 스크롤할 메시지 및 초기 위치
message = "Hello, LED Matrix!"
pos = canvas.width

# 5) 메인 루프
try:
    while True:
        canvas.Clear()
        text_length = graphics.DrawText(canvas, font, pos, 30, color, message)
        canvas = matrix.SwapOnVSync(canvas)

        pos -= 1
        if pos + text_length < 0:
            pos = canvas.width

        time.sleep(0.03)  # 스크롤 속도 조절
except KeyboardInterrupt:
    # 종료 시 화면 클리어
    matrix.Clear()
