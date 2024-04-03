import PyPDF2 as pp2

# PDFファイルが入っているフォルダのパス
path = r"C:\Users\owner\pdf_folder"

# フォルダ内のPDFファイル（４ページ）を読み込み
reader = pp2.PdfReader(fr"{path}\pdf-input.pdf")

# ループを使って、各ページをPDFファイルとして出力
# len(reader.pages)→読み込んだPDFファイルの総ページ数
for pages in range(len(reader.pages)):
  # 新しいPDFの格納先を作成 兼 リセット
  writer = pp2.PdfWriter()
  # 格納先にPDFファイルの１ページを追加
  writer.add_page(reader.pages[pages])
  # "wb"を指定して新しいファイルとして保存＆with open()によって自動的にcloseさせる
  with open(fr"{path}\split_{str(pages)}.pdf", "wb") as fp:
    writer.write(fp)
