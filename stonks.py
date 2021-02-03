#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import requests
import json

symbol1 = "AMC"
symbol2 = "GME"
symbol3 = "AAPL"

token = "c0d1mk748v6oo0bff2r0"

amc_params = (
    ('symbol', symbol1),
    ('token', token),
)

gme_params = (
    ('symbol', symbol2),
    ('token', token),
)

aapl_params = (
    ('symbol', symbol3),
    ('token', token),
)

amc_response = requests.get('https://finnhub.io/api/v1/quote', params=amc_params)
amc_data = amc_response.json()
amc_price_string = (symbol1 + " | $" + str(amc_data.values()[0]))

gme_response = requests.get('https://finnhub.io/api/v1/quote', params=gme_params)
gme_data = gme_response.json()
gme_price_string = (symbol2 + " | $" + str(gme_data.values()[0]))

aapl_response = requests.get('https://finnhub.io/api/v1/quote', params=aapl_params)
aapl_data = aapl_response.json()
aapl_price_string = (symbol3 + " | $" + str(aapl_data.values()[0]))

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("10x20.bdf")
        textColor = graphics.Color(255, 255, 255)
        pos = offscreen_canvas.width
        my_text = (amc_price_string + " " + gme_price_string + " " + aapl_price_string)

        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
