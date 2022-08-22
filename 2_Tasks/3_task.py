# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, x):
#         if x > 0:
#             super().append(x)
#         else:
#             raise NonPositiveError
#
#
# modified_list = PositiveList()
#
# while len(modified_list) < 6:
#     try:
#         modified_list.append(int(input()))
#         print(f'{modified_list[-1]} has ben successfully added')
#     except NonPositiveError:
#         print('Not positive number, try again.')

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError('Not positive number')


modified_list = PositiveList()

while True:
    try:
        modified_list.append(int(input()))
    except NonPositiveError:
        print('Try again')
