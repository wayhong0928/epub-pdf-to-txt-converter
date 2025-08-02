#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EPUB & PDF to TXT Converter v1.0.0
Entry point for the application
"""

import sys
import os
import tkinter as tk
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import from the modular structure
from gui.main_window import MainWindow
from utils import app_logger


def main():
    """Main entry point"""
    logger = app_logger.get_logger()
    
    try:
        logger.info("Starting EPUB & PDF to TXT Converter v1.0.0")
        
        # Create root window
        root = tk.Tk()
        
        # Create main window
        app = MainWindow(root)
        
        # Set window close handler
        def on_closing():
            app.save_settings()
            root.destroy()
        
        root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Start main loop
        root.mainloop()
        
        logger.info("Application closed normally")
        
    except Exception as e:
        logger.error(f"Error starting application: {e}")
        print(f"Error starting application: {e}")
        # Show error dialog if tkinter is available
        try:
            import tkinter.messagebox as msgbox
            msgbox.showerror("錯誤", f"應用程式啟動失敗: {e}")
        except:
            pass
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
