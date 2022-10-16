import requests
import pyperclip
import ctypes
import webbrowser

while True:
    missing = pyperclip.paste()

    bypassURL = "https://bypass.bot.nu/bypass2?" + missing


    params = {'url': missing}

    r = requests.get(bypassURL, params=params)
    jjson = r.json()



    try:

        target = str(jjson['destination'])
        succes_box = "Imported link ==>  "+ missing + "\n\n\nSTATUS:VALID\n\n\n"   + "BYPASS STATUS: OK\n\n\n\n\n\nDo you wish to open it in your Web Browser ?"
        answer = ctypes.windll.user32.MessageBoxW(0,str(succes_box) ,"ARBOFF BYPASSER 1.0           STATUS: SUCCESS", 4)
        # 6 = true 7= false
        if(str(answer) == "6"):
            webbrowser.open(target, new=1)
            strr = "Link coppied to your clipboard. A browser should open now."
            ctypes.windll.user32.MessageBoxW(0, strr, "ARBOFF BYPASSER 1.0           STATUS: SUCCESS", 0)
            pyperclip.copy(jjson['destination'])
            break
        else:
            pyperclip.copy(jjson['destination'])
            link = str(jjson['destination'])
            strr = "Link coppied to your clipboard.\n\nOriginal link routes to:  " + link
            ctypes.windll.user32.MessageBoxW(0, strr , "ARBOFF BYPASSER 1.0           STATUS: SUCCESS", 0)
            break



        break
    except KeyError:
        error_message = "Unexpected Error.\n\nThis might be due to Bad Link / API server down. \n\nPlease, Try again later, or chekc your clipboard bellow.\n\n\n\n\n\n\n\n Current Clipboard:   " + missing
        ctypes.windll.user32.MessageBoxW(0,error_message , "ARBOFF BYPASSER 1.0           STATUS: FAIL", 0)
        break