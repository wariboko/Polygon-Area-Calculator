class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if (self.width or self.height) >= 50:
      return "Too big for picture."
    else:
      return ("*" * self.width + "\n") * self.height

  def get_amount_inside(self, square):
    new_width = self.width // square.width
    new_height = self.height // square.height
    return new_width * new_height

  def __str__(self):
    return 'Rectangle(width=' + str(self.width) +', height=' + str(self.height) + ')'


class Square(Rectangle):

  #We could use a Super() __init__ also
  def __init__(self,length):
    self.width = length
    self.height = length

  def set_side (self, newlength):
    self.width = newlength
    self.height = newlength

  def set_width (self, newwidth):
    self.width = newwidth
    self.height = newwidth

  def set_height (self, newheight):
    self.height = newheight
    self.width = newheight

  def __str__(self):
    return 'Square(side=' + str(self.width) + ')'
