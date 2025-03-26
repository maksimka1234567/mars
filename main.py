from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    lines = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
             "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(lines)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                        <div>Вот она какая, красная планета.</div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astr_sel():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/astro.css')}">
                            <h1 align="center">Анкета претендента</h1>
                            <h2 align="center">на участие в миссии</h2>
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <p><br></p>
                                    <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">
                                    <div class="form-group">
                                        <label for="educationSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group form-check">
                                        <label for="professions">Какие у вас есть профессии?</label><br>
                                        <div id="professions">
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="engineer-researcher" name="professions" value="инженер-исследователь">
                                                <label class="form-check-label" for="engineer-researcher">Инженер-исследователь</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="pilot" name="professions" value="пилот">
                                                <label class="form-check-label" for="pilot">Пилот</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="builder" name="professions" value="строитель">
                                                <label class="form-check-label" for="builder">Строитель</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="exobiologist" name="professions" value="экзобиолог">
                                                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="doctor" name="professions" value="врач">
                                                <label class="form-check-label" for="doctor">Врач</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="terraformer" name="professions" value="инженер по терраформированию">
                                                <label class="form-check-label" for="terraformer">Инженер по терраформированию</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="climatologist" name="professions" value="климатолог">
                                                <label class="form-check-label" for="climatologist">Климатолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="radiation-specialist" name="professions" value="специалист по радиационной защите">
                                                <label class="form-check-label" for="radiation-specialist">Специалист по радиационной защите</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="astrogeologist" name="professions" value="астрогеолог">
                                                <label class="form-check-label" for="astrogeologist">Астрогеолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="glaciologist" name="professions" value="гляциолог">
                                                <label class="form-check-label" for="glaciologist">Гляциолог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="life-support-engineer" name="professions" value="инженер жизнеобеспечения">
                                                <label class="form-check-label" for="life-support-engineer">Инженер жизнеобеспечения</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="meteorologist" name="professions" value="метеоролог">
                                                <label class="form-check-label" for="meteorologist">Метеоролог</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="rover-operator" name="professions" value="оператор марсохода">
                                                <label class="form-check-label" for="rover-operator">Оператор марсохода</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="cyber-engineer" name="professions" value="киберинженер">
                                                <label class="form-check-label" for="cyber-engineer">Киберинженер</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="navigator" name="professions" value="штурман">
                                                <label class="form-check-label" for="navigator">Штурман</label>
                                            </div>
                                            <div class="form-check">
                                                <input class="form-check-input" type="checkbox" id="drone-pilot" name="professions" value="пилот дронов">
                                                <label class="form-check-label" for="drone-pilot">Пилот дронов</label>
                                            </div>
                                        </div>
                                    </div>

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
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['professions'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                        integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                        crossorigin="anonymous">
                        <link rel="stylesheet"
                        href={url_for('static', filename='css/style.css')}>
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
               alt="здесь должна была быть картинка, но не нашлась">
                        <h2 class="alert alert-dark" id="123">Человечество вырастает из детства.</div>
                        <h2 class="alert alert-success">Человечеству мала одна планета.</div>
                        <h2 class="alert alert-secondary">Мы сделаем обитаемыми безжизненные пока планеты.</div>
                        <h2 class="alert alert-warning">И начнем с Марса!</div>
                        <h2 class="alert alert-danger">Присоединяйся!</div>
                      </body>
                    </html>"""


@app.route('/choice/<planet_name>')
def planet_name(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet" 
                            href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                            integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                            crossorigin="anonymous">
                            <title>Варианты выбора</title>
                          </head>
                          <body>
                            <h1>Моё предложение: {planet_name}</h1>
                            <h2>Эта планета близка к Земле;</h2>
                            <h2 class="alert alert-success" id="123">На ней много необходимых ресурсов;</div>
                            <h2 class="alert alert-dark">На ней есть вода и атмосфера;</div>
                            <h2 class="alert alert-warning">На ней есть небольшое магнитное поле;</div>
                            <h2 class="alert alert-danger">Наконец, она просто красива!</div>
                          </body>
                        </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet" 
                                href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                                integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                                crossorigin="anonymous">
                                <title>Результаты</title>
                              </head>
                              <body>
                                <h1>Результаты отбора</h1>
                                <h2>Претендента на участие в миссии {nickname}:</h2>
                                <h3 class="alert alert-success" id="123">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                                <h3>составляет {rating}!</h3>
                                <h3 class="alert alert-warning">Желаем удачи!</div>
                              </body>
                            </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/img/download.png')
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" 
                        href={url_for('static', filename='css/astro.css')}>
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                        <h1 align="center">Загрузка фотографии</h1>
                        <h2 align="center">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <img src={url_for('static', filename='img/download.png')} width=400>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                  </body>
                </html>"""


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                        <h1 align="center">Пейзажи Марса</h1>
                            <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img src="static/landscapes/landscape1.png" class="d-block w-100" alt="Пейзаж 1">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/landscape2.png" class="d-block w-100" alt="Пейзаж 2">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/landscape3.png" class="d-block w-100" alt="Пейзаж 3">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/landscape4.png" class="d-block w-100" alt="Пейзаж 4">
                                </div>
                                <div class="carousel-item">
                                  <img src="static/landscapes/landscape5.png" class="d-block w-100" alt="Пейзаж 5">
                                </div>
                              </div>
                              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Предыдущий</span>
                              </button>
                              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Следующий</span>
                              </button>
                            </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
