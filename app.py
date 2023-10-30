from flask import Flask, request, render_template

app = Flask(__name)


@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Kullanıcının cevaplarını işleyin ve puanı hesaplayın
        score = calculate_score(request.form)
        # Puanı en yüksek puanla karşılaştırın ve gerekirse güncelleyin
        update_high_score(score)
    # En yüksek puanı alın
    high_score = get_high_score()
    return render_template('quiz.html', high_score=high_score)


def calculate_score(answers):
    # Cevapları işleyerek puanı hesaplayın
    # Örneğin, answers['question1'], answers['question2'], vb. kullanarak cevapları kontrol edebilirsiniz.
    # Bu kısmı doldurmanız gerekiyor
    # Pass ifadesi, fonksiyonu geçici olarak boş bırakmanıza olanak tanır.
    pass


def get_high_score():
    # En yüksek puanı okuyun ve döndürün
    try:
        with open('high_score.txt', 'r') as file:
            high_score = file.read()
        return high_score
    except FileNotFoundError:
        return "0"


def update_high_score(score):
    # Yeni puan, mevcut en yüksek puandan daha yüksekse güncelleyin
    high_score = get_high_score()
    if int(score) > int(high_score):
        with open('high_score.txt', 'w') as file:
            file.write(str(score))


if __name__ == '__main__':
    app.run(debug=True)
