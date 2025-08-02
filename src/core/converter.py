"""
Main document converter for EPUB and PDF files
"""

from pathlib import Path
from typing import Optional, Callable, List, Tuple
import logging

from .epub_processor import EpubProcessor
from .pdf_processor import PdfProcessor
from utils import app_logger, reporter


class DocumentToTxtConverter:
    """Main converter for EPUB and PDF documents to TXT format"""
    
    def __init__(self):
        self.logger = app_logger.get_logger()
        self.epub_processor = EpubProcessor()
        self.pdf_processor = PdfProcessor()
        
        # Conversion settings
        self.preserve_structure = True
        self.skip_existing = True
        
        # Statistics
        self.stats = {
            'total_files': 0,
            'successful': 0,
            'failed': 0,
            'skipped': 0
        }
        
        self.logger.info("DocumentToTxtConverter initialized")
    
    def convert_file(self, input_path: str, output_dir: str, 
                    progress_callback: Optional[Callable[[int, str], None]] = None) -> bool:
        """
        Convert a single file to TXT format
        
        Args:
            input_path: Path to input file
            output_dir: Output directory
            progress_callback: Optional progress callback
            
        Returns:
            bool: True if successful
        """
        try:
            input_file = Path(input_path)
            output_path = Path(output_dir)
            
            if not input_file.exists():
                self.logger.error(f"Input file does not exist: {input_path}")
                return False
            
            if not output_path.exists():
                output_path.mkdir(parents=True, exist_ok=True)
            
            # Reset statistics
            self.stats = {'total_files': 1, 'successful': 0, 'failed': 0, 'skipped': 0}
            
            if progress_callback:
                progress_callback(10, f"Processing {input_file.name}...")
            
            # Determine file type and process
            file_ext = input_file.suffix.lower()
            
            if file_ext == '.epub':
                success = self._convert_epub_file(input_file, output_path, progress_callback)
            elif file_ext == '.pdf':
                success = self._convert_pdf_file(input_file, output_path, progress_callback)
            else:
                self.logger.warning(f"Unsupported file type: {file_ext}")
                return False
            
            if success:
                self.stats['successful'] += 1
                if progress_callback:
                    progress_callback(100, "Conversion completed successfully")
            else:
                self.stats['failed'] += 1
                if progress_callback:
                    progress_callback(100, "Conversion failed")
            
            return success
            
        except Exception as e:
            self.logger.error(f"Error converting file {input_path}: {str(e)}")
            return False
    
    def convert_directory(self, input_dir: str, output_dir: str,
                         progress_callback: Optional[Callable[[int, str], None]] = None) -> bool:
        """
        Convert all supported files in a directory
        
        Args:
            input_dir: Input directory
            output_dir: Output directory
            progress_callback: Optional progress callback
            
        Returns:
            bool: True if at least one file was converted successfully
        """
        try:
            input_path = Path(input_dir)
            output_path = Path(output_dir)
            
            if not input_path.exists():
                self.logger.error(f"Input directory does not exist: {input_dir}")
                return False
            
            if not output_path.exists():
                output_path.mkdir(parents=True, exist_ok=True)
            
            # Find all supported files
            supported_files = self._find_supported_files(input_path)
            
            if not supported_files:
                self.logger.warning(f"No supported files found in {input_dir}")
                return False
            
            # Reset statistics
            self.stats = {
                'total_files': len(supported_files),
                'successful': 0,
                'failed': 0,
                'skipped': 0
            }
            
            if progress_callback:
                progress_callback(5, f"Found {len(supported_files)} files to convert...")
            
            # Process each file
            for i, file_path in enumerate(supported_files):
                try:
                    relative_path = file_path.relative_to(input_path)
                    
                    # Calculate output path
                    if self.preserve_structure:
                        output_file_dir = output_path / relative_path.parent
                    else:
                        output_file_dir = output_path
                    
                    # Ensure output directory exists
                    output_file_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Progress update
                    if progress_callback:
                        progress = 10 + int((i / len(supported_files)) * 80)
                        progress_callback(progress, f"Converting {relative_path.name}... ({i+1}/{len(supported_files)})")
                    
                    # Convert file
                    file_ext = file_path.suffix.lower()
                    
                    if file_ext == '.epub':
                        success = self._convert_epub_file(file_path, output_file_dir, None)
                    elif file_ext == '.pdf':
                        success = self._convert_pdf_file(file_path, output_file_dir, None)
                    else:
                        self.logger.warning(f"Unsupported file type: {file_ext}")
                        continue
                    
                    if success:
                        self.stats['successful'] += 1
                    else:
                        self.stats['failed'] += 1
                
                except Exception as e:
                    self.logger.error(f"Error processing file {file_path}: {str(e)}")
                    self.stats['failed'] += 1
            
            # Final progress update
            if progress_callback:
                progress_callback(100, f"Completed: {self.stats['successful']} successful, {self.stats['failed']} failed")
            
            # Generate report
            report_path = output_path / "conversion_report.txt"
            reporter.generate_conversion_report(self.stats, supported_files, report_path)
            
            return self.stats['successful'] > 0
            
        except Exception as e:
            self.logger.error(f"Error converting directory {input_dir}: {str(e)}")
            return False
    
    def _find_supported_files(self, directory: Path) -> List[Path]:
        """Find all supported files in directory"""
        supported_extensions = {'.epub', '.pdf'}
        supported_files = []
        
        for file_path in directory.rglob('*'):
            if file_path.is_file() and file_path.suffix.lower() in supported_extensions:
                supported_files.append(file_path)
        
        return sorted(supported_files)
    
    def _convert_epub_file(self, input_file: Path, output_dir: Path,
                          progress_callback: Optional[Callable[[int, str], None]] = None) -> bool:
        """Convert EPUB file to TXT"""
        try:
            output_file = output_dir / f"{input_file.stem}.txt"
            
            # Skip if file exists and skip_existing is True
            if self.skip_existing and output_file.exists():
                self.logger.info(f"Skipping existing file: {output_file}")
                self.stats['skipped'] += 1
                return True
            
            # Extract text from EPUB
            text_content = self.epub_processor.extract_text(str(input_file), progress_callback)
            
            if not text_content:
                self.logger.warning(f"No text content extracted from {input_file}")
                return False
            
            # Save to TXT file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            self.logger.info(f"Successfully converted {input_file} to {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error converting EPUB file {input_file}: {str(e)}")
            return False
    
    def _convert_pdf_file(self, input_file: Path, output_dir: Path,
                         progress_callback: Optional[Callable[[int, str], None]] = None) -> bool:
        """Convert PDF file to TXT"""
        try:
            output_file = output_dir / f"{input_file.stem}.txt"
            
            # Skip if file exists and skip_existing is True
            if self.skip_existing and output_file.exists():
                self.logger.info(f"Skipping existing file: {output_file}")
                self.stats['skipped'] += 1
                return True
            
            # Extract text from PDF
            text_content = self.pdf_processor.extract_text(str(input_file), progress_callback)
            
            if not text_content:
                self.logger.warning(f"No text content extracted from {input_file}")
                return False
            
            # Save to TXT file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(text_content)
            
            self.logger.info(f"Successfully converted {input_file} to {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error converting PDF file {input_file}: {str(e)}")
            return False
    
    def get_statistics(self) -> dict:
        """Get conversion statistics"""
        return self.stats.copy()
