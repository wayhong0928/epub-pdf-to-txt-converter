"""
Application logger configuration
"""

import logging
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional


class AppLogger:
    """Application logger manager"""
    
    _instance = None
    _logger = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppLogger, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._logger is None:
            self._setup_logger()
    
    def _setup_logger(self):
        """Setup the application logger"""
        # Create logger
        self._logger = logging.getLogger('epub_pdf_converter')
        self._logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers
        if self._logger.handlers:
            return
        
        # Create formatters
        console_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)
        self._logger.addHandler(console_handler)
        
        # File handler
        try:
            # Create logs directory if it doesn't exist
            logs_dir = Path('logs')
            logs_dir.mkdir(exist_ok=True)
            
            # Create log file with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            log_file = logs_dir / f'epub_converter_{timestamp}.log'
            
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(file_formatter)
            self._logger.addHandler(file_handler)
            
            self._logger.info(f"Log file created: {log_file}")
            
        except Exception as e:
            self._logger.warning(f"Could not create file logger: {str(e)}")
    
    def get_logger(self) -> logging.Logger:
        """Get the application logger"""
        return self._logger
    
    def set_level(self, level: str):
        """Set logging level"""
        level_map = {
            'DEBUG': logging.DEBUG,
            'INFO': logging.INFO,
            'WARNING': logging.WARNING,
            'ERROR': logging.ERROR,
            'CRITICAL': logging.CRITICAL
        }
        
        if level.upper() in level_map:
            self._logger.setLevel(level_map[level.upper()])
            self._logger.info(f"Log level set to {level.upper()}")
        else:
            self._logger.warning(f"Invalid log level: {level}")


# Global logger instance
_app_logger = AppLogger()


def get_logger() -> logging.Logger:
    """Get the application logger"""
    return _app_logger.get_logger()


def set_log_level(level: str):
    """Set the logging level"""
    _app_logger.set_level(level)
