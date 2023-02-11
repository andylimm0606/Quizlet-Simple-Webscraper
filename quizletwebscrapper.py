from selenium import webdriver
from selenium.webdriver.common.by import By
import random


def main():
    
    load()

    print("Type 'end' to exit.\nIf wrong, question will be repeated.\nType 'hint', if you do not know & wish to skip.\n")
    f = open("data.txt", "r")
    lib = dict()
    total = 0
    while True:
        question = f.readline()
        if not question:
            break
        else:
            total += 1
        lib[question] = f.readline()
    
    score = 0
    while (len(lib) >= 0):
        key = random.choice(list(lib))
        print("Question: " + key)
        user_def = input("definition: ")
        if user_def == str(lib[key]).strip("\n"):
            lib.pop(key)
            score += 1
            print("Correct!")
            continue
        elif user_def == "hint":
            print(lib[key])
            continue
        elif user_def == "end":
            break
        else:
            print("Wrong. Correct answer: " + lib[key])

        
    print("\nfinal score: " + str(score) + "/" + str(total))





def load():
    f = open("data.txt", "w")
    user_url = "https://quizlet.com/260245848/short-flash-cards/"
    user_browser = webdriver.Chrome()
    user_browser.get(user_url)

    user_browser.execute_script("window.scrollBy(0, document.body.scrollHeight || document.documentElement.scrollHeight)")
   
    user_all = user_browser.find_elements(By.CLASS_NAME, "TermText.notranslate.lang-en")

    for i in range(len(user_all)):
        if i % 2 == 0:
            f.write(user_all[i].text.strip("\n") + "\n")
        else:
            f.write(user_all[i].text.strip("\n") + "\n")

    f.close()
    user_browser.close()


if '__main__':
    main()