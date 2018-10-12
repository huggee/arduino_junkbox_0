import pdb
import serial
import serial.tools.list_ports
import Tkinter as tk

class Button(tk.Frame):
    def init(self, master=None, btext=''):
        self.text = btext

        tk.Frame.__init__(self, master)
        self.button = tk.Button(self, text=self.text, command=self.clicked)
        self.button.pack()

    def clicked(self):
        self.text = 'CLICKED'

        
devices = serial.tools.list_ports.comports()
usb_name = []
for d in devices:
    if 'Arduino' in d[1]:
        usb_name.append(d[0])


ports = []
for l in usb_name:
    ports.append(serial.Serial(l, 115200, timeout = 0.1))
    
for i in range(len(ports)):
    print('%d: %s' % (i, ports[i].name))
print('Detect %d Arduino ' % len(ports))


# while True:
#     ports[0].write('L')
#     if ports[0].in_waiting > 0:
#         print(ports[0].read())
#         #print(type(ports[0].readline()))

root = tk.Tk()
# root.title(u'FPGA2I')
# root.geometry('400x300')
# root.configure(background='black')
# button_a = tk.Button(text = u'A', command = a_clicked)
# button_a.pack()

b1 = Button(master=root, btext='A')
b1.pack()
root.pack()
root.mainloop()

