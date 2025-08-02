"""
Build Script for EPUB & PDF to TXT Converter
Creates executable using PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    print("Installing PyInstaller...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyinstaller'])
        print("✅ PyInstaller installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install PyInstaller: {e}")
        return False

def build_exe():
    """Build executable using PyInstaller"""
    print("Starting build process...")
    
    # Get project directory (parent of scripts)
    project_dir = Path(__file__).parent.parent
    main_file = project_dir / "main.py"
    
    if not main_file.exists():
        print(f"❌ Main file not found: {main_file}")
        return False
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                              # Single file executable
        '--windowed',                             # Hide console window (GUI app)
        '--name=EPUB_PDF_to_TXT_Converter',      # Executable name
        '--icon=icon.ico',                        # Icon file (if exists)
        f'--add-data={project_dir}/src/localization/*.json;localization',  # Language files
        '--hidden-import=tkinter',                # Ensure tkinter is included
        '--hidden-import=beautifulsoup4',         # Ensure BeautifulSoup is included
        '--hidden-import=pdfplumber',             # Ensure pdfplumber is included
        '--hidden-import=PyPDF2',                 # Ensure PyPDF2 is included
        '--hidden-import=lxml',                   # Ensure lxml is included
        '--distpath=dist',                        # Output directory
        '--workpath=build',                       # Working directory
        '--specpath=.',                           # Spec file location
        str(main_file)                            # Main program file
    ]
    
    try:
        # Check if icon file exists, remove icon parameter if not
        icon_path = project_dir / 'icon.ico'
        if not icon_path.exists():
            cmd = [c for c in cmd if not c.startswith('--icon')]
        
        # Change to project directory
        os.chdir(project_dir)
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Build successful!")
            exe_path = project_dir / "dist" / "EPUB_PDF_to_TXT_Converter.exe"
            print(f"Executable location: {exe_path}")
            return True
        else:
            print("❌ Build failed!")
            print("Error output:")
            print(result.stderr)
            return False
            
    except FileNotFoundError:
        print("❌ PyInstaller not found, please install first")
        return False
    except Exception as e:
        print(f"❌ Error during build process: {e}")
        return False

def create_release_package():
    """Create release package"""
    print("Creating release package...")
    
    project_dir = Path(__file__).parent.parent
    
    # Create release directory
    release_dir = project_dir / 'release'
    if release_dir.exists():
        shutil.rmtree(release_dir)
    release_dir.mkdir()
    
    # Files to copy
    files_to_copy = [
        'dist/EPUB_PDF_to_TXT_Converter.exe',
        'README.md',
        'README_zh_TW.md',
        'LICENSE',
        'requirements.txt',
        'RELEASE_NOTES.md'
    ]
    
    for file_path in files_to_copy:
        src = project_dir / file_path
        if src.exists():
            if src.is_file():
                shutil.copy2(src, release_dir / src.name)
                print(f"✅ Copied: {file_path}")
            else:
                print(f"⚠️ Skipped directory: {file_path}")
        else:
            print(f"⚠️ File not found: {file_path}")
    
    # Create ZIP package
    try:
        zip_name = 'EPUB-PDF-to-TXT-Converter-v1.0.0'
        shutil.make_archive(project_dir / zip_name, 'zip', release_dir)
        print(f"✅ Release package created: {zip_name}.zip")
        return True
    except Exception as e:
        print(f"❌ Failed to create release package: {e}")
        return False

def main():
    """Main build process"""
    print("=== EPUB & PDF to TXT Converter Build Script ===\n")
    
    # Install PyInstaller
    if not install_pyinstaller():
        return
    
    # Build executable
    if not build_exe():
        return
    
    # Create release package
    if not create_release_package():
        return
    
    print("\n🎉 Build completed successfully!")
    print("📦 Release file: EPUB-PDF-to-TXT-Converter-v1.0.0.zip")
    print("📁 Executable location: dist/EPUB_PDF_to_TXT_Converter.exe")
    print("\nNext steps:")
    print("1. Test executable functionality")
    print("2. Upload to GitHub Releases")
    print("3. Update download links in README")

if __name__ == "__main__":
    main()
