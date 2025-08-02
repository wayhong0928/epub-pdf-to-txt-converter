"""
Main window GUI for EPUB/PDF to TXT Converter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
from pathlib import Path
from typing import Optional
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.converter import DocumentToTxtConverter
from config.settings import Settings
from localization.lang_manager import LanguageManager
from utils import app_logger


class MainWindow:
    """Main application window"""
    
    def __init__(self, root):
        self.root = root
        self.converter = DocumentToTxtConverter()
        self.settings = Settings()
        self.lang_manager = LanguageManager()
        self.logger = app_logger.get_logger()
        
        # UI components
        self.progress_var = tk.StringVar()
        self.progress_bar = None
        self.convert_button = None
        self.status_label = None
        
        # File selection variables
        self.input_path_var = tk.StringVar()
        self.output_path_var = tk.StringVar()
        
        # Language variables
        self.current_language = self.settings.get_language()
        self.lang_manager.set_language(self.current_language)
        
        self._setup_ui()
        self._load_settings()
        
        # Initialize progress display
        self.progress_var.set(self.lang_manager.get_text('ready'))
        
        self.logger.info("Main window initialized")
    
    def _setup_ui(self):
        """Setup the user interface"""
        self.root.title("EPUB/PDF to TXT Converter v1.0.0")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Create main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(1, weight=1)
        
        # Language selection frame
        self._create_language_frame(main_frame)
        
        # File selection frame
        self._create_file_selection_frame(main_frame)
        
        # Options frame
        self._create_options_frame(main_frame)
        
        # Progress frame
        self._create_progress_frame(main_frame)
        
        # Control buttons frame
        self._create_control_frame(main_frame)
        
        # Status frame
        self._create_status_frame(main_frame)
        
        # Update text based on current language
        self._update_ui_text()
    
    def _create_language_frame(self, parent):
        """Create language selection frame"""
        lang_frame = ttk.LabelFrame(parent, text="Language / 語言", padding="5")
        lang_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        lang_frame.columnconfigure(0, weight=1)
        
        # Language selection
        self.lang_var = tk.StringVar(value=self.current_language)
        
        ttk.Radiobutton(
            lang_frame, 
            text="English", 
            variable=self.lang_var, 
            value="en",
            command=lambda: self._change_language("en")
        ).grid(row=0, column=0, sticky=tk.W, padx=(0, 20))
        
        ttk.Radiobutton(
            lang_frame, 
            text="中文 (繁體)", 
            variable=self.lang_var, 
            value="zh_TW",
            command=lambda: self._change_language("zh_TW")
        ).grid(row=0, column=1, sticky=tk.W)
    
    def _create_file_selection_frame(self, parent):
        """Create file/folder selection frame"""
        self.file_frame = ttk.LabelFrame(parent, text="File Selection", padding="5")
        self.file_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        self.file_frame.columnconfigure(1, weight=1)
        
        # Input selection
        self.input_label = ttk.Label(self.file_frame, text="Input:")
        self.input_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        input_entry = ttk.Entry(self.file_frame, textvariable=self.input_path_var, width=50)
        input_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 5), pady=(0, 5))
        
        self.browse_input_btn = ttk.Button(
            self.file_frame, 
            text="Browse", 
            command=self._browse_input,
            width=10
        )
        self.browse_input_btn.grid(row=0, column=2, padx=(5, 0), pady=(0, 5))
        
        # Output selection
        self.output_label = ttk.Label(self.file_frame, text="Output:")
        self.output_label.grid(row=1, column=0, sticky=tk.W)
        
        output_entry = ttk.Entry(self.file_frame, textvariable=self.output_path_var, width=50)
        output_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        
        self.browse_output_btn = ttk.Button(
            self.file_frame, 
            text="Browse", 
            command=self._browse_output,
            width=10
        )
        self.browse_output_btn.grid(row=1, column=2, padx=(5, 0))
    
    def _create_options_frame(self, parent):
        """Create conversion options frame"""
        self.options_frame = ttk.LabelFrame(parent, text="Options", padding="5")
        self.options_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Preserve structure option
        self.preserve_structure_var = tk.BooleanVar(value=self.settings.get_preserve_structure())
        self.preserve_structure_cb = ttk.Checkbutton(
            self.options_frame,
            text="Preserve folder structure",
            variable=self.preserve_structure_var
        )
        self.preserve_structure_cb.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # Skip existing files option
        self.skip_existing_var = tk.BooleanVar(value=self.settings.get_skip_existing())
        self.skip_existing_cb = ttk.Checkbutton(
            self.options_frame,
            text="Skip existing files",
            variable=self.skip_existing_var
        )
        self.skip_existing_cb.grid(row=1, column=0, sticky=tk.W)
    
    def _create_progress_frame(self, parent):
        """Create progress display frame"""
        progress_frame = ttk.LabelFrame(parent, text="Progress", padding="5")
        progress_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        progress_frame.columnconfigure(0, weight=1)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(
            progress_frame, 
            mode='determinate',
            length=400
        )
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # Progress text
        self.progress_label = ttk.Label(
            progress_frame, 
            textvariable=self.progress_var,
            wraplength=500
        )
        self.progress_label.grid(row=1, column=0, sticky=tk.W)
    
    def _create_control_frame(self, parent):
        """Create control buttons frame"""
        control_frame = ttk.Frame(parent)
        control_frame.grid(row=4, column=0, columnspan=2, pady=(0, 10))
        
        # Convert button
        self.convert_button = ttk.Button(
            control_frame,
            text="Convert",
            command=self._start_conversion,
            width=15
        )
        self.convert_button.grid(row=0, column=0, padx=(0, 10))
        
        # Clear button
        self.clear_button = ttk.Button(
            control_frame,
            text="Clear",
            command=self._clear_inputs,
            width=15
        )
        self.clear_button.grid(row=0, column=1, padx=(0, 10))
        
        # Exit button
        self.exit_button = ttk.Button(
            control_frame,
            text="Exit",
            command=self._exit_app,
            width=15
        )
        self.exit_button.grid(row=0, column=2)
    
    def _create_status_frame(self, parent):
        """Create status bar frame"""
        status_frame = ttk.Frame(parent)
        status_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E))
        status_frame.columnconfigure(0, weight=1)
        
        # Status label
        self.status_label = ttk.Label(
            status_frame,
            text="Ready",
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding="2"
        )
        self.status_label.grid(row=0, column=0, sticky=(tk.W, tk.E))
    
    def _change_language(self, language: str):
        """Change application language"""
        self.current_language = language
        self.lang_manager.set_language(language)
        self.settings.set_language(language)
        self._update_ui_text()
        self.logger.info(f"Language changed to {language}")
    
    def _update_ui_text(self):
        """Update UI text based on current language"""
        # Update window title
        self.root.title(self.lang_manager.get_text('app_title'))
        
        # Update frame labels
        self.file_frame.config(text=self.lang_manager.get_text('file_selection'))
        self.options_frame.config(text=self.lang_manager.get_text('options'))
        
        # Update labels
        self.input_label.config(text=self.lang_manager.get_text('input') + ":")
        self.output_label.config(text=self.lang_manager.get_text('output') + ":")
        
        # Update buttons
        self.browse_input_btn.config(text=self.lang_manager.get_text('browse'))
        self.browse_output_btn.config(text=self.lang_manager.get_text('browse'))
        self.convert_button.config(text=self.lang_manager.get_text('convert'))
        self.clear_button.config(text=self.lang_manager.get_text('clear'))
        self.exit_button.config(text=self.lang_manager.get_text('exit'))
        
        # Update checkboxes
        self.preserve_structure_cb.config(text=self.lang_manager.get_text('preserve_structure'))
        self.skip_existing_cb.config(text=self.lang_manager.get_text('skip_existing'))
        
        # Update status
        self.status_label.config(text=self.lang_manager.get_text('ready'))
        self.progress_var.set(self.lang_manager.get_text('ready'))
    
    def _browse_input(self):
        """Browse for input file or folder"""
        file_types = [
            (self.lang_manager.get_text('all_supported'), '*.epub;*.pdf'),
            (self.lang_manager.get_text('epub_files'), '*.epub'),
            (self.lang_manager.get_text('pdf_files'), '*.pdf'),
            (self.lang_manager.get_text('all_files'), '*.*')
        ]
        
        # Ask user to choose file or folder
        choice = messagebox.askyesnocancel(
            self.lang_manager.get_text('select_input'),
            self.lang_manager.get_text('select_input_type')
        )
        
        if choice is True:  # Yes - select file
            filename = filedialog.askopenfilename(
                title=self.lang_manager.get_text('select_input_file'),
                filetypes=file_types
            )
            if filename:
                self.input_path_var.set(filename)
        elif choice is False:  # No - select folder
            dirname = filedialog.askdirectory(
                title=self.lang_manager.get_text('select_input_folder')
            )
            if dirname:
                self.input_path_var.set(dirname)
    
    def _browse_output(self):
        """Browse for output folder"""
        dirname = filedialog.askdirectory(
            title=self.lang_manager.get_text('select_output_folder')
        )
        if dirname:
            self.output_path_var.set(dirname)
    
    def _clear_inputs(self):
        """Clear all input fields"""
        self.input_path_var.set("")
        self.output_path_var.set("")
        self.progress_bar['value'] = 0
        self.progress_var.set(self.lang_manager.get_text('ready'))
        self.status_label.config(text=self.lang_manager.get_text('ready'))
    
    def _load_settings(self):
        """Load settings into UI"""
        self.preserve_structure_var.set(self.settings.get_preserve_structure())
        self.skip_existing_var.set(self.settings.get_skip_existing())
        
        # Load last used paths
        last_input = self.settings.get_last_input_path()
        last_output = self.settings.get_last_output_path()
        if last_input:
            self.input_path_var.set(last_input)
        if last_output:
            self.output_path_var.set(last_output)
    
    def save_settings(self):
        """Save current settings"""
        self.settings.set_preserve_structure(self.preserve_structure_var.get())
        self.settings.set_skip_existing(self.skip_existing_var.get())
        self.settings.set_last_input_path(self.input_path_var.get())
        self.settings.set_last_output_path(self.output_path_var.get())
        self.settings.save()
    
    def _start_conversion(self):
        """Start the conversion process"""
        input_path = self.input_path_var.get().strip()
        output_path = self.output_path_var.get().strip()
        
        if not input_path:
            messagebox.showerror(
                self.lang_manager.get_text('error'),
                self.lang_manager.get_text('select_input_path')
            )
            return
        
        if not output_path:
            messagebox.showerror(
                self.lang_manager.get_text('error'),
                self.lang_manager.get_text('select_output_path')
            )
            return
        
        if not Path(input_path).exists():
            messagebox.showerror(
                self.lang_manager.get_text('error'),
                self.lang_manager.get_text('input_not_exist')
            )
            return
        
        # Save settings
        self.save_settings()
        
        # Disable convert button during conversion
        self.convert_button.config(state='disabled')
        
        # Start conversion in separate thread
        thread = threading.Thread(target=self._convert_files, args=(input_path, output_path))
        thread.daemon = True
        thread.start()
    
    def _convert_files(self, input_path: str, output_path: str):
        """Convert files in background thread"""
        try:
            # Progress callback
            def progress_callback(progress: int, message: str):
                self.root.after(0, self._update_progress, progress, message)
            
            # Update converter settings
            self.converter.preserve_structure = self.preserve_structure_var.get()
            self.converter.skip_existing = self.skip_existing_var.get()
            
            # Convert files
            if Path(input_path).is_file():
                success = self.converter.convert_file(input_path, output_path, progress_callback)
            else:
                success = self.converter.convert_directory(input_path, output_path, progress_callback)
            
            # Show completion message
            if success:
                self.root.after(0, self._conversion_complete, True)
            else:
                self.root.after(0, self._conversion_complete, False)
                
        except Exception as e:
            self.logger.error(f"Conversion error: {str(e)}")
            self.root.after(0, self._conversion_error, str(e))
    
    def _update_progress(self, progress: int, message: str):
        """Update progress bar and message"""
        self.progress_bar['value'] = progress
        self.progress_var.set(message)
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def _conversion_complete(self, success: bool):
        """Handle conversion completion"""
        self.convert_button.config(state='normal')
        
        if success:
            self.progress_bar['value'] = 100
            self.progress_var.set(self.lang_manager.get_text('conversion_complete'))
            self.status_label.config(text=self.lang_manager.get_text('conversion_complete'))
            
            messagebox.showinfo(
                self.lang_manager.get_text('success'),
                self.lang_manager.get_text('conversion_successful')
            )
        else:
            self.progress_var.set(self.lang_manager.get_text('conversion_failed'))
            self.status_label.config(text=self.lang_manager.get_text('conversion_failed'))
            
            messagebox.showerror(
                self.lang_manager.get_text('error'),
                self.lang_manager.get_text('conversion_failed')
            )
    
    def _conversion_error(self, error_message: str):
        """Handle conversion error"""
        self.convert_button.config(state='normal')
        self.progress_var.set(self.lang_manager.get_text('conversion_failed'))
        self.status_label.config(text=self.lang_manager.get_text('conversion_failed'))
        
        messagebox.showerror(
            self.lang_manager.get_text('error'),
            f"{self.lang_manager.get_text('conversion_error')}: {error_message}"
        )
    
    def _exit_app(self):
        """Exit the application"""
        if messagebox.askyesno(
            self.lang_manager.get_text('confirm'),
            self.lang_manager.get_text('confirm_exit')
        ):
            self.save_settings()
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
