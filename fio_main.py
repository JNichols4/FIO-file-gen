import generators
import structures as s
import Tkinter as tk

# Things to remember with FIO:
# ';' and '#' denote commented-out lines
# global section sets defaults for the jobs described in the file.
# global section is defined as [global] and all values below it are considered global children.
# Jobs can over-ride global section params, and jobs can have multiple global params.
# Jobs are only affected by the global section above them.
# Jobs are denoted as [job #n] in brackets.
#
# File structure: Global, Global Params, Job 1, Job1 params, Job 2, Job 2 params.. etc.

#fio file repository for all fio files

file_repository = 'C:\\Users\\njordan\\Desktop\\fio files'

#pre-converted file name
fileName = 'generic_txt_to_fio_name.txt'

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)

        #define the variables
        self.staticIntVarGlobal = tk.IntVar()
        self.staticIntVarJobs = tk.IntVar()

        #define the text window
        self.globalsWindow = tk.Text(master, height=15,width=25,font=('Helvetica',8),bd=3)
        self.jobsWindow = tk.Text(master,height=15,width=25,font=('Helvetica',8),bd=3)

        #define radio buttons
        self.globalRadiobutton = tk.Radiobutton(master, text='Enable Globals',variable=self.staticIntVarGlobal,value=0)
        self.globalRadiobutton1 = tk.Radiobutton(master, text='Disable Globals',variable=self.staticIntVarGlobal,value=1)
        self.numofjobsRadiobutton = tk.Radiobutton(master, text='Enable Jobs',variable=self.staticIntVarJobs,value=0)
        self.numofjobsRadiobutton1 = tk.Radiobutton(master, text='Disable Jobs',variable=self.staticIntVarJobs,value=1)

        #define the buttons
        self.button1 = tk.Button(master, text='Proceed',command=self.proceed)

        #define text entries
        self.numofjobsEntry = tk.Entry(master,bd=2)


        #structure the frame
        self.globalRadiobutton.grid(row=0,column=0)
        self.globalRadiobutton1.grid(row=0,column=1)
        self.numofjobsRadiobutton.grid(row=1,column=0)
        self.numofjobsRadiobutton1.grid(row=1,column=1)
        self.button1.grid(row=2,columnspan=2)
        #self.numofjobsEntry.grid(row=2,column=0)
        #self.globalsWindow.grid(row=3,column=0,columnspan=1)
        #self.jobsWindow.grid(row=3,column=1,columnspan=1)

        #self.globalsWindow.insert(tk.END,'Globals:\n')
        #self.jobsWindow.insert(tk.END,'Jobs:\n')
    def proceed(self):
        return 0

if __name__ == "__main__":
    rootWindow = tk.Tk()
    rootWindow.title('FIO File Generator')
    app = App(rootWindow)
    app.mainloop()