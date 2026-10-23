import sys
import os

# Ensure the app's directory is always in sys.path (needed on Android)
app_dir = os.path.dirname(os.path.abspath(__file__))
if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Import the KivyTerminalApp from renderer_kivy
from renderer_kivy import KivyTerminalApp

if __name__ == "__main__":
    KivyTerminalApp().run()
