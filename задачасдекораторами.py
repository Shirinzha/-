# РАДУГА
def color(func):
  def external():
    print('red')
    func()
    print('red')
  return external

def inside(func):
  def external():
    print(' yellow')
    func()    
    print(' yellow')
  return external

@color
@inside
def rainbow(color = '  blue'):
  print(color)

# color = color(inside(rainbow))
# color()

rainbow()