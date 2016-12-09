import threading
import time
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix


class Display(threading.Thread):
    def __init__(self, weather, dimmer):
        threading.Thread.__init__(self)
        self.setDaemon(True)

        self._weather = weather
        self._dimmer = dimmer

        # Configure LED matrix driver
        self._matrix = RGBMatrix(32, 2, 1)
        self._matrix.pwmBits = 11
        self._matrix.brightness = 25

        # Load fonts
        self._font_large = graphics.Font()
        self._font_large.LoadFont("rpi-rgb-led-matrix/fonts/10x20.bdf")
        self._font_small = graphics.Font()
        self._font_small.LoadFont("rpi-rgb-led-matrix/fonts/6x10.bdf")
        self._font_tiny = graphics.Font()
        self._font_tiny.LoadFont("rpi-rgb-led-matrix/fonts/4x6.bdf")

        # Define colors
        self._white = graphics.Color(255, 255, 255)
        self._red = graphics.Color(255, 32, 32)
        self._blue = graphics.Color(64, 64, 255)

    def _draw(self, canvas):
        canvas.Clear()

        graphics.DrawText(canvas, self._font_large, 1, 13, self._white, time.strftime("%-2I:%M"))
        graphics.DrawText(canvas, self._font_small, 53, 13, self._white, time.strftime("%p"))

        graphics.DrawText(canvas, self._font_small, 2, 22, self._white, time.strftime("%a %b %-d"))

        temp_str = "%3.0f" % self._weather.cur_temp
        graphics.DrawText(canvas, self._font_small, 0, 31, self._white, temp_str)
        graphics.DrawText(canvas, self._font_tiny, 18, 31, self._white, "F")

        hi_str = "%3.0f" % self._weather.high_temp
        graphics.DrawText(canvas, self._font_small, 22, 31, self._white, hi_str)
        graphics.DrawText(canvas, self._font_tiny, 40, 31, self._red, "F")

        low_str = "%3.0f" % self._weather.low_temp
        graphics.DrawText(canvas, self._font_small, 43, 31, self._white, low_str)
        graphics.DrawText(canvas, self._font_tiny, 61, 31, self._blue, "F")

    def run(self):
        canvas = self._matrix.CreateFrameCanvas()

        while True:
            self._draw(canvas)
            time.sleep(0.05)
            canvas = self._matrix.SwapOnVSync(canvas)
            self._matrix.brightness = self._dimmer.brightness
