#!/usr/bin/env python3
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# 1) 매트릭스 설정
options = RGBMatrixOptions()
options.rows = 40               # 단일 패널 세로 픽셀 수
options.cols = 80               # 단일 패널 가로 픽셀 수
options.chain_length = 3        # 가로로 연결된 패널 수
options.parallel = 2            # 세로로 연결된 패널 수
options.brightness = 80         # 밝기 (1~100)
options.hardware_mapping = 'regular'  # HAT 없이 직접 결선할 때

matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# 2) 폰트 로드 (기본 제공 폰트 중 하나)
font = graphics.Font()
font.LoadFont("/home/pi/rpi-rgb-led-matrix/fonts/7x13.bdf")
color = graphics.Color(255, 255, 255)  # 흰색

# 3) 스크롤할 텍스트와 초기 위치
message = "Hello, LED Matrix!"
pos = canvas.width

try:
    while True:
        canvas.Clear()
        # 텍스트 그리기 (y 위치는 baseline 기준; 0~rows-1 사이)
        text_length = graphics.DrawText(canvas, font, pos, 30, color, message)
        # 다음 프레임 준비
        canvas = matrix.SwapOnVSync(canvas)

        # 위치 이동
        pos -= 1
        # 완전히 화면 밖으로 나가면 다시 오른쪽 끝으로
        if pos + text_length < 0:
            pos = canvas.width

        time.sleep(0.03)  # 속도 조절
except KeyboardInterrupt:
    # 종료 시 매트릭스 클리어
    matrix.Clear()
