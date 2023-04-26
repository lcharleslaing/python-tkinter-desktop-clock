import tkinter as tk
import time
import configparser
import os.path

config_file = "config.ini"

# create configuration file if it does not exist
if not os.path.exists(config_file):
    with open(config_file, "w") as f:
        f.write("[window]\n")
        f.write("x_pos = 100\n")
        f.write("y_pos = 100\n")

# load configuration
config = configparser.ConfigParser()
config.read(config_file)
x_pos = config.getint("window", "x_pos")
y_pos = config.getint("window", "y_pos")

def update_time():
    curr_time = time.strftime("%H:%M:%S")
    label.config(text=curr_time)
    label.after(1000, update_time) # update every second

root = tk.Tk()
root.overrideredirect(True) # remove title bar
root.wm_attributes("-topmost", True) # make window always on top

label = tk.Label(root, font=("Arial", 50))
label.pack()

update_time() # start the clock

# alternative way to close the app
def close_app(event):
    # save configuration before closing
    config.set("window", "x_pos", str(root.winfo_x())) # convert to string
    config.set("window", "y_pos", str(root.winfo_y())) # convert to string
    with open(config_file, "w") as f:
        config.write(f)
    root.destroy()

def on_hover(event):
    exit_label.place(x=label.winfo_width() - 25, y=0)
    exit_label.config(fg="white")

def on_leave(event):
    # delay hiding the label by 200 milliseconds
    root.after(200, exit_label.place_forget)

def move_window(event):
    root.geometry("+{0}+{1}".format(event.x_root, event.y_root))

label.bind("<Double-Button-1>", close_app)
label.bind("<Enter>", on_hover)
label.bind("<Leave>", on_leave)
label.bind("<B1-Motion>", move_window)

exit_label = tk.Label(root, text="X", font=("Arial", 16), bg="#444444", fg="#dddddd")
exit_label.bind("<Button-1>", close_app)

# set the position of the window
root.geometry("+{0}+{1}".format(x_pos, y_pos))

root.mainloop()
