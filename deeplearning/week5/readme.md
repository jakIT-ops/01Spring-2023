Жинг анх санамсаргүй байдлаар олгоно.

```py
np.random.seed(1)

weights = 2 * np.random.random((3,1)) - 1

print("Random initilized weights: ")
print(weights)
```

## Training - Сургалтын алхамууд:

1. Оролтуудын утгыг сигмоид идэвхжүүлэх функцэд дамжуулан гаралтыг олно.
2. Алдааг тооцоолно. Ингэхдээ гаралтуудын ялгаврыг олно.

error = y_true – y_predict

1. Алдааны утгаас хамаарч жингийн утгыг тохируулж өгнө.
2. Уг процессыг 10000 удаа давтана.

### Жин тохируулах

adjustWeights = error * input * f'(output)

error = y_trues - y_predict
input = 1 or 0 
f'(output) = x*(1-x)


