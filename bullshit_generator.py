import tkinter
import jieba.posseg as pseg


class FindLocation(object):
    def __init__(self):
        self.root = tkinter.Tk()
        # 给主窗口设置标题内容
        self.root.title("营销号生成器")
        # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root, width=30)

        # 创建一个文本框
        self.display_info = tkinter.Text(self.root, width=100,height = 10,bd=5,relief='groove')

        # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command=self.shit_article, text="生成")


    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    def shit_article(self):
        question = self.ip_input.get()
        words = pseg.cut(question)
        key_word = ''
        for w in words:
            if w.flag == 'ns':
                key_word = w.word
            else:
                key_word = question
        shit = '''
        {0}是怎么回事呢？{1}相信大家都很熟悉，但是{0}是怎么回事呢，下面就让小编带大家一起了解吧。

        {0}，其实就是{0}，大家可能会很惊讶呢,但事实就是这样，小编也感到非常惊讶。

        这就是关于{0}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！
        '''.format(question, key_word)
        self.display_info.delete('1.0','end')
        self.display_info.insert(tkinter.END,shit)

def main():
    FL = FindLocation()
    FL.gui_arrang()
    tkinter.mainloop()


if __name__ == "__main__":
    main()