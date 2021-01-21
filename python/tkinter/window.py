from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *


def menuSearch():
    messagebox.showinfo("notice", "이것이 버튼이다")
    

def chkBtn():
    if chk.get():
        messagebox.showinfo("notice", "이것이 체크다")
    else:
        messagebox.showinfo("notice", "이것이 체크다")
        

def rBtn():
    if rbvar.get() == 1:
        label2.configure(text="버튼1")
    elif rbvar.get() == 2:
        label2.configure(text="버튼2")
    else:
        label2.configure(text="버튼3")
        

def d_input(event):
    date = entry.get()
    label3.config(text=date)

window = Tk()

#윈도우 기본 창 생성
window.title("타이틀이다")
window.geometry("400x800")
window.resizable(width=False, height=True)


#레이블: 문자를 표현할 수 있는 도구
label1 = Label(window, text="이것은 레이블", font=("맑은고딕",12, "bold","underline"),fg="red", bg="blue",width=50, height=2, anchor=CENTER)  #anchokr=N, NE, E, SE, S, SW, W, NW, CENTER(default)
label1.pack()

label2 = Label(window, text="이것도 레이블", font=("맑은고딕",12, "bold","underline"))  #anchokr=N, NE, E, SE, S, SW, W, NW, CENTER(default)
label2.pack()

label3 = Label(window, text="요것도 레이블", font=("맑은고딕",12, "bold"))  #anchokr=N, NE, E, SE, S, SW, W, NW, CENTER(default)
label3.place(x=150, y=300)

'''
family : 텍스트의 글꼴
size : 텍스트의 글꼴 크기
weight : 텍스트를 진하게 (normal, bold)
slant : 텍스트의 기울임 (roamn, italic)
underline : 텍스트의 밑줄 (False)
overstrike: 텍스트의 취소선 (False)
'''

#버튼
button = Button(window, text="버튼", font=("맑은고딕",12, "bold"), fg="green", command=menuSearch)
button.pack()

#체크버튼
chk=IntVar()
cbtn1 = Checkbutton(window, text="체크버튼", font=("맑은고딕",12, "bold"), variable=chk, command=chkBtn)
cbtn1.pack()

#라디오버튼
rbvar = IntVar()
rb1 = Radiobutton(window, text="라디오버튼", font=("맑은고딕",12, "bold"), variable=rbvar, value=1, command=rBtn)
rb2 = Radiobutton(window, text="라디오버튼", font=("맑은고딕",12, "bold"), variable=rbvar, value=2, command=rBtn)
rb3 = Radiobutton(window, text="라디오버튼", font=("맑은고딕",12, "bold"), variable=rbvar, value=3, command=rBtn)

rb1.place(x=70, y=250)
rb2.place(x=170, y=250)
rb3.place(x=270, y=250)

#기입창
entry = Entry(window)
entry.bind("<Return>", d_input)
entry.pack()

window.mainloop()