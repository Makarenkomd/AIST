import xml.etree.cElementTree as xml
import random


def QType1():
    #термин-определение
    global items, nets, nets_types
    data = []
    d = min(5, len(nets['DESC']))
    while len(data) != d:
        r = random.randint(0, d - 1)
        box = nets['DESC'][r]
        if not box in data:
            data.append(box)
    q = items[data[0][0]]
    ans = [items[data[0][1]]]
    while len(ans) != d:
        r = random.randint(0, d - 1)
        box = items[data[r][1]]
        if not box in ans:
            ans.append(box)
    #первый элемент массива ans ¤вл¤етс¤ правильным ответом 
    #[str, list[str]]
    return [q, ans]

def QType2():
    #определение-термин
    global items, nets, nets_types    
    data = []
    d = min(5, len(nets['DESC']))
    while len(data) != d:
        r = random.randint(0, d - 1)
        box = nets['DESC'][r]
        if not box in data:
            data.append(box)
    q = items[data[0][1]]
    ans = [items[data[0][0]]]
    while len(ans) != d:
        r = random.randint(0, d - 1)
        box = items[data[r][0]]
        if not box in ans:
            ans.append(box)
    #первый элемент массива ans ¤вл¤етс¤ правильным ответом 
    #[str, list[str]]
    return [q, ans]   

def QType3():
    #состав
    global items, nets, nets_types
    d = len(nets['HP'])
    r = random.randint(0, d - 1)
    qid = nets['HP'][r][0]
    q = items[qid]
    right_ans = []
    wrong_ans = []
    for i in nets['HP']:
        if i[0] == qid and not items[i[1]] in right_ans:
            right_ans.append(items[i[1]])
    box = len(right_ans)
    for i in nets['HP']:
        if i[0] != qid and not items[i[1]] in wrong_ans and not items[i[1]] in right_ans:
            wrong_ans.append(items[i[1]])
        if box * 4 <= len(wrong_ans):
            break
    #q - то, состав чего твебуетс¤ найти 
    #right_ans - правильные составл¤ющие
    #wrong_ans - непрвильные составл¤ющие
    #[str, list[str], list[str]]
    return [q, right_ans, wrong_ans]

def QType4():
    #свойства 
    global items, nets, nets_types
    d = len(nets['AKO'])
    r = random.randint(0, d - 1)
    qid = nets['AKO'][r][0]
    q = items[qid]
    right_ans = []
    wrong_ans = []
    for i in nets['AKO']:
        if i[0] == qid and not items[i[1]] in right_ans:
            right_ans.append(items[i[1]])
    box = len(right_ans)
    for i in nets['AKO']:
        if i[0] != qid and not items[i[1]] in wrong_ans and not items[i[1]] in right_ans:
            wrong_ans.append(items[i[1]])
        if box * 4 <= len(wrong_ans):
            break
    #q - то, свойства чего надо определить 
    #right_ans - правильные свойства объекта q
    #wrong_ans - неправильные свойства объекта q
    #[str, list[str], list[str]]
    return [q, right_ans, wrong_ans]    


def QType5():
    #примеры
    global items, nets, nets_types
    d = len(nets['ISA'])
    r = random.randint(0, d - 1)
    qid = nets['ISA'][r][0]
    q = items[qid]
    right_ans = []
    wrong_ans = []
    for i in nets['ISA']:
        if i[0] == qid and not items[i[1]] in right_ans:
            right_ans.append(items[i[1]])
    box = len(right_ans)
    for i in nets['ISA']:
        if i[0] != qid and not items[i[1]] in wrong_ans and not items[i[1]] in right_ans:
            wrong_ans.append(items[i[1]])
        if box * 4 <= len(wrong_ans):
            break
    #q - то, примеры чего надо определить 
    #right_ans - правильные примеры объекта q
    #wrong_ans - неправильные примеры объекта q
    #[str, list[str], list[str]]
    return [q, right_ans, wrong_ans]    

def QType6():
    #класс - тип
    global items, nets, nets_types
    d = len(nets['ISA'])
    r = random.randint(0, d - 1)
    qid = nets['ISA'][r][1]
    q = items[qid]
    right_ans = []
    wrong_ans = []
    for i in nets['ISA']:
        if i[1] == qid and not items[i[0]] in right_ans:
            right_ans.append(items[i[0]])
    box = len(right_ans)
    for i in nets['ISA']:
        if i[1] != qid and not items[i[0]] in wrong_ans and not items[i[0]] in right_ans:
            wrong_ans.append(items[i[0]])
        if box * 4 <= len(wrong_ans):
            break
    #q - то, примеры чего надо определить 
    #right_ans - правильные примеры объекта q
    #wrong_ans - неправильные примеры объекта q
    #[str, list[str], list[str]]
    return [q, right_ans, wrong_ans]   

def QuestionsNumber(file_path):
    kint = 10 ** 9 + 5
    box = main(file_path, kint, p = 1)
    return box

def parsing_xml(file_path):

    kint = 10 ** 9
    kstr = '{urn:xmind:xmap:xmlns:content:2.0}'

    xml_file = xml.parse(file_path)
    #xml_file = xml.parse(file_path)
    root = xml_file.getroot()

    # items - dictionary вершин сети [id] = text
    # nets -
    # парсинг вершин
    items = {}
    items[root[0][0].attrib['id']] = root[0][0][0].text
    ind = 0
    for i in range(kint):
        tag = root[0][0][i].tag
        if tag == kstr + 'children':
            ind = i
            break
    for i in root[0][0][ind][0]:
        id = i.attrib['id']
        text = i[0].text
        items[id] = text
    # парсинг связей
    # словарь связей
    nets = {}
    nets_types = []
    for i in root[0][2]:
        a = i.attrib['end1']
        b = i.attrib['end2']
        ind = 0
        for j in range(kint):
            tag = i[j].tag
            if tag == kstr + 'title':
                ind = j
                break
        # получили тип связи
        tp = i[ind].text
        if not tp in nets_types:
            nets_types.append(tp)
            nets[tp] = []
        nets[tp].append([a, b])
    # возвращаем словарь вершин, словарь связей, содержащий список пар вершин, список всех существующих свзей
    return items, nets, nets_types

# def make_question( r = -1):
def make_question():

    box = []
    holost_step = 0
    while True:
        #if r == -1: r = random.randint(1, 6)
        r = random.randint(1, 6)
        if r == 1 and 'DESC' in nets_types:
            box = QType1()
        elif r == 2 and 'DESC' in nets_types:
            box = QType2()
        elif r == 3 and 'HP' in nets_types:
            box = QType3()
        elif r == 4 and 'AKO' in nets_types:
            box = QType4()
        elif r == 5 and 'ISA' in nets_types:
            box = QType5()
        elif r == 6 and 'ISA' in nets_types:
            box = QType6()
        else:
            holost_step += 1
        # если получилось создать вопрос закончить
        if len(box)>0 : return r, box
        if holost_step>10: return -1, box


def main(file_path, questions_number):

    global items, nets, nets_types
    items, nets, nets_types = parsing_xml(file_path)
        
    ret = []
    questions = []
    l = 0
    p = 0
    while l != questions_number:
        r, box = make_question()
        if r == -1:
            questions_number = l
            break
        if not [r, box[0]] in questions:
            ret.append([r, box])
            questions.append([r, box[0]])
            l += 1
            p = 0
        else:
            p += 1
    return ret



