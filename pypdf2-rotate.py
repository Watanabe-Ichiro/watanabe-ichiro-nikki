import PyPDF2 as pp2

# PDFファイルが入っているフォルダのパス
path = r"C:\Users\owner\pdf-folder"

# フォルダ内のPDFファイルを読み込み
reader = pp2.PdfReader(fr"{path}\pdf-input.pdf")

# 新しいPDFの格納先を作成
writer = pp2.PdfWriter()

# ループで全ページを格納先に追加
for pages in reader.pages:
  writer.add_page(pages)

# １ページ目を右に90度回転させる
rotate_right = writer.pages[0].rotate(90)

# "wb"を指定して新しいファイルとして保存＆with open()によって自動的にcloseさせる
with open(fr"{path}\rotated.pdf", "wb") as fp:
  writer.write(fp)
