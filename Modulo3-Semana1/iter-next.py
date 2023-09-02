iterable = 'Hello World'
iter_obj = iter(iterable)

# # try:
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #     print(next(iter_obj))
# #   

# # except StopIteration:
# #     print('Deu exception')

# #outra opção
# for i in iter_obj:
#     print(i)

# print('Fora do for')


# #

# exemplo com o While
# valor_string = 'Hello World'
# objeto_iter = iter(valor_string)

# for item in iter_obj:
#     print(item)


while True: 
    try:
        item = next(iter_obj)
        print(item)
    except StopIteration:
        break
