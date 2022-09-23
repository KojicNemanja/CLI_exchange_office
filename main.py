from currency import exchange
import errors
import options

while(True):
    try:
        option = options.get().lower()
        if option == '1':
            exchange()
        if option == 'q':
            print("Quit")
            break
    except ValueError as ex:
        print("Quantity value isn't valid!")
    except Exception as ex:
        print(ex)
