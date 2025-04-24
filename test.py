#!/usr/bin/env python3
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# --- 패널 해상도에 맞춰 조정하세요 ---
WIDTH  = 64    # 컬럼 수
HEIGHT = 32    # 행 수
# -----------------------------------

# 1) 옵션 설정
options = RGBMatrixOptions()
options.rows         = HEIGHT
options.cols         = WIDTH
options.chain_length = 1      # 패널을 체인으로 연결했으면 그 수
options.parallel     = 1      # 병렬로 묶었다면 그 수
options.hardware_mapping = 'regular'  # 보통 'adafruit-hat' 쓰는 분들도 많습니다
options.gpio_slowdown    = 2  # 속도 조절 (깜빡임이 심하면 1→4 사이 조정)

# 2) 매트릭스 초기화
matrix = RGBMatrix(options=options)

# 3) 출력할 이미지를 만듭니다
#    - 예제로 빨강/초록/파랑 세 영역을 채워 봅니다
im = Image.new("RGB", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)
draw.rectangle((0,0, WIDTH//3,   HEIGHT), fill=(255,  0,  0))  # 왼쪽 1/3: 빨강
draw.rectangle((WIDTH//3,0, 2*WIDTH//3, HEIGHT), fill=(  0,255,  0))  # 중간 1/3: 초록
draw.rectangle((2*WIDTH//3,0, WIDTH, HEIGHT), fill=(  0,  0,255))  # 오른쪽 1/3: 파랑

# 4) 매트릭스에 뿌리기
matrix.SetImage(im.convert('RGB'))

# 5) 프로그램이 종료되지 않도록 대기
print("빨강·초록·파랑 출력 중… Ctrl+C 로 종료")
try:
    while True:
        pass
except KeyboardInterrupt:
    matrix.Clear()
    print("\n클리어하고 종료합니다.")
