import time 
from colorama import Fore  
print(Fore.CYAN + r'''                                                                                                                                              
                                                                                   ,-.----.                                  ____             
                                                           .--.--.                 \    /  \  ,-.----.       ,---,.        ,'  , `.    ,---,. 
                                                          /  /    '.          ,--, |   :    \ \    /  \    ,'  .' |     ,-+-,.' _ |  ,'  .' | 
                                                         |  :  /`. /        ,'_ /| |   |  .\ :;   :    \ ,---.'   |  ,-+-. ;   , ||,---.'   | 
                                                         ;  |  |--`    .--. |  | : .   :  |: ||   | .\ : |   |   .' ,--.'|'   |  ;||   |   .' 
                                                         |  :  ;_    ,'_ /| :  . | |   |   \ :.   : |: | :   :  |-,|   |  ,', |  '::   :  |-, 
                                                          \  \    `. |  ' | |  . . |   : .   /|   |  \ : :   |  ;/||   | /  | |  ||:   |  ;/| 
                                                           `----.   \|  | ' |  | | ;   | |`-' |   : .  / |   :   .''   | :  | :  |,|   :   .' 
                                                           __ \  \  |:  | | :  ' ; |   | ;    ;   | |  \ |   |  |-,;   . |  ; |--' |   |  |-, 
                                                          /  /`--'  /|  ; ' |  | ' :   ' |    |   | ;\  \'   :  ;/||   : |  | ,    '   :  ;/| 
                                                         '--'.     / :  | : ;  ; | :   : :    :   ' | \.'|   |    \|   : '  |/     |   |    \ 
                                                           `--'---'  '  :  `--'   \|   | :    :   : :-'  |   :   .';   | |`-'      |   :   .' 
                                                                     :  ,      .-./`---'.|    |   |.'    |   | ,'  |   ;/          |   | ,'   
                                                                      `--`----'      `---`    `---'      `----'    '---' ,----,    `----'     
                                                                               ,----..                                 ,/   .`|               
                                                                  ,----..     /   /   \                ,-.----.      ,`   .'  :               
                                                                 /   /   \   /   .     :          ,--, \    /  \   ;    ;     /               
                                                                |   :     : .   /   ;.  \       ,'_ /| ;   :    \.'___,/    ,'                
                                                                .   |  ;. /.   ;   /  ` ;  .--. |  | : |   | .\ :|    :     |                 
                                                                .   ; /--` ;   |  ; \ ; |,'_ /| :  . | .   : |: |;    |.';  ;                 
                                                                ;   | ;    |   :  | ; | '|  ' | |  . . |   |  \ :`----'  |  |                 
                                                                |   : |    .   |  ' ' ' :|  | ' |  | | |   : .  /    '   :  ;                 
                                                                .   | '___ '   ;  \; /  |:  | | :  ' ; ;   | |  \    |   |  '                 
                                                                '   ; : .'| \   \  ',  / |  ; ' |  | ' |   | ;\  \   '   :  |                 
                                                                '   | '/  :  ;   :    /  :  | : ;  ; | :   ' | \.'   ;   |.'                  
                                                                |   :    /    \   \ .'   '  :  `--'   \:   : :-'     '---'                    
                                                                 \   \ .'      `---`     :  ,      .-./|   |.'                                
                                                                  `---`                   `--`----'    `---'                                  
                                                                                                                                                 ''')
time.sleep(2)
print(Fore.WHITE + "Welcome to the game of life.")
time.sleep(1)
input("Press Enter To Continue...")
name = []
for i in range(1,6):
  name.append(input(f"Enter your name player{i}:"))
  time.sleep(0.5)
time.sleep(1)
print(f"welcome: {name[0]}\n{name[1]}\n{name[2]}\n{name[3]}\n{name[4]}\n" )
score = {}
for j in range(len(name)):
  score.update({name[j] : 0})
  time.sleep(0.5)
print(f"Score : {score}")
time.sleep(1)
ro = 1
while len(name) > 1:
  print(f"ROUND {ro}")
  ro += 1
  list = []
  for i in range(len(name)):
    while True:
      num = int(input(f"Enter your number {name[i]}: "))
      time.sleep(0.8)
      if 0 <= num <= 100:
        list.append(num)
        break
      print("The number should be in between 0 to 100 ! Try Again")
  s = sum(list)/len(list)
  print(f"The average is {s}")
  time.sleep(1)
  target = s*0.8
  target = round(target,1)
  print(f"The calculated value {s} x 0.8 is {target}")
  time.sleep(1)
  new_list = [round(abs(i - target),1) for i in list]
  #print(new_list)
  win = []
  for i in range(len(new_list)):
    if new_list[i]== min(new_list):
      win.append(i)
  for i in range(len(win)):
    print(Fore.GREEN + f"🎉  {name[win[i]]} is the winner! 🎉")
    time.sleep(1)
    print(Fore.WHITE+ f"Congratulations!! {name[win[i]]}")
  time.sleep(1)
  for w in range(len(name)):
    if w not in win:
      score.update({name[w]:score[name[w]]-1})
  print(f"Score : {score}")
  removal_list = []
  for i in name[:]:
    if score[i] <= -10:
      print(Fore.RED + f"{i} is Eliminated")
      removal_list.append(i)
  for i in removal_list:
    name.remove(i)
time.sleep(1.5)      
print(Fore.RED + "\n🔥 THE GAME HAS ENDED! 🔥")
time.sleep(1)
print(Fore.YELLOW + f"🏆 {name[0].upper()} is the FINAL WINNER! 🏆")
print(Fore.WHITE + "Thank you for playing the game")
