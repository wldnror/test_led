#!/usr/bin/env python3
import time
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# 1. 매트릭스 옵션 설정
options = RGBMatrixOptions()
options.drop_privileges = False            # 반드시 루트 권한 유지
options.disable_hardware_pulsing = True    # 하드웨어 펄스 비활성화

options.rows = 40                          # 단일 패널의 세로 픽셀 수 (P4 기준)
options.cols = 80                          # 단일 패널의 가로 픽셀 수
options.chain_length = 3                   # 가로로 연결된 패널 수
options.parallel = 2                       # 세로로 연결된 패널 수
options.brightness = 80                    # 밝기 (1~100)
options.hardware_mapping = 'regular'       # 직접 GPIO 결선이면 'regular'

# 2. 매트릭스 인스턴스 생성
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# 3. 폰트 로드
FONT_PATH = "/home/user/rpi-rgb-led-matrix/fonts/7x13.bdf"  # 홈 디렉터리에 맞게 수정
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"Font file not found: {FONT_PATH}")
font = graphics.Font()
font.LoadFont(FONT_PATH)

color = graphics.Color(255, 255, 255)  # 흰색

# 4. 출력할 메시지와 시작 위치
message = "Hello, LED Matrix!"
pos = canvas.width  # 오른쪽에서 시작

# 5. 메인 루프 (스크롤 애니메이션)
try:
    while True:
        canvas.Clear()
        text_len = graphics.DrawText(canvas, font, pos, 30, color, message)
        canvas = matrix.SwapOnVSync(canvas)

        pos -= 1
        if pos + text_len < 0:
            pos = canvas.width

        time.sleep(0.03)
except KeyboardInterrupt:
    matrix.Clear()
