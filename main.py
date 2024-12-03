import tkinter as tk
from vision_extractor import VisionExtractor
from audio_translation import AudioTranslation
from resume_builder import ResumeBuilder
from question_generator import QuestionGenerator
from grammar_fixer import GrammarFixer

class AIToolkitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Toolkit")
        self.root.geometry("800x600")
        self.frames = {}

        # Define tools and their respective classes
        tools = {
            "Home": None,
            "Vision Extractor": VisionExtractor,
            "Audio Translation": AudioTranslation,
            "Resume Builder": ResumeBuilder,
            "Question Generator": QuestionGenerator,
            "Grammar Fixer": GrammarFixer,
        }

        # Initialize frames
        for tool_name, tool_class in tools.items():
            frame = tk.Frame(root)
            self.frames[tool_name] = frame

            if tool_name == "Home":
                self.setup_home(frame)
            else:
                tool_class(frame, self.show_frame)  # Pass the show_frame method

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")  # Show the Home frame initially

    def show_frame(self, name):
        """Raise the specified frame to the top."""
        frame = self.frames[name]
        frame.tkraise()

    def setup_home(self, frame):
        """Set up the Home screen."""
        tk.Label(frame, text="Welcome to the AI Toolkit!", font=("Arial", 18)).pack(pady=20)
        tools = ["Vision Extractor", "Audio Translation", "Resume Builder", "Question Generator", "Grammar Fixer"]

        for tool in tools:
            tk.Button(frame, text=tool, command=lambda t=tool: self.show_frame(t), width=25).pack(pady=10)


if __name__ == "__main__": 
    root = tk.Tk()
    app = AIToolkitApp(root)
    root.mainloop()
# import tkinter as tk
# from vision_extractor import VisionExtractor
# from audio_translation import AudioTranslation
# from resume_builder import ResumeBuilder
# from question_generator import QuestionGenerator
# from grammar_fixer import GrammarFixer


# class AIToolkitApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Toolkit")
#         self.root.geometry("800x600")
#         self.frames = {}

#         # Define tools and their respective classes
#         tools = {
#             "Home": None,
#             "Vision Extractor": VisionExtractor,
#             "Audio Translation": AudioTranslation,
#             "Resume Builder": ResumeBuilder,
#             "Question Generator": QuestionGenerator,
#             "Grammar Fixer": GrammarFixer,
#         }

#         # Initialize frames
#         for tool_name, tool_class in tools.items():
#             frame = tk.Frame(root)
#             self.frames[tool_name] = frame

#             if tool_name == "Home":
#                 self.setup_home(frame)
#             elif tool_class is not None:
#                 try:
#                     # Initialize tool classes with frame and show_frame
#                     tool_class(frame, self.show_frame)
#                 except TypeError:
#                     # Fallback for tools requiring only a frame
#                     tool_class(frame)

#             frame.place(relwidth=1, relheight=1)

#         # Show the Home frame initially
#         self.show_frame("Home")

#     def show_frame(self, name):
#         """Raise the specified frame to the top and hide others."""
#         for frame_name, frame in self.frames.items():
#             if frame_name == name:
#                 frame.lift()
#                 frame.pack(fill="both", expand=True)
#             else:
#                 frame.pack_forget()

#     def setup_home(self, frame):
#         """Set up the Home screen."""
#         tk.Label(frame, text="Welcome to the AI Toolkit!", font=("Arial", 18)).pack(pady=20)
#         tools = ["Vision Extractor", "Audio Translation", "Resume Builder", "Question Generator", "Grammar Fixer"]

#         # Create buttons for available tools
#         for tool in tools:
#             if tool in self.frames:
#                 tk.Button(frame, text=tool, command=lambda t=tool: self.show_frame(t), width=25).pack(pady=10)


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = AIToolkitApp(root)
#     root.mainloop()
