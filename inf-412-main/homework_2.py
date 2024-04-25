# дз 2
# возвести каждый 4-й элемент в квадрат

a = [4, 6, 5, 9, 88, 11, 35, 79, 168, 11, 2, 16, 22, 8, 19, 50]
b = a.copy()

for i in range(len(a)):
    a[i] = a[i] **2

c = list(range(3,len(a),4))

for i in c:
    b[i] = a[i]

print('old a',a)
print('new a',b)

# реализовать функцию, которая по букве увеличивает ее в строке и отдает новую строку

s = 'lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. euismod faucibus rutrum sollicitudin ex purus faucibus aliquam ipsum tellus etiam blandit dictumst. vestibulum vel lorem lectus finibus eros tempus laoreet condimentum porttitor taciti nec hac. faucibus quam feugiat mauris venenatis auctor aliquet quis interdum consectetur convallis proin. proin dui condimentum vitae conubia nec justo at mollis aliquam ad vitae. luctus ante donec dictum ultrices ligula volutpat eget dolor tortor eros finibus habitant habitant. curabitur quis cras sapien dapibus phasellus. maximus metus taciti vestibulum litora dolor metus eu fames libero volutpat nullam lacinia condimentum nibh. amet aliquet semper at nullam cubilia erat lorem eros morbi fringilla fusce nullam. non suscipit vel ut consequat justo nisl consectetur taciti ipsum enim suscipit vehicula. metus consequat vulputate enim lacus habitant. ullamcorper massa maecenas arcu ultricies luctus sociosqu placerat sodales. pretium donec enim ut mauris eget maximus. quam cras conubia congue erat maecenas. Netus lacinia auctor id venenatis tellus blandit felis mattis. nostra vestibulum lacinia rhoncus metus suspendisse volutpat curae proin. convallis leo porta posuere mi proin suspendisse quisque conubia non duis mollis. pharetra aliquet risus eleifend dolor velit viverra class consequat scelerisque feugiat eu ornare. lobortis nisl scelerisque sapien placerat ultrices feugiat venenatis habitant cras et quisque neque ex. sem lacinia purus dui cursus ullamcorper venenatis massa faucibus vivamus donec pulvinar dictum lacinia. etiam mi volutpat phasellus inceptos luctus primis duis orci ex porta. feugiat lacinia urna cubilia fusce odio habitasse ullamcorper sit adipiscing erat pharetra.'

def upp(s, letter):
     s1 = ''
     for i in s:
        if i == letter:
            s1 = s1 + letter.upper()
        else:
            s1 = s1 + i
     print(s1)

letter = input('Букву введи: ')

upp(s, letter)
    