# Fill out the main function below so that you handle two exceptions that may
# be raised by your call to some_function. If this function raises a
# ValueError, print “value error happening now”; if this function raises a
# UnicodeError, print “unicode error happening now”. Make sure your code can
# handle both errors. (Note: since some_function isn’t filled out, neither
# exception will be raised when you run the program.)


#  def some_function():
#      # Imagine code that could raise value or unicode errors
#      pass
#
#  def main():
#      # Put your exception handling code below
#      some_function()
#
#  if __name__ == "__main__":
#      main()


def some_function():
    # Imagine code that could raise value or unicode errors
    pass
    # raise ValueError
    # raise UnicodeError


def main():
    # Put your exception handling code below
    # Note: since UnicodeError is a subclass of ValueError, it probably needs
    #       to appear first
    try:
        some_function()
    except UnicodeError:
        print('unicode error happening now')
    except ValueError:
        print('value error happening now')


if __name__ == "__main__":
    main()
