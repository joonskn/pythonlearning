# 클래스 변수와 인스턴스 변수의 차이 예제

class Dog:
    # 클래스 변수: 모든 인스턴스가 공유
    species = "Canis familiaris"

    def __init__(self, name, age):
        # 인스턴스 변수: 각 인스턴스마다 별도
        self.name = name
        self.age = age

# 인스턴스 생성
buddy = Dog("Buddy", 3)
charlie = Dog("Charlie", 5)

# 인스턴스 변수 출력
print(f"buddy의 이름: {buddy.name}, 나이: {buddy.age}")
print(f"charlie의 이름: {charlie.name}, 나이: {charlie.age}")

# 클래스 변수 출력 (모든 인스턴스에서 동일)
print(f"buddy의 종: {buddy.species}")
print(f"charlie의 종: {charlie.species}")

# 클래스 변수 변경 (클래스 자체에 적용)
Dog.species = "Canis lupus familiaris"
print(f"(변경 후) buddy의 종: {buddy.species}")
print(f"(변경 후) charlie의 종: {charlie.species}")

# 인스턴스 변수 변경 (해당 인스턴스에만 적용)
buddy.name = "Max"
print(f"(이름 변경 후) buddy의 이름: {buddy.name}")
print(f"charlie의 이름: {charlie.name}")