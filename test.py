#!/usr/bin/env python3
import time
import os
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# 실행 중 UID 출력 (0이면 루트)
print("🔍 Effective UID:", os.geteuid())

# 1) 매트릭스 옵션 설정
options = RGBMatrixOptions()

# ✅ 루트 권한 유지 및 하드웨어 펄스 비활성화 설정
options.drop_privileges = False
options.disable_hardware_pulsing = True

# ✅ 패널 구성 설정 (P4 패널 기준 80x40)
options.rows = 40                # 한 패널의 세로 픽셀 수
options.cols = 80                # 한 패널의 가로 픽셀 수
options.chain_length = 3         # 가로로 연결된 패널 수
options.parallel = 2             # 세로로 연결된 패널 수
options.brightness = 80          # 밝기 (1~100)
options.hardware_mapping = 'regular'  # 직접 배선 시 'regular'

# 2) 매트릭스 및 캔버스 생성
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# 3) 폰트 로드
FONT_PATH = "/home/user/rpi-rgb-led-matrix/fonts/7x13.bdf"  # 사용자 경로 맞게 수정
if not os.path.exists(FONT_PATH):
    raise FileNotFoundError(f"❌ 폰트 파일 없음: {FONT_PATH}")
font = graphics.Font()
font.LoadFont(FONT_PATH)

color = graphics.Color(255, 255, 255)  # 흰색

# 4) 스크롤할 메시지 및 초기 위치
message = "Hello, LED Matrix!"
pos = canvas.width

# 5) 메인 루프
try:
    while True:
        canvas.Clear()
        text_len = graphics.DrawText(canvas, font, pos, 30, color, message)
        canvas = matrix.SwapOnVSync(canvas)

        pos -= 1
        if pos + text_len < 0:
            pos = canvas.width

        time.sleep(0.03)  # 스크롤 속도 조절
except KeyboardInterrupt:
    matrix.Clear()
    print("🛑 종료되었습니다.")
