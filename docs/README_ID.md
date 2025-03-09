# AI Hedge Fund

[English](../README.md) | [Bahasa Indonesia](README_ID.md)

Ini adalah bukti konsep untuk hedge fund yang ditenagai oleh AI. Tujuan dari proyek ini adalah untuk mengeksplorasi penggunaan AI dalam membuat keputusan trading. Proyek ini hanya untuk tujuan **edukasi** dan tidak dimaksudkan untuk trading atau investasi nyata.

Sistem ini menggunakan beberapa agen yang bekerja bersama:

1. Agen Ben Graham - Bapak investasi nilai, hanya membeli permata tersembunyi dengan margin of safety
2. Agen Bill Ackman - Investor aktivis, mengambil posisi berani dan mendorong perubahan
3. Agen Cathie Wood - Ratu investasi pertumbuhan, percaya pada kekuatan inovasi dan disrupsi
4. Agen Charlie Munger - Partner Warren Buffett, hanya membeli bisnis luar biasa dengan harga wajar
5. Agen Stanley Druckenmiller - Legenda trading makro yang mencari peluang asimetris dengan potensi pertumbuhan eksplosif
6. Agen Warren Buffett - Oracle dari Omaha, mencari perusahaan luar biasa dengan harga wajar
7. Agen Valuasi - Menghitung nilai intrinsik saham dan menghasilkan sinyal trading
8. Agen Sentimen - Menganalisis sentimen pasar dan menghasilkan sinyal trading
9. Agen Fundamental - Menganalisis data fundamental dan menghasilkan sinyal trading
10. Agen Teknikal - Menganalisis indikator teknikal dan menghasilkan sinyal trading
11. Manajer Risiko - Menghitung metrik risiko dan menetapkan batas posisi
12. Manajer Portofolio - Membuat keputusan trading akhir dan menghasilkan order

**Catatan**: sistem ini mensimulasikan keputusan trading, tidak benar-benar melakukan trading.

## Disclaimer

Proyek ini hanya untuk **tujuan pendidikan dan penelitian**.

- Tidak dimaksudkan untuk trading atau investasi nyata
- Tidak ada jaminan atau garansi yang diberikan
- Kinerja masa lalu tidak menunjukkan hasil masa depan
- Pembuat tidak bertanggung jawab atas kerugian finansial
- Konsultasikan dengan penasihat keuangan untuk keputusan investasi

Dengan menggunakan perangkat lunak ini, Anda setuju untuk menggunakannya hanya untuk tujuan pembelajaran.

## Pengaturan

Clone repositori:
```bash
git clone https://github.com/virattt/ai-hedge-fund.git
cd ai-hedge-fund
```

1. Install Python 3.9 atau lebih tinggi dari [python.org](https://www.python.org/downloads/)

2. Install Poetry:

Untuk Windows (PowerShell), jalankan sebagai administrator:
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Tambahkan Poetry ke PATH dan verifikasi instalasi:
```powershell
# Tambahkan ke PATH
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$env:APPDATA\Python\Scripts", "User")

# Perbarui variabel lingkungan di terminal saat ini
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

# Verifikasi instalasi
poetry --version
```

3. Install dependensi:
```powershell
# Konfigurasi poetry untuk membuat virtual environment di direktori proyek
poetry config virtualenvs.in-project true

# Install dependensi
poetry install

# Generate file lock jika diperlukan
poetry lock
```

4. Pengaturan variabel lingkungan:
```powershell
# Buat file .env untuk API key Anda
copy .env.example .env
```

5. Atur API key Anda:
```bash
# Untuk menjalankan LLM yang di-host oleh OpenAI (gpt-4o, gpt-4o-mini, dll.)
# Dapatkan API key OpenAI dari https://platform.openai.com/
OPENAI_API_KEY=api-key-openai-anda

# Untuk menjalankan LLM yang di-host oleh Groq (deepseek, llama3, dll.)
# Dapatkan API key Groq dari https://groq.com/
GROQ_API_KEY=api-key-groq-anda

# Untuk menjalankan LLM melalui OpenRouter (claude-3, mistral, dll.)
# Dapatkan API key OpenRouter dari https://openrouter.ai/
OPENROUTER_API_KEY=api-key-openrouter-anda

# Untuk mendapatkan data keuangan
# Dapatkan API key Financial Datasets dari https://financialdatasets.ai/
FINANCIAL_DATASETS_API_KEY=api-key-financial-datasets-anda
```

**Penting**: Anda harus mengatur setidaknya satu dari API key berikut agar hedge fund dapat berfungsi:
- `OPENAI_API_KEY` - Untuk model OpenAI (GPT-4, GPT-3.5)
- `GROQ_API_KEY` - Untuk model yang di-host Groq (LLaMA, DeepSeek)
- `OPENROUTER_API_KEY` - Untuk model OpenRouter (Claude-3, Mistral)
- `ANTHROPIC_API_KEY` - Untuk model Anthropic (Claude)

Jika Anda ingin menggunakan model dari semua penyedia, Anda perlu mengatur semua API key.

Data keuangan untuk AAPL, GOOGL, MSFT, NVDA, dan TSLA gratis dan tidak memerlukan API key.

Untuk ticker lainnya, Anda perlu mengatur `FINANCIAL_DATASETS_API_KEY` di file .env.

Catatan: Setelah menginstal Poetry, Anda mungkin perlu:
1. Tutup dan buka kembali terminal Anda
2. Atau restart Visual Studio Code
3. Atau restart komputer Anda

Anda dapat memverifikasi instalasi dengan menjalankan:
```powershell
%APPDATA%\Python\Scripts\poetry --version
```

## Penggunaan

### Menjalankan Hedge Fund
```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA
```

Anda dapat menambahkan flag `--show-reasoning` untuk menampilkan alasan dari setiap agen:
```bash
poetry run python src/main.py --ticker AAPL,MSFT,NVDA --show-reasoning
```

### Menjalankan Backtester
```bash
poetry run python src/backtester.py --ticker AAPL,MSFT,NVDA
```

## Struktur Proyek
```
ai-hedge-fund/
├── src/
│   ├── agents/                   # Definisi dan alur kerja agen
│   ├── tools/                    # Alat-alat agen
│   ├── backtester.py            # Alat backtesting
│   ├── main.py                  # Titik masuk utama
├── docs/                         # Dokumentasi
├── pyproject.toml
├── ...
```

## Kontribusi

1. Fork repositori
2. Buat branch fitur
3. Commit perubahan Anda
4. Push ke branch
5. Buat Pull Request

## Permintaan Fitur

Jika Anda memiliki permintaan fitur, silakan buka [issue](https://github.com/virattt/ai-hedge-fund/issues) dan pastikan ditandai dengan `enhancement`.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detailnya.