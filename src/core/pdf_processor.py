"""
PDF processor for extracting text content from PDF files
"""

import PyPDF2
import pdfplumber
from pathlib import Path
from typing import Optional, Callable
import logging

from utils import app_logger


class PdfProcessor:
    """Processor for PDF files"""
    
    def __init__(self):
        self.logger = app_logger.get_logger()
        
        # Try to determine which PDF library to use
        self.preferred_library = self._detect_pdf_library()
        self.logger.info(f"Using {self.preferred_library} for PDF processing (recommended)")
    
    def _detect_pdf_library(self) -> str:
        """Detect which PDF library to use"""
        try:
            import pdfplumber
            return 'pdfplumber'
        except ImportError:
            try:
                import PyPDF2
                return 'PyPDF2'
            except ImportError:
                raise ImportError("No PDF processing library found. Please install pdfplumber or PyPDF2.")
    
    def extract_text(self, pdf_path: str, progress_callback: Optional[Callable[[int, str], None]] = None) -> str:
        """
        Extract text content from PDF file
        
        Args:
            pdf_path: Path to PDF file
            progress_callback: Optional progress callback
            
        Returns:
            str: Extracted text content
        """
        try:
            if progress_callback:
                progress_callback(20, "Opening PDF file...")
            
            # Try pdfplumber first (better text extraction)
            text_content = self._extract_with_pdfplumber(pdf_path, progress_callback)
            
            if not text_content:
                if progress_callback:
                    progress_callback(30, "Trying alternative extraction method...")
                # Fallback to PyPDF2
                text_content = self._extract_with_pypdf2(pdf_path, progress_callback)
            
            if not text_content:
                self.logger.warning(f"No text content extracted from {pdf_path}")
                return ""
            
            self.logger.info(f"Successfully extracted {len(text_content)} characters from {pdf_path}")
            return text_content
            
        except Exception as e:
            self.logger.error(f"Error extracting text from PDF {pdf_path}: {str(e)}")
            return ""
    
    def _extract_with_pdfplumber(self, pdf_path: str, progress_callback: Optional[Callable[[int, str], None]] = None) -> str:
        """Extract text using pdfplumber (preferred method)"""
        try:
            text_content = []
            
            with pdfplumber.open(pdf_path) as pdf:
                total_pages = len(pdf.pages)
                
                if progress_callback:
                    progress_callback(30, f"Processing {total_pages} pages with pdfplumber...")
                
                for page_num, page in enumerate(pdf.pages):
                    try:
                        page_text = page.extract_text()
                        if page_text:
                            # Clean the text
                            page_text = self._clean_text(page_text)
                            if page_text.strip():
                                text_content.append(page_text)
                        
                        if progress_callback and total_pages > 0:
                            progress = 30 + int((page_num / total_pages) * 50)
                            progress_callback(progress, f"Processing page {page_num + 1}/{total_pages}")
                    
                    except Exception as e:
                        self.logger.warning(f"Error processing page {page_num + 1}: {str(e)}")
                        continue
            
            return '\n\n'.join(text_content)
            
        except Exception as e:
            self.logger.warning(f"pdfplumber extraction failed for {pdf_path}: {str(e)}")
            return ""
    
    def _extract_with_pypdf2(self, pdf_path: str, progress_callback: Optional[Callable[[int, str], None]] = None) -> str:
        """Extract text using PyPDF2 (fallback method)"""
        try:
            text_content = []
            
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)
                
                if progress_callback:
                    progress_callback(30, f"Processing {total_pages} pages with PyPDF2...")
                
                for page_num in range(total_pages):
                    try:
                        page = pdf_reader.pages[page_num]
                        page_text = page.extract_text()
                        
                        if page_text:
                            # Clean the text
                            page_text = self._clean_text(page_text)
                            if page_text.strip():
                                text_content.append(page_text)
                        
                        if progress_callback and total_pages > 0:
                            progress = 30 + int((page_num / total_pages) * 50)
                            progress_callback(progress, f"Processing page {page_num + 1}/{total_pages}")
                    
                    except Exception as e:
                        self.logger.warning(f"Error processing page {page_num + 1}: {str(e)}")
                        continue
            
            return '\n\n'.join(text_content)
            
        except Exception as e:
            self.logger.warning(f"PyPDF2 extraction failed for {pdf_path}: {str(e)}")
            return ""
    
    def _clean_text(self, text: str) -> str:
        """Clean extracted text"""
        if not text:
            return ""
        
        # Remove excessive whitespace
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line:  # Only keep non-empty lines
                # Replace multiple spaces with single space
                line = ' '.join(line.split())
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def get_metadata(self, pdf_path: str) -> dict:
        """
        Extract metadata from PDF file
        
        Args:
            pdf_path: Path to PDF file
            
        Returns:
            dict: PDF metadata
        """
        metadata = {
            'title': '',
            'author': '',
            'subject': '',
            'creator': '',
            'producer': '',
            'creation_date': '',
            'modification_date': '',
            'pages': 0
        }
        
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                # Page count
                metadata['pages'] = len(pdf_reader.pages)
                
                # Document metadata
                if pdf_reader.metadata:
                    metadata['title'] = str(pdf_reader.metadata.get('/Title', ''))
                    metadata['author'] = str(pdf_reader.metadata.get('/Author', ''))
                    metadata['subject'] = str(pdf_reader.metadata.get('/Subject', ''))
                    metadata['creator'] = str(pdf_reader.metadata.get('/Creator', ''))
                    metadata['producer'] = str(pdf_reader.metadata.get('/Producer', ''))
                    
                    # Dates
                    creation_date = pdf_reader.metadata.get('/CreationDate')
                    if creation_date:
                        metadata['creation_date'] = str(creation_date)
                    
                    mod_date = pdf_reader.metadata.get('/ModDate')
                    if mod_date:
                        metadata['modification_date'] = str(mod_date)
                
        except Exception as e:
            self.logger.warning(f"Error extracting metadata from {pdf_path}: {str(e)}")
        
        return metadata
