from Tkinter import Tk, Frame, Button, Label
from Tkinter import BOTH, BOTTOM, RIGHT
import subprocess

#basic function
def shutdown():
    subprocess.call(["shutdown", "-s", "-t", "60"])
def abortShutdown():
    subprocess.call(["shutdown", "-a"])

#Our Full Screen App, inheriting from Frame
class FullScreenApp(Frame):

    #set App properties than call the initUI function
    def __init__(self, parent):
        #call Frame constructor, set background
        Frame.__init__(self, parent, background="black")
        #remove root titlebar
        parent.overrideredirect(1)
        #set the root geometry as full screen
        self.wRoot, self.hRoot = parent.winfo_screenwidth(), parent.winfo_screenheight()
        parent.geometry("%dx%d+0+0" % (self.wRoot, self.hRoot))
        #bind the escape key to the exit function
        parent.bind('<Escape>', lambda f: self.root.quit())
        #save root and call initUI function
        self.root = parent
        self.initUI()

    def initUI(self):
        #top frame using all the remaining space
        innerTopFrame = Frame(self, background="black")
        innerTopFrame.pack(fill=BOTH, expand=1)
        #CLOSE Label
        innerBottomLeftFrame = Frame(self, background="black")
        innerBottomLeftFrame.place(x=0, width=self.wRoot/2, 
            y=self.hRoot-200, height=200)
        closeLabel = Label(innerBottomLeftFrame, bg="black", fg="black",
            text="CLOSE", font=("Comic Sans MS", 48, "bold"))
        innerBottomLeftFrame.bind("<Enter>", lambda f: closeLabel.config(fg="white"))
        innerBottomLeftFrame.bind("<Leave>", lambda f: closeLabel.config(fg="black"))
        innerBottomLeftFrame.bind("<Button-1>", lambda f: self.root.quit())
        closeLabel.bind("<Button-1>", lambda f: self.root.quit())
        closeLabel.pack(fill=BOTH)
        #SHUT DOWN Label
        innerBottomRightFrame = Frame(self, background="black")
        innerBottomRightFrame.place(x=self.wRoot/2, width=self.wRoot/2, 
            y=self.hRoot-200, height=200)
        shutdownLabel = Label(innerBottomRightFrame, bg="black", fg="black",
            text="SHUT DOWN", font=("Comic Sans MS", 48, "bold"))
        innerBottomRightFrame.bind("<Enter>", lambda f: shutdownLabel.config(fg="white"))
        innerBottomRightFrame.bind("<Leave>", lambda f: shutdownLabel.config(fg="black"))
        innerBottomRightFrame.bind("<Button-1>", self.shutdown)
        shutdownLabel.bind("<Button-1>", self.shutdown)
        shutdownLabel.pack(fill=BOTH)
        #design the FullScreenApp
        self.pack(fill=BOTH, expand=1)
    
    def shutdown(self, event):
        shutdown()
        self.root.quit()

def main():
    #abort shutdown
    abortShutdown()
    #load the application
    root = Tk()
    app = FullScreenApp(root)
    root.mainloop()

#run just if it is the main
if __name__ == '__main__':
    main()  