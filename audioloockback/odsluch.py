
import pyaudio
import threading
import tkinter as tk

class AudioLoopbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Loopback")
        
        self.is_running = False
        
        self.start_button = tk.Button(root, text="Start", command=self.start_loopback)
        self.start_button.pack(pady=20)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_loopback, state=tk.DISABLED)
        self.stop_button.pack(pady=20)
        
        self.info_label = tk.Label(root, text="Click 'Start' to begin loopback.")
        self.info_label.pack(pady=20)
        
        self.thread = None
        self.p = pyaudio.PyAudio()

    def start_loopback(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.loopback)
            self.thread.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.info_label.config(text="Loopback is running...")

    def stop_loopback(self):
        if self.is_running:
            self.is_running = False
            self.thread.join()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.info_label.config(text="Loopback stopped.")

    def loopback(self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        stream_in = self.p.open(format=FORMAT,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                frames_per_buffer=CHUNK)

        stream_out = self.p.open(format=FORMAT,
                                 channels=CHANNELS,
                                 rate=RATE,
                                 output=True,
                                 frames_per_buffer=CHUNK)

        while self.is_running:
            data = stream_in.read(CHUNK)
            stream_out.write(data)

        stream_in.stop_stream()
        stream_in.close()
        stream_out.stop_stream()
        stream_out.close()

    def on_closing(self):
        self.stop_loopback()
        self.p.terminate()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioLoopbackApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
