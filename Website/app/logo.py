from turtle import*

def Logo(l):
    color("gray") #border/base color
    begin_fill()
    right(40)
    forward(l+l/3)
    left(90)
    forward(l/8) 
    left(90)
    forward(l+l/3)
    left(90)
    forward(l/8)
    left(180)

    forward (l/8)
    right(90)
    end_fill()
    forward(l/7)

    left(70)
    
    color("red") #main hat color
    begin_fill()    
    forward(l)
    right(30)
    forward(l/2)
    right(40)
    forward(l/3)
    right(60)
    forward(l/2)

    right(150)
    forward(l/2)
    
    left(100)
    forward(l/4)
    left(30)
    forward(l/3)
    left(15)
    forward(l/3)
    forward(l/4)
    
    end_fill()
    color("gray") #base color
    penup()
    goto(173,-18)
    pendown()
    forward(l/4)
    #flower(l/8) #flower
    snowflake(l/3,2) #snowflake
    #penup()
    #goto(75,-10)
    #pendown() 
    #snowflake(l/3,1)
    hideturtle()
    #getscreen().getcanvas().postscript(file='santahat.ps')
    done()

def edge(lengthSide,levels): #edges
    if levels == 0:
        forward(lengthSide)
    else:
        edge(lengthSide/3,levels-1)
        left(60) 
        edge(lengthSide/3,levels-1)
        right(120)
        edge(lengthSide/3,levels-1)
        left(60)
        edge(lengthSide/3,levels-1)
         
def snowflake(lengthSide,levels): #snowflake process
        color("gray")
        begin_fill() 
        
        edge(lengthSide,levels)
        right(120)
        edge(lengthSide,levels) 
        right(120)
        edge(lengthSide,levels) 
        end_fill()
    
def flower(l): #flower process
    leaf(l)
    right (90)
    petals(l)
    leaf(l)
    right (90)
    petals(l)
    leaf(l)
    right (90)
    petals(l)
    leaf(l)
    right (90)
    petals(l)
    leaf(l)
    right (90)
    petals(l)     
    done()

def petals(l): #petals for flowers
    color("purple")
    begin_fill()
    forward(l)
    right (30)
    forward(l) 
    right (140)
    forward (l)
    right (30)
    forward (l)
    end_fill()
    return 
 
def leaf(l): #leaf for flower
    color("green")
    begin_fill()
    forward(l)
    right (30)
    forward(l)
    left (40)
    forward(l)
    left (140)
    forward(l)
    left (40)
    forward(l)
    right (10)
    forward(l)
    right (180)
    end_fill()

def runscreen(): #running
    Logo(100)
   
runscreen()    