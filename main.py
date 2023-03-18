from tkinter import *
from tkinter import filedialog
import pyttsx3, PyPDF2
import os

###### Button Functions ######

# Get PDF
def get_pdf():
    PDF_file = filedialog.askopenfilename(title="Open PDF File", filetypes=(("pdf files","*.pdf"), ("all files","*.*")))
    in_file.set(PDF_file)

#Get Audio Path
def get_audio_path():
    Audio_path = filedialog.askdirectory(title="Directory to Save Audio")
    
    out_path.set(Audio_path)

# Convert PDF to Audio
def convert_pdf_to_audio():
    PDF = in_file.get()
    pdfreader = PyPDF2.PdfReader(open(PDF,'rb'))
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices') 
    speaker.setProperty('voice', voices[1].id) 

    sRange = nPageRange.get()
    sRange = sRange.replace('[', '')
    sRange = sRange.replace(']', '')
    sRange = sRange.split('-')
    
    nRange = list(sRange)
    nRange[0] = int(nRange[0])
    nRange[1] = int(nRange[1])

    clean_text = ''
    for page_num in range(nRange[0]-1, nRange[1]-1):
        text = pdfreader.pages[page_num].extract_text()
        clean_text += text.strip().replace('\n', ' ')

    path = out_path.get()
    file = audio_file.get()
    file = file + '.mp3'

    save_file = os.path.join(path,file)
    speaker.save_to_file(clean_text, save_file)
    speaker.runAndWait()

    speaker.stop()

###### GUI ######

# Setting Main Window
root = Tk()
root.title("Welcome to PDF to Audio Book Converter")
#root.geometry('750x600')

# Adding a Label for PDF Path
sPDF_label = Label(root, text = "PDF Path")
sPDF_label.grid(column =0, row =0)

# Adding a Text Entry Box for PDF Path
in_file = StringVar()
sPDF_path = Entry(root, width=50, textvariable=in_file)
sPDF_path.grid(column =1, row =0)

# Adding Button to Open A Dialogue Box to Select PDF
PDF_btn = Button(root, bg = 'red', width = 30, text = "Get PDF File" ,
             activebackground = 'white', fg = "black", command=get_pdf)
PDF_btn.grid(column=2, row=0)

# Adding a Label for Audio Path
sAudioPath_label = Label(root, text = "Audio Path")
sAudioPath_label.grid(column =0, row =1)

# Adding a Text Entry Box for Audio Output Path
out_path = StringVar()
sAudio_path = Entry(root, width=50, textvariable=out_path)
sAudio_path.grid(column =1, row =1)

# Adding Button to Open A Dialogue Box to Select Audio Path
Audio_btn = Button(root, bg = 'red', width = 30, 
            activebackground = 'white', text = "Get Path to Save Audio File" ,
             fg = "black", command=get_audio_path)
Audio_btn.grid(column=2, row=1)

# Adding a Label for Audio File
sAudio_label = Label(root, text = "Audio File Name")
sAudio_label.grid(column =0, row =2)

# Adding a Text Entry Box for Audio File Name
audio_file = StringVar()
sAudio_file = Entry(root, width=50, textvariable=audio_file)
sAudio_file.grid(column =1, row =2)

# Adding a Label for Page Range
sPages_label = Label(root, text = "Page Range")
sPages_label.grid(column =0, row =3)

# Adding a Text Entry Box for Page Range
nPageRange = StringVar()
nPages = Entry(root, width=50, textvariable=nPageRange)
nPages.insert(0, "[-]")
nPages.grid(column =1, row =3)

# Adding Button to Convert PDF to Audio
Convert_btn = Button(root, height = 2, width = 30, bg = 'green', 
            activebackground = 'lightgreen', text = "Convert PDF to Audio" ,
             fg = "black", command=convert_pdf_to_audio)
Convert_btn.grid(column =2, row =4)

root.mainloop()
