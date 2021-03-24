
# Soma FM Radio
* [Soma FM](http://somafm.com) is an internet radio station with an eclectic choice of stations.
* This project turns your Raspberry Pi into a dedicated Soma FM radio.
* The project requires an [LCD Display with RGB Backlight and Touch Buttons.](<https://thepihut.com/products/gfx-hat-128x64-lcd-display-with-rgb-backlight-and-touch-buttons>)

## Preparation: 

 1. Obtain a Raspberry Pi 3B+ and slap on Raspbian. I used Buster.

 2. Install the GFX Hat library:
 
```
curl -sS https://get.pimoroni.com/gfxhat | bash
```

 3. There's a chance the  GFX Hat library is out of date.
    If you get an error running the gfx hat examples, e.g. contrast-scanner.py:
    
```
File “contrast-scanner.py”, line 60, in
lcd.contrast(0)
AttributeError: ‘module’ object has no attribute ‘contrast’
```

This is a (hacky) fix (for python3), which grabs the latest files and uses them instead of what was installed:

```
cd /usr/local/lib/python3.7/dist-packages
sudo mkdir old
sudo mv gfxhat old
sudo git clone https://github.com/pimoroni/gfx-hat
sudo cp -r gfx-hat/library/gfxhat gfxhat
```

Pimoroni have been alerted, the thread is here: https://forums.pimoroni.com/t/gfx-hat-contrast-problems/11610
   
 3. Install the VLC libary
``` 
sudo pip3 install python-vlc
    Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
    Collecting python-vlc
      Downloading https://files.pythonhosted.org/packages/e3/8e/1d0f30c4f8741f09014f961d49c55b1590d546e2199a54f396d288e978dd/python_vlc-3.0.11115-py3-none-any.whl (80kB)
        100% |████████████████████████████████| 81kB 429kB/s 
    Installing collected packages: python-vlc
    Successfully installed python-vlc-3.0.11115
```
 4. The code needs a bit of organising; run `command_pattern.py` to start using it.
