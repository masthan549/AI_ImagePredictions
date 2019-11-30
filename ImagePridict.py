
from clarifai.rest import ClarifaiApp
from tkinter import Label, Button, Entry
from tkinter import filedialog, messagebox, StringVar, BOTTOM, X, SUNKEN, W, DISABLED

import tkinter as tk
import sys, os, time
import tkinter.scrolledtext as tkscrolled

class GUI_COntroller:
    '''
       This class initialize the required controls for TkInter GUI
    '''
    def __init__(self,TkObject):
 

        global imageLocation_dynamicUpdate, statusBarText, TkObject_ref, predictionResult
        TkObject_ref = TkObject

        #Load company image
        Imageloc = tk.PhotoImage(file='./Images/alstom_logo.gif')
        logLabel=Label(image=Imageloc,)
        logLabel.image = Imageloc
        logLabel.place(x=200,y=20)

        #Select Prediction image label
        ImagelocBrowseButton=Button(TkObject_ref, text="Click Here to browse image location", fg="black", cursor="hand2", command=lambda:GUI_COntroller.openfile(self))
        ImagelocBrowseButton.place(x=10, y=120)
        ImagelocBrowseButton.config(font=('helvetica', 10, 'bold'))

        # 1. Select model train data
        imageLocation_dynamicUpdate = tk.StringVar()
        imageLocStorage = Entry(TkObject_ref, width=80, textvariable=imageLocation_dynamicUpdate, bd=1)
        imageLocStorage.place(x=265, y=125)
        imageLocStorage.config(font=('helvetica', 10), state=DISABLED)

        #Exit Window
        closeButton=Button(TkObject_ref,activebackground='green',borderwidth=3, text='Close Window', command=GUI_COntroller.exitWindow)
        closeButton.place(x=650,y=180)
        closeButton.config(font=('helvetica',10,'bold'))

        #1. Run Pridiction
        processPredictionButton=Button(TkObject_ref, activebackground='green',borderwidth=3, anchor="w", text='Run ML Prediction Model', command=lambda:GUI_COntroller.startPridiction(self, TkObject_ref), cursor="hand2")
        processPredictionButton.place(x=350, y=180)
        processPredictionButton.config(font=('helvetica',10,'bold'))

        #Fill status bar
        statusBarText = StringVar()
        StatusLabel = Label(TkObject_ref, textvariable=statusBarText, fg="green", bd=1,relief=SUNKEN,anchor=W)
        StatusLabel.config(font=('helvetica',11,'bold'))
        StatusLabel.pack(side=BOTTOM, fill=X)

        #Print prediction results in scrollable view.
        predictionResult = tkscrolled.ScrolledText(width = 99, wrap='word')
        predictionResult.place(x=20, y=240)
        statusBarText.set("Prediction result will be displayed in text box...")

    def startPridiction(self, TkObject_ref):

        if not os.path.isfile(imageLocation_dynamicUpdate.get()):
            messagebox.showerror('Error', 'Please Select valid image and try again!')
            statusBarText.set(" ")
        else:
            imageLoc = imageLocation_dynamicUpdate.get()

            #################  CORE LOGIC TO BUILD MODEL ######################

            try:

                #Build model which pridicts image attributes
                app = ClarifaiApp(api_key='9229dbaf8f044284b4837d397b50d372')
                model = app.public_models.general_model
                response = model.predict_by_filename(imageLoc)

                #Display pridicted attributes on UI
                concepts = response['outputs'][0]['data']['concepts']
                result = "\t   NAME\t\t\t\t  Prediction (%)\n"
                result = result + "\t========= \t\t\t\t================\n\n"
                for concept in concepts:
                    result = result+"\t"+concept['name']+" \t\t\t\t:: \t"+str(round((concept['value']*100),4))+"\n"
                    #print(concept['name'], concept['value'])

                predictionResult.insert(1.0, result)

                #################  END OF CORE LOGIC ######################

                statusBarText.set("DONE, please look at predictions!")
                messagebox.showinfo('DONE!!', "Please look at predictions in text field!")

            except Exception as e:
                predictionResult.insert(1.0, e)
                statusBarText.set("Exception raised while predicting, please look at error details given!")
                messagebox.showinfo('Exception!!', "Exception raised while predicting, please look at error details given!")

    def openfile(self):
        global imageLocation_dynamicUpdate
        selectedImage = filedialog.askopenfilename(initialdir = "/", title = "Select Image for which you want predictions ",filetypes = (("Image types (png/jpg)","*.jpg;*.png"), ("all files","*.*")))
        imageLocation_dynamicUpdate.set(selectedImage)

    def exitWindow():
            TkObject_ref.destroy()

if __name__ == '__main__':
    root = tk.Tk()

    # Change the background window color
    root.configure(background='#b7bbc7')

    # Set window parameters
    root.geometry('850x680')
    root.title('Image Prediction with ML modeling')

    # Removes the maximizing option
    root.resizable(0, 0)

    ObjController = GUI_COntroller(root)

    # keep the main window is running
    root.mainloop()
    sys.exit()
