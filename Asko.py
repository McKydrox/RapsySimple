from tkinter import *
import pytube
from PIL import Image

root = Tk()

root.geometry('600x400')
root.resizable(0,0)
canvas = Canvas(root, bg="#4392F1", height=400, width=800, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)
root.title("YouTube Video Downloader")
background_img = PhotoImage()
background = canvas.create_image(400.0, 200.0, image=background_img)
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


link = StringVar()
Label(root, text = 'Paste Youtube Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 90, y = 90)
def Downloader():
    url = pytube.YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(r'Video Downloaded')
    Label(root, text = ' VIDEO DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()