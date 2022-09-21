def calculate_isbn_checksum(isbn):
    total = 0
    index = len(isbn)-1
    for n in range(2,11,1):
        total += n * int(isbn[index])
        index -=1

    checkSum=0
    for i in range(11):
        if (total+i) % 11 ==0:
            checkSum = i
    print('checksum :',checkSum)

    def is_isbn (check_isbn):
        if check_isbn == checkSum :
            print('True')
            print('ISBN is  valid (Checksum  match)')
        else:
            print('false')
            print('ISBN is not valid (Checksum did not match)')
    check_isbn = int(input('Enter Your CheckSum :'))
    is_isbn(check_isbn)

def check_box_book_size ():
    large_box = 20 * 20 * 4
    medium_box = 15 * 15 * 3
    small_box = 10 * 10 * 2
    book_w = int(input('Book Width :'))
    book_d = int(input('Book depth :'))
    book_h = int(input('Book  height :'))
    book_size = book_w * book_d * book_h

    print('Large Box = ',large_box)
    print('Medium Box = ', medium_box)
    print('Small Box = ', small_box)
    print('Book Size = ', book_size)

def get_smallest_box_size_for_book():

    large_box = 20 * 20 * 4
    medium_box = 15 * 15 * 3
    small_box = 10 * 10 * 2
    book_w = int(input('Book Width :'))
    book_d = int(input('Book depth :'))
    book_h = int(input('Book  height :'))
    book_size = book_w * book_d * book_h

    if  book_size == large_box or book_size > medium_box :
        print('Get Large Box For Book ')
    elif book_size == medium_box or book_size > small_box :
        print('Get Medium Box For Book')
    else:
        print('Get Small Box For Book  ')

def get_num_books_for_box():
    large_box = 20 * 20 * 4
    medium_box = 15 * 15 * 3
    small_box = 10 * 10 * 2
    book_w = int(input('Book Width :'))
    book_d = int(input('Book depth :'))
    book_h = int(input('Book  height :'))
    book_size = book_w * book_d * book_h

    result1 = int(small_box / book_size)
    print(result1, ' are books enter in small box')

    result2 = int(medium_box / book_size)
    print(result2, ' are books enter in medium box')

    result3 = int(large_box / book_size)
    print(result3, ' are books enter in large box')


print('Welcome to the shipment calculation system')
def choice ():
    print('''    1) Check ISBN
    2) Check box/book size
    3) Get smallest box size for book
    4) Get num equally-sized books per box\n''')
    choose = int(input('Enter Choice (1-4) : '))

    if choose == 1:
        print('Check ISBN')
        isbn = input('Enter 9 Digit : ')
        len_check = len(isbn)
        if len_check == 9:
            print('Enter Between 1 - 9 Number ')
        elif len_check < 9 or len_check >= 10:
            print('Incorrect Number ')
            choice()
        calculate_isbn_checksum(isbn)

    elif choose == 2:
        print('Book/Box size')
        check_box_book_size()

    elif choose == 3:
        print('Get smallest box size for book')
        get_smallest_box_size_for_book()

    elif choose == 4:
        print('Get num equally-sized books per box')
        get_num_books_for_box()

    elif choose == 0:
        print('Invalid Choose')

    elif choose > 4 :
        print('Invalid Choose')

    choose2 = input('Do you continue y/n : ')
    if choose2 =='y' and 'Y':
        choice()
    elif choose2 == 'n' and 'Y':
        print('Thank you')
    else:
        pass
choice()
















