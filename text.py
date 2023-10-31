##### start.py
greeting = "Здравствуйте"
#####
grade = "Классы"
#####
choose = "Выберите нужный раздел"
#####
inputGrade = "Введите класс:"
gradeType = "Выберите тип!"
####
cancel = "❌ Отменено!"
####
saved = "Сохранено"
####
empty = "Ничего не существует"
####
next = "Следующий"
####
prev = "Предыдущий"
####
delete = "Вы действительно удаляете?"
####
deleted = "Успешно удалено!"
####
inputBookName = "Введите название книги!"
inputBookDesc = "Введите дополнительную информацию!"
sendPDF = "Отправить PDF-файл"
confirmBook = "Сохранить данные?"
sendFile = "Пожалуйста, отправьте файл!"
# logic questions
#####
inputLogicQuestion = "Введите вопрос!"
inputLogicAnswer = "Введите ответ!"

# school book
#####
inputSchoolBookGrade = "Введите класс!"
inputSchoolBookName = "Введите имя!"
########### buttons



confirmBtn = ['✅ Подтверждение', "❌ Отмена"]
######
btnMenu = ["Школьные книги", "Логические вопросы", "Книги для развития", "Информация об учителях", "Список уроков"]
#####
btnAdmin = ['Классы', "Логические вопросы", "Книги для развития", "Школьные книги", "Список уроков"]
#####
btnGradeMenu = ["Список классов", "Добавить новый класс", "Главное меню"]
#####
btnBooksMenu = ["Список книг по развитию", "Добавление новой книги развития", "Главное меню"]
#####
btnGradeUpdate = ["Изменить", "Удалить", "Назад"]
#####
btnLogicQuestion = ["Список Логические вопросы", "Добавление новой Логические вопросы", "Главное меню"]
#####
btnSchoolBook = ["Список Школьные книги", "Добавление новой Школьные книги", "Главное меню"]
#####
###function text
def ConfirmGrade(grade, type):
    msg = f"""
Класс: {grade}
Тип: {type}
    """
    return msg

def ConfirmGradeId(id, grade, type):
    msg = f"""
#{id}.Класс: {grade}
Тип: {type}
    """
    return msg

def QuestionsList(id, grade, type):
    msg = f"""
#{id}.Вопрос: {grade}
Ответ: {type}
    """
    return msg

def QuestionOne(grade, type):
    msg = f"""
Вопрос: {grade}
Ответ: {type}
    """
    return msg

def SchoolBook(grade, type):
    msg = f"""
Класс: {grade}
Название книги: {type}
    """
    return msg

def BookMsg(id, book):
    msg = f"""
#{id}. {book}
    """
    return msg

def BookAboutMsg(id, book, caption):
    msg = f"""
#{id}. <b>{book}</b>
----------------
{caption}
    """
    return msg