import turtle
import random

# Function to draw a polygon
def draw_polygon(sides, length, color):
    angle = 360 / sides
    turtle.color(color)
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

# Main function
def main():
    while True:
        # Get user input for sides, length, and color
        sides = int(input("Enter the number of sides for the polygon (greater than 0 and less than 100): "))
        while sides <= 0 or sides >= 100:
            print("Number of sides must be greater than 0 and less than 100.")
            sides = int(input("Enter the number of sides for the polygon: "))

        length = int(input("Enter the length of each side: "))

        print("What color would you like your polygon to be:")
        print("1. Red")
        print("2. Orange")
        print("3. Black")
        print("4. Green")
        print("5. Indigo")
        print("6. Blue")
        print("7. Purple")
        print("8. Violet")
        print("9. Gold")
        print("10. Cyan")
        print("11. Rainbow (random colors)")
        color_choice = input("Enter the number corresponding to your color choice: ")

        if color_choice == '1':
            color = 'red'
        elif color_choice == '2':
            color = 'orange'
        elif color_choice == '3':
            color = 'black'
        elif color_choice == '4':
            color = 'green'
        elif color_choice == '5':
            color = 'indigo'
        elif color_choice == '6':
            color = 'blue'
        elif color_choice == '7':
            color = 'purple'
        elif color_choice == '8':
            color = 'violet'
        elif color_choice == '9':
            color = 'gold'
        elif color_choice == '10':
            color = 'cyan'
        elif color_choice == '11':
            color = 'rainbow'
        else:
            print("Invalid color choice. Defaulting to black.")
            color = 'black'

        # Draw the polygon
        turtle.speed(0)
        turtle.penup()
        turtle.goto(-length / 2, 0)
        turtle.pendown()
        if color == 'rainbow':
            for _ in range(sides):
                turtle.color(random.choice(['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'brown', 'black']))
                turtle.forward(length)
                turtle.right(360 / sides)
        else:
            draw_polygon(sides, length, color)

        # Ask the user if they want to draw another polygon
        choice = input("Do you want to draw another polygon? (yes/no): ")
        if choice.lower() != 'yes':
            break

    turtle.done()

# Run the main function
if __name__ == "__main__":
    main()
