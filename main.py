import pandas
import turtle
#Squirrel Stuff
"""
data = pandas.read_csv("./data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" :[gray_squirrels,black_squirrels,red_squirrels]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_Table.csv")
"""


#US States Game

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./data/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

state_data = pandas.read_csv("./data/50_states.csv")

guessed_states = []
missing_states = []
all_states = state_data.state.to_list()
while len(guessed_states) < 50:
    guess = screen.textinput(f"{len(guessed_states)}/50 States Correct ","What's another state's name?").title()

    if guess == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("./Output/MissingStates.csv", index=False)
        break

    if guess in all_states and guess not in guessed_states:
        guessed_states.append(guess)
        tim = turtle.Turtle()
        tim.hideturtle
        tim.pu()
        state = state_data[state_data.state == guess]
        tim.goto(int(state.x), int(state.y))
        tim.write(guess,False,align="center",font =("Arial",12,"normal"))

    


#def get_mouse_click_coor(x,y):
#    print(x,y)
#turtle.onscreenclick(get_mouse_click_coor)

#states_csv = pandas.read_csv("./data/50_states.csv")
#screen.exitonclick()
