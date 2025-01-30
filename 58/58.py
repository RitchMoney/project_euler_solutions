def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n Â± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
#    print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

corner_itter = 0
side_length = 3
current_corner = 1 # must start at 1 to include 1 that is in the center
prime_corners = 0
corner_count = 1
ratio = 1

#iterate over all 4 sides grabbing each corner and checking if it is prime.
while corner_itter <= 4:
    print("current ratio is: ", ratio, "current side length is: ", side_length)
    new_corner = current_corner + side_length - 1
    if is_prime(new_corner) :
        prime_corners += 1

    corner_itter += 1
    corner_count += 1
    current_corner = new_corner

    # update ratio only after each full set of sides is done
    if corner_itter == 4:
        ratio = prime_corners / corner_count

        # break while loop once goal ratio is met
        if ratio < 0.1:
            break

        # if goal is not met reset itteration and update side length
        corner_itter = 0
        side_length += 2

print("final side lenght = ", side_length)
print("final ratio = ", ratio)