import moviepy.editor as mp
from tkinter.filedialog import askopenfilename
import tkinter as tk

root = tk.Tk()
root.withdraw()

vid = askopenfilename()

if vid:
    video = mp.VideoFileClip(vid)

    
    aud = video.audio


    aud.write_audiofile("demo.mp3")

    print("Audio extraction and conversion successful!")
else:
    print("No file selected.")

print("--End---")

