import pyttsx3, PyPDF2

def get_pdf():
    ''

def get_audio_path():
    ''

def convert_pdf_to_audio():
    pdfreader = PyPDF2.PdfReader(open("D:\\NERL_Lab\\Publications\\Papers\\NASA Conference\\paper\\Microgravity Skill Acquisition Manuscript_FINAL.pdf",'rb'))
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150)
    voices = speaker.getProperty('voices') 
    speaker.setProperty('voice', voices[1].id) 

    for page_num in range(len(pdfreader.pages)):
        text = pdfreader.pages[page_num].extract_text()
        clean_text = text.strip().replace('\n', ' ')

    speaker.save_to_file(clean_text,'D:\\Audio Books\\IAC_Paper.mp3')
    speaker.runAndWait()

    speaker.stop()

