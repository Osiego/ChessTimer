import tkinter as tk


class ChessTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Timer")

        self.time1 = 300  # 5 minutes in seconds for Jennifer
        self.time2 = 300  # 5 minutes in seconds for Cody
        self.turn_count1 = 0  # Turn counter for Jennifer
        self.turn_count2 = 0  # Turn counter for Cody
        self.current_player = 1
        self.running = False
        self.timer_id = None  # Store the after() id to cancel it when needed

        # Label to display player name Jennifer
        self.player1_label = tk.Label(root, text="Jennifer", font=('Helvetica', 16))
        self.player1_label.grid(row=0, column=0, padx=20, pady=10)

        # Label to display player name Cody
        self.player2_label = tk.Label(root, text="Cody", font=('Helvetica', 16))
        self.player2_label.grid(row=0, column=1, padx=20, pady=10)

        # Label to display timer for Jennifer
        self.label1 = tk.Label(root, text=self.format_time(self.time1), font=('Helvetica', 48), bg='white')
        self.label1.grid(row=1, column=0, padx=20, pady=20)

        # Label to display timer for Cody
        self.label2 = tk.Label(root, text=self.format_time(self.time2), font=('Helvetica', 48), bg='white')
        self.label2.grid(row=1, column=1, padx=20, pady=20)

        # Label to display turn counter for Jennifer
        self.turn_label1 = tk.Label(root, text=f"Turns: {self.turn_count1}", font=('Helvetica', 12))
        self.turn_label1.grid(row=2, column=0)

        # Label to display turn counter for Cody
        self.turn_label2 = tk.Label(root, text=f"Turns: {self.turn_count2}", font=('Helvetica', 12))
        self.turn_label2.grid(row=2, column=1)

        # Canvas for the horizontal red line for Jennifer
        self.canvas1 = tk.Canvas(root, width=300, height=10, bg='white', highlightthickness=0)
        self.canvas1.grid(row=3, column=0)

        # Canvas for the horizontal red line for Cody
        self.canvas2 = tk.Canvas(root, width=300, height=10, bg='white', highlightthickness=0)
        self.canvas2.grid(row=3, column=1)

        # Button to start/stop the timer
        self.button = tk.Button(root, text="Start/Stop", command=self.toggle, font=('Helvetica', 12), bg='red',
                                fg='white')
        self.button.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        # Button to reset the timers and turn counters
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=('Helvetica', 12))
        self.reset_button.grid(row=5, column=0, columnspan=2, padx=20, pady=20)

    def format_time(self, seconds):
        """Convert seconds to minutes and seconds in mm:ss format."""
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def update_timer(self):
        """Update the current player's timer and redraw the red line."""
        if self.running:
            if self.current_player == 1 and self.time1 > 0:
                self.time1 -= 1
                self.label1.config(text=self.format_time(self.time1))
            elif self.current_player == 2 and self.time2 > 0:
                self.time2 -= 1
                self.label2.config(text=self.format_time(self.time2))

            # Stop the timer if either player's time runs out
            if (self.current_player == 1 and self.time1 == 0) or (self.current_player == 2 and self.time2 == 0):
                self.running = False

            # Schedule the next timer update
            if self.running:
                self.timer_id = self.root.after(1000, self.update_timer)

        # Update the red line indicator
        self.update_canvas()

    def toggle(self):
        """Start or stop the timer and switch the current player."""
        if self.running:
            # Stop the timer
            self.running = False
            if self.timer_id:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None
        else:
            # Start the timer and switch the current player
            self.running = True
            self.current_player = 2 if self.current_player == 1 else 1

            # Increment the turn counter for the current player
            if self.current_player == 1:
                self.turn_count1 += 1
                self.turn_label1.config(text=f"Turns: {self.turn_count1}")
            else:
                self.turn_count2 += 1
                self.turn_label2.config(text=f"Turns: {self.turn_count2}")

            # Start updating the timer
            self.update_timer()

    def reset(self):
        """Reset the timers and turn counters to their initial state."""
        self.running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None
        self.time1 = 300
        self.time2 = 300
        self.turn_count1 = 0
        self.turn_count2 = 0
        self.label1.config(text=self.format_time(self.time1))
        self.label2.config(text=self.format_time(self.time2))
        self.turn_label1.config(text=f"Turns: {self.turn_count1}")
        self.turn_label2.config(text=f"Turns: {self.turn_count2}")
        self.update_canvas()

    def update_canvas(self):
        """Update the red line to indicate the current player's turn."""
        self.canvas1.delete("line")
        self.canvas2.delete("line")
        if self.running:
            if self.current_player == 1:
                self.canvas1.create_line(0, 5, 300, 5, fill="red", width=3, tags="line")
            elif self.current_player == 2:
                self.canvas2.create_line(0, 5, 300, 5, fill="red", width=3, tags="line")


if __name__ == "__main__":
    root = tk.Tk()
    app = ChessTimer(root)
    root.mainloop()
