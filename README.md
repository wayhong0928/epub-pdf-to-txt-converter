# 📚 EPUB & PDF to TXT Converter v1.0.0

A powerful, professional-grade batch converter that transforms EPUB and PDF files into clean, readable TXT format with an intuitive multi-language graphical interface.

[**English**](README.md) | [**繁體中文**](README_zh-TW.md)

## 📖 Documentation

- **[Quick Start Guide](docs/quick_start_guide.md)**: Get started quickly
- **[User Manual](docs/user_manual.md)**: Comprehensive usage guide
- **[Release Notes](docs/RELEASE_NOTES.md)**: Version history and changelog

## ✨ Key Features

### 🌍 Multi-Language Support
- **Auto Language Detection**: Automatically detects and applies system language
- **Real-time Language Switching**: Switch between English and Traditional Chinese instantly
- **Complete Localization**: All interface elements fully support multiple languages
- **Persistent Preferences**: Language settings saved automatically

### 📄 Advanced Document Processing
- **Dual Format Support**: Seamlessly convert both EPUB and PDF files to TXT
- **Intelligent Batch Processing**: Handle hundreds of files automatically with smart queuing
- **Multiple Extraction Methods**: Advanced fallback strategies for difficult files
- **Content Validation**: Ensures meaningful content extraction (minimum 50 characters)
- **Large File Handling**: Support for files up to 200MB (PDF) and 50MB (EPUB)

### 💻 Professional User Experience
- **Modern GUI Design**: Clean, intuitive graphical interface built with tkinter
- **Real-time Progress Tracking**: Live conversion progress with detailed status indicators
- **Comprehensive Logging**: Detailed conversion logs with visual status indicators (✅ Success, ❌ Failed, ⚠️ Skipped)
- **Smart Error Handling**: Graceful handling of problematic files with detailed error reporting
- **Configuration Memory**: Automatically remembers window size, position, and user preferences

### 📊 Enterprise-Grade Features
- **Detailed Statistics**: Comprehensive conversion reports with metrics and analytics
- **Flexible Size Limits**: Configurable file size limits with intelligent warnings
- **Folder Structure Preservation**: Maintains original directory organization in output
- **Multiple Output Strategies**: Smart output folder generation and management
- **Robust Error Recovery**: Multiple fallback methods for challenging document formats

## 🛠️ Installation & Setup

### Method 1: Download Executable (Recommended)
1. Go to [Releases](https://github.com/wayhong0928/epub-pdf-to-txt-converter/releases) and download the latest version
2. Extract the ZIP file to your desired location
3. Double-click `epub_to_txt_converter.exe` to launch
4. Select your input folder containing EPUB/PDF files
5. Choose output folder for TXT files
6. Click "Start Conversion" and monitor progress

### Method 2: Run from Source
```bash
# Clone the repository
git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
cd epub-pdf-to-txt-converter

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

### Method 3: Build from Source
```bash
# For developers who want to create executable
python scripts/build_exe.py
```

## � System Requirements

### For Executable Version
- **OS**: Windows 7/10/11 (64-bit)
- **Memory**: 512MB RAM minimum, 1GB+ recommended
- **Storage**: 100MB free space for installation
- **No additional dependencies required**

### For Python Version
- **Python**: 3.7 or higher
- **OS**: Windows, macOS, Linux
- **Dependencies**: Automatically installed via requirements.txt

## �📖 Documentation

- **[Quick Start Guide](docs/Quick_Start_Guide.md)**: Detailed usage instructions
- **[Release Notes](docs/RELEASE_NOTES.md)**: Version history and changelog
- **[繁體中文說明](README_zh-TW.md)**: Traditional Chinese documentation

## 📊 Supported Formats & Specifications

| Format | Support Level | Max File Size | Processing Method |
|--------|---------------|---------------|-------------------|
| **EPUB** | ✅ Full Support | 50MB | ebooklib + BeautifulSoup |
| **PDF** | ✅ Full Support | 200MB | PyPDF2 + pdfplumber |
| **Future** | 🔄 Planned | TBD | MOBI, AZW, FB2 |

### Quality Features
- **Smart Content Detection**: Requires minimum 50 characters of actual content
- **Multiple Extraction Methods**: Fallback strategies for difficult files
- **Clean Text Output**: Removes formatting while preserving readable structure
- **Unicode Support**: Full international character support

## 🏗️ Project Structure

```
epub-pdf-to-txt/
├── main.py                     # Application entry point
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
├── README.md                   # Main documentation (English)
├── README_zh-TW.md             # 繁體中文說明文件
├── src/                        # Source code
│   ├── core/                   # Document conversion logic
│   ├── gui/                    # User interface components
│   ├── localization/           # Multi-language support
│   ├── config/                 # Configuration management
│   └── utils/                  # Utilities and logging
├── scripts/                    # Development tools
│   └── build_exe.py            # Executable builder
└── docs/                       # Documentation
    ├── Quick_Start_Guide.md    # Detailed usage guide
    └── RELEASE_NOTES.md        # Version history
```

### Core Architecture
- **Modular Design**: Clean separation between conversion logic, UI, and utilities
- **Multi-Language**: Complete internationalization with English and Traditional Chinese
- **Configuration**: Persistent user settings and preferences
- **Error Handling**: Comprehensive error catching with detailed reporting
- **Extensible**: Easy to add new document formats and languages

## 🔧 Configuration & Customization

### File Size Limits
- **EPUB**: 50MB (configurable in source)
- **PDF**: 200MB (configurable in source)
- **Content Minimum**: 50 characters

### Language Support
- **English**: Full support
- **Traditional Chinese**: Full support
- **System Detection**: Automatic language detection
- **Extensible**: Easy to add new languages

## 📁 Output Structure

```
Output_Folder/
├── Converted_TXT_Files/    # Main output directory
│   ├── book1.txt
│   ├── book2.txt
│   └── subfolder/
│       └── book3.txt
├── conversion_report_YYYYMMDD_HHMMSS.txt
└── (logs saved separately in application folder)
```

## 🐛 Troubleshooting

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| "Content insufficient" | File encrypted/corrupted | Verify file can be opened manually |
| "File too large" | Exceeds size limits | Split file or modify limits in source |
| Conversion failed | Complex PDF layout | Try different PDF reader first |
| UI not responding | Large batch processing | Wait and monitor log window |
| Language not switching | Display issue | Restart application if needed |

### Error Log Analysis
- 📁 **Log Location**: `logs/` folder in application directory
- 📊 **Report Files**: Generated in output folder after conversion
- 🔍 **Detailed Analysis**: Check conversion report for file-by-file status

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Development Setup
```bash
git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
cd epub-pdf-to-txt-converter
pip install -r requirements.txt
```

### Adding New Languages
1. Create new language file in `src/localization/`
2. Follow the structure of existing language files
3. Update language list in `src/localization/__init__.py`
4. Test thoroughly with both GUI and conversion features

### Building Executable
```bash
python scripts/build_exe.py
```

### Contribution Guidelines
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## � License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[ebooklib](https://github.com/aerkalov/ebooklib)**: For excellent EPUB processing capabilities
- **[PyPDF2 & pdfplumber](https://github.com/jsvine/pdfplumber)**: For robust PDF text extraction
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)**: For reliable HTML parsing
- **tkinter**: For cross-platform GUI framework
- **Community**: For feedback and contributions

## � Support

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)

## �📈 Project Status

[![GitHub release](https://img.shields.io/github/v/release/wayhong0928/epub-pdf-to-txt-converter?style=flat-square)](../../releases)
[![License](https://img.shields.io/github/license/wayhong0928/epub-pdf-to-txt-converter?style=flat-square)](LICENSE)
[![Downloads](https://img.shields.io/github/downloads/wayhong0928/epub-pdf-to-txt-converter/total?style=flat-square)](../../releases)

---

**Made with ❤️ for the digital reading community**
