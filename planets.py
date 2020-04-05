def weight_on_planets():
   weight = int(input('What do you weigh on earth? '))
   mars = weight*0.38
   jupiter = weight*2.34
   print('\nOn Mars you would weight %.2f pounds.\nOn Jupiter you would weight %.2f pounds.' % (mars,jupiter))
   
if __name__ == '__main__':
   weight_on_planets()
