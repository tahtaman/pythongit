'''
'''
while 1:
    reply_distantion = input('input distantion(km) - ')
    reply_time = input('input time(min) - ')
    break

#formula for different speed
def speed(a,b):
    '''
    a - distantion
    b - time
    '''
    sa = int(a)
    sb = int(b)
    sb = sb/60
    return sa/sb

total = speed(reply_distantion, reply_time)
print(total, ' km/h')
