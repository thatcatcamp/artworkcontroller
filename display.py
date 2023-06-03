import tkinter as tk
from tkVideoPlayer import TkinterVideo


def update_duration(event):
    """ updates the duration after finding the duration """
    duration = vid_player.video_info()["duration"]


def update_scale(event):
    """ updates the scale value """

def video_ended(event):
    """ handle video ended """
    print("ended")
    exit(0)


root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("hoomanfood")
vid_player = TkinterVideo(scaled=True, master=root)
vid_player.pack(expand=True, fill="both")
vid_player.bind("<<Ended>>", video_ended)
vid_player.load("sample.mp4")
vid_player.play()
root.mainloop()
