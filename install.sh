#!/bin/bash
cd rpi-rgb-led-matrix
echo "Running rgbmatrix installation..."
sudo apt-get update && sudo apt-get install python2.7-dev python-pillow -y
make build-python
sudo make install-python
cd bindings
sudo pip install -e python/
cd ../../

echo "Installation complete! Run the ticker with sudo python runtext.py --led-gpio-mapping=adafruit-hat --led-cols=64 --led-rows=32"
