# precendence
print(3+8*5)
print(3+8-5)
print(3/8*5)
# We known these are basics 'BODMAS'
name = "Bittu"
age = 20
fun1 = name == "Bittu" and name == "Shivam" or age <= 18
print(fun1)
fun2 = name == "Bittu" or name == "Shivam" and age <= 18
print(fun2)

# # Here perecedency comes in to the picture
# # python operate "and" 1st then "or", because of python follow perecedency order.
# '''
# |   Priority   | Operator             | Meaning                                 | Example          |
#      ------    | -------------------- | --------------------------------------- | ---------------- |
# |      1️⃣      | `()`                 | Parentheses                             | `(2 + 3) * 4`    |
# |      2️⃣      | `**`                 | Exponent / Power                        | `2 ** 3`         |
# |      3️⃣      | `+x`, `-x`, `~x`     | Unary plus, minus, NOT                  | `-5`             |
# |      4️⃣      | `*`, `/`, `//`, `%`  | Multiply, Divide, Floor Divide, Modulus | `10 * 2`         |
# |      5️⃣      | `+`, `-`             | Addition, Subtraction                   | `10 + 2`         |
# |      6️⃣      | `<<`, `>>`           | Bitwise shift                           | `4 << 1`         |
# |      7️⃣      | `&`                  | Bitwise AND                             | `5 & 3`          |
# |      8️⃣      | `^`                  | Bitwise XOR                             | `5 ^ 3`          |
# |      9️⃣      | `\|`                 | Bitwise OR                              | `5 \| 3`         |
# |      🔟      | `<`, `<=`, `>`, `>=` | Comparison                              | `5 > 3`          |
# |     1️⃣1️⃣     |  `==`, `!=`           | Equality                               | `5 == 5`         |
# |     1️⃣2️⃣     |  `is`, `is not`       | Identity                               | `a is b`         |
# |     1️⃣3️⃣     |  `in`, `not in`       | Membership                             | `x in list`      |
# |     1️⃣4️⃣     |  `not`                | Logical NOT                            | `not True`       |
# |     1️⃣5️⃣     |  `and`                | Logical AND                            | `True and False` |
# |     1️⃣6️⃣     |  `or`                 | Logical OR                             | `True or False`  |
# '''



print((4-8)*5)
print((4+8)/5)
print(5-7*5)
print(2*3*6)
print(10/10-10)
print(10*10/10)

# Associativity
## classification of operators based on the number of oprands

#Unary
print(-55)
print(not True)

#Binary
print(45-76)
print(True and False)
print(True or False)

### Ternary ........
