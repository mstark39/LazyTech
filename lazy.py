import tkinter
import customtkinter
from tkinter import ttk
import ctypes

def runCommands():
    sfc = item_sfc_var.get()
    dism = item_dism_var.get()
    avQuick = item_av_quick_var.get()
    avFull = item_av_full_var.get()
    wuModule = item_psupdate_module_var.get()
    wuCheck = item_psupdate_check_var.get()
    wuInstall = item_psupdate_install_var.get()
    
    # Windows Tools Logic
    if sfc and dism == "1":
        run_both_cmd()
    else:
        if sfc == "1":
            run_sfc_cmd()
        if dism == "1":
            run_dism_cmd()
    
    # AntiVirus Logic


    






window = tkinter.Tk()
window.title("Lazy Tech 1.0")
# window.geometry("800x600")
# window.iconbitmap("lt_logo.ico")
# window.grid_rowconfigure(0, weight = 1)
# window.grid_columnconfigure(1, weight=1)

frame = tkinter.Frame(window)
frame.pack()

# Windows Tools CMD and Powershell Commands
tools_frame = tkinter.LabelFrame(frame, text = "Windows Tools")
tools_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)

item_sfc_var = tkinter.StringVar()
item_sfc_var.set(False)
item_sfc = tkinter.Checkbutton(tools_frame, text = "SFC (Scan and Repair", variable=item_sfc_var, onvalue="1", offvalue="0")
item_sfc.grid(row=0, column=0, padx=1, pady=1)

item_dism_var = tkinter.StringVar()
item_dism_var.set(False)
item_dism = tkinter.Checkbutton(tools_frame, text = "DISM Restore Health", variable=item_dism_var, onvalue="1", offvalue="0")
item_dism.grid(row=1, column=0, padx=1, pady=1)

for widget in tools_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Windows Antivirus tools
av_frame = tkinter.LabelFrame(frame, text = "AntiVirus Tools")
av_frame.grid(row = 1, column = 0, sticky="news", padx=20, pady=10)

item_av_quick_var = tkinter.StringVar()
item_av_quick_var.set(False)
item_av_quick = tkinter.Checkbutton(av_frame, text = "Windows Defendar (Quick Scan)", variable=item_av_quick_var, onvalue="1", offvalue="0")
item_av_quick.grid(row=0, column=0, padx=1, pady=1)

item_av_full_var = tkinter.StringVar()
item_av_full_var.set(False)
item_av_full = tkinter.Checkbutton(av_frame, text = "Windows Defendar (Quick Scan)", variable=item_av_full_var, onvalue="1", offvalue="0")
item_av_full.grid(row=1, column=0, padx=1, pady=1)

for widget in av_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Windows updates tools
windows_updates_frame = tkinter.LabelFrame(frame, text = "Windows Updates Tools")
windows_updates_frame.grid(row = 2, column = 0, sticky="news", padx=20, pady=10)

item_psupdate_module_var = tkinter.StringVar()
item_psupdate_module_var.set(False)
item_psupdate_module = tkinter.Checkbutton(windows_updates_frame, text = "Install PSWindows Updates Module", variable=item_psupdate_module_var, onvalue="1", offvalue="0")
item_psupdate_module.grid(row=0, column=0, padx=1, pady=1, sticky="w")

item_psupdate_check_var = tkinter.StringVar()
item_psupdate_check_var.set(False)
item_psupdate_check = tkinter.Checkbutton(windows_updates_frame, text = "PSWindows Updates Check for updates", variable=item_psupdate_check_var, onvalue="1", offvalue="0")
item_psupdate_check.grid(row=1, column=0, padx=1, pady=1)

item_psupdate_install_var = tkinter.StringVar()
item_psupdate_install_var.set(False)
item_psupdate_install = tkinter.Checkbutton(windows_updates_frame, text = "PSWindows Updates Check for updates", variable=item_psupdate_install_var, onvalue="1", offvalue="0")
item_psupdate_install.grid(row=2, column=0, padx=1, pady=1)

for widget in windows_updates_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Run options Buttion
#button_frame = tkinter.LabelFrame(frame, text = "")
#button_frame.grid(row = 3, column = 0, sticky="news")

item_button = tkinter.Button(frame, text = "Run All", command=runCommands)
item_button.grid(row = 4, column = 0, sticky="news", padx=20, pady=10)

##################################################################
################## WINDOWS TOOLS START HERE ######################
##################################################################


def run_sfc_cmd(): # Run the SFC Tool
    commands = u'sfc /scannow ; dism /online /cleanup-image /restorehealth '
    ctypes.windll.shell32.ShellExecuteW(
    None,
    u"runas",
    u"powershell.exe",
    commands,
    None,
    1)

def run_dism_cmd(): # Run the DISM Tool
    commands = u'dism /online /cleanup-image /restorehealth '
    ctypes.windll.shell32.ShellExecuteW(
    None,
    u"runas",
    u"powershell.exe",
    commands,
    None,
    1)

def run_both_cmd(): # Run the SFC and DISM Tool
    commands = u'sfc /scannow ; dism /online /cleanup-image /restorehealth  ; dism /online /cleanup-image /restorehealth '
    ctypes.windll.shell32.ShellExecuteW(
    None,
    u"runas",
    u"powershell.exe",
    commands,
    None,
    1)




if __name__ == '__main__':
    window.mainloop()
