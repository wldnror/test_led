#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# 패널 해상도 (예: 64×32)
WIDTH  = 64
HEIGHT = 32

# 1) 옵션 설정
options = RGBMatrixOptions()
options.rows         = HEIGHT
options.cols         = WIDTH
options.chain_length = 1
options.parallel     = 1
options.hardware_mapping = 'regular'
options.gpio_slowdown    = 2
options.disable_hardware_pulse = True    # 하드웨어 펄스 비활성화

# 2) 매트릭스 초기화
matrix = RGBMatrix(options=options)

# 3) 이미지 생성 (빨강/초록/파랑 테스트)
im = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)
draw.rectangle((0,0, WIDTH//3,   HEIGHT), fill=(255,  0,  0))
draw.rectangle((WIDTH//3,0, 2*WIDTH//3, HEIGHT), fill=(  0,255,  0))
draw.rectangle((2*WIDTH//3,0, WIDTH, HEIGHT), fill=(  0,  0,255))

# 4) 디스플레이
matrix.SetImage(im)

# 5) 종료 대기
print("컬러 바 테스트 중… Ctrl+C 로 종료")
try:
    while True:
        pass
except KeyboardInterrupt:
    matrix.Clear()
    print("종료하고 클리어했습니다.")
