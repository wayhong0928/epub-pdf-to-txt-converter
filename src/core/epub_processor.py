"""
EPUB processor for extracting text content from EPUB files
"""

import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Callable, List
from bs4 import BeautifulSoup
import logging

from utils import app_logger


class EpubProcessor:
    """Processor for EPUB files"""
    
    def __init__(self):
        self.logger = app_logger.get_logger()
        self.namespaces = {
            'container': 'urn:oasis:names:tc:opendocument:xmlns:container',
            'opf': 'http://www.idpf.org/2007/opf',
            'dc': 'http://purl.org/dc/elements/1.1/'
        }
    
    def extract_text(self, epub_path: str, progress_callback: Optional[Callable[[int, str], None]] = None) -> str:
        """
        Extract text content from EPUB file
        
        Args:
            epub_path: Path to EPUB file
            progress_callback: Optional progress callback
            
        Returns:
            str: Extracted text content
        """
        try:
            if progress_callback:
                progress_callback(20, "Opening EPUB file...")
            
            with zipfile.ZipFile(epub_path, 'r') as zip_file:
                # Find OPF file
                opf_path = self._find_opf_path(zip_file)
                if not opf_path:
                    self.logger.error(f"Could not find OPF file in {epub_path}")
                    return ""
                
                if progress_callback:
                    progress_callback(30, "Reading OPF file...")
                
                # Parse OPF file to get reading order
                spine_items = self._parse_opf_spine(zip_file, opf_path)
                if not spine_items:
                    self.logger.error(f"Could not parse spine from OPF file in {epub_path}")
                    return ""
                
                if progress_callback:
                    progress_callback(40, f"Found {len(spine_items)} content files...")
                
                # Extract text from each spine item
                text_content = []
                total_items = len(spine_items)
                
                for i, item_path in enumerate(spine_items):
                    try:
                        if progress_callback:
                            progress = 40 + int((i / total_items) * 40)
                            progress_callback(progress, f"Processing {Path(item_path).name}...")
                        
                        # Read content file
                        content = zip_file.read(item_path).decode('utf-8', errors='ignore')
                        
                        # Extract text using BeautifulSoup
                        soup = BeautifulSoup(content, 'html.parser')
                        text = soup.get_text(separator='\n', strip=True)
                        
                        if text:
                            # Clean the text
                            cleaned_text = self._clean_text(text)
                            if cleaned_text:
                                text_content.append(cleaned_text)
                    
                    except Exception as e:
                        self.logger.warning(f"Error processing content file {item_path}: {str(e)}")
                        continue
                
                if progress_callback:
                    progress_callback(90, "Finalizing text extraction...")
                
                result = '\n\n'.join(text_content)
                self.logger.info(f"Successfully extracted {len(result)} characters from {epub_path}")
                return result
                
        except Exception as e:
            self.logger.error(f"Error extracting text from EPUB {epub_path}: {str(e)}")
            return ""
    
    def _find_opf_path(self, zip_file: zipfile.ZipFile) -> Optional[str]:
        """Find the OPF file path in the EPUB"""
        try:
            # Read container.xml
            container_content = zip_file.read('META-INF/container.xml')
            root = ET.fromstring(container_content)
            
            # Find rootfile element
            rootfile = root.find('.//container:rootfile', self.namespaces)
            if rootfile is not None:
                return rootfile.get('full-path')
            
            return None
            
        except Exception as e:
            self.logger.error(f"Error finding OPF path: {str(e)}")
            return None
    
    def _parse_opf_spine(self, zip_file: zipfile.ZipFile, opf_path: str) -> List[str]:
        """Parse OPF file to get spine reading order"""
        try:
            # Read OPF file
            opf_content = zip_file.read(opf_path)
            root = ET.fromstring(opf_content)
            
            # Get manifest items
            manifest = {}
            for item in root.findall('.//opf:item', self.namespaces):
                item_id = item.get('id')
                href = item.get('href')
                if item_id and href:
                    # Resolve relative path
                    opf_dir = str(Path(opf_path).parent)
                    if opf_dir == '.':
                        manifest[item_id] = href
                    else:
                        manifest[item_id] = f"{opf_dir}/{href}"
            
            # Get spine order
            spine_items = []
            for itemref in root.findall('.//opf:itemref', self.namespaces):
                idref = itemref.get('idref')
                if idref in manifest:
                    spine_items.append(manifest[idref])
            
            return spine_items
            
        except Exception as e:
            self.logger.error(f"Error parsing OPF spine: {str(e)}")
            return []
    
    def _clean_text(self, text: str) -> str:
        """Clean extracted text"""
        if not text:
            return ""
        
        # Split into lines and clean each line
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            line = line.strip()
            if line:  # Only keep non-empty lines
                # Replace multiple spaces with single space
                line = ' '.join(line.split())
                cleaned_lines.append(line)
        
        return '\n'.join(cleaned_lines)
    
    def get_metadata(self, epub_path: str) -> dict:
        """
        Extract metadata from EPUB file
        
        Args:
            epub_path: Path to EPUB file
            
        Returns:
            dict: EPUB metadata
        """
        metadata = {
            'title': '',
            'author': '',
            'language': '',
            'publisher': '',
            'identifier': '',
            'date': ''
        }
        
        try:
            with zipfile.ZipFile(epub_path, 'r') as zip_file:
                # Find OPF file
                opf_path = self._find_opf_path(zip_file)
                if not opf_path:
                    return metadata
                
                # Read OPF file
                opf_content = zip_file.read(opf_path)
                root = ET.fromstring(opf_content)
                
                # Extract metadata
                metadata_elem = root.find('.//opf:metadata', self.namespaces)
                if metadata_elem is not None:
                    # Title
                    title_elem = metadata_elem.find('.//dc:title', self.namespaces)
                    if title_elem is not None:
                        metadata['title'] = title_elem.text or ''
                    
                    # Author
                    author_elem = metadata_elem.find('.//dc:creator', self.namespaces)
                    if author_elem is not None:
                        metadata['author'] = author_elem.text or ''
                    
                    # Language
                    lang_elem = metadata_elem.find('.//dc:language', self.namespaces)
                    if lang_elem is not None:
                        metadata['language'] = lang_elem.text or ''
                    
                    # Publisher
                    pub_elem = metadata_elem.find('.//dc:publisher', self.namespaces)
                    if pub_elem is not None:
                        metadata['publisher'] = pub_elem.text or ''
                    
                    # Identifier
                    id_elem = metadata_elem.find('.//dc:identifier', self.namespaces)
                    if id_elem is not None:
                        metadata['identifier'] = id_elem.text or ''
                    
                    # Date
                    date_elem = metadata_elem.find('.//dc:date', self.namespaces)
                    if date_elem is not None:
                        metadata['date'] = date_elem.text or ''
                
        except Exception as e:
            self.logger.warning(f"Error extracting metadata from {epub_path}: {str(e)}")
        
        return metadata
