#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw
import time

# ── 모듈 사양 ───────────────────────────
WIDTH   = 80    # 픽셀 수 (module width)
HEIGHT  = 40    # 픽셀 수 (module height)
CHAIN   = 1     # panel을 체인으로 연결했을 때 갯수
PARALLEL= 1     # 병렬로 묶었을 때 갯수
# 10-스캔은 라이브러리가 자동으로 처리해 주므로 별도 설정 불필요
# 그레이 스케일 입력: 8비트, 밝기 조절: 0~100
# ───────────────────────────────────────

options = RGBMatrixOptions()
options.rows           = HEIGHT
options.cols           = WIDTH
options.chain_length   = CHAIN
options.parallel       = PARALLEL
options.hardware_mapping   = 'regular'  # 직접 배선하셨다면 'regular'
options.pwm_bits       = 8              # 그레이스케일 8비트
options.brightness     = 100            # 밝기 0~100
options.disable_hardware_pulse = True   # --led-no-hardware-pulse 플래그 대체
options.gpio_slowdown  = 2              # 필요 시 1~4 조정

matrix = RGBMatrix(options=options)

# 간단히 빨강→초록→파랑 3색 블록 채우기
im = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)
draw.rectangle((0, 0, WIDTH//3,        HEIGHT), fill=(255,   0,   0))  # 왼쪽 1/3: 빨강
draw.rectangle((WIDTH//3, 0, 2*WIDTH//3, HEIGHT), fill=(0,   255,   0))  # 중간 1/3: 초록
draw.rectangle((2*WIDTH//3, 0, WIDTH,   HEIGHT), fill=(0,     0, 255))  # 오른쪽 1/3: 파랑

matrix.SetImage(im)

print("80×40 모듈 테스트: 3색 출력 중… Ctrl+C 로 종료하세요")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    matrix.Clear()
    print("\n종료하고 화면 클리어했습니다.")
