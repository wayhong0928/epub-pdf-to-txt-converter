# 快速入門指南

[**English**](quick_start_guide.md) | [**繁體中文**](quick_start_guide_zh_TW.md)

本指南將幫助您快速開始使用 EPUB/PDF 轉 TXT 轉換器。

## 安裝

### 方式一：下載執行檔（推薦）
1. 從 [GitHub Releases](https://github.com/wayhong0928/epub-pdf-to-txt-converter/releases) 下載最新版本
2. 解壓縮 ZIP 檔案
3. 執行 `EPUB_PDF_to_TXT_Converter.exe`

### 方式二：從原始碼執行
1. 複製專案：
   ```bash
   git clone https://github.com/wayhong0928/epub-pdf-to-txt-converter.git
   cd epub-pdf-to-txt-converter
   ```

2. 安裝相依套件：
   ```bash
   pip install -r requirements.txt
   ```

3. 執行應用程式：
   ```bash
   python main.py
   ```

## 基本使用

### 1. 選擇語言
- 在 English 和中文（繁體）之間選擇
- 介面會立即更新

### 2. 選擇輸入
- 點選輸入欄位旁的「瀏覽」
- 選擇：
  - **是**：選擇單一 EPUB 或 PDF 檔案
  - **否**：選擇包含多個檔案的資料夾
  - **取消**：取消選擇

### 3. 選擇輸出資料夾
- 點選輸出欄位旁的「瀏覽」
- 選擇轉換後 TXT 檔案的目標資料夾

### 4. 設定選項
- **保留資料夾結構**：維持原始資料夾階層
- **跳過現有檔案**：跳過輸出資料夾中已存在的檔案

### 5. 開始轉換
- 點選「轉換」開始
- 在進度條中監控進度
- 查看詳細狀態訊息

## 支援格式

### 輸入格式
- **EPUB**：電子出版格式
- **PDF**：可攜式文件格式

### 輸出格式
- **TXT**：純文字檔案（UTF-8 編碼）

## 功能特色

- **批次處理**：一次轉換多個檔案
- **進度追蹤**：即時轉換進度
- **多語言支援**：英文和繁體中文
- **資料夾結構保留**：維持原始組織結構
- **智慧檔案跳過**：避免重複處理現有檔案
- **詳細日誌**：完整的轉換記錄
- **統計報告**：轉換結果摘要

## 使用技巧

1. **大檔案**：頁數多的 PDF 檔案可能需要較長處理時間
2. **檔案組織**：使用「保留資料夾結構」來組織輸出
3. **批次處理**：處理整個資料夾以提高效率
4. **錯誤處理**：檢查日誌以獲得詳細錯誤資訊

## 疑難排解

### 常見問題

**應用程式無法啟動**
- 確保已安裝所有相依套件
- 檢查 Python 版本（需要 3.7+）

**無法提取文字**
- 某些 PDF 檔案可能包含圖片文字（不支援）
- EPUB 檔案可能有 DRM 保護

**轉換錯誤**
- 檢查檔案權限
- 確保有足夠的磁碟空間
- 驗證檔案格式相容性

### 取得協助

- 查看[文檔](docs/)
- 檢視[發布說明](RELEASE_NOTES.md)
- 在 [GitHub Issues](https://github.com/wayhong0928/epub-pdf-to-txt-converter/issues) 回報問題

## 下一步

- 探索[使用手冊](user_manual_zh_TW.md)中的進階功能
- 查看[發布說明](../RELEASE_NOTES.md)了解最新更新
- 在 [GitHub](https://github.com/wayhong0928/epub-pdf-to-txt-converter) 參與貢獻
