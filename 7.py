from flask import Flask
from flask import request
from flask import url_for

app = Flask(__name__)
a = [
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept1>\n<label class ="form-check-label" for ="acceptRules">"Инженер-исследователь"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept2>\n<label class ="form-check-label" for ="acceptRules">"Пилот"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept3>\n<label class ="form-check-label" for ="acceptRules">"Строитель"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept4>\n<label class ="form-check-label" for ="acceptRules">"Экзобиолог"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept5>\n<label class ="form-check-label" for ="acceptRules">"Врач"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept6>\n<label class ="form-check-label" for ="acceptRules">"Инженер по терраформированию"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept7>\n<label class ="form-check-label" for ="acceptRules">"Климатолог"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept8>\n<label class ="form-check-label" for ="acceptRules">"Специалист по радиационной защите"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept9>\n<label class ="form-check-label" for ="acceptRules">"Астрогеолог"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept10>\n<label class ="form-check-label" for ="acceptRules">"Гляциолог"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept11>\n<label class ="form-check-label" for ="acceptRules">"Инженер жизнеобеспечения"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept12>\n<label class ="form-check-label" for ="acceptRules">"Метеоролог"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept13>\n<label class ="form-check-label" for ="acceptRules">"Оператор марсохода"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept14>\n<label class ="form-check-label" for ="acceptRules">"Киберинженер"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept15>\n<label class ="form-check-label" for ="acceptRules">"Штурман"</label>',
    '<input type="checkbox" class="form-check-input" id="acceptRules" name=accept16>\n<label class ="form-check-label" for ="acceptRules">"Пилот дронов"</label>']


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Title</title>
                          </head>
                          <body bgcolor="black">
                            <center><h1><font size="32" color="#FF0000">Metallica</font></h1></center>
                            <p>hhh</p>
                            <div>
                            <center><textarea id='a' cols="75" rows="15" name="about"></textarea></center>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" placeholder="Фамилия" name="surname">
                                    <input type="text" class="form-control" id="text" placeholder="Имя" name="name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <br>
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <br>Какие у Вас есть професии?
                                    <div class="form-group form-check">
                                        {"<br>".join(a)}
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept0">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form["surname"])
        print(request.form["name"])
        print(request.form['email'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['accept0'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
