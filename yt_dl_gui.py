import tkinter as tk
from pytube import YouTube
import threading


#----------------------------------１枚目のフレーム----------------------------------

# １枚目のフレーム作成
def downloader_1():
  # ウィンドウのタイトル指定
  root.title("Youtube Downloader")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl1_1 = tk.Label(frame, text="URLを入力してください", font=(yu_font, 30))
  txtbox1_1 = tk.Entry(frame, font=(yu_font, 15))
  btn1_1 = tk.Button(frame, text="実行", font=(yu_font, 20), cursor=mouse,
                     command=lambda: downloader_2(txtbox1_1.get()))
  #
  # ホバー時にボタンの色を変更
  btn1_1.bind("<Enter>", enter_bg)
  btn1_1.bind("<Leave>", leave_bg)
  #
  # ウィジェット配置
  lbl1_1.place(x=180, y=150)
  txtbox1_1.place(x=100, y=300, width=450, height=35)
  btn1_1.place(x=600, y=300, width=100, height=35)
  #
  # フレームを最上面へ
  frame.tkraise()
  #

#-----------------------------------------------------------------------------------
#----------------------------------２枚目のフレーム----------------------------------

# ２枚目のフレーム作成
def downloader_2(url):
  # ウィンドウのタイトル指定
  root.title("Youtube Downloader")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl2_1 = tk.Label(frame, text="動画をダウンロードしています．．．", font=(yu_font, 30))
  #
  # ウィジェット配置
  lbl2_1.place(x=80, y=200)
  #
  # ラベルを表示した5秒後に、３枚目へ進む
  lbl2_1.after(5000, downloader_3)
  #
  # 並列処理の命令
  thr2_1 = threading.Thread(target=frame.tkraise)
  thr2_2 = threading.Thread(target=YouTube(str(url)).streams.get_highest_resolution().download)
  #
  # フレームを最上面へ
  thr2_1.start()
  #
  # 動画のダウンロード
  thr2_2.start()
  #

#-----------------------------------------------------------------------------------
#----------------------------------３枚目のフレーム----------------------------------

# ３枚目のフレーム作成
def downloader_3():
  # ウィンドウのタイトル指定
  root.title("Youtube Downloader")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl3_1 = tk.Label(frame, text="ダウンロードが完了しました", font=(yu_font, 30))
  lbl3_2 = tk.Label(frame, text="最初のページに戻ります", font=(yu_font, 15))
  #
  # ウィジェット配置
  lbl3_1.place(x=130, y=200)
  lbl3_2.place(x=280, y=350)
  #
  # 3秒後、１枚目に戻る
  lbl3_1.after(3000, downloader_1)
  #
  # フレームを最上面へ
  frame.tkraise()
  #

#-----------------------------------------------------------------------------------
#------------------------------------初期設定------------------------------------

# ウィンドウ作成
root = tk.Tk()

# ウィンドウの大きさを固定
root.minsize(width=800, height=500)
root.maxsize(width=800, height=500)

# ウィンドウ内部のエリア変化率を１：１に固定
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# フォント指定
yu_font = "游ゴシック"

# ボタンにカーソルが乗ったときの色指定
def enter_bg(event):
  event.widget["bg"] = "#D3D3D3"

# ボタンからカーソルが離れたときの色指定
def leave_bg(event):
  event.widget["bg"] = "SystemButtonFace"

# マウスホバー時のカーソル変更
mouse = "hand2"

#-----------------------------------------------------------------------------------

downloader_1()

root.mainloop()
