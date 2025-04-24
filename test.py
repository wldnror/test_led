#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from time import sleep

# ─── 1. 매트릭스 옵션 설정 ──────────────────────────────────
options = RGBMatrixOptions()
options.rows           = 40      # 패널 높이 (픽셀)
options.cols           = 80      # 패널 너비 (픽셀)
options.chain_length   = 3       # 가로로 연결된 패널 수
options.parallel       = 2       # 세로로 연결된 패널 수
options.brightness     = 80      # 밝기 (0–100)
options.hardware_mapping = 'regular'  
+options.disable_hardware_pulse = True    # ← 이 줄 추가
#  → HAT/Bonnet 쓰면 'adafruit-hat' 로 변경

# ─── 2. 매트릭스 객체 생성 ──────────────────────────────────
matrix = RGBMatrix(options=options)

# ─── 3. 컬러 풀스크린 테스트 루프 ───────────────────────────
try:
    while True:
        matrix.Fill(255, 0, 0)   # 빨강
        sleep(1)
        matrix.Fill(0, 255, 0)   # 초록
        sleep(1)
        matrix.Fill(0, 0, 255)   # 파랑
        sleep(1)
        matrix.Clear()           # 화면 지우기
        sleep(1)

except KeyboardInterrupt:
    matrix.Clear()             # Ctrl+C 로 종료 시 화면 클리어
