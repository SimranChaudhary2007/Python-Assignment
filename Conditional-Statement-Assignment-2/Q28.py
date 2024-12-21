"""Ask the user for a subject score. If it's above 90, congratulate him. If it's between 50 and 90,
suggest improvement. Otherwise, advise on retaking the course."""

score=int(input('Enter your subject score:'))
if score>90:
    print('Congratulation! Keep it up.')
elif 50<= score <=90:
    print('Good effort! Study harder. You can improve.')
else:
    print('Your score is not good. I suggest to you to retake the course.')