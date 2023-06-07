import turtle
screen = turtle.Screen()
screen.title("us states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



# gett the csv data

import pandas
states_df = pandas.read_csv("50_states.csv")
correct_guesses = []

def get_state():
  answer_state = screen.textinput(
      title=f"correct guesses {len(correct_guesses)}/50", prompt="another state")
  return answer_state
def write_to_screen(x,y,state):
  text_turtle = turtle.Turtle()
  text_turtle.up()
  text_turtle.goto(int(x),int(y))
  text_turtle.hideturtle()
  text_turtle.write(state,align="center",font=("Courier",10,"normal"))


def states_not_given():
  staes_not_given = []
  for state in states_list:
    if state not in correct_guesses:
      staes_not_given.append(state)
      print(state)
  states_to_csv = pandas.DataFrame({
      "state missed": staes_not_given
  })
  states_to_csv.to_csv("states missed.csv")

states_list = states_df["state"].to_list()
#return the row that matche,s the user input
while len(correct_guesses) < 50:
  state_input =get_state().title()
  if state_input == "Exit":
    states_not_given()
    turtle.bye()
  if state_input in states_list:
    if state_input not in correct_guesses:
      state = states_df[states_df["state"] == state_input].iloc[0]
      write_to_screen(state.x,state.y,state.state)
      correct_guesses.append(state.state)




turtle.mainloop()
