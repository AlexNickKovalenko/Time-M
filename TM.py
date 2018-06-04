import tkinter as tk
import tkinter.ttk as ttk
parent=tk.Tk()
activity=("Coding","Byking","Testing","Reading/Writing","Misc","")
M='Morning'
N='Noon'
E='Evening'
Cmbbx='Combobox'
#FIRST ROW FORMATION
firstRow={1:"week start",4:"middle week",7:"weekend"}
for key in firstRow.keys():
     ttk.Label(parent,text=firstRow[key]).grid(row=0,column=key,sticky='e')
#SECOND ROW FORMATION
secondRow={0:"MONDAY",3:"WEDNESDAY",6:"SATURDAY"}
for key in secondRow.keys():
     ttk.Label(parent,text=secondRow[key]).grid(row=1,column=key,sticky='e')
#THIRD ROW FORMATION
thirdRowLabel={0:M,3:M,6:M}
thirdRowCombobox={1:Cmbbx,4:Cmbbx,7:Cmbbx}
for key in thirdRowLabel.keys():
     ttk.Label(parent,text=thirdRowLabel[key]).grid(row=2,column=key,sticky='e')
for key in thirdRowCombobox.keys():     
     ttk.Combobox(parent,value=activity).grid(row=2,column=key,sticky='we')
#FORTH ROW FORMATION
forthRowLabel={0:N,3:N,6:N}
forthRowCombobox=thirdRowCombobox
for key in forthRowLabel.keys():
     ttk.Label(parent,text=forthRowLabel[key]).grid(row=3,column=key,sticky='e')
for key in forthRowCombobox:
     ttk.Combobox(parent,value=activity).grid(row=3,column=key,sticky='we')
#FIFTH ROW FORMATION
fifthRowLabel={0:E,3:E,6:E}
fifthRowCombobox=forthRowCombobox
for key in fifthRowLabel.keys():
     ttk.Label(parent,text=fifthRowLabel[key]).grid(row=4,column=key,sticky='e')
for key in fifthRowCombobox.keys():
     ttk.Combobox(parent,value=activity).grid(row=4,column=key,sticky='we')
#SIXTH ROW FORMATION
sixthRowLabel={0:"TUESDAY",3:"THURSDAY",6:"SUNDAY"}
for key in sixthRowLabel.keys():
     ttk.Label(parent,text=sixthRowLabel[key]).grid(row=5,column=key,sticky='e')
#SEVENTH RAW FORMATION
seventhRowLabel=thirdRowLabel
seventhRowCombobox=fifthRowCombobox
for key in seventhRowLabel.keys():
     ttk.Label(parent,text=seventhRowLabel[key]).grid(row=6,column=key,sticky="e")
for key in seventhRowCombobox.keys():
     ttk.Combobox(parent,value=activity).grid(row=6,column=key,sticky='we')
#EIGTHT ROW FORMATION
eigthtRowLabel=forthRowLabel
eigthtRowCombobox=fifthRowCombobox
for key in eigthtRowLabel.keys():
     ttk.Label(parent,text=eigthtRowLabel[key]).grid(row=7,column=key,sticky='e')
for key in eigthtRowCombobox.keys():
     ttk.Combobox(parent,value=activity).grid(row=7,column=key,sticky='we')
#NINTH ROW FORMATION
ninthRowLabel={0:E,3:E,6:E}
ninthRowCombobox=eigthtRowCombobox
for key in ninthRowLabel.keys():
     ttk.Label(parent,text=ninthRowLabel[key]).grid(row=8,column=key,sticky='e')
for key in ninthRowCombobox.keys():
     ttk.Combobox(parent,value=activity).grid(row=8,column=key,sticky='we')


parent.mainloop()
