#!/usr/bin/env python3
import subprocess
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics

# ──── 매트릭스 설정 ────
options = RGBMatrixOptions()
options.rows = 64       # 패널 세로 픽셀
options.cols = 80       # 패널 가로 픽셀
options.chain_length = 3  # 가로로 패널 3장
options.parallel = 2      # 세로로 패널 2장
options.hardware_mapping = 'regular'  # 배선 직접 결선 시
matrix = RGBMatrix(options=options)

canvas = matrix.CreateFrameCanvas()
font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
text_color = graphics.Color(255, 255, 0)  # 노란색

def scroll_text(msg, speed=0.05):
    pos = canvas.width
    length = graphics.DrawText(canvas, font, pos, 20, text_color, msg)
    while pos + length > 0:
        canvas.Clear()
        graphics.DrawText(canvas, font, pos, 20, text_color, msg)
        canvas = matrix.SwapOnVSync(canvas)
        pos -= 1
        time.sleep(speed)
    matrix.Clear()

def speak(msg, lang='ko'):
    # espeak-ng 예제 (한글은 음질이 다소 기계적)
    # 한글 대신 영어라면 '-v en' 옵션
    cmd = ['espeak-ng', f'-v {lang}', msg]
    subprocess.Popen(cmd)

if __name__ == "__main__":
    message = "안녕하세요! 전광판과 TTS 기능입니다."
    # 1) 음성 출력
    speak(message, lang='ko')  
    # 2) 텍스트 스크롤
    scroll_text(message)
