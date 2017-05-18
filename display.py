import threading
import time
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix
from PIL import Image
from PIL import ImageDraw


class Display(threading.Thread):
    def __init__(self, weather, dimmer):
        threading.Thread.__init__(self)
        self.setDaemon(True)

        self._weather = weather
        self._dimmer = dimmer

        # Configure LED matrix driver
        self._matrix = RGBMatrix(16, 1, 1)
        self._matrix.pwmBits = 11
        self._matrix.brightness = 10

        # Load fonts
        self._font_large = graphics.Font()
        self._font_large.LoadFont("rpi-rgb-led-matrix/fonts/6x13B.bdf")
        self._font_small = graphics.Font()
        self._font_small.LoadFont("rpi-rgb-led-matrix/fonts/6x10.bdf")
        self._font_tiny = graphics.Font()
        self._font_tiny.LoadFont("rpi-rgb-led-matrix/fonts/4x6.bdf")

        # Define colors
        self._white = graphics.Color(255, 255, 255)
        self._red = graphics.Color(255, 32, 32)
        self._blue = graphics.Color(64, 64, 255)
        self._green = graphics.Color(32, 255, 32)
        self._yellow = graphics.Color(0, 255, 255)
        self._orange = graphics.Color(255, 165, 0)
        self._grey = graphics.Color(128, 128, 128)
        self._grey1 = graphics.Color(115, 115, 115)
        self._grey2 = graphics.Color(102, 102, 102)
        self._grey3 = graphics.Color(89, 89, 89)
        self._grey4 = graphics.Color(76, 76, 76)
        self._grey5 = graphics.Color(64, 64, 64)
        self._grey6 = graphics.Color(51, 51, 51)
        self._grey7 = graphics.Color(38, 38, 38)
        self._grey8 = graphics.Color(25, 25, 25)
        self._grey9 = graphics.Color(0, 0, 0)
        self._greyA = graphics.Color(140,140,140)
        self._greyB = graphics.Color(153,153,153)
        self._greyC = graphics.Color(166,166,166)
        self._greyD = graphics.Color(178,178,178)
        self._greyE = graphics.Color(191,191,191)
        self._greyF = graphics.Color(204,204,204)
        self._greyG = graphics.Color(216,216,216)
        self._greyH = graphics.Color(229,229,229)
        self._greyI = graphics.Color(242,242,242)
        self._greyJ = graphics.Color(255,255,255)


    def _draw(self, canvas):
        canvas.Clear()

        if self._dimmer.brightness > 29:


            cur_weather_str = "%s" % self._weather.cur_weather_desc
            #graphics.DrawText(canvas, self._font_tiny, 0, 5, self._blue, cur_weather_str)




            if cur_weather_str == "sunny":
                graphics.DrawCircle(canvas, 30, 1, 2, self._yellow)
                graphics.DrawCircle(canvas, 30, 1, 1, self._orange)
                graphics.DrawCircle(canvas, 30, 1, 0, self._yellow) 
            
            elif cur_weather_str in ("Breezy", "A Few Clouds and Breezy", "A Few Clouds", "A Few Clouds and Windy", "Partly Cloudy and Breezy", "Partly Cloudy"):
            #     x=1
            #     while x < 32:
            #         graphics.DrawCircle(canvas, x+1, 1, 3, self._white)
            #         graphics.DrawCircle(canvas, x+5, 1, 3, self._white)
            #         graphics.DrawCircle(canvas, x+9, 1, 3, self._white)
            #         time.sleep(1)
            #         x += 1

            #     else:
            #         x = 1


                #CLOUDS

                # graphics.DrawCircle(canvas, 17, 1, 4, self._white)
                # graphics.DrawCircle(canvas, 17, 1, 3, self._white)
                graphics.DrawCircle(canvas, 30, 3, 2, self._white)
                graphics.DrawCircle(canvas, 30, 3, 1, self._grey)
                graphics.DrawCircle(canvas, 30, 3, 0, self._white)   

                graphics.DrawCircle(canvas, 27, 1, 2, self._grey)
                graphics.DrawCircle(canvas, 27, 1, 1, self._white)
                graphics.DrawCircle(canvas, 27, 1, 0, self._grey)       

                
                graphics.DrawCircle(canvas, 1, 1, 2, self._grey)
                graphics.DrawCircle(canvas, 1, 1, 1, self._white)
                graphics.DrawCircle(canvas, 1, 1, 0, self._grey)

                graphics.DrawCircle(canvas, 4, 3, 2, self._white)
                graphics.DrawCircle(canvas, 4, 3, 1, self._grey)
                # graphics.DrawCircle(canvas, 7, 1, 1, self._white)
                # graphics.DrawCircle(canvas, 7, 1, 0, self._white)        
                # graphics.DrawCircle(canvas, 5, 1, 2, self._white)
                graphics.DrawCircle(canvas, 9, 1, 2, self._grey)
                # graphics.DrawCircle(canvas, 1, 1, 1, self._white)
                graphics.DrawCircle(canvas, 9, 1, 1, self._white)


            # elif cur_weather_str in ("Fair", "Fair and Breezy", "Clear"):

            #     #CLOUDS
            #     graphics.DrawCircle(canvas, 1, 1, 2, self._white)
            #     graphics.DrawCircle(canvas, 5, 1, 4, self._white)
            #     # graphics.DrawCircle(canvas, 5, 1, 3, self._white)
            #     graphics.DrawCircle(canvas, 5, 1, 2, self._white)
            #     graphics.DrawCircle(canvas, 4, 2, 2, self._white)
            #     graphics.DrawCircle(canvas, 5, 1, 1, self._white)
            #     graphics.DrawCircle(canvas, 5, 1, 0, self._white)        
            #     graphics.DrawCircle(canvas, 5, 1, 2, self._white)
            #     graphics.DrawCircle(canvas, 9, 1, 2, self._white)
            #     # graphics.DrawCircle(canvas, 1, 1, 1, self._white)
            #     graphics.DrawCircle(canvas, 9, 1, 1, self._white)  





            elif cur_weather_str in ("Mostly Cloudy", "Mostly Cloudy and Breezy", "Mostly Cloudy and Windy"):

                graphics.DrawCircle(canvas, 30, 3, 2, self._white)
                graphics.DrawCircle(canvas, 30, 3, 1, self._grey)
                graphics.DrawCircle(canvas, 30, 3, 0, self._white)   

                graphics.DrawCircle(canvas, 27, 1, 2, self._grey)
                graphics.DrawCircle(canvas, 27, 1, 1, self._white)
                graphics.DrawCircle(canvas, 27, 1, 0, self._grey)       

                
                graphics.DrawCircle(canvas, 1, 1, 2, self._grey)
                graphics.DrawCircle(canvas, 1, 1, 1, self._white)
                graphics.DrawCircle(canvas, 1, 1, 0, self._grey)

                graphics.DrawCircle(canvas, 4, 3, 2, self._white)
                graphics.DrawCircle(canvas, 4, 3, 1, self._grey)
                # graphics.DrawCircle(canvas, 7, 1, 1, self._white)
                # graphics.DrawCircle(canvas, 7, 1, 0, self._white)        
                # graphics.DrawCircle(canvas, 5, 1, 2, self._white)
                graphics.DrawCircle(canvas, 9, 1, 2, self._grey)
                # graphics.DrawCircle(canvas, 1, 1, 1, self._white)
                graphics.DrawCircle(canvas, 9, 1, 1, self._white) 

    # , "Overcast", "Overcast and Breezy"

            elif cur_weather_str == "Fair":
                graphics.DrawLine(canvas, 1, 1, 32, 1, self._grey1)
                graphics.DrawLine(canvas, 1, 2, 32, 2, self._grey2)
                graphics.DrawLine(canvas, 1, 3, 32, 3, self._grey3)
                graphics.DrawLine(canvas, 1, 4, 32, 4, self._grey4)
                graphics.DrawLine(canvas, 1, 5, 32, 5, self._grey5)
                graphics.DrawText(canvas, self._font_tiny, 1, 6, self._grey9, "OVERCAST")
                # graphics.DrawLine(canvas, 1, 6, 32, 6, self._grey6)
                # graphics.DrawLine(canvas, 1, 7, 32, 7, self._grey7)
                # graphics.DrawLine(canvas, 1, 8, 32, 8, self._grey8)
                # graphics.DrawLine(canvas, 1, 9, 32, 9, self._grey9)
                # graphics.DrawLine(canvas, 1, 10, 32, 10, self._greyA)
                # graphics.DrawLine(canvas, 1, 11, 32, 11, self._grey1)
                # graphics.DrawLine(canvas, 1, 12, 32, 12, self._grey2)
                # graphics.DrawLine(canvas, 1, 13, 32, 13, self._grey3)
                # graphics.DrawLine(canvas, 1, 14, 32, 14, self._grey4)
                # graphics.DrawLine(canvas, 1, 15, 32, 15, self._grey5)
                # graphics.DrawLine(canvas, 1, 16, 32, 16, self._grey6)
                # graphics.DrawLine(canvas, 1, 17, 32, 17, self._grey7)
                # graphics.DrawLine(canvas, 1, 18, 32, 18, self._grey8)
                # graphics.DrawLine(canvas, 1, 19, 32, 19, self._grey9)

                # graphics.DrawLine(canvas, 1, 1, 32, 1, self._grey9)
                # graphics.DrawLine(canvas, 1, 2, 32, 2, self._grey8)
                # graphics.DrawLine(canvas, 1, 3, 32, 3, self._grey7)
                # graphics.DrawLine(canvas, 1, 4, 32, 4, self._grey6)
                # graphics.DrawLine(canvas, 1, 5, 32, 5, self._grey5)
                # graphics.DrawLine(canvas, 1, 6, 32, 6, self._grey4)
                # graphics.DrawLine(canvas, 1, 7, 32, 7, self._grey3)
                # graphics.DrawLine(canvas, 1, 8, 32, 8, self._grey2)
                # graphics.DrawLine(canvas, 1, 9, 32, 9, self._grey1)
                # graphics.DrawLine(canvas, 1, 10, 32, 10, self._greyA)
                # graphics.DrawLine(canvas, 1, 11, 32, 11, self._greyB)
                # graphics.DrawLine(canvas, 1, 12, 32, 12, self._greyC)
                # graphics.DrawLine(canvas, 1, 13, 32, 13, self._greyD)
                # graphics.DrawLine(canvas, 1, 14, 32, 14, self._greyE)
                # graphics.DrawLine(canvas, 1, 15, 32, 15, self._greyF)
                # graphics.DrawLine(canvas, 1, 16, 32, 16, self._greyG)
                # graphics.DrawLine(canvas, 1, 17, 32, 17, self._greyH)
                # graphics.DrawLine(canvas, 1, 18, 32, 18, self._greyI)
                # graphics.DrawLine(canvas, 1, 19, 32, 19, self._greyJ)



            elif cur_weather_str in ("Light Rain", "Light Rain Fog/Mist", "Light Rain and Breezy", "Rain Fog/Mist"):
                graphics.DrawCircle(canvas, 16, -12, 16, self._green)                           #test
                #no condition

            elif cur_weather_str in ("Thunderstorm in Vicinity Light Rain", "Thunderstorm in Vicinity", "Thunderstorm Light Rain", "Thunderstorm Light Rain Fog/Mist", "Thunderstorm Rain", "Thunderstorm Rain and Breezy"):
                graphics.DrawText(canvas, self._font_tiny, -4, 5, self._green, "Thunderstorm!")

            else:
                graphics.DrawCircle(canvas, 16, -12, 16, self._green)                           #test
                #no condition
        else:
            pass

# CLOCK AREA

        #original smaller format
        # graphics.DrawText(canvas, self._font_small, 0, 7, self._red, time.strftime("%-2I:%M"))
        # graphics.DrawText(canvas, self._font_small, 21, 13, self._white, time.strftime("%P"))

        #large screen format
        #this hides the leading 0 on numbers less than 10
        if int(time.strftime("%-I")) < 10:
            graphics.DrawText(canvas, self._font_large, 8, 16, self._green, time.strftime("%-I:%M"))
            #graphics.DrawText(canvas, self._font_small, 21, 13, self._white, time.strftime("%P")) # AM / PM

        else:
            graphics.DrawText(canvas, self._font_large, 1, 16, self._green, time.strftime("%-I:%M"))


        # graphics.DrawText(canvas, self._font_small, 2, 22, self._white, time.strftime("%a %b %-d"))

        #temp_str = "%3.0f" % self._weather.cur_temp
        #graphics.DrawText(canvas, self._font_tiny, -4, 5, self._blue, temp_str)
        #graphics.DrawText(canvas, self._font_tiny, 8, 5, self._green, "F")




        # Gradient Backgrounds:

        #     graphics.DrawLine(canvas, 1, 1, 32, 1, self._greyJ)
        #     graphics.DrawLine(canvas, 1, 2, 32, 2, self._greyI)
        #     graphics.DrawLine(canvas, 1, 3, 32, 3, self._greyH)
        #     graphics.DrawLine(canvas, 1, 4, 32, 4, self._greyG)
        #     graphics.DrawLine(canvas, 1, 5, 32, 5, self._greyF)
        #     graphics.DrawLine(canvas, 1, 6, 32, 6, self._greyE)
        #     graphics.DrawLine(canvas, 1, 7, 32, 7, self._greyD)
        #     graphics.DrawLine(canvas, 1, 8, 32, 8, self._greyC)
        #     graphics.DrawLine(canvas, 1, 9, 32, 9, self._greyB)
        #     graphics.DrawLine(canvas, 1, 10, 32, 10, self._greyA)
        #     graphics.DrawLine(canvas, 1, 11, 32, 11, self._grey1)
        #     graphics.DrawLine(canvas, 1, 12, 32, 12, self._grey2)
        #     graphics.DrawLine(canvas, 1, 13, 32, 13, self._grey3)
        #     graphics.DrawLine(canvas, 1, 14, 32, 14, self._grey4)
        #     graphics.DrawLine(canvas, 1, 15, 32, 15, self._grey5)
        #     graphics.DrawLine(canvas, 1, 16, 32, 16, self._grey6)
        #     graphics.DrawLine(canvas, 1, 17, 32, 17, self._grey7)
        #     graphics.DrawLine(canvas, 1, 18, 32, 18, self._grey8)
        #     graphics.DrawLine(canvas, 1, 19, 32, 19, self._grey9)

            # graphics.DrawLine(canvas, 1, 1, 32, 1, self._grey9)
            # graphics.DrawLine(canvas, 1, 2, 32, 2, self._grey8)
            # graphics.DrawLine(canvas, 1, 3, 32, 3, self._grey7)
            # graphics.DrawLine(canvas, 1, 4, 32, 4, self._grey6)
            # graphics.DrawLine(canvas, 1, 5, 32, 5, self._grey5)
            # graphics.DrawLine(canvas, 1, 6, 32, 6, self._grey4)
            # graphics.DrawLine(canvas, 1, 7, 32, 7, self._grey3)
            # graphics.DrawLine(canvas, 1, 8, 32, 8, self._grey2)
            # graphics.DrawLine(canvas, 1, 9, 32, 9, self._grey1)
            # graphics.DrawLine(canvas, 1, 10, 32, 10, self._greyA)
            # graphics.DrawLine(canvas, 1, 11, 32, 11, self._greyB)
            # graphics.DrawLine(canvas, 1, 12, 32, 12, self._greyC)
            # graphics.DrawLine(canvas, 1, 13, 32, 13, self._greyD)
            # graphics.DrawLine(canvas, 1, 14, 32, 14, self._greyE)
            # graphics.DrawLine(canvas, 1, 15, 32, 15, self._greyF)
            # graphics.DrawLine(canvas, 1, 16, 32, 16, self._greyG)
            # graphics.DrawLine(canvas, 1, 17, 32, 17, self._greyH)
            # graphics.DrawLine(canvas, 1, 18, 32, 18, self._greyI)
            # graphics.DrawLine(canvas, 1, 19, 32, 19, self._greyJ)


            #TEMPERATURE STRINGS

        # temp_str = "%3.00d" % self._weather.cur_temp
        # graphics.DrawText(canvas, self._font_tiny, 5, 5, self._blue, temp_str)

        # hi_str = "%3.0f" % self._weather.high_temp
        # graphics.DrawText(canvas, self._font_small, 22, 31, self._white, hi_str)
        # graphics.DrawText(canvas, self._font_tiny, 40, 31, self._red, "F")

        # low_str = "%3.0f" % self._weather.low_temp
        # graphics.DrawText(canvas, self._font_small, 43, 31, self._white, low_str)
        # graphics.DrawText(canvas, self._font_tiny, 61, 31, self._blue, "F")

    def run(self):
        canvas = self._matrix.CreateFrameCanvas()

        while True:
            self._draw(canvas)
            time.sleep(0.05)
            canvas = self._matrix.SwapOnVSync(canvas)
            self._matrix.brightness = self._dimmer.brightness
