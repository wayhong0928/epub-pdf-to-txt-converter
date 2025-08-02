# 📚 EPUB & PDF 轉 TXT 轉換器 v1.0.0

一個功能強大的專業級批次轉換器，能將 EPUB 和 PDF 檔案轉換為乾淨、可讀的 TXT 格式，並提供直觀的多語言圖形介面。

[**English**](README.md) | [**繁體中文**](README_zh-TW.md)

## 📖 文件

- **[快速入門指南](docs/quick_start_guide_zh_TW.md)**: 快速開始使用
- **[使用手冊](docs/user_manual_zh_TW.md)**: 詳盡的使用指南
- **[發布說明](docs/RELEASE_NOTES_zh-TW.md)**: 版本歷史與更新記錄

## ✨ 主要功能

### 🌍 多語言支援
- **自動語言偵測**：自動偵測並套用系統語言
- **即時語言切換**：在英文和繁體中文之間即時切換
- **完整本地化**：所有介面元素都完全支援多語言
- **持久化偏好設定**：語言設定自動儲存

### 📄 進階文件處理
- **雙格式支援**：無縫轉換 EPUB 和 PDF 檔案為 TXT
- **智慧批次處理**：透過智慧佇列自動處理數百個檔案
- **多重擷取方法**：針對困難檔案的進階備援策略
- **內容驗證**：確保有意義的內容擷取（最少 50 個字元）
- **大檔案處理**：支援最大 200MB（PDF）和 50MB（EPUB）的檔案

### 💻 專業使用者體驗
- **現代化 GUI 設計**：使用 tkinter 建構的簡潔、直觀圖形介面
- **即時進度追蹤**：即時轉換進度與詳細狀態指示器
- **完整日誌記錄**：詳細的轉換日誌與視覺狀態指示器（✅ 成功、❌ 失敗、⚠️ 跳過）
- **智慧錯誤處理**：優雅地處理問題檔案並提供詳細錯誤報告
- **設定記憶**：自動記憶視窗大小、位置和使用者偏好設定

### 📊 企業級功能
- **詳細統計**：包含指標和分析的完整轉換報告
- **檔案結構保留**：維持原始資料夾階層組織
- **智慧跳過機制**：避免重複處理現有檔案
- **背景處理**：不阻塞介面的非同步轉換
- **記憶體優化**：對大型批次作業進行高效的記憶體管理

## 🚀 快速開始

### 方式 1：下載執行檔（推薦）
1. 從 [Releases](https://github.com/wayhong0928/epub-pdf-to-txt-converter/releases) 下載最新版本
2. 解壓縮 ZIP 檔案
3. 執行 `EPUB_PDF_to_TXT_Converter.exe`

### 方式 2：從原始碼執行
```bash
# 複製儲存庫
git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
cd epub-pdf-to-txt-converter

# 安裝相依套件
pip install -r requirements.txt

# 執行應用程式
python main.py
```

## 📖 使用方法

### 基本轉換
1. **選擇語言**：在 English 和中文（繁體）之間選擇
2. **選擇輸入**：選擇檔案或包含 EPUB/PDF 檔案的資料夾
3. **選擇輸出**：指定轉換後 TXT 檔案的目標資料夾
4. **設定選項**：
   - ☑️ 保留資料夾結構
   - ☑️ 跳過現有檔案
5. **開始轉換**：點選「轉換」並監控進度

### 進階功能
- **批次處理**：一次選擇整個資料夾進行轉換
- **進度監控**：即時查看轉換狀態和統計
- **錯誤處理**：檢視詳細的轉換日誌和錯誤報告

## 🔧 設定

應用程式會在 `config.json` 中自動儲存您的偏好設定：

```json
{
    "language": "zh_TW",
    "preserve_structure": true,
    "skip_existing": true,
    "output_encoding": "utf-8",
    "window_geometry": "600x500"
}
```

## 📚 支援格式

| 輸入格式 | 副檔名 | 支援功能 |
|---------|--------|----------|
| EPUB | `.epub` | ✅ 文字擷取<br>✅ 中繼資料<br>✅ 章節順序 |
| PDF | `.pdf` | ✅ 文字擷取<br>✅ 多種引擎<br>⚠️ 影像文字受限 |

| 輸出格式 | 副檔名 | 編碼 |
|---------|--------|------|
| 純文字 | `.txt` | UTF-8 |

## 🏗️ 專案架構

```
epub-pdf-to-txt-converter/
├── main.py                 # 應用程式入口點
├── requirements.txt        # Python 相依套件
├── config.json            # 使用者設定（自動生成）
├── src/                   # 原始碼模組
│   ├── core/              # 核心轉換邏輯
│   │   ├── converter.py   # 主要轉換器
│   │   ├── epub_processor.py  # EPUB 處理器
│   │   └── pdf_processor.py   # PDF 處理器
│   ├── gui/               # 圖形使用者介面
│   │   └── main_window.py # 主視窗
│   ├── config/            # 設定管理
│   │   └── settings.py    # 設定處理器
│   ├── localization/      # 多語言支援
│   │   ├── lang_manager.py    # 語言管理器
│   │   ├── en.json        # 英文語言包
│   │   └── zh_TW.json     # 繁體中文語言包
│   └── utils/             # 工具模組
│       ├── app_logger.py  # 日誌系統
│       └── reporter.py    # 報告生成器
├── scripts/               # 建置和部署腳本
│   └── build_exe.py       # 可執行檔建置腳本
├── docs/                  # 文檔
│   ├── quick_start_guide.md        # 英文快速入門
│   ├── quick_start_guide_zh_TW.md  # 中文快速入門
│   └── ...                # 其他文檔
├── logs/                  # 應用程式日誌（自動生成）
├── dist/                  # 建置輸出（自動生成）
└── build/                 # 建置暫存（自動生成）
```

## 🔍 疑難排解

### 常見問題

**❓ 應用程式無法啟動**
```bash
# 檢查 Python 版本
python --version  # 需要 3.7+

# 重新安裝相依套件
pip install -r requirements.txt --force-reinstall
```

**❓ 無法提取文字**
- **PDF 問題**：某些 PDF 包含掃描影像而非文字
- **EPUB 問題**：某些 EPUB 檔案可能有 DRM 保護
- **解決方案**：檢查轉換日誌以獲得詳細錯誤資訊

**❓ 轉換速度慢**
- **大檔案**：PDF 檔案頁數多會需要較長時間
- **最佳化**：使用「跳過現有檔案」選項避免重複處理
- **硬體**：考慮升級到 SSD 和更多 RAM

### 錯誤代碼

| 代碼 | 說明 | 解決方案 |
|------|------|----------|
| `E001` | 檔案不存在 | 檢查輸入路徑 |
| `E002` | 權限被拒 | 以管理員身分執行 |
| `E003` | 磁碟空間不足 | 釋放儲存空間 |
| `E004` | 格式不支援 | 使用支援的檔案格式 |

## 📈 效能指標

| 檔案類型 | 平均速度 | 記憶體使用 |
|---------|---------|-----------|
| EPUB (小) | 1-5 MB/s | ~50MB |
| EPUB (大) | 0.5-2 MB/s | ~100MB |
| PDF (文字) | 2-10 MB/s | ~75MB |
| PDF (複雜) | 0.2-1 MB/s | ~150MB |

## 🤝 貢獻

我們歡迎各種形式的貢獻！

### 開發設定
```bash
# 複製專案
git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
cd epub-pdf-to-txt-converter

# 建立虛擬環境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安裝開發相依套件
pip install -r requirements.txt

# 執行測試
python -m pytest tests/
```

### 貢獻指南
1. Fork 專案
2. 建立功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交變更 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 開啟 Pull Request

### 議題報告
在回報 bug 時，請包含：
- 作業系統和版本
- Python 版本
- 錯誤訊息的完整內容
- 重現步驟
- 範例檔案（如果可能）

## 📄 授權條款

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案。

## 🙏 致謝

### 核心相依套件
- **BeautifulSoup4** - HTML/XML 解析
- **PyPDF2** - PDF 處理
- **pdfplumber** - 進階 PDF 文字擷取
- **lxml** - 高效能 XML 處理
- **tkinter** - GUI 框架

### 社群貢獻
感謝所有貢獻者和使用者的回饋，讓這個專案持續改善。

## 📞 聯絡資訊

- **專案主頁**：[GitHub Repository](https://github.com/wayhong0928/epub-pdf-to-txt-converter)
- **問題回報**：[GitHub Issues](https://github.com/wayhong0928/epub-pdf-to-txt-converter/issues)
- **功能請求**：[GitHub Discussions](https://github.com/wayhong0928/epub-pdf-to-txt-converter/discussions)

---

**⭐ 如果這個專案對您有幫助，請考慮給它一個星星！**
