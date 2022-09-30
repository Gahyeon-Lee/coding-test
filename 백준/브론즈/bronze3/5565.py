# 영수증
# 첫째 줄에 10권의 총 가격이 주어진다. 
# 둘째 줄부터 9개 줄에는 가격을 읽을 수 있는 책 9권의 가격이 주어진다. 책의 가격은 10,000이하인 양의 정수이다.
# 첫째 줄에 가격을 읽을 수 없는 책의 가격을 출력한다.

books = []
total_price = int(input())

for _ in range(9):
    price = int(input())
    books.append(price) 

print(total_price - sum(books))