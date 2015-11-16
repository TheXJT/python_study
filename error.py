import logging
try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
print('============')
try:
    #foo()
    print('test') 
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
print('============')
print('============')
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
#        print('Error:',e)
#    finally:
#        print('finally...')
main()
print('END')
