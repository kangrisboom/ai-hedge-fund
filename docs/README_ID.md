# AI Hedge Fund

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

1. Install Poetry (jika belum terinstall):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Atur variabel lingkungan:
```bash
# Buat file .env untuk API key Anda
cp .env.example .env
```

4. Atur API key:
```bash
# Untuk menjalankan LLM yang di-host oleh OpenAI (gpt-4, gpt-4-mini, dll.)
OPENAI_API_KEY=api-key-openai-anda

# Untuk menjalankan LLM yang di-host oleh Groq (deepseek, llama3, dll.)
GROQ_API_KEY=api-key-groq-anda

# Untuk mendapatkan data keuangan
FINANCIAL_DATASETS_API_KEY=api-key-financial-datasets-anda
```

**Penting**: Anda harus mengatur `OPENAI_API_KEY`, `GROQ_API_KEY`, atau `ANTHROPIC_API_KEY` agar hedge fund dapat berfungsi.

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