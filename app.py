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
    # Her sorunun doğru cevapları
    correct_answers = {
        'question1': 'John',  # İlk soru için doğru cevap
        'question2': 'blue',  # İkinci soru için doğru cevap
        'question3': 'dog'    # Üçüncü soru için doğru cevap
    }

    # Başlangıçta kullanıcının puanını 0 olarak ayarlayın
    score = 0

    # Kullanıcının verdiği cevapları doğru cevaplarla karşılaştırın
    for question, user_answer in answers.items():
        if question in correct_answers and user_answer == correct_answers[question]:
            # Kullanıcının cevabı doğruysa, puanı artırın (örneğin 10 puan her soru için)
            score += 10

    return score


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
