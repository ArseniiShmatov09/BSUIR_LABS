import tkinter as tk

class Protected_entry(tk.Entry):
    def __init__(self, master=None, is_protected=True, buffer_size=10, **kwargs):
        super().__init__(master, **kwargs)

        self.buffer = [''] * buffer_size
        self.buffer_size = buffer_size
        self.is_protected = is_protected

        self.bind('<KeyRelease>', self.update_buffer)

    def update_buffer(self, event) -> None:
        current = self.get()

        # the "buffer overflow" attack
        if self.is_protected and len(current) > self.buffer_size:
            self.delete(self.buffer_size, tk.END)
            self.update_buffer(event)
            return

        current = list(current)
        self.buffer = [''] * self.buffer_size
        for i in range(len(current)):
            self.buffer[i] = current[i]

    def get_string(self) -> str:
        return ''.join(self.buffer)