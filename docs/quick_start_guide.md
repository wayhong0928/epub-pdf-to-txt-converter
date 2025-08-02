# Quick Start Guide

This guide will help you get started with the EPUB/PDF to TXT Converter quickly.

## Installation

### Option 1: Download Executable (Recommended)
1. Download the latest release from [GitHub Releases](https://github.com/wayhong0928/epub-pdf-to-txt-converter/releases)
2. Extract the ZIP file
3. Run `EPUB_PDF_to_TXT_Converter.exe`

### Option 2: Run from Source
1. Clone the repository:
   ```bash
   git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
   cd epub-pdf-to-txt-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Basic Usage

### 1. Select Language
- Choose between English and Traditional Chinese (繁體中文)
- The interface will update immediately

### 2. Choose Input
- Click "Browse" next to Input field
- Select either:
  - **Yes**: Choose a single EPUB or PDF file
  - **No**: Choose a folder containing multiple files
  - **Cancel**: Cancel selection

### 3. Choose Output Folder
- Click "Browse" next to Output field
- Select the destination folder for converted TXT files

### 4. Configure Options
- **Preserve folder structure**: Maintains the original folder hierarchy
- **Skip existing files**: Skips files that already exist in output folder

### 5. Start Conversion
- Click "Convert" to begin
- Monitor progress in the progress bar
- View detailed status messages

## Supported Formats

### Input Formats
- **EPUB**: Electronic publication format
- **PDF**: Portable Document Format

### Output Format
- **TXT**: Plain text files (UTF-8 encoding)

## Features

- **Batch Processing**: Convert multiple files at once
- **Progress Tracking**: Real-time conversion progress
- **Multi-language Support**: English and Traditional Chinese
- **Folder Structure Preservation**: Maintain original organization
- **Smart File Skipping**: Avoid re-processing existing files
- **Detailed Logging**: Comprehensive conversion logs
- **Statistics Reporting**: Summary of conversion results

## Tips

1. **Large Files**: PDF files with many pages may take longer to process
2. **File Organization**: Use "Preserve folder structure" for organized output
3. **Batch Processing**: Process entire folders for efficiency
4. **Error Handling**: Check logs for detailed error information

## Troubleshooting

### Common Issues

**Application won't start**
- Ensure all dependencies are installed
- Check Python version (3.7+ required)

**No text extracted**
- Some PDF files may have text as images (not supported)
- EPUB files may have DRM protection

**Conversion errors**
- Check file permissions
- Ensure sufficient disk space
- Verify file format compatibility

### Getting Help

- Check the [documentation](.)
- View [Release Notes](../RELEASE_NOTES.md)
- Report issues on [GitHub Issues](https://github.com/wayhong0928/epub-pdf-to-txt-converter/issues)

## Next Steps

- Explore advanced features in the [User Manual](user_manual.md)
- View [Release Notes](../RELEASE_NOTES.md) for latest updates
- Contribute on [GitHub](https://github.com/wayhong0928/epub-pdf-to-txt-converter)