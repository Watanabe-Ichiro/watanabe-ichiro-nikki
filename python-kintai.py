import tkinter as tk
import pandas as pd
import nfc
import binascii
import datetime as dt
import subprocess
import os


#-----------------------------------1.ホーム画面-----------------------------------

def home_display():
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール")
  #
  # メインページフレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ボタン作成
  button1_1 = tk.Button(frame, text="出社確認", font=(yu_font, 35, "bold"),
                        cursor=mouse, command=in_office1)
  button1_2 = tk.Button(frame, text="退社確認", font=(yu_font, 35, "bold"),
                        cursor=mouse, command=out_office1)
  button1_3 = tk.Button(frame, text="メンバー登録", font=(yu_font, 35, "bold"),
                        cursor=mouse, command=subscribe_member1)
  button1_4 = tk.Button(frame, text="管理ファイルを開く", font=(yu_font, 15),
                        fg="blue", cursor=mouse, command=folder_open)
  #
  # ボタンのカーソル時色変更
  button1_1.bind("<Enter>", enter_bg)
  button1_1.bind("<Leave>", leave_bg)
  button1_2.bind("<Enter>", enter_bg)
  button1_2.bind("<Leave>", leave_bg)
  button1_3.bind("<Enter>", enter_bg)
  button1_3.bind("<Leave>", leave_bg)
  button1_4.bind("<Enter>", enter_bg)
  button1_4.bind("<Leave>", leave_bg)
  #
  # ボタン配置
  button1_1.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  button1_2.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  button1_3.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  button1_4.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  #
  # frameを最上面へ
  frame.tkraise()


def folder_open():
  # 管理ファイルがあるフォルダを開く
  subprocess.Popen(["explorer", folder_path], shell=True)

#------------------------------------------------------------------------------

#-----------------------------------2_1.出社確認-----------------------------------

def in_office1():
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜出社確認")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label2_1 = tk.Label(frame, text="出社確認", font=(yu_font, 35))
  label2_2 = tk.Label(frame, text="ICカードを置いて\r\nOKボタンを押してください",
                      font=(yu_font, 35, "bold"))
  button2_1 = tk.Button(frame, text="OK", font=(yu_font, 25, "bold"),
                        cursor=mouse, command=ic_read2)
  button2_2 = tk.Button(frame, text="ホームへ", font=(yu_font, 15),
                        cursor=mouse, command=home_display)
  #
  # ボタンのカーソル時色変更
  button2_1.bind("<Enter>", enter_bg)
  button2_1.bind("<Leave>", leave_bg)
  button2_2.bind("<Enter>", enter_bg)
  button2_2.bind("<Leave>", leave_bg)
  #
  # ラベル・ボタン配置
  label2_1.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label2_2.pack(side=tk.TOP, pady=30, ipadx=20, ipady=10)
  button2_1.pack(pady=20, ipadx=20, ipady=10)
  button2_2.pack(side=tk.BOTTOM, pady=20)
  #
  # frameを最上面へ
  frame.tkraise()


def ic_read2():
  # 読み取り待機
  clf = nfc.ContactlessFrontend("usb")
  try:
    tag = clf.connect(rdwr={"targets": ["212F", "424F"],
                            "on-connect": lambda tag: False})
  finally:
    clf.close()
  #
  # タグ情報からIDmを抽出
  if tag.TYPE == "Type3Tag":
    idm = binascii.hexlify(tag.idm).decode()
  #
  # 次のフレームへ
  in_office2(idm)

#-------------------------------------------------------------------------------
#-----------------------------------2_2.出社確認-----------------------------------

def in_office2(id_info):
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜出社確認")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # 現時刻を取得
  date2 = dt.datetime.now().strftime(r"%Y/%m/%d")
  time2 = dt.datetime.now().strftime(r"%X")
  #
  # 読み取ったカードの持ち主の名前を取得
  df_read = pd.read_csv(id_path, header=0, index_col=None, encoding="shift jis")
  human_info = df_read[df_read["id"]==str(id_info)]
  last_name = human_info.iat[0, 1]
  full_name = human_info.iat[0, 3]
  #
  # 該当者のcsvファイルに記録
  df_rec2 = pd.read_csv(fr"{folder_path}\{full_name}.csv",
                        header=0, index_col=None, encoding="shift jis")
  df_app2 = pd.DataFrame([[date2, time2, "出"]], columns=df_rec2.columns.values)
  df_rec2 = pd.concat([df_rec2, df_app2])
  df_rec2.to_csv(fr"{folder_path}\{full_name}.csv", index=None, encoding="shift jis")
  #
  # ラベル・ボタン作成
  label2_3 = tk.Label(frame, text="読み取り完了！", font=(yu_font, 35, "bold"))
  label2_4 = tk.Label(frame, text=fr"{last_name}さん、おはようございます！",
                      font=(yu_font, 35, "bold"))
  label2_5 = tk.Label(frame, text=fr"タイムスタンプ｜{time2}", font=(yu_font, 35, "bold"))
  #
  # ラベル・ボタン配置
  label2_3.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label2_4.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label2_5.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  #
  # 3秒後、ホーム画面へ戻る
  label2_4.after(3000, home_display)
  #
  # frameを最上面へ
  frame.tkraise()

#-------------------------------------------------------------------------------

#-----------------------------------3_1.退社確認-----------------------------------

def out_office1():
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜退社確認")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label3_1 = tk.Label(frame, text="退社確認", font=(yu_font, 35))
  label3_2 = tk.Label(frame, text="ICカードを置いて\r\nOKボタンを押してください",
                      font=(yu_font, 35, "bold"))
  button3_1 = tk.Button(frame, text="OK", font=(yu_font, 25, "bold"),
                        cursor=mouse, command=ic_read3)
  button3_2 = tk.Button(frame, text="ホームへ", font=(yu_font, 15),
                        cursor=mouse, command=home_display)
  #
  # ボタンのカーソル時色変更
  button3_1.bind("<Enter>", enter_bg)
  button3_1.bind("<Leave>", leave_bg)
  button3_2.bind("<Enter>", enter_bg)
  button3_2.bind("<Leave>", leave_bg)
  #
  # ラベル・ボタン配置
  label3_1.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label3_2.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  button3_1.pack(pady=20, ipadx=20, ipady=10)
  button3_2.pack(side=tk.BOTTOM, pady=20)
  #
  # frameを最上面へ
  frame.tkraise()


def ic_read3():
  # 読み取り待機
  clf = nfc.ContactlessFrontend("usb")
  try:
    tag = clf.connect(rdwr={"targets": ["212F", "424F"],
                            "on-connect": lambda tag: False})
  finally:
    clf.close()
  #
  # タグ情報からIDmを抽出
  if tag.TYPE == "Type3Tag":
    idm = binascii.hexlify(tag.idm).decode()
  #
  # 次のフレームへ
  out_office2(idm)

#-------------------------------------------------------------------------------
#-----------------------------------3_2.退社確認-----------------------------------

def out_office2(id_info):
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜出社確認")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # 現時刻を取得
  date3 = dt.datetime.now().strftime(r"%Y/%m/%d")
  time3 = dt.datetime.now().strftime(r"%X")
  #
  # 読み取ったカードの持ち主の名前を取得
  df_read = pd.read_csv(id_path, header=0, index_col=None, encoding="shift jis")
  human_info = df_read[df_read["id"]==str(id_info)]
  last_name = human_info.iat[0, 1]
  full_name = human_info.iat[0, 3]
  #
  # 該当者のcsvファイルに記録
  df_rec3 = pd.read_csv(fr"{folder_path}\{full_name}.csv",
                        header=0, index_col=None, encoding="shift jis")
  df_app3 = pd.DataFrame([[date3, time3, "退"]], columns=df_rec3.columns.values)
  df_rec3 = pd.concat([df_rec3, df_app3])
  df_rec3.to_csv(fr"{folder_path}\{full_name}.csv", index=None, encoding="shift jis")
  #
  # ラベル・ボタン作成
  label3_3 = tk.Label(frame, text="読み取り完了！", font=(yu_font, 35, "bold"))
  label3_4 = tk.Label(frame, text=fr"{last_name}さん、お疲れ様でした！",
                      font=(yu_font, 35, "bold"))
  label3_5 = tk.Label(frame, text=fr"タイムスタンプ｜{time3}", font=(yu_font, 35, "bold"))
  #
  # ラベル・ボタン配置
  label3_3.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label3_4.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label3_5.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  #
  # 3秒後、ホーム画面へ戻る
  label3_4.after(3000, home_display)
  #
  # frameを最上面へ
  frame.tkraise()

#-------------------------------------------------------------------------------

#-----------------------------------4_1.メンバー登録-----------------------------------

def subscribe_member1():
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜メンバー登録")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label4_1 = tk.Label(frame, text="氏名を入力してください", font=(yu_font, 35, "bold"))
  label4_2 = tk.Label(frame, text="姓：", font=(yu_font, 25))
  label4_3 = tk.Label(frame, text="名：", font=(yu_font, 25))
  text4_1 = tk.Entry(frame, font=(yu_font, 20))
  text4_2 = tk.Entry(frame, font=(yu_font, 20))
  button4_1 = tk.Button(frame, text="OK", font=(yu_font, 20), cursor=mouse,
                        command=lambda: subscribe_member2(text4_1.get(),text4_2.get()))
  button4_2 = tk.Button(frame, text="ホームへ", font=(yu_font, 15), cursor=mouse,
                        command=home_display)
  #
  # ボタンのカーソル時色変更
  button4_1.bind("<Enter>", enter_bg)
  button4_1.bind("<Leave>", leave_bg)
  button4_2.bind("<Enter>", enter_bg)
  button4_2.bind("<Leave>", leave_bg)
  #
  # ラベル・ボタン配置
  label4_1.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label4_2.place(x=200, y=200)
  text4_1.place(x=300, y=200, width=300, height=35)
  label4_3.place(x=200, y=300)
  text4_2.place(x=300, y=300, width=300, height=35)
  button4_1.place(x=350, y=400, width=100, height=50)
  button4_2.pack(side=tk.BOTTOM, pady=20)
  #
  # frameを最上面へ
  frame.tkraise()

#-------------------------------------------------------------------------------------
#-----------------------------------4_2.メンバー登録-----------------------------------

def subscribe_member2(last_name2, first_name2):
  # 名前の情報は上の関数から変数として渡す
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜メンバー登録")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label4_4 = tk.Label(frame, text=f"{last_name2} {first_name2}さん\r\nでよろしいでしょうか？",
                      font=(yu_font, 35, "bold"))
  button4_3 = tk.Button(frame, text="OK", font=(yu_font, 20), cursor=mouse,
                        command=lambda: subscribe_member3(last_name2, first_name2))
  button4_4 = tk.Button(frame, text="戻る", font=(yu_font, 20), cursor=mouse,
                        command=subscribe_member1)
  button4_5 = tk.Button(frame, text="ホームへ", font=(yu_font, 15), cursor=mouse,
                        command=home_display)
  #
  # ボタンのカーソル時色変更
  button4_3.bind("<Enter>", enter_bg)
  button4_3.bind("<Leave>", leave_bg)
  button4_4.bind("<Enter>", enter_bg)
  button4_4.bind("<Leave>", leave_bg)
  button4_5.bind("<Enter>", enter_bg)
  button4_5.bind("<Leave>", leave_bg)
  #
  # ラベル・ボタン配置
  label4_4.pack(side=tk.TOP, pady=60, ipadx=20, ipady=20)
  button4_3.place(x=250, y=400, width=100, height=50)
  button4_4.place(x=450, y=400, width=100, height=50)
  button4_5.pack(side=tk.BOTTOM, pady=20)
  #
  # frameを最上面へ
  frame.tkraise()

#-------------------------------------------------------------------------------------
#-----------------------------------4_3.メンバー登録-----------------------------------

def subscribe_member3(last_name3, first_name3):
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜メンバー登録")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label4_5 = tk.Label(frame, text="氏名を登録しました！", font=(yu_font, 35, "bold"))
  label4_6 = tk.Label(frame, text="ICカードを置いて\r\nOKボタンを押してください",
                      font=(yu_font, 35, "bold"))
  button4_6 = tk.Button(frame, text="OK", font=(yu_font, 25, "bold"), cursor=mouse,
                        command=lambda: ic_read4(last_name3, first_name3))
  button4_7 = tk.Button(frame, text="ホームへ", font=(yu_font, 15), cursor=mouse,
                        command=home_display)
  #
  # ボタンのカーソル時色変更
  button4_6.bind("<Enter>", enter_bg)
  button4_6.bind("<Leave>", leave_bg)
  button4_7.bind("<Enter>", enter_bg)
  button4_7.bind("<Leave>", leave_bg)
  #
  # ラベル・ボタン配置
  label4_5.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label4_6.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  button4_6.pack(pady=20, ipadx=20, ipady=10)
  button4_7.pack(side=tk.BOTTOM, pady=20)
  #
  # frameを最上面へ
  frame.tkraise()


def ic_read4(last, first):
  # 読み取り待機
  clf = nfc.ContactlessFrontend("usb")
  try:
    tag = clf.connect(rdwr={"targets": ["212F", "424F"],
                            "on-connect": lambda tag: False})
  finally:
    clf.close()
  #
  # タグ情報からIDmを抽出
  if tag.TYPE == "Type3Tag":
    idm = binascii.hexlify(tag.idm).decode()
  #
  # idmの重複確認 ＞ 重複していたらエラー画面｜重複していなければ記録
  df_rec4 = pd.read_csv(id_path, header=0, index_col=None, encoding="shift jis")
  id_conf = df_rec4[df_rec4["id"]==idm]
  if id_conf.size > 0:
    # 重複している > エラー画面
    subscribe_error(last, first)
  else:
    # 重複していない > id_name.csvに登録者の情報を記録
    date4 = dt.datetime.now().strftime(r"%Y/%m/%d")
    time4 = dt.datetime.now().strftime(r"%X")
    df_app4 = pd.DataFrame([[f"{date4} {time4}", last, first, last + first, idm]],
                           columns=df_rec4.columns.values)
    df_rec4 = pd.concat([df_rec4, df_app4])
    df_rec4.to_csv(id_path, index=None, encoding="shift jis")
    #
    # 登録者のcsvファイルを作成
    df_make = pd.DataFrame([[None]*3], columns=["日付", "時間", "出/退"])
    df_make = df_make.drop([0])
    df_make.to_csv(fr"{folder_path}\{last}{first}.csv",
                   index=None, encoding="shift jis")
    #
    # 次のフレームへ
    subscribe_member4(last)

#-------------------------------------------------------------------------------------
#-----------------------------------4_4.メンバー登録-----------------------------------

def subscribe_member4(name):
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜メンバー登録")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label4_7 = tk.Label(frame, text="ICカードを登録しました！", font=(yu_font, 35, "bold"))
  label4_8 = tk.Label(frame, text=f"{name}さんよろしくお願いします！",
                      font=(yu_font, 35, "bold"))
  #
  # ラベル・ボタン配置
  label4_7.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label4_8.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  #
  # 3秒後、ホーム画面へ戻る
  label4_8.after(3000, home_display)
  #
  # frameを最上面へ
  frame.tkraise()


# id情報重複エラー画面
def subscribe_error(last_name4, first_name4):
  # ウィンドウのタイトル
  root.title(r"勤怠管理ツール｜メンバー登録")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ラベル・ボタン作成
  label4_9 = tk.Label(frame, text="ID情報が重複しています", font=(yu_font, 35, "bold"))
  label4_10 = tk.Label(frame, text="もう一度やり直してください",
                       font=(yu_font, 35, "bold"))
  #
  # ラベル・ボタン配置
  label4_9.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  label4_10.pack(side=tk.TOP, pady=20, ipadx=20, ipady=20)
  #
  # 2秒後、前の画面へ戻る
  label4_10.after(2000, lambda: subscribe_member3(last_name4, first_name4))
  #
  # frameを最上面へ
  frame.tkraise()

#-------------------------------------------------------------------------------------

#-----------------------------------基本設定-----------------------------------

# メインウィンドウ作成
root = tk.Tk()

# ウィンドウ内のエリア変化率を等倍に指定
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ウィンドウの大きさを決定
root.minsize(width=800, height=700)
root.maxsize(width=800, height=700)

# 使用したいフォント
yu_font = "游ゴシック"

# ボタンにカーソルが乗ったときの色
def enter_bg(event):
  event.widget["bg"] = "#D3D3D3"

# ボタンからカーソルが離れたときの色
def leave_bg(event):
  event.widget["bg"] = "SystemButtonFace"

# マウスカーソル時のポイント変更
mouse = "hand2"


# フォルダ・ファイルのパス
folder_path = r"C:\User\Owner\Documents\kintai"
id_path = fr"{folder_path}\id_name.csv"

# id_name.csvが無ければ作成
if os.path.exists(id_path) == False:
  # id_name.csvファイルのテンプレート作成
  df_temp = pd.DataFrame([[None]*5],
                         columns=["time", "last_name", "first_name", "full_name", "id"])
  df_temp = df_temp.drop([0])
  #
  # id_name.csvファイルを作成
  df_temp.to_csv(id_path, index=None, encoding="shift jis")

#-----------------------------------------------------------------------------

home_display()

root.mainloop()
