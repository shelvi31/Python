def prime_numbers(N):
  for D in range(2, N):
    if (D * D > N):          #extra line to make prog fast for gigantic prime numbers
      break                       
    if N % D == 0:                             
      print(N, "is not prime; divisible by", D)
      return
  print(N, "is prime") 

prime_numbers(324635459)

#if N is not prime, one of its divisors is at most sqrt(N)
#A*B == N , If A <= sqrt(N) or B <= sqrt(N), then we are happy: we found a factor of N that is small,
#  like we wanted. But actually these are the only possibilities: otherwise we get the impossible contradiction

N = A*B > sqrt(N)*sqrt(N) = N

