# User Manual

Complete guide for using the EPUB/PDF to TXT Converter.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Conversion Process](#conversion-process)
4. [Advanced Features](#advanced-features)
5. [Settings and Preferences](#settings-and-preferences)
6. [Troubleshooting](#troubleshooting)

## Getting Started

### System Requirements
- Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- Python 3.7+ (for source installation)
- 512MB available RAM (minimum)
- 50MB available disk space

### Installation Options

#### Option 1: Executable (Recommended)
1. Download from [GitHub Releases](https://github.com/wayhong0928/epub-pdf-to-txt-converter/releases)
2. Extract the ZIP file to your desired location
3. Run `EPUB_PDF_to_TXT_Converter.exe`

#### Option 2: Source Code
1. Clone or download the repository
2. Install Python 3.7+ from [python.org](https://python.org)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## Interface Overview

### Main Window Layout
```
┌─────────────────────────────────────────────────┐
│ Language Selection: [English] [中文(繁體)]      │
├─────────────────────────────────────────────────┤
│ File Selection                                  │
│ Input:  [Path Field]              [Browse]     │
│ Output: [Path Field]              [Browse]     │
├─────────────────────────────────────────────────┤
│ Options                                         │
│ □ Preserve folder structure                     │
│ □ Skip existing files                           │
├─────────────────────────────────────────────────┤
│ Progress                                        │
│ [████████████████████████████████] 100%        │
│ Status: Conversion completed successfully       │
├─────────────────────────────────────────────────┤
│ [Convert]  [Clear]  [Exit]                     │
├─────────────────────────────────────────────────┤
│ Status Bar: Ready                               │
└─────────────────────────────────────────────────┘
```

### Language Selection
- **English**: Sets interface to English
- **中文(繁體)**: Sets interface to Traditional Chinese
- Changes are applied immediately and saved automatically

### File Selection
- **Input**: Choose source files or folders containing EPUB/PDF files
- **Output**: Choose destination folder for converted TXT files
- **Browse Buttons**: Open file/folder selection dialogs

### Options
- **Preserve folder structure**: Maintains original directory hierarchy
- **Skip existing files**: Avoids re-processing files that already exist

### Progress Section
- **Progress Bar**: Visual indication of conversion progress
- **Status Text**: Detailed information about current operation
- **Real-time Updates**: Shows current file being processed

### Control Buttons
- **Convert**: Start the conversion process
- **Clear**: Reset all fields and progress
- **Exit**: Close the application (with confirmation)

## Conversion Process

### Single File Conversion
1. Click "Browse" next to Input field
2. Select "Yes" when prompted
3. Choose an EPUB or PDF file
4. Select output folder
5. Configure options as needed
6. Click "Convert"

### Batch Conversion
1. Click "Browse" next to Input field
2. Select "No" when prompted
3. Choose folder containing EPUB/PDF files
4. Select output folder
5. Configure options as needed
6. Click "Convert"

### Progress Monitoring
- Monitor the progress bar for overall completion
- Read status messages for detailed information
- Check logs folder for comprehensive conversion logs

### Completion
- Success message displayed upon completion
- Conversion statistics shown in final status
- Log files saved automatically for review

## Advanced Features

### Folder Structure Preservation
When enabled, maintains the original directory structure:
```
Input:
└── Books/
    ├── Fiction/
    │   ├── book1.epub
    │   └── book2.pdf
    └── Non-Fiction/
        └── book3.epub

Output:
└── Converted/
    ├── Fiction/
    │   ├── book1.txt
    │   └── book2.txt
    └── Non-Fiction/
        └── book3.txt
```

### Smart File Skipping
- Automatically detects existing output files
- Compares modification dates
- Skips files that don't need re-processing
- Displays skip statistics in final report

### Multi-Engine PDF Processing
- **Primary**: pdfplumber (best text extraction)
- **Fallback**: PyPDF2 (compatibility mode)
- Automatic selection based on file characteristics

### Comprehensive Logging
- Real-time conversion logs
- Detailed error reporting
- Performance statistics
- Saved to `logs/` directory

## Settings and Preferences

### Configuration File
Settings are automatically saved in `config.json`:

```json
{
    "language": "en",
    "preserve_structure": true,
    "skip_existing": true,
    "output_encoding": "utf-8",
    "log_level": "INFO",
    "window_geometry": "600x500",
    "last_input_path": "",
    "last_output_path": ""
}
```

### Customizable Settings
- **Language**: Interface language preference
- **Structure Preservation**: Default folder structure behavior
- **File Skipping**: Default skip existing files behavior
- **Window Geometry**: Remembered window size and position
- **Path Memory**: Remembers last used input/output paths

### Manual Configuration
You can manually edit `config.json` to customize:
- **Output Encoding**: Change text file encoding
- **Log Level**: Adjust logging verbosity
- **Window Size**: Set default window dimensions

## Troubleshooting

### Common Issues and Solutions

#### Application Won't Start
**Symptoms**: Error messages on startup, application crashes
**Solutions**:
1. Check Python version: `python --version` (needs 3.7+)
2. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`
3. Check for missing system libraries
4. Run from command line to see detailed error messages

#### No Text Extracted
**Symptoms**: Empty or very short TXT files generated
**Possible Causes**:
- PDF contains images instead of text (scanned documents)
- EPUB has DRM protection
- File corruption or unusual formatting
**Solutions**:
1. Check conversion logs for specific errors
2. Try alternative PDF processing software for scanned documents
3. Verify file integrity by opening in standard readers

#### Slow Conversion Speed
**Symptoms**: Conversion takes much longer than expected
**Optimization**:
1. Enable "Skip existing files" to avoid re-processing
2. Close other applications to free system resources
3. Use SSD storage for better I/O performance
4. Process smaller batches for large collections

#### Permission Errors
**Symptoms**: "Access denied" or "Permission denied" errors
**Solutions**:
1. Run application as administrator (Windows)
2. Check file and folder permissions
3. Ensure output directory is writable
4. Verify input files are not locked by other applications

#### Memory Issues
**Symptoms**: Application crashes with large files or batches
**Solutions**:
1. Process files in smaller batches
2. Close other applications to free RAM
3. Restart application between large conversion jobs
4. Check available system memory

### Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| E001 | File not found | Verify input path exists |
| E002 | Permission denied | Check file permissions |
| E003 | Insufficient disk space | Free up storage space |
| E004 | Unsupported format | Use supported file types |
| E005 | Memory allocation error | Reduce batch size |
| E006 | Network timeout | Check internet connection |

### Performance Optimization

#### For Large Batches
1. **Memory Management**: Close other applications
2. **Disk I/O**: Use fast storage (SSD preferred)
3. **Batch Size**: Process 50-100 files at a time
4. **System Resources**: Monitor CPU and memory usage

#### For Large Files
1. **PDF Files**: Files >100MB may take several minutes
2. **EPUB Files**: Complex layouts may slow processing
3. **Memory**: Ensure 2GB+ available RAM for large files
4. **Patience**: Some files legitimately take time to process

### Getting Additional Help

1. **Check Logs**: Review files in `logs/` directory
2. **Documentation**: Read complete documentation in `docs/`
3. **GitHub Issues**: Report bugs or request features
4. **Community**: Join discussions on GitHub

### Reporting Issues

When reporting problems, please include:
- Operating system and version
- Python version (if running from source)
- Complete error message
- Steps to reproduce the issue
- Sample files (if possible and not confidential)
- Log files from the conversion attempt

This information helps diagnose and resolve issues quickly.
