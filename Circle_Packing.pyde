w, h = 1280, 720

circles = []
gridless = []

grid_width = 30
grid_height = 30

cell_width = float(w)/grid_width
cell_height = float(h)/grid_height

gifFrame = 1

color_palette = [(229, 115, 118), (235, 167, 114), (114, 178, 241), (211, 173, 223), (170, 198, 166)]

def set_palette_color():
    c = color_palette[int(random(len(color_palette)))]
    fill(c[0], c[1], c[2])

def get_grid_position(x, y):
    return x/cell_width + y/cell_height * grid_width 

class Circ:
    def __init__(self, size):
        # self.position = (0, 0)
        self.size = size
        self.valid = True
        
    def add_gridless(self):
        for i in range(20):
            self.position = (random(w), random(h))
            
            valid = True
            for c in gridless:
                distance = sqrt(pow(c.position[1] - self.position[1], 2) + pow(c.position[0] - self.position[0], 2))
                if (distance < (c.size/2 + self.size/2 + 2)):
                    valid = False
                    
            if (self.position[0] + self.size/2 > w or self.position[0] - self.size/2 < 0 or self.position[1] + self.size/2 > h or self.position[1] - self.size/2 < 0):
                valid = False
                    
            if (valid == True):
                gridless.append(self)
                self.display()
                break
            
    def place_manually(self, position):
        self.position = position
        gridless.append(self)
        self.display()
        
    def find_valid_position(self):
        for i in range(20):
            self.position = (random(w), random(h))
            grid_position = int(self.get_grid_position())
            
            compare_list = []
            
            for c in gridless:
                compare_list.append(c)
        
            for c in circles[grid_position]:
                compare_list.append(c)
                
            if (grid_position % grid_width > 0):
                for c in circles[grid_position - 1]:
                    compare_list.append(c)
                    
            if (grid_position % grid_width < grid_width - 1):
                for c in circles[grid_position + 1]:
                    compare_list.append(c)
                    
            if (grid_position >= grid_width):
                for c in circles[grid_position - grid_width]:
                    compare_list.append(c)
                    
            if (grid_position < (grid_width * grid_height) - grid_width):
                for c in circles[grid_position + grid_width]:
                    compare_list.append(c)
                    
            if (grid_position % grid_width > 0 and grid_position > grid_width):
                for c in circles[grid_position - grid_width - 1]:
                    compare_list.append(c)
                    
            if (grid_position % grid_width > 0 and grid_position < (grid_width * grid_height) - grid_width):
                for c in circles[grid_position + grid_width - 1]:
                    compare_list.append(c)
                    
            if (grid_position % grid_width < grid_width - 1 and grid_position > grid_width):
                for c in circles[grid_position - grid_width + 1]:
                    compare_list.append(c)
            
            if (grid_position % grid_width < grid_width - 1 and grid_position < (grid_width * grid_height) - grid_width):
                for c in circles[grid_position + grid_width + 1]:
                    compare_list.append(c)
            
            valid = True
            for c in compare_list:
                distance = sqrt(pow(c.position[1] - self.position[1], 2) + pow(c.position[0] - self.position[0], 2))
                if (distance < (c.size/2 + self.size/2 + 1)):
                    valid = False
                    
            if (self.position[0] + self.size/2 > w or self.position[0] - self.size/2 < 0 or self.position[1] + self.size/2 > h or self.position[1] - self.size/2 < 0):
                valid = False
                    
            if (valid == True):
                circles[grid_position].append(self)
                self.display()
                break
                
            
    def get_grid_position(self):
        x = self.position[0]
        y = self.position[1]
        return int(x/cell_width) + int(y/cell_height) * grid_width 
        
    def display(self):
        c = color_palette[int(random(len(color_palette)))]
        fill(c[0], c[1], c[2] )
        circle(self.position[0], self.position[1], self.size)
        
        
# Performance Test
# 10000 circles size 10, grid 1x1 ->   3:41
#                        grid 20x20 -> 0:06.19
        
def setup():
    size(w, h)

    pixelDensity(2)
    background(30, 30, 30)
    noStroke()
    
    
    for i in range(grid_width * grid_height):
        circles.append([])
        
    noFill()
    # c = Circ(500)
    # c.place_manually((500, 500))

    # for j in range(20):
    #     c = Circ(75)
    #     c.add_gridless()
        
    for j in range(10):
        c = Circ(50)
        c.add_gridless()
    
    save('Examples/Gif/' + str(gifFrame) + '.png')
    gifFrame += 1
    
    for j in range(10):
        c = Circ(50)
        c.add_gridless()
    
    save('Examples/Gif/' + str(gifFrame) + '.png')
    gifFrame += 1
        
    for x in range(2000):
        c = Circ(20)
        c.find_valid_position()
        
    for x in range(5000):
        c = Circ(3)
        c.find_valid_position()
        
    save('Examples/Gif/test.png')
        
    
