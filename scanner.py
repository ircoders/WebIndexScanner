import urllib2
import sys
import time
import random
import os
import re
import urllib
import requests

try:

    from colorama import Fore, Back, Style

except ImportError:
    print '[*] pip install colorama'
    print '   [-] You need to install colorama Module!'
    sys.exit()

r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA
res = Style.RESET_ALL

def Clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


def Welcome():
    Clear()
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37, 30, 33, 38, 39]
    Text = """
    +=============================================================+
    |                  WebSite  InDeX  Scanner                    |
    |                   Writed By : HydraBoy                      |
    |                     iraniancoders.ir                        |
    +=============================================================+
    """
    for N, line in enumerate(Text.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.01)


def ScanIndex(WebSite=None):
    try:
        print('{}     [{}+{}] {}WebSite:{} {}'.format(r,y,r,g,b,WebSite))
        print('{}        [{}~{}] {}Scan For Information...{} '.format(r,y,r,g,b))
        time.sleep(1)
        Index = urllib.urlopen(WebSite).read()
        StyleFiles = re.findall('<link href="(.*?)"', Index)
        Images = re.findall('<img src="(.*?)"', Index)
        ScriptFiles = re.findall('<script src="(.*?)"', Index)
        Links = re.findall('<a href="(.*?)"', Index)
        Email = re.findall('<a href="mailto:(.*?)"', Index)
        Tel = re.findall('<a href="tel:(.*?)"', Index)
        Callto = re.findall('<a href="callto:(.*?)"', Index)
        Fax = re.findall('<a href="fax:(.*?)"', Index)

        # Start (Grab Information)

        for email in enumerate(Email):
                print('{}     [{}+{}] {}E-Mail Found:{} {}'.format(r,y,r,g,b,email[1]))
                time.sleep(0.20)

        for tel in enumerate(Tel):
                print('{}     [{}+{}] {}TelPhoneNumber Found:{} {}'.format(r,y,r,g,b,tel[1]))
                time.sleep(0.20)

        for callto in enumerate(Callto):
                print('{}     [{}+{}] {}SkypeNumber Found:{} {}'.format(r,y,r,g,b,callto[1]))
                time.sleep(0.20)

        for faz in enumerate(Fax):
                print('{}     [{}+{}] {}FaxNumber Found:{} {}'.format(r,y,r,g,b,fax[1]))
                time.sleep(0.20)
        # End Of Grabing Information

        # Start (Step 1)
        print('{}        [{}~{}] {}Scan For Script Files...{} '.format(r,y,r,g,b))
        time.sleep(0.10)

        for script in enumerate(ScriptFiles):
            if 'https://' not in script[1]:
                if 'http://' in script[1]:
                    print('{}     [{}+{}] {}Script Found:{} {}'.format(r,y,r,g,b,script[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}Script Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',script[1]))
                    time.sleep(0.20)
            elif 'http://' not in script[1]:
                if 'https://' in script[1]:
                    print('{}     [{}+{}] {}Script Found:{} {}'.format(r,y,r,g,b,script[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}Script Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',script[1]))
                    time.sleep(0.20)
            else:
                print('{}     [{}+{}] {}Script Found:{} {}'.format(r,y,r,g,b,script[1]))
                time.sleep(0.20)

        # End Of Searching (Step 1)
        print('{}        [{}~{}] {}Scan For Links...{} '.format(r,y,r,g,b))
        #time.sleep(3)
        # Start (Step 2)

        for link in enumerate(Links):
            if str(link[1]) == "#":
                pass
            elif re.findall('#(.*)', link[1]):
                pass
            elif re.findall('mailto:(.*)', link[1]):
                pass
            else:
                if 'https://' not in link[1]:
                    if 'http://' in link[1]:
                        print('{}     [{}+{}] {}Link Found:{} {}'.format(r,y,r,g,b,link[1]))
                        time.sleep(0.20)
                    else:
                        print('{}     [{}+{}] {}Link Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',link[1]))
                        time.sleep(0.20)
                elif 'http://' not in link[1]:
                    if 'https://' in link[1]:
                        print('{}     [{}+{}] {}Link Found:{} {}'.format(r,y,r,g,b,link[1]))
                        time.sleep(0.20)
                    else:
                        print('{}     [{}+{}] {}Link Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',link[1]))
                        time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}Link Found:{} {}'.format(r,y,r,g,b,link[1]))
                    time.sleep(0.20)


        # End Of Searching (Step 2)
        print('{}        [{}~{}] {}Scan For StyleFiles...{} '.format(r,y,r,g,b))
        time.sleep(3)
        # Start (Step 3)

        for style in enumerate(StyleFiles):
            if 'https://' not in style[1]:
                if 'http://' in style[1]:
                    print('{}     [{}+{}] {}StyleFile Found:{} {}'.format(r,y,r,g,b,style[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}StyleFile Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',style[1]))
                    time.sleep(0.20)
            elif 'http://' not in style[1]:
                if 'https://' in style[1]:
                    print('{}     [{}+{}] {}StyleFile Found:{} {}'.format(r,y,r,g,b,style[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}StyleFile Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',style[1]))
                    time.sleep(0.20)
            else:
                print('{}     [{}+{}] {}StyleFile Found:{} {}'.format(r,y,r,g,b,style[1]))
                time.sleep(0.20)

        # End Of Searching (Step 3)
        print('{}        [{}~{}] {}Scan For Images...{} '.format(r,y,r,g,b))
        time.sleep(3)
        # Start (Step 4)

        for Image in enumerate(Images):
            if 'https://' not in Image[1]:
                if 'http://' in Image[1]:
                    print('{}     [{}+{}] {}Image Found:{} {}'.format(r,y,r,g,b,Image[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}Image Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',Image[1]))
                    time.sleep(0.20)
            elif 'http://' not in Image[1]:
                if 'https://' in Image[1]:
                    print('{}     [{}+{}] {}Image Found:{} {}'.format(r,y,r,g,b,Image[1]))
                    time.sleep(0.20)
                else:
                    print('{}     [{}+{}] {}Image Found:{} {}{}'.format(r,y,r,g,b,WebSite + '/',Image[1]))
                    time.sleep(0.20)
            else:
                print('{}     [{}+{}] {}Image Found:{} {}'.format(r,y,r,g,b,Image[1]))
                time.sleep(0.20)


        # End Of Searching (Step 4)




    except Exception as Error:
        if 'No such file or directory:' in str(Error):
            print '\n' + r + '    [' + y + '!' + r + ']' + r + ' Invlid Website...' + y
        else:
            print '\n' + r + '    [' + y + '!' + r + ']' + r + ' Error Found: ' + y + str(Error)
    except KeyboardInterrupt:
        print '\n' + r + '    [' + y + '!' + r + ']' + r + ' KeyboardInterrupt found exiting...' + y

try:
    Welcome()
    if '.' not in sys.argv[1]:
        print r + '    [' + y + '!' + r + ']' + r + 'Error Found:' + y +' Pleas Enter a Vilad Site Address.'
        print '  ' + r + '    [' + y + '-' + r + ']' + r + 'Try: ' + y + ' python ' + sys.argv[0] + ' iraniancoders.ir'
    else:
        ScanIndex(WebSite=sys.argv[1])
except Exception as Error:
    if 'list index out of range' in str(Error):
        print '  ' + r + '    [' + y + '-' + r + ']' + r + 'Try: ' + y + ' python ' + sys.argv[0] + ' iraniancoders.ir '
    else:
        print '\n' + r + '    [' + y + '!' + r + ']' + r + ' Error Found: ' + y + str(Error)
