# 📦 發行版本 v1.0.0 - 初始版本

[**English**](RELEASE_NOTES.md) | [**繁體中文**](RELEASE_NOTES_zh-TW.md)

## 🎉 EPUB & PDF 轉換為 TXT - 第一個穩定版本

### 🌍 多語言功能
- **自動語言檢測**：啟動時自動檢測系統語言
- **即時語言切換**：可即時在英文與繁體中文之間切換
- **完整本地化**：所有介面元素完全支援多語言
- **偏好設定保存**：語言設定自動保存

### 🚀 核心功能
- **雙格式支援**：同時支援 EPUB 和 PDF 文件轉換為乾淨的 TXT 格式
- **智能批次處理**：自動處理數百個文件，具備智能排隊功能
- **專業錯誤處理**：多種提取方法，並提供詳細的錯誤報告
- **全面日誌記錄**：即時狀態更新，並提供視覺指示（✅ 成功，❌ 失敗，⚠️ 跳過）
- **現代化 GUI 設計**：直觀的介面，具備即時進度追蹤

### ✨ 進階功能
- 📚 **EPUB 處理**：完整的章節結構提取，並進行內容驗證
- 📄 **PDF 處理**：進階文字提取，並提供備援方法（支援高達 200MB 的文件）
- 🔄 **智能批次處理**：處理整個資料夾結構，並保持組織性
- 🛠️ **強大的錯誤恢復**：針對困難文件自動啟用備援方法
- 📊 **企業級報告**：提供全面的轉換報告與分析
- 🎯 **高成功率**：轉換成功率超過 95%，並驗證至少 50 個字元

### 📋 系統需求
- **Windows**：7/10/11 (64 位元)
- **無需依賴**：獨立執行檔，無需安裝 Python

### 📥 下載與安裝

#### 選項 1：獨立執行檔（推薦）
- 下載 `epub-pdf-to-txt-converter-v1.0.0.zip`
- 解壓縮並執行 `epub_to_txt_converter.exe`
- 無需安裝或依賴

#### 選項 2：Python 原始碼
- 下載原始碼
- 安裝需求：`pip install -r requirements.txt`
- 執行：`python main.py`

#### 選項 3：從原始碼建置
- 使用內建建置腳本：`python scripts/build_exe.py`

### 🔧 技術規格
- **專案架構**：模組化設計，清晰的關注點分離
- **EPUB 處理**：使用 ebooklib 與 BeautifulSoup4 進行 HTML 解析
- **PDF 處理**：PyPDF2 + pdfplumber 雙引擎
- **GUI 框架**：具備專業設計的 tkinter
- **檔案大小限制**：EPUB（50MB）、PDF（200MB）
- **內容驗證**：最少需要 50 字元
- **錯誤處理**：具備全面日誌記錄的多層級備用機制

### 📊 效能基準
- **小檔案**（<1MB）：每個檔案約 2 秒
- **中檔案**（1-10MB）：每個檔案約 5 秒
- **大檔案**（10-50MB）：每個檔案約 15 秒
- **批次處理**：100 個檔案約 5 分鐘

### 🐛 已知問題
- 超大 PDF 檔案（>200MB）會自動跳過
- 某些高度加密的 PDF 可能無法處理
- 純圖片 PDF 會產生極少文字提取結果

### 🔄 更新記錄
```
v1.0.0 (2025-08-02)
- 首個穩定版本發布
- EPUB 和 PDF 轉換支援
- 具備 GUI 的批次處理
- 全面錯誤處理
- 詳細報告系統
- Windows 執行檔建置
- 多語言介面支援
```

### 📖 快速開始指南
1. 下載並解壓縮 `epub-pdf-to-txt-converter-v1.0.0.zip`
2. 執行 `epub_to_txt_converter.exe`
3. 選擇語言（預設為自動偵測）
4. 選擇包含 EPUB/PDF 檔案的輸入資料夾
5. 選擇 TXT 檔案的輸出資料夾
6. 點選「開始轉換」並監控即時進度
7. 檢視詳細轉換日誌和統計資料

### 📞 支援與資源
- 📖 **文件**：[README.md](../README.md) | [繁體中文](../README_zh-TW.md)
- 🚀 **快速開始**：[Quick_Start_Guide.md](Quick_Start_Guide.md)
- 🐛 **問題回報**：[GitHub Issues](../../issues)
- 💬 **討論區**：[GitHub Discussions](../../discussions)

### 🙏 致謝
- **[ebooklib](https://github.com/aerkalov/ebooklib)** 團隊提供優秀的 EPUB 處理功能
- **[pdfplumber](https://github.com/jsvine/pdfplumber)** 開發者提供強健的 PDF 文字提取
- **[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)** 提供可靠的 HTML 解析
- **PyInstaller** 團隊提供專業的執行檔封裝
- **社群** 提供回饋和支援

---

**用 ❤️ 為數位閱讀社群打造**

### 📁 本版本包含檔案：
- `epub_to_txt_converter.exe` - 主執行檔（Windows）
- `README.md` - 完整文件（英文）
- `README_zh-TW.md` - 完整文件（繁體中文）
- `Quick_Start_Guide.md` - 快速開始指南
- `LICENSE` - MIT 授權條款
- `requirements.txt` - Python 相依套件
