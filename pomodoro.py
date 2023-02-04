import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

SIZE = "700x300"
TITLE = "Pomodoro Timer"

class Pomodoro:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(SIZE)
        self.root.title(TITLE)
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='tomato.png'))


        #simple style adding
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))

        #creating a notebook, which allows us to select pages of contents by clicking on tabs
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)

        #creating individual frames for each tab
        tWidth, tHeight = 700, 100
        self.tab1 = ttk.Frame(self.tabs, width=tWidth, height=tHeight)
        self.tab2 = ttk.Frame(self.tabs, width=tWidth, height=tHeight)
        self.tab3 = ttk.Frame(self.tabs, width=tWidth, height=tHeight)

        #the timers are adjustable up to the preference of the user
        self.pomodoro_label = ttk.Label(self.tab1, text="35:00", font=("Ubuntu", 50))
        self.pomodoro_label.pack(pady=20)

        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu", 50))
        self.short_break_timer_label.pack(pady=20)

        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu", 50))
        self.long_break_timer_label.pack(pady=20)

        #creating and naming tabs
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")

        #creating buttons that start, skip and reset the timer
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_timer)
        self.skip_button.grid(row=0, column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2)

        #creating and adding pomodoro counter
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoros: 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=6)

        self.pomodoros = 0
        self.skipped = self.stopped = self.running = False

        # runs the application so it can be interacted with limitlessly
        self.root.mainloop()

    #creating thread so the timer can run simultaneously with the app
    def start_timer_thread(self):
        if not self.running:
            t = threading.Thread(target=self.start_timer)
            t.start()
            self.running = True

    def start_timer(self):
        #stopping other functions in case they are true
        self.stopped =  self.skipped = False
        timer_id = self.tabs.index(self.tabs.select()) + 1

        ## TODO Finish function `start_timer`

        if timer_id == 1:
            full_seconds = 60 * 35
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            #adding pomodoros and selecting whether the user should have short or long break
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                else:
                    self.tabs.select(1)
                self.start_timer()
        elif timer_id == 2:
            full_seconds = 60 * 5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
            else:
                print("Invalid timer id")
                def reset_timer(self):
        self.stopped = True
        self.reset = False
        self.pomodoros = 0
        self.pomodoro_label.config(text="35:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="15:00")
        self.pomodoro_counter_label.config(text="Pomodoros: 0")
        self.running = False

    def skip_timer(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.pomodoro_label.config(text="35:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="15:00")

        self.stopped = True
        self.skipped = True

Pomodoro()