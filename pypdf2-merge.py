import PyPDF2 as pp2
import glob

# PDFファイルが入っているフォルダのパス
path = r"C:\Users\owner\pdf_folder"

# フォルダ内の全PDFファイルを読み込み
pdf_list = glob.glob(fr"{path}\*.pdf")

# 結合機能を呼び出し
merger = pp2.PdfMerger()

# ループで全PDFファイルを結合機能へ格納
for pdf in pdf_list:
  merger.append(pdf)

# 結合して保存する
merger.write(fr"{path}\merged.pdf")

# 結合機能を閉じる
merger.close()
