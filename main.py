from tkinter import *
from button_functions import get_pdf, get_audio_path, convert_pdf_to_audio

# Setting Main Window
root = Tk()
root.title("Welcome to PDF to Audio Book Converter")
#root.geometry('750x600')

# Adding a Label for PDF Path
sPDF_label = Label(root, text = "PDF Path")
sPDF_label.grid(column =0, row =0)

# Adding a Text Entry Box for PDF Path
sPDF_path = Entry(root, width=50)
sPDF_path.grid(column =1, row =0)

# Adding Button to Open A Dialogue Box to Select PDF
PDF_btn = Button(root, bg = 'red', width = 30, text = "Get PDF File" ,
             activebackground = 'white', fg = "black", command=get_pdf)
PDF_btn.grid(column=2, row=0)

# Adding a Label for Audio Path
sAudioPath_label = Label(root, text = "Audio Path")
sAudioPath_label.grid(column =0, row =1)

# Adding a Text Entry Box for Audio Output Path
sAudio_path = Entry(root, width=50)
sAudio_path.grid(column =1, row =1)

# Adding Button to Open A Dialogue Box to Select PDF
Audio_btn = Button(root, bg = 'red', width = 30, 
            activebackground = 'white', text = "Get Path to Save Audio File" ,
             fg = "black", command=get_audio_path)
Audio_btn.grid(column=2, row=1)

# Adding a Label for Audio Path
sAudio_label = Label(root, text = "Audio File Name")
sAudio_label.grid(column =0, row =2)

# Adding a Text Entry Box for Audio File Name
sAudio_path = Entry(root, width=50)
sAudio_path.grid(column =1, row =2)

# Adding a Label for Audio Path
sPages_label = Label(root, text = "Page Range")
sPages_label.grid(column =0, row =3)

# Adding a Text Entry Box for Audio File Name
nPages = Entry(root, width=50)
nPages.grid(column =1, row =3)

# Adding Button to Convert PDF to Audio
Convert_btn = Button(root, height = 2, width = 30, bg = 'green', 
            activebackground = 'lightgreen', text = "Convert PDF to Audio" ,
             fg = "black", command=convert_pdf_to_audio)
Convert_btn.grid(column =2, row =4)

root.mainloop()
