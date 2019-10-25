from tkinter import *
#hopefully this should be a window manager for python


def main():
    window = Tk()
    window.title("Political Data")
    window.mainloop()
    #opens and saves the contents of a file to 'text' variable
    file = open("data/pac_example.txt", "r")
    text = file.read()


    #splits 'text' and stores in an array
    array = text.split('\n')

    #a vague attempt to loop through and parse the array even further
    for x in range(0, array.__len__()):
        array[x] = array[x].split('|,')
        for y in array[x]:
            # print (y)
            y = y.strip('|')
            # print (y)
    #classic print statement debugging
    print(array)

if __name__== "__main__":
  main()

