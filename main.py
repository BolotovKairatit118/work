import csv
points = 0

with open('Книга1.csv', newline='') as File:  
    reader = csv.reader(File, delimiter=',')
    for row in reader:
      print(row[0])
      print(row[1],row[2],row[3])
      i = input("Введите вариант ответа (а, б, в): ")
      if i == 'а':
        if row[1] == row[4]:
          print("Правильно!")
          points += 5
        else:
          print("Неправильно!")
      elif i == 'б':
        if row[2] == row[4]:
          print("Правильно")
          points += 5
        else:
          print("Неправильно.!.")
      elif i == 'в':
        if row[3] == row[4]:
          print("Правильно!")
          points += 5
        else:
          print("Неправильно!")
      else:
        print("Такого ответа нет")
    
print('Вы набрали баллов  + str ')
if points <= 60:
  print("Вы набрали F")
elif points >59 and points <=63:  
  print("Вы набрали D-")
elif points >63 and points <=66:
  print("Вы набрали D")
elif points >66 and points <=70: 
  print("Вы набрали D+")
elif points >70 and points <=75:
  print("Вы набрали C-")
elif points >75 and points <=79:
  print("Вы набрали C")
elif points >79 and points <=83:
  print("Вы набрали C+")
elif points >83 and points <=87:
  print("Вы набрали B-")
elif points >87 and points <=90:
  print("Вы набрали B")
elif points >90 and points <=93:
  print("Вы набрали B+")
elif points >93 and points <=95:
  print("Вы набрали A-")
elif points >95 and points <=97:
  print("Вы набрали A")
elif points >97 and points <=98:
  print("Вы набрали A+")
elif points >98 and points <=100:
  print("Вы набрали A+")