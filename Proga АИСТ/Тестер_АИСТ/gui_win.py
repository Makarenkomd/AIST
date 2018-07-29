from tkinter import *
import QuestionGenerator_win
import random
from tkinter import messagebox

#
class AnsItem:
    global test_info
    def __init__(self, parent, ans_text, rw):
        self.RW = rw
        self.value = IntVar()
        self.back = Frame(parent, bg='aliceblue', height=3)
        self.check = Checkbutton(self.back,bg='aliceblue', text = ans_text, variable = self.value, onvalue = 1, offvalue = 0, font = 'a 15',wraplength=600, justify=LEFT, activebackground='lightgrey')
        self.sep = Frame(parent, bg = 'lightgrey', height = 3)

        self.back.pack(side='top', fill='x', expand=False, padx=55, pady=3)
        self.check.pack(side='left', fill = BOTH, expand = False)
        self.sep.pack(side = 'top', fill = 'x', expand = False)
        
            
    def GetValue(self):
        return self.vlaue
    
    def GetRW(self):
        return self.RW
    
    def Destroy(self):
        self.back.destroy()
        self.check.destroy() 
        self.sep.destroy()
        
    def Get(self):
        return self.value.get()
    
    def Select(self):
        self.check.select()

# окно тестирования
def GuiTesting(file, qnum):
    
    def Finish(event):
        global test_info, right_results, main, last_used
        if not last_used:
            return
        l = len(test_info)
        cnt = 0
        for i in range(l):
            if test_info[i] == right_results[i]:
                cnt += 1
        per = int((cnt / l) * 100 * 100) / 100
        mark = per // 20
        message = Toplevel(main, bg = 'lightgrey')
        message.geometry('300x300+250+100')
        box = Frame(message, bg = 'lightgrey')
        label_fin1 = Label(box, text = 'percents: ' + str(per) + '%', font = 'a 20', bg = 'lightgrey')
        label_fin2 = Label(box, text = 'mark: ' + str(mark), font = 'a 20', bg = 'lightgrey')
        label_fin1.pack(side = 'top', fil = None, expand = False)
        label_fin2.pack(side = 'top', fil = None, expand = False)
        box.pack(side = 'top', fil = 'x', expand = True)
        for i in main.winfo_children():
            if str(type(i)) != '<class \'tkinter.Toplevel\'>':
                i.destroy()
        print(str(right_results) + '\n' + str(test_info) + '\n-->\n')
        GuiStart()
            
    def MakeQuestion(q, qtype):
        if qtype == 1:
            return q + ' это?'
        elif qtype == 2:
            return q + ' называется?'
        elif qtype == 3:
            return q + ' состоит из?'
        elif qtype == 4:
            return 'Выберете свойства, которыми обладает ' + q
        elif qtype == 5:
            return 'Выберете примеры ' + q
        elif qtype == 6:
            return q + ' это?' 

    # создание визуального списка вопросов
    def CreateTestItem():
        global questions_frame, question_label, data, current_question_ind, qnum_label, test_info, right_results, shuffled, all_test
        q = data[current_question_ind][1]
        q_type = data[current_question_ind][0]
        ms = []
        if q_type == 1 or q_type == 2:
            ans_ms = []
            if not shuffled[current_question_ind]:
                shuffled[current_question_ind] = 1
                ans_ms = [[q[1][0], 1]]
                for i in range(1, len(q[1])):
                    ans_ms.append([q[1][i], 0])                
                random.shuffle(ans_ms)
                all_test[current_question_ind] = ans_ms
            else:
                ans_ms = all_test[current_question_ind]
            l = len(ans_ms)
            for i in range(l):
                right_results[current_question_ind][i] = ans_ms[i][1]
                ms.append(AnsItem(parent = questions_frame, ans_text = ans_ms[i][0], rw = ans_ms[i][1]))
                if test_info[current_question_ind][i]:
                    ms[-1].Select()            
        elif q_type == 3 or q_type == 4 or q_type == 5 or q_type == 6:
            ans_ms = []
            if not shuffled[current_question_ind]:
                shuffled[current_question_ind] = 1
                for i in q[1]:
                    ans_ms.append([i, 1])
                for i in q[2]:
                    ans_ms.append([i, 0])  
                random.shuffle(ans_ms)
                all_test[current_question_ind] = ans_ms
            else:
                ans_ms = all_test[current_question_ind]
            l = len(ans_ms)
            for i in range(l):
                right_results[current_question_ind][i] = ans_ms[i][1]
                ms.append(AnsItem(parent = questions_frame, ans_text = ans_ms[i][0], rw = ans_ms[i][1]))
                if test_info[current_question_ind][i]:
                    ms[-1].Select()             
        return ms
                
    def PrevQuestion(event):  
        global questions_frame, question_label, data, current_question_ind, qnum_label, current_answers, test_info
        for i in range(len(current_answers)):
            test_info[current_question_ind][i] = current_answers[i].Get()
            current_answers[i].Destroy()        
        if current_question_ind == len(data) - 1:
            last_used = 1        
        if current_question_ind != 0:
            current_question_ind -= 1
        box = ' ' + str(current_question_ind + 1) + '/' + str(len(data)) + ' '
        qnum_label['text'] = box    
        question_type = data[current_question_ind][0]
        question = data[current_question_ind][1][0]
        question_label['text'] = MakeQuestion(question, question_type)    
        current_answers = CreateTestItem()

    def NextQuestion(event):
        global questions_frame, question_label, data, current_question_ind, qnum_label, current_answers, last_used
        for i in range(len(current_answers)):
            test_info[current_question_ind][i] = current_answers[i].Get()
            current_answers[i].Destroy()
        if current_question_ind != len(data) - 1:
            current_question_ind += 1
        else:
            last_used = 1
        box = ' ' + str(current_question_ind + 1) + '/' + str(len(data)) + ' '
        qnum_label['text'] = box     
        question_type = data[current_question_ind][0]
        question = data[current_question_ind][1][0]
        question_label['text'] = MakeQuestion(question, question_type)  
        current_answers = CreateTestItem()

    def RestartTesting(event):
        global last_used
        top_frame.destroy()
        sep1_frame.destroy()
        question_label.destroy()
        sep2_frame.destroy()
        questions_frame.destroy()
        GuiTesting(file, qnum)
        
    global main, questions_frame, question_label, qnum_label, data, current_question_ind, current_answers, test_info, right_results, shuffled, last_used, all_test

# отобразить элементы окна тестирования
    top_frame = Frame(main, bg = 'lightgrey')
    tool_frame = Frame(main, bg='red', height=2)
    fin_button = Button(top_frame, text = 'Завершить', font = 'Arial 15')
    restart_button = Button(top_frame, text = 'Заново', font = 'Arial 15')
    restart_button.bind('<Button-1>', RestartTesting)
    qnum_label = Label(top_frame, text = ' 0/0 ', font = 'Arial 17', bg = 'lightgrey')
    prev_button = Button(top_frame, text = '<-')
    prev_button.bind('<Button-1>', PrevQuestion)
    next_button = Button(top_frame, text = '->')
    next_button.bind('<Button-1>', NextQuestion)

    sep1_frame = Frame(main, bg = 'grey', height = 2)
    question_label = Label(main, text = 'Вопросительный элемент', font = 'Arial 16', bg = 'lightgrey', height = 5, justify=LEFT, wraplength=800)
    sep2_frame = Frame(main, bg = 'grey', height = 2)
    questions_frame = Frame(main, bg = 'lightgrey')    

    fin_button.pack(side = 'right')
    fin_button.bind('<Button-1>', Finish)

    restart_button.pack(side = 'right')
    qnum_label.pack(side = 'left')
    prev_button.pack(side = 'left')
    next_button.pack(side = 'left')
    top_frame.pack(side = 'top', fil = 'x', expand = False)
    sep1_frame.pack(side = 'top', fil = 'x', expand = False)
    question_label.pack(side = 'top', fil = 'x', expand = False)

    sep2_frame.pack(side = 'top', fil = 'x', expand = False)
    questions_frame.pack(side = 'top', fil = 'both', expand = True)    
    
    data = QuestionGenerator_win.main(file, qnum) 
    random.shuffle(data)
    shuffled = []
    all_test = []
    test_info = []
    right_results = []
    for i in data:
        shuffled.append(0)
        all_test.append([])
        q_type = i[0]
        q = i[1]
        if q_type == 1:
            test_info.append([0 for i in range(len(q[1]))])
            right_results.append([0 for i in range(len(q[1]))])
        elif q_type == 2:
            test_info.append([0 for i in range(len(q[1]))])
            right_results.append([0 for i in range(len(q[1]))])
        elif q_type == 3:
            test_info.append([0 for i in range(len(q[1]) + len(q[2]))])
            right_results.append([0 for i in range(len(q[1]) + len(q[2]))])
        elif q_type == 4:
            test_info.append([0 for i in range(len(q[1]) + len(q[2]))])
            right_results.append([0 for i in range(len(q[1]) + len(q[2]))])
        elif q_type == 5:
            test_info.append([0 for i in range(len(q[1]) + len(q[2]))])
            right_results.append([0 for i in range(len(q[1]) + len(q[2]))])
        elif q_type == 6:
            test_info.append([0 for i in range(len(q[1]) + len(q[2]))])
            right_results.append([0 for i in range(len(q[1]) + len(q[2]))])
        
            
    
    current_question_ind = 0  
    current_answers = []
    last_used = 0
    PrevQuestion(0)
### окно тестирования


# отображение стартового окна
def GuiStart():

    #запуск окна тестировани
    def StartGuiTesting(event):
        global text_filename, text_qnum, box1, box2, button_start
        file = text_filename.get()
        p = 1
        try:
            qnum = int(text_qnum.get())  
        except ValueError:
            p = 0
        try:
            open('data_test\\'+file+'.xml')
        except IOError:
            p = 0
            variable = messagebox.askquestion('ошибка', 'Файл не найден')
        if p:
            box1.destroy()
            box2.destroy()
            button_start.destroy()
            GuiTesting(file, qnum)


    global main, text_filename, text_qnum, box1, box2, button_start
    box1 = Frame(main, bg = 'lightgrey', height = 50)
    box2 = Frame(main, bg = 'lightgrey')
    box3 = Frame(box2, bg = 'lightgrey')
    label1 = Label(box3, text = 'Название файла', font = '20', bg = 'lightgrey')
    text_filename = Entry(box3, font = '30', width = '10')
    text_filename. insert(END,'electro')
    box4 = Frame(box2, height = 20, bg = 'lightgrey')
    box5 = Frame(box2, bg = 'lightgrey')
    label2 = Label(box5, text = 'Кол-во вопросов', font = '20', bg = 'lightgrey')
    text_qnum = Entry(box5, font = '30', width = 10)
    text_qnum.insert(END,'10')
    box6 = Frame(box2, height = 20, bg = 'lightgrey')
    button_start = Button(box2, text = 'Начать тестирование', font = '15')
    # по нажатию запустить окно тестирования
    button_start.bind('<Button-1>', StartGuiTesting)
    
    box1.pack(side = 'top', fil = 'x', expand = False)
    box2.pack(side = 'top', fil = 'both', expand = True)
    box3.pack(side = 'top', fil = None, expand = False)
    label1.pack(side = 'left', fil = None, expand = True)
    text_filename.pack(side = 'right', fil = None, expand = False)   
    box4.pack(side = 'top', fil = 'x', expand = False)
    box5.pack(side = 'top', fil = None, expand = False)
    label2.pack(side = 'left', fil = None, expand = False)
    text_qnum.pack(side = 'right', fil = None, expand = False)
    box6.pack(side = 'top', fil = 'x', expand = False)
    button_start.pack(side = 'top', fil = None, expand = False)
    
global main
# создать пустое окно
main = Tk()
main.geometry('700x400+100+100')
main.title('Система тестирования')
# отрисовать элементы окна
GuiStart()
# запустить основной цикл программы
main.mainloop()
