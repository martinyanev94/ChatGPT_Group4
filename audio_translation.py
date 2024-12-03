import tkinter as tk
from tkinter import filedialog, messagebox
import openai
import os

class AudioTranslation:
    def __init__(self, frame,show_home_callback):
        self.frame = frame
        self.show_home_callback = show_home_callback
        self.api_key = os.getenv("OPENAI_API_KEY")  # Fetch API key from environment
        if not self.api_key:
            raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
        openai.api_key = self.api_key
        self.setup_ui()

    def setup_ui(self):
        # Title Label
        tk.Label(self.frame, text="Audio Translation", font=("Arial", 18)).pack(pady=20)

        # Select File Button
        tk.Button(self.frame, text="Select Audio File", command=self.upload_audio).pack(pady=10)

        # Display Translated Text
        self.audio_text = tk.Text(self.frame, height=10, width=60)
        self.audio_text.pack(pady=10)
        tk.Button(self.frame, text="Back to Home", command=lambda: self.show_home_callback("Home")).pack(pady=20)


    def upload_audio(self):
        # Open file dialog to select an audio file
        file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
        if not file_path:
            return

        try:
            # Translate audio using Whisper API
            translated_text = self.translate_audio(file_path)

            # Display translated text in the text widget
            self.audio_text.delete("1.0", "end")
            self.audio_text.insert("1.0", translated_text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def translate_audio(self, file_path):
        # Use OpenAI Whisper API to translate audio
        try:
            with open(file_path, "rb") as audio_file:
                response = openai.Audio.transcribe(
                    model="whisper-1",  # Whisper model
                    file=audio_file
                )
            return response["text"]
        except Exception as e:
            raise Exception(f"Failed to translate audio: {e}")
