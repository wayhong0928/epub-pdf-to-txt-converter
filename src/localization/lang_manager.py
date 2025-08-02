"""
Language manager for multi-language support
"""

import json
from pathlib import Path
from typing import Dict, Any
import logging

from utils import app_logger


class LanguageManager:
    """Manages multi-language text for the application"""
    
    def __init__(self):
        self.logger = app_logger.get_logger()
        self.current_language = 'en'
        self.translations = {}
        self.lang_dir = Path(__file__).parent
        self._load_all_languages()
    
    def _load_all_languages(self):
        """Load all available language files"""
        try:
            # Load English (default)
            self._load_language('en')
            # Load Traditional Chinese
            self._load_language('zh_TW')
            self.logger.info("All language files loaded successfully")
        except Exception as e:
            self.logger.error(f"Error loading language files: {str(e)}")
    
    def _load_language(self, language: str):
        """Load a specific language file"""
        lang_file = self.lang_dir / f"{language}.json"
        
        if language == 'en':
            # Create English translations if file doesn't exist
            self.translations[language] = self._get_english_translations()
            if not lang_file.exists():
                self._save_language_file(language)
        elif language == 'zh_TW':
            # Create Traditional Chinese translations if file doesn't exist
            self.translations[language] = self._get_chinese_translations()
            if not lang_file.exists():
                self._save_language_file(language)
        else:
            # Try to load from file
            if lang_file.exists():
                try:
                    with open(lang_file, 'r', encoding='utf-8') as f:
                        self.translations[language] = json.load(f)
                except Exception as e:
                    self.logger.error(f"Error loading {lang_file}: {str(e)}")
                    # Fallback to English
                    self.translations[language] = self.translations.get('en', {})
    
    def _save_language_file(self, language: str):
        """Save language translations to file"""
        try:
            lang_file = self.lang_dir / f"{language}.json"
            with open(lang_file, 'w', encoding='utf-8') as f:
                json.dump(self.translations[language], f, indent=4, ensure_ascii=False)
            self.logger.info(f"Language file saved: {lang_file}")
        except Exception as e:
            self.logger.error(f"Error saving language file for {language}: {str(e)}")
    
    def _get_english_translations(self) -> Dict[str, str]:
        """Get English translations"""
        return {
            # Application
            'app_title': 'EPUB/PDF to TXT Converter v1.0.0',
            'ready': 'Ready',
            'loading': 'Loading...',
            'processing': 'Processing...',
            'complete': 'Complete',
            'error': 'Error',
            'success': 'Success',
            'warning': 'Warning',
            'confirm': 'Confirm',
            
            # File operations
            'file_selection': 'File Selection',
            'input': 'Input',
            'output': 'Output',
            'browse': 'Browse',
            'select_input': 'Select Input',
            'select_input_type': 'Select a file or folder?\n\nYes = Select a file\nNo = Select a folder\nCancel = Cancel',
            'select_input_file': 'Select Input File',
            'select_input_folder': 'Select Input Folder',
            'select_output_folder': 'Select Output Folder',
            'select_input_path': 'Please select an input file or folder',
            'select_output_path': 'Please select an output folder',
            'input_not_exist': 'Input path does not exist',
            
            # File types
            'all_supported': 'All Supported Files',
            'epub_files': 'EPUB Files',
            'pdf_files': 'PDF Files',
            'all_files': 'All Files',
            
            # Options
            'options': 'Options',
            'preserve_structure': 'Preserve folder structure',
            'skip_existing': 'Skip existing files',
            
            # Conversion
            'convert': 'Convert',
            'converting': 'Converting...',
            'conversion_complete': 'Conversion completed successfully',
            'conversion_successful': 'Conversion completed successfully!',
            'conversion_failed': 'Conversion failed',
            'conversion_error': 'Conversion error',
            
            # Progress messages
            'scanning_files': 'Scanning files...',
            'converting_file': 'Converting file',
            'extracting_text': 'Extracting text...',
            'saving_file': 'Saving file...',
            'processing_epub': 'Processing EPUB file...',
            'processing_pdf': 'Processing PDF file...',
            
            # Controls
            'clear': 'Clear',
            'exit': 'Exit',
            'confirm_exit': 'Are you sure you want to exit?',
            
            # Statistics
            'files_processed': 'Files processed',
            'files_successful': 'Files successful',
            'files_failed': 'Files failed',
            'total_files': 'Total files',
            
            # Errors
            'file_not_found': 'File not found',
            'permission_denied': 'Permission denied',
            'invalid_file_format': 'Invalid file format',
            'conversion_interrupted': 'Conversion was interrupted',
            'unknown_error': 'Unknown error occurred'
        }
    
    def _get_chinese_translations(self) -> Dict[str, str]:
        """Get Traditional Chinese translations"""
        return {
            # Application
            'app_title': 'EPUB/PDF 轉 TXT 轉換器 v1.0.0',
            'ready': '準備就緒',
            'loading': '載入中...',
            'processing': '處理中...',
            'complete': '完成',
            'error': '錯誤',
            'success': '成功',
            'warning': '警告',
            'confirm': '確認',
            
            # File operations
            'file_selection': '檔案選擇',
            'input': '輸入',
            'output': '輸出',
            'browse': '瀏覽',
            'select_input': '選擇輸入',
            'select_input_type': '選擇檔案或資料夾？\n\n是 = 選擇檔案\n否 = 選擇資料夾\n取消 = 取消',
            'select_input_file': '選擇輸入檔案',
            'select_input_folder': '選擇輸入資料夾',
            'select_output_folder': '選擇輸出資料夾',
            'select_input_path': '請選擇輸入檔案或資料夾',
            'select_output_path': '請選擇輸出資料夾',
            'input_not_exist': '輸入路徑不存在',
            
            # File types
            'all_supported': '所有支援的檔案',
            'epub_files': 'EPUB 檔案',
            'pdf_files': 'PDF 檔案',
            'all_files': '所有檔案',
            
            # Options
            'options': '選項',
            'preserve_structure': '保留資料夾結構',
            'skip_existing': '跳過現有檔案',
            
            # Conversion
            'convert': '轉換',
            'converting': '轉換中...',
            'conversion_complete': '轉換成功完成',
            'conversion_successful': '轉換成功完成！',
            'conversion_failed': '轉換失敗',
            'conversion_error': '轉換錯誤',
            
            # Progress messages
            'scanning_files': '掃描檔案中...',
            'converting_file': '轉換檔案',
            'extracting_text': '提取文字中...',
            'saving_file': '儲存檔案中...',
            'processing_epub': '處理 EPUB 檔案中...',
            'processing_pdf': '處理 PDF 檔案中...',
            
            # Controls
            'clear': '清除',
            'exit': '離開',
            'confirm_exit': '您確定要離開嗎？',
            
            # Statistics
            'files_processed': '已處理檔案',
            'files_successful': '成功檔案',
            'files_failed': '失敗檔案',
            'total_files': '總檔案數',
            
            # Errors
            'file_not_found': '檔案未找到',
            'permission_denied': '權限被拒絕',
            'invalid_file_format': '無效的檔案格式',
            'conversion_interrupted': '轉換被中斷',
            'unknown_error': '發生未知錯誤'
        }
    
    def set_language(self, language: str):
        """Set current language"""
        if language in self.translations:
            self.current_language = language
            self.logger.info(f"Language set to {language}")
        else:
            self.logger.warning(f"Language {language} not found, using English")
            self.current_language = 'en'
    
    def get_text(self, key: str) -> str:
        """Get translated text for a key"""
        # Try current language first
        if self.current_language in self.translations:
            text = self.translations[self.current_language].get(key)
            if text:
                return text
        
        # Fallback to English
        if 'en' in self.translations:
            text = self.translations['en'].get(key)
            if text:
                return text
        
        # Fallback to key itself
        self.logger.warning(f"Translation not found for key: {key}")
        return key
    
    def get_available_languages(self) -> list:
        """Get list of available languages"""
        return list(self.translations.keys())
    
    def get_language_name(self, language: str) -> str:
        """Get display name for a language"""
        names = {
            'en': 'English',
            'zh_TW': '中文 (繁體)'
        }
        return names.get(language, language)
