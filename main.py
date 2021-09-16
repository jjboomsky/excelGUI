import random
import tkinter as tk
import tkinter.font as tkFont
import numpy as np

import xlwt


def print_hello():
    for index in range(0, 5):
        x = random.uniform(-0.2, 0.2)
        print(x)


class App:
    hang = None
    lei = None
    pian_cah = None
    junzhi = None

    def __init__(self, root):
        root.title("关闭表格,生成数据")
        # setting window size
        width = 400
        height = 300
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_968 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_968["font"] = ft
        GLabel_968["fg"] = "#333333"
        GLabel_968["justify"] = "center"
        GLabel_968["text"] = "行"
        GLabel_968.place(x=0, y=20, width=61, height=36)

        self.hang = tk.Entry(root)
        self.hang["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.hang["font"] = ft
        self.hang["fg"] = "#333333"
        self.hang["justify"] = "center"
        self.hang["text"] = "hang"
        self.hang.place(x=70, y=20, width=109, height=36)

        GLabel_672 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_672["font"] = ft
        GLabel_672["fg"] = "#333333"
        GLabel_672["justify"] = "center"
        GLabel_672["text"] = "列"
        GLabel_672.place(x=180, y=20, width=61, height=36)

        self.lie = tk.Entry(root)
        self.lie["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.lie["font"] = ft
        self.lie["fg"] = "#333333"
        self.lie["justify"] = "center"
        self.lie["text"] = "lie"
        self.lie.place(x=230, y=20, width=109, height=36)

        GLabel_903 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        GLabel_903["font"] = ft
        GLabel_903["fg"] = "#333333"
        GLabel_903["justify"] = "center"
        GLabel_903["text"] = "均值"
        GLabel_903.place(x=0, y=100, width=70, height=36)

        self.junzhi = tk.Entry(root)
        self.junzhi["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.junzhi["font"] = ft
        self.junzhi["fg"] = "#333333"
        self.junzhi["justify"] = "center"
        self.junzhi["text"] = "junzhi"
        self.junzhi.place(x=70, y=100, width=109, height=36)

        pian_cha_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=14)
        pian_cha_label["font"] = ft
        pian_cha_label["fg"] = "#333333"
        pian_cha_label["justify"] = "center"
        pian_cha_label["text"] = "偏差"
        pian_cha_label.place(x=170, y=100, width=70, height=36)

        self.pian_cha = tk.Entry(root)
        self.pian_cha["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.pian_cha["font"] = ft
        self.pian_cha["fg"] = "#333333"
        self.pian_cha["justify"] = "center"
        self.pian_cha["text"] = "pian_cha"
        self.pian_cha.place(x=230, y=100, width=109, height=36)

        GButton_79 = tk.Button(root)
        GButton_79["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=14)
        GButton_79["font"] = ft
        GButton_79["fg"] = "#000000"
        GButton_79["justify"] = "center"
        GButton_79["text"] = "生成"
        GButton_79.place(x=130, y=200, width=111, height=46)

        GButton_79["command"] = self.GButton_79_command

    def GButton_79_command(self):
        hang = int(self.hang.get())
        lie = int(self.lie.get())
        junzhi = float(self.junzhi.get())
        pian_cha = float(self.pian_cha.get())

        if hang is not None and lie is not None and junzhi is not None and pian_cha is not None:
            np.random.seed(0)
            s = np.random.normal(junzhi, pian_cha, size=(hang, lie))
            workbook = xlwt.Workbook(encoding='ascii')
            worksheet = workbook.add_sheet("Sheet1")
            for x in range(0, hang):
                for y in range(0, lie):
                    worksheet.write(x, y, s[x][y])

            workbook.save("数据.xls")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
