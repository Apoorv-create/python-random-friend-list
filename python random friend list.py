from tkinter import*
import random

root=Tk()

root.title("Lucky friend wheel")
root.geometry("500x500")

list1 = ["James", "Isbella", "Oliver", "Peter", "Barry"]
print(list1)

def randomnumber():
    random_int = random.randint(0, 4)
    print(random_int)
    random_lucky_friend = list1[random_int]
    print("That lucky friend is:" + random_lucky_friend)

btn1 = Button(root)
btn1 = Button(root, text = "Who is your lucky friend!", command=randomnumber )
btn1.place(relx = 0.5, rely = 0.5, anchor=CENTER)


root.mainloop()