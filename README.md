
# Soma FM Radio
* [Soma FM](http://somafm.com) is an internet radio station with an eclectic choice of stations.
* This project turns your Raspberry Pi into a dedicated Soma FM radio.
* The project requires an [LCD Display with RGB Backlight and Touch Buttons.](<https://thepihut.com/products/gfx-hat-128x64-lcd-display-with-rgb-backlight-and-touch-buttons>)

The code needs a bit of organising; see/execute: command_pattern.py to use it.

## Preparation: 

 1. Obtain a Raspberry Pi 3B+ and slap on Raspbian

    pi@somafm:~ $ uname -a
    Linux somafm 5.10.17-v7+ #1403 SMP Mon Feb 22 11:29:51 GMT 2021 armv7l GNU/Linux
    pi@somafm:~ $ cat /etc/os-release
    PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
    NAME="Raspbian GNU/Linux"
    VERSION_ID="10"
    VERSION="10 (buster)"
    VERSION_CODENAME=buster
    ID=raspbian
    ID_LIKE=debian
    HOME_URL="http://www.raspbian.org/"
    SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
    BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

 2. Install the GFX Hat
    
    pi@somafm:~ $ curl -sS https://get.pimoroni.com/gfxhat | bash
    
    This script will install everything needed to use
    GFX HAT
    
    Always be careful when running scripts and commands copied
    from the internet. Ensure they are from a trusted source.
    
    If you want to see what this script does before running it,
    you should run: 'curl https://get.pimoroni.com/gfxhat'
    
    Note: GFX HAT requires SPI communication
    Note: GFX HAT requires I2C communication
    
    Do you wish to continue? [y/N] y
    
    Checking environment...
    Updating apt indexes...
    .....................
    
    Checking hardware requirements...
    
    Checking for packages required for GPIO control...
    RPi.GPIO installed and up-to-date
    
    SPI must be enabled for GFX HAT to work
    SPI is now enabled
    
    Checking packages required by SPI interface...
    spidev installed and up-to-date
    
    I2C must be enabled for GFX HAT to work
    I2C is now enabled
    
    Checking packages required by I2C interface...
    Python 2 smbus installed and up-to-date
    Python 3 smbus installed and up-to-date
    
    GFX HAT comes with examples and documentation that you may wish to install.
    Performing a full install will ensure those resources are installed,
    along with all required dependencies. It may however take a while!
    
    Do you wish to perform a full install? [y/N] y
    
    Checking for dependencies...
    python-sn3218 is already installed
    python3-sn3218 is already installed
    python-cap1xxx is already installed
    python3-cap1xxx is already installed
    
    Installing GFX HAT library for Python 2...
    
    Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
    Collecting gfxhat
      Downloading https://files.pythonhosted.org/packages/e1/bf/decc90cb5252ead4145a70c782f366194db0fb43322d51222abf1c877509/gfxhat-0.0.1-py2-none-any.whl (240kB)
        100% |████████████████████████████████| 245kB 333kB/s 
    Requirement already satisfied: sn3218 in /usr/lib/python2.7/dist-packages (from gfxhat) (1.2.7)
    Requirement already satisfied: cap1xxx in /usr/lib/python2.7/dist-packages (from gfxhat) (0.1.3)
    Requirement already satisfied: RPi.GPIO in /usr/lib/python2.7/dist-packages (from cap1xxx->gfxhat) (0.7.0)
    Installing collected packages: gfxhat
    Successfully installed gfxhat-0.0.1
    
    Installing GFX HAT library for Python 3...
    
    Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
    Collecting gfxhat
      Downloading https://files.pythonhosted.org/packages/a5/29/c04d56b51e7aad72671a72247459d3e05fff9a7c827a7cebcb2af35e1c94/gfxhat-0.0.1-py3-none-any.whl (240kB)
        100% |████████████████████████████████| 245kB 735kB/s 
    Requirement already satisfied: cap1xxx in /usr/lib/python3/dist-packages (from gfxhat) (0.1.3)
    Requirement already satisfied: sn3218 in /usr/lib/python3/dist-packages (from gfxhat) (1.2.7)
    Requirement already satisfied: RPi.GPIO in /usr/lib/python3/dist-packages (from cap1xxx->gfxhat) (0.7.0)
    Installing collected packages: gfxhat
    Successfully installed gfxhat-0.0.1
    
    Checking for additional software...
    python-pil is already installed
    python3-pil is already installed
    
    Downloading examples and documentation...
    Resources for your GFX HAT were copied to
    /home/pi/Pimoroni/gfxhat
    
    All done. Enjoy your GFX HAT!

 3. There's a chance the gfxhat libraries are out of date, despite the above.
    If you get an error running the gfx hat examples, e.g. contrast-scanner.py:
    File “contrast-scanner.py”, line 60, in
    lcd.contrast(0)
    AttributeError: ‘module’ object has no attribute ‘contrast’		
    This is my (hacky) fix (for python3), which grabs the latest files and uses them instead of what was installed:
    pi@somafm:~ $ cd /usr/local/lib/python3.7/dist-packages
    pi@somafm:/usr/local/lib/python3.7/dist-packages $ sudo mkdir old
    pi@somafm:/usr/local/lib/python3.7/dist-packages $ sudo mv gfxhat old/
    pi@somafm:/usr/local/lib/python3.7/dist-packages $ sudo git clone https://github.com/pimoroni/gfx-hat
    Cloning into 'gfx-hat'...
    remote: Enumerating objects: 33, done.
    remote: Counting objects: 100% (33/33), done.
    remote: Compressing objects: 100% (24/24), done.
    remote: Total 276 (delta 7), reused 23 (delta 7), pack-reused 243
    Receiving objects: 100% (276/276), 355.06 KiB | 2.32 MiB/s, done.
    Resolving deltas: 100% (123/123), done.
    pi@somafm:/usr/local/lib/python3.7/dist-packages $ sudo cp -r gfx-hat/library/gfxhat gfxhat
This is the fix I posted here: https://forums.pimoroni.com/t/gfx-hat-contrast-problems/11610 maybe pimoroni will fix this someday..
    
 3. Install the VLC libary
    pi@somafm:~ $  sudo pip3 install python-vlc
    Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
    Collecting python-vlc
      Downloading https://files.pythonhosted.org/packages/e3/8e/1d0f30c4f8741f09014f961d49c55b1590d546e2199a54f396d288e978dd/python_vlc-3.0.11115-py3-none-any.whl (80kB)
        100% |████████████████████████████████| 81kB 429kB/s 
    Installing collected packages: python-vlc
    Successfully installed python-vlc-3.0.11115
