x = int(input ('введите х '))
y = int(input ('введите y '))
if x > 0 and y > 0:
    print ('1')
elif x < 0 and y > 0:
    print ('2')
elif x < 0 and y < 0:
    print ('3')
elif x > 0 and y < 0:
    print ('4')
elif x == 0 and y < 0:
    print ('х и y не должены быть равены нулю. Попробуйте еще раз')
elif x == 0 and y > 0:
    print ('х и y не должены быть равены нулю. Попробуйте еще раз')
elif x > 0 and y == 0:
    print ('х и y не должены быть равены нулю. Попробуйте еще раз')
elif x < 0 and y == 0:
    print ('х и y не должены быть равены нулю. Попробуйте еще раз')
else:
    print ('х и y не должены быть равены нулю. Попробуйте еще раз')
    