def write_to_file():
    with open('text_files/CustomerUserManager.txt') as customer_manager:
        with open('text_files/info_from_CustomerUserManager.txt', 'w') as write_to_customer_manager:
            i = 0
            for line in customer_manager:
                i += 1
                write_to_customer_manager.writelines((str(i) + ' ' + line.rstrip()) +'\n')

def write_with_print():
    with open('text_files/SubscriberUserManager.txt') as subscriber_manager:
        with open('text_files/info_from_SubscriberUserManager.txt', 'w') as write_to_subscriber_manager:
            i = 0
            for line in subscriber_manager:
                i += 1
                print((str(i) + ' ' + line.rstrip()), file=write_to_subscriber_manager)



if __name__== "__main__":
    write_to_file()
    write_with_print()
