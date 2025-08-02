"""
Settings management for EPUB/PDF to TXT Converter
"""

import json
from pathlib import Path
from typing import Any
import logging

from utils import app_logger


class Settings:
    """Settings manager for the application"""
    
    def __init__(self, config_file: str = "config.json"):
        self.logger = app_logger.get_logger()
        self.config_file = Path(config_file)
        self.settings = self._load_default_settings()
        self.load()
    
    def _load_default_settings(self) -> dict:
        """Load default settings"""
        return {
            'language': 'en',
            'preserve_structure': True,
            'skip_existing': True,
            'output_encoding': 'utf-8',
            'log_level': 'INFO',
            'window_geometry': '600x500',
            'last_input_path': '',
            'last_output_path': ''
        }
    
    def load(self):
        """Load settings from file"""
        try:
            if self.config_file.exists():
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_settings = json.load(f)
                    # Update settings with loaded values, keeping defaults for missing keys
                    self.settings.update(loaded_settings)
                    self.logger.info(f"Settings loaded from {self.config_file}")
            else:
                self.logger.info("Config file not found, using default settings")
        except Exception as e:
            self.logger.warning(f"Error loading settings: {str(e)}, using defaults")
    
    def save(self):
        """Save settings to file"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
                self.logger.info(f"Settings saved to {self.config_file}")
        except Exception as e:
            self.logger.error(f"Error saving settings: {str(e)}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a setting value"""
        self.settings[key] = value
    
    # Convenience methods for common settings
    
    def get_language(self) -> str:
        """Get current language"""
        return self.settings.get('language', 'en')
    
    def set_language(self, language: str):
        """Set current language"""
        self.settings['language'] = language
    
    def get_preserve_structure(self) -> bool:
        """Get preserve structure setting"""
        return self.settings.get('preserve_structure', True)
    
    def set_preserve_structure(self, preserve: bool):
        """Set preserve structure setting"""
        self.settings['preserve_structure'] = preserve
    
    def get_skip_existing(self) -> bool:
        """Get skip existing files setting"""
        return self.settings.get('skip_existing', True)
    
    def set_skip_existing(self, skip: bool):
        """Set skip existing files setting"""
        self.settings['skip_existing'] = skip
    
    def get_output_encoding(self) -> str:
        """Get output file encoding"""
        return self.settings.get('output_encoding', 'utf-8')
    
    def set_output_encoding(self, encoding: str):
        """Set output file encoding"""
        self.settings['output_encoding'] = encoding
    
    def get_log_level(self) -> str:
        """Get logging level"""
        return self.settings.get('log_level', 'INFO')
    
    def set_log_level(self, level: str):
        """Set logging level"""
        self.settings['log_level'] = level
    
    def get_window_geometry(self) -> str:
        """Get window geometry"""
        return self.settings.get('window_geometry', '600x500')
    
    def set_window_geometry(self, geometry: str):
        """Set window geometry"""
        self.settings['window_geometry'] = geometry
    
    def get_last_input_path(self) -> str:
        """Get last used input path"""
        return self.settings.get('last_input_path', '')
    
    def set_last_input_path(self, path: str):
        """Set last used input path"""
        self.settings['last_input_path'] = path
    
    def get_last_output_path(self) -> str:
        """Get last used output path"""
        return self.settings.get('last_output_path', '')
    
    def set_last_output_path(self, path: str):
        """Set last used output path"""
        self.settings['last_output_path'] = path
    
    def reset_to_defaults(self):
        """Reset all settings to defaults"""
        self.settings = self._load_default_settings()
        self.save()
        self.logger.info("Settings reset to defaults")
