import tkinter as tk
from decimal import Decimal


#----------------------------------最初のフレーム----------------------------------

# フレーム作成
def home_frame():
  # ウィンドウのタイトル指定
  root.title("四則演算ツール")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl = tk.Label(frame, text="四則演算ツール", font=(yu_font, 30))
  btn1_1 = tk.Button(frame, text="足し算", font=(yu_font, 20),
                     command=addition)
  btn1_2 = tk.Button(frame, text="引き算", font=(yu_font, 20),
                     command=subtraction)
  btn1_3 = tk.Button(frame, text="掛け算", font=(yu_font, 20),
                     command=multiplication)
  btn1_4 = tk.Button(frame, text="割り算", font=(yu_font, 20),
                     command=division)
  #
  # ウィジェット配置
  lbl.place(x=270, y=50)
  btn1_1.place(x=150, y=180, width=200, height=100)
  btn1_2.place(x=450, y=180, width=200, height=100)
  btn1_3.place(x=150, y=350, width=200, height=100)
  btn1_4.place(x=450, y=350, width=200, height=100)
  #
  # フレームを最上面へ
  frame.tkraise()
  #

#-----------------------------------------------------------------------------------

#----------------------------------足し算のフレーム----------------------------------

# フレーム作成
def addition():
  # ウィンドウのタイトル指定
  root.title("四則演算ツール｜足し算")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl_1 = tk.Label(frame, text="足し算", font=(yu_font, 30))
  box_1 = tk.Entry(frame, font=(yu_font, 15))
  lbl_2 = tk.Label(frame, text="＋", font=(yu_font, 30))
  lbl_3 = tk.Label(frame, text="⇓", font=(yu_font, 30))
  box_2 = tk.Entry(frame, font=(yu_font, 15))
  box_3 = tk.Entry(frame, font=(yu_font, 15))
  btn = tk.Button(frame, text="計算", font=(yu_font, 20),
                  command=lambda: box_3.insert(tk.END,str(func_1(box_3,box_1.get(),box_2.get()))))
  back = tk.Button(frame, text="ホームへ", command=home_frame)
  #
  # ウィジェット配置
  lbl_1.place(x=300, y=50, width=200, height=40)
  box_1.place(x=100, y=150, width=200, height=40)
  lbl_2.place(x=375, y=150, width=50, height=40)
  lbl_3.place(x=375, y=230, width=50, height=40)
  box_2.place(x=500, y=150, width=200, height=40)
  box_3.place(x=300, y=300, width=200, height=40)
  btn.place(x=350, y=400, width=100, height=50)
  back.place(x=370, y=460, width=60, height=30)
  #
  # フレームを最上面へ
  frame.tkraise()
  #


# 足し算
def func_1(arg1, arg2, arg3):
  dele = arg1.delete(0, tk.END)
  calc = Decimal(arg2) + Decimal(arg3)
  return calc


#-----------------------------------------------------------------------------------

#----------------------------------引き算のフレーム----------------------------------

# フレーム作成
def subtraction():
  # ウィンドウのタイトル指定
  root.title("四則演算ツール｜引き算")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl_1 = tk.Label(frame, text="引き算", font=(yu_font, 30))
  box_1 = tk.Entry(frame, font=(yu_font, 15))
  lbl_2 = tk.Label(frame, text="－", font=(yu_font, 30))
  lbl_3 = tk.Label(frame, text="⇓", font=(yu_font, 30))
  box_2 = tk.Entry(frame, font=(yu_font, 15))
  box_3 = tk.Entry(frame, font=(yu_font, 15))
  btn = tk.Button(frame, text="計算", font=(yu_font, 20),
                  command=lambda: box_3.insert(tk.END,str(func_2(box_3,box_1.get(),box_2.get()))))
  back = tk.Button(frame, text="ホームへ", command=home_frame)
  #
  # ウィジェット配置
  lbl_1.place(x=300, y=50, width=200, height=40)
  box_1.place(x=100, y=150, width=200, height=40)
  lbl_2.place(x=375, y=150, width=50, height=40)
  lbl_3.place(x=375, y=230, width=50, height=40)
  box_2.place(x=500, y=150, width=200, height=40)
  box_3.place(x=300, y=300, width=200, height=40)
  btn.place(x=350, y=400, width=100, height=50)
  back.place(x=370, y=460, width=60, height=30)
  #
  # フレームを最上面へ
  frame.tkraise()
  #


# 引き算
def func_2(arg1, arg2, arg3):
  dele = arg1.delete(0, tk.END)
  calc = Decimal(arg2) - Decimal(arg3)
  return calc


#-----------------------------------------------------------------------------------

#----------------------------------掛け算のフレーム----------------------------------

# フレーム作成
def multiplication():
  # ウィンドウのタイトル指定
  root.title("四則演算ツール｜掛け算")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl_1 = tk.Label(frame, text="掛け算", font=(yu_font, 30))
  box_1 = tk.Entry(frame, font=(yu_font, 15))
  lbl_2 = tk.Label(frame, text="×", font=(yu_font, 30))
  lbl_3 = tk.Label(frame, text="⇓", font=(yu_font, 30))
  box_2 = tk.Entry(frame, font=(yu_font, 15))
  box_3 = tk.Entry(frame, font=(yu_font, 15))
  btn = tk.Button(frame, text="計算", font=(yu_font, 20),
                  command=lambda: box_3.insert(tk.END,str(func_3(box_3,box_1.get(),box_2.get()))))
  back = tk.Button(frame, text="ホームへ", command=home_frame)
  #
  # ウィジェット配置
  lbl_1.place(x=300, y=50, width=200, height=40)
  box_1.place(x=100, y=150, width=200, height=40)
  lbl_2.place(x=375, y=150, width=50, height=40)
  lbl_3.place(x=375, y=230, width=50, height=40)
  box_2.place(x=500, y=150, width=200, height=40)
  box_3.place(x=300, y=300, width=200, height=40)
  btn.place(x=350, y=400, width=100, height=50)
  back.place(x=370, y=460, width=60, height=30)
  #
  # フレームを最上面へ
  frame.tkraise()
  #


# 掛け算
def func_3(arg1, arg2, arg3):
  dele = arg1.delete(0, tk.END)
  calc = Decimal(arg2) * Decimal(arg3)
  return calc


#-----------------------------------------------------------------------------------

#----------------------------------割り算のフレーム----------------------------------

# フレーム作成
def division():
  # ウィンドウのタイトル指定
  root.title("四則演算ツール｜割り算")
  #
  # フレーム作成
  frame = tk.Frame(root)
  frame.grid(row=0, column=0, sticky=tk.NSEW)
  #
  # ウィジェット作成
  lbl_1 = tk.Label(frame, text="割り算", font=(yu_font, 30))
  box_1 = tk.Entry(frame, font=(yu_font, 15))
  lbl_2 = tk.Label(frame, text="÷", font=(yu_font, 30))
  lbl_3 = tk.Label(frame, text="⇓", font=(yu_font, 30))
  box_2 = tk.Entry(frame, font=(yu_font, 15))
  box_3 = tk.Entry(frame, font=(yu_font, 15))
  btn = tk.Button(frame, text="計算", font=(yu_font, 20),
                  command=lambda: box_3.insert(tk.END,str(func_4(box_3,box_1.get(),box_2.get()))))
  back = tk.Button(frame, text="ホームへ", command=home_frame)
  #
  # ウィジェット配置
  lbl_1.place(x=300, y=50, width=200, height=40)
  box_1.place(x=100, y=150, width=200, height=40)
  lbl_2.place(x=375, y=150, width=50, height=40)
  lbl_3.place(x=375, y=230, width=50, height=40)
  box_2.place(x=500, y=150, width=200, height=40)
  box_3.place(x=300, y=300, width=200, height=40)
  btn.place(x=350, y=400, width=100, height=50)
  back.place(x=370, y=460, width=60, height=30)
  #
  # フレームを最上面へ
  frame.tkraise()
  #


# 割り算
def func_4(arg1, arg2, arg3):
  dele = arg1.delete(0, tk.END)
  calc = Decimal(arg2) / Decimal(arg3)
  return calc


#-----------------------------------------------------------------------------------

#---------------------------------------設定---------------------------------------

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

#-----------------------------------------------------------------------------------

home_frame()

root.mainloop()
