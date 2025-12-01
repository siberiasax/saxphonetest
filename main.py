def question1():
  print("どっちがすき？")
  print("A.おえかき")
  print("B.ぬりえ")

  while True:
   select=input()
   if select=="A":
    question4()
    break
   elif select=="B":
    question2()
    break
   else:
    print("AかBを入力してください")

def question2():
  print("食べるものを決められない")
  print("A.はい")
  print("B.いいえ")

  select=input()

  while True:
    if select=="A":
      question3()
      break
    elif select=="B":
      question5()
      break
    else:
      print("AかBを入力してください")

def question3():
  print("どっちが多い？")
  print("A.人の話をきく")
  print("B.自分の話をする")

  while True:
    select=input()
    if select=="A":
      question6()
      break
    elif select=="B":
      print("あなたはアルトサックス！")
      break
    else:
      print("AかBを入力してください")

def question4():
  print("自分で作ったルールは必ず守るべきだと思う")
  print("A.はい")
  print("B.いいえ")

  while True:
    select=input()
    if select=="A":
      question7()
      break
    elif select=="B":
      question5()
      break
    else:
      print("AかBを入力してください")

def question5():
  print("気持ちのムラが少なくたんたんとしている")
  print("A.はい")
  print("B.いいえ")

  while True:
    select=input()
    if select=="A":
      question9()
      break
    elif select=="B":
      question6()
      break
    else:
      print("AかBを入力してください")

def question6():
  print("どちらかというと")
  print("A.リーダーに従う")
  print("B.自分のポリシーを大切にする")

  while True:
    select=input()
    if select=="A":
      print("あなたはテナーサックス！")
      break
    elif select=="B":
      print("あなたはアルトサックス！")
      break
    else:
      print("AかBを入力してください")

def question7():
  print("人ともめることはあまりない")
  print("A.はい")
  print("B.いいえ")

  while True:
    select=input()
    if select=="A":
      question8()
      break
    elif select=="B":
      print("あなたはソプラノサックス！")
      break
    else:
      print("AかBを入力してください")

def question8():
  print("チャレンジ精神を大切にしている")
  print("A.はい")
  print("B.いいえ")

  while True:
    select=input()
    if select=="A":
      print("あなたはソプラノサックス！")
      break
    elif select=="B":
      print("あなたはバリトンサックス！")
      break
    else:
      print("AかBを入力してください")

def question9():
  print("どっちが得意？")
  print("A.1つのことに集中する")
  print("B.いろんなことを同時にする")

  while True:
    select=input()
    if select=="A":
      print("あなたはバリトンサックス！")
      break
    elif select=="B":
      print("あなたはテナーサックス！")
      break
    else:
      print("AかBを入力してください")


print("サックス適性診断")
question1()
