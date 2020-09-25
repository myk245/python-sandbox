lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''

lovely_loveseat_price = 254.00

stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''

stylish_settee_price = 180.50

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''

luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0

customer_one_itemization = ''

customer_one_total += lovely_loveseat_price

customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price

customer_one_itemization += ' ' + luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print('Customer One Items:')

print(customer_one_itemization)

print('Customer One Total:')

print(customer_one_total)

# functions with parameters
def mult_x_add_y(number, x, y):
  print(number*x + y)

mult_x_add_y(5, 2, 3)

mult_x_add_y(1, 3, 1)


# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called "+title +
        " with " + str(row_count) + " rows")


# Call create_spreadsheet() below with the required arguments:
create_spreadsheet(title="Applications", row_count=10)


# mutliple return values
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin

  return low_limit, high_limit


low, high = get_boundaries(100, 20)

print(low)
print(high)


def f_to_c(f_temp):
  c_temp = ((f_temp) - 32) * 5/9
  return c_temp


f100_in_celsius = f_to_c(100)

print(f100_in_celsius)


def c_to_f(c_temp):
  f_temp = ((c_temp) * (9/5)) + 32
  return f_temp


c0_in_fahrenheit = c_to_f(0)

print(c0_in_fahrenheit)


def get_force(mass, acceleration):
  return mass * acceleration


train_force = get_force(train_mass, train_acceleration)

print(train_force)

print('The GE train supplies ' + str(train_force) + ' Newtons of force.')


def get_energy(mass, c=3*10**8):
  return mass*c**2


bomb_energy = get_energy(bomb_mass)

print(bomb_energy)

print('A 1kg bomb supplies ' + str(bomb_energy) + ' Joules.')
