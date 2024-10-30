#importing the pyplot module
import matplotlib.pyplot as plt

#Defing the function
def plot_data():

#Opening the file containing coordinates
    coordinate_file = open('C:/Users/TEVES/Downloads/x_y_coordinates.txt', 'r')

#reading the file 1st exhibit
    print(coordinate_file.read())

#reading the file final exhibit
    print(coordinate_file.readline())

#Creating two empty lists, one for x coordinates and one for y coordinates
    x_coordinates = []
    y_coordinates = []
    coordinate_file.readline()

#Looping, splitting and parsing the data type as float
    for line in coordinate_file.readlines():
        x_coordinates.append(float(line.split(',')[0]))
        y_coordinates.append(float(line.split(',')[1]))

#Setting up properties for the scatterplot
    plt.scatter(x_coordinates, y_coordinates)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Graph showing a scatterplot of coordinates')
    plt.grid(True)
    plt.show()
#Finally to plot the graph representing the scatterplot
plot_data()