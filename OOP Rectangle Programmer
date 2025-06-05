import random as rd  # Import random module 

# Base Rectangle Class
class Rectangle:
    def __init__(self, height, width, x_coord, y_coord, number):
        # Store rectangle dimensions and coordinates
        self.height = abs(height)  # Ensure positive height
        self.width = abs(width)    # Ensure positive width
        self.x_coord = x_coord     # X position (bottom-left corner)
        self.y_coord = y_coord     # Y position (bottom-left corner)
        self.number = number       # Identifier number for the rectangle

    def set_properties(self, x, y, width, height):
        # Set rectangle position and dimensions with validation
        if width <= 0 or height <= 0:
            print("Width and height must be positive.")
            return False
        self.x_coord = x
        self.y_coord = y
        self.width = width
        self.height = height
        return True

    def move_rectangle(self, dx, dy):
        # Move rectangle by given x and y offsets
        self.x_coord += dx
        self.y_coord += dy

    def resize_rectangle(self, new_width, new_height):
        # Resize rectangle with validation
        if new_width > 0 and new_height > 0:
            self.width = new_width
            self.height = new_height
        else:
            print("Error: width and height must be positive!")

    def rotate_rectangle(self):
        # Rotate rectangle by 90 degrees (swap width and height)
        self.width, self.height = self.height, self.width

    def get_properties(self):
        # Return rectangle's current properties as a tuple
        return (self.x_coord, self.y_coord, self.width, self.height)

    def __str__(self):
        # Return string representation of rectangle for printing
        return f"Rectangle {self.number} - Corner({self.x_coord}, {self.y_coord}), Width: {self.width}, Height: {self.height}"


# Derived ColoredRectangle Class
class ColoredRectangle(Rectangle):
    def __init__(self, height, width, x_coord, y_coord, number, color="none"):
        # Inherit from Rectangle and add color attribute
        super().__init__(height, width, x_coord, y_coord, number)
        self.color = color  # Default color is 'none'

    def set_color(self, color):
        # Set color of the rectangle
        self.color = color
        print(f"Color set to {self.color}")

    def get_color(self):
        # Return color of the rectangle
        return self.color

    def __str__(self):
        # Override string method to include color
        base = super().__str__()
        return f"{base}, Color: {self.color}"


# Recursive Menu System
def menu(rectangles):
    while True:
        # Print menu options
        print("\nChoose from the following options:")
        print("s: Set a rectangle's properties")
        print("c: Set a rectangle's color")
        print("m: Move a rectangle")
        print("z: Resize a rectangle")
        print("r: Rotate a rectangle")
        print("p: Print a rectangle's properties")
        print("q: Quit\n")
    
        choice = input("Enter Choice: ").lower()  # Convert input to lowercase
        
        # Quit option
        if choice == 'q':
            print("Exiting program. Goodbye!")
            break

        # Invalid menu option
        elif choice not in ['s', 'c', 'm', 'z', 'r', 'p']:
            print("That is not a valid option.")
            continue

        # Ask user which rectangle to modify
        try:
            idx = int(input("Which rectangle? (1-3): "))
            if not 1 <= idx <= 3:
                print("Invalid rectangle number!")
                continue
            rect = rectangles[idx - 1]  # Select rectangle from list
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        # Set properties
        if choice == 's':
            try:
                x, y, w, h = map(int, input("Enter x, y, width, and height: ").split())
                if rect.set_properties(x, y, w, h):
                    print(rect)
            except:
                print("Invalid input! Please enter numbers.")

        # Set color
        elif choice == 'c':
            if isinstance(rect, ColoredRectangle):
                color = input("Enter color: ")
                rect.set_color(color)
            else:
                print(f"Rectangle {idx} does not support color.")

        # Move rectangle
        elif choice == 'm':
            try:
                dx, dy = map(int, input("Enter the amount to move in x and y directions: ").split())
                rect.move_rectangle(dx, dy)
                print(f"Rectangle {idx}'s new position: Corner({rect.x_coord}, {rect.y_coord})")
            except:
                print("Invalid input! Please enter numbers.")

        # Resize rectangle
        elif choice == 'z':
            try:
                w, h = map(int, input("Enter the new width and height: ").split())
                rect.resize_rectangle(w, h)
            except:
                print("Invalid input! Please enter numbers.")

        # Rotate rectangle
        elif choice == 'r':
            rect.rotate_rectangle()
            print(f"Rotated Rectangle {idx}. New dimensions: Width {rect.width}, Height {rect.height}")

        # Print rectangle properties
        elif choice == 'p':
            print(rect)



# Main Program Entry
if __name__ == "__main__":
    # Create 3 rectangles: 1 ColoredRectangle, 2 basic Rectangles
    rect1 = ColoredRectangle(0, 0, 0, 0, 1)
    rect2 = Rectangle(0, 0, 0, 0, 2)
    rect3 = Rectangle(0, 0, 0, 0, 3)

    all_rects = [rect1, rect2, rect3]  # Store in list
    menu(all_rects)  # Start interactive menu
