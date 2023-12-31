import os

def wget(url, filename):
    from urequests import get
    r = get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)
 
# Install Webserver
if not 'www' in os.listdir(): os.mkdir("/www")
get("https://raw.githubusercontent.com/jczic/MicroWebSrv/master/microWebTemplate.py", "microWebTemplate.py")
wget("https://raw.githubusercontent.com/jczic/MicroWebSrv/master/microWebSrv.py", "microWebSrv.py")

#Sample Files
wget("https://raw.githubusercontent.com/jczic/MicroWebSrv/master/www/index.html","www/index.html")
wget("https://raw.githubusercontent.com/jczic/MicroWebSrv/master/www/test.pyhtml","www/test.pyhtml")

#Install the running files
if not 'logs' in os.listdir(): os.mkdir("/logs")
wget("https://raw.githubusercontent.com/RattyDAVE/micropython/master/www/boot.py","boot.py")
wget("https://raw.githubusercontent.com/RattyDAVE/micropython/crypto/master/www/main.py","main.py")
wget("https://raw.githubusercontent.com/RattyDAVE/micropython/crypto/master/www/functions.py","functions.py")

#Install Libs
if not 'lib' in os.listdir(): os.mkdir("/lib")
wget("https://raw.githubusercontent.com/RattyDAVE/EPD_2in13_B_V4_Landscape/main/EPD_2in13_B_V4_Landscape.py","lib/EPD_2in13_B_V4_Landscape.py")
