import tkinter as tk
import pygame




# 初期化
pygame.mixer.init()




# 数字ボタンが押されたときの処理
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)
    play_sound(value)




# "="ボタンが押されたときの処理
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        print("エラー:", e)
        entry.delete(0, tk.END)
        entry.insert(tk.END, "エラー")




# クリアボタンが押されたときの処理
def clear():
    entry.delete(0, tk.END)




# キーボードからの入力を処理する関数
def key_pressed(event):
    key = event.char
    if key.isdigit() or key == "+" or key == "-" or key == "*" or key == "/" or key == ".":
        button_click(key)
    elif key == "\r":
        calculate()
    elif key == "\x08":
        clear()




# 音を再生する関数
def play_sound(value):
    try:
        sound = pygame.mixer.Sound(f"{value}.wav")
        sound.play()
    except Exception as e:
        print("音声ファイルが見つかりませんでした:", e)




# ウィンドウの作成
window = tk.Tk()
window.title("電卓")




# テキストエントリ
entry = tk.Entry(window, width=16, borderwidth=20, font=('ＭＳ ゴシック', 40))
entry.grid(row=0, column=0, columnspan=10)




# 数字ボタン
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), # "=" ボタンの列を調整しました
]




for (text, row, column) in buttons:
    ###################################
    # ボタンの高さ、幅を揃えるところから #
    ###################################
    button = tk.Button(window, text=text, padx=46, pady=32, command=lambda text=text: button_click(text), font=('ＭＳ ゴシック', 30), width=1, height=1)
    # button = tk.Button(window, text=text, command=lambda text=text: button_click(text), font=('ＭＳ ゴシック', 30), width=10, height=10)
    button.grid(row=row, column=column, columnspan=1)  # 各ボタンの列幅を1に変更しました




# クリアボタン
clear_button = tk.Button(window, text="C", padx=46, pady=32, command=clear, font=('ＭＳ ゴシック', 30), width=1, height=1)
clear_button.grid(row=5, column=3)




# "=" ボタン
equal_button = tk.Button(window, text="=", padx=46, pady=32, command=calculate, font=('ＭＳ ゴシック', 30), width=1, height=1)
equal_button.grid(row=4, column=3)




# キーボードからの入力をウィンドウにバインドする
window.bind('<Key>', key_pressed)




# ウィンドウの表示
window.mainloop()
