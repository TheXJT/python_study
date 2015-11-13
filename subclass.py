class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

if __name__=='__main__':
    dog=Dog()
    print(isinstance(dog,Dog))
    print(isinstance(dog,Animal))
    b=Animal()
    print(isinstance(b,Animal))
    print(isinstance(b,Dog))
    #dog.run()
    cat=Cat()
    #cat.run()
    print('========')
    run_twice(b)
    print('========')
    run_twice(dog)
