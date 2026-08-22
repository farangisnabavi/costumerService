import orders
import products
import users
import reports

flag = True
while flag:
    print("1.orders\n2.products\n3.reports\n4.users")
    whichPart = input("Please enter which part to use: ")
    if whichPart == "1":
        print("1.add order\n2.totals\n3.delete orders\n4.orders per costumer")
        whichOrderFunction = input("Please enter which order option to use: ")
        if whichOrderFunction == "1":
            orders.add_order()
        elif whichOrderFunction == "2":
            orders.print_total()
        elif whichOrderFunction == "3":
            orders.delete_order()
        elif whichOrderFunction == "4":
            orders.orders_per_costumer()
        else:
            print("out of range. try again.")
        whichPart = ""
    elif whichPart == "2":
        print("1.add products\n2.remove products\n3.update products\n4.search products by name\n5.search products by category\n6.show products\n7.sort by price\n8.sort by stock")
        whichProductsFunction = input("Please enter which order option to use: ")
        if whichProductsFunction == "1":
            products.add_products()
        elif whichProductsFunction == "2":
            products.remove_products()
        elif whichProductsFunction == "3":
            products.edit_products()
        elif whichProductsFunction == "4":
            products.search_products_by_name()
        elif whichProductsFunction == "5":
            products.search_products_by_category()
        elif whichProductsFunction == "6":
            products.show_products()
        elif whichProductsFunction == "7":
            products.sort_by_price()
        elif whichProductsFunction == "8":
            products.sort_by_stock()
        else:
            print("out of range. try again.")
        whichPart = ""
    elif whichPart == "3":
        print("1.stock worth\n2.count stock\n3.count costumers\n4.vip users count\n5.orders count\n6.unavailable products\n7.products that have less than five\n8.average price\n9.count by category\n10.count per user")
        whichReportFunction = input("Please enter which report option to use: ")
        if whichReportFunction == "1":
            reports.stock_worth()
        elif whichReportFunction == "2":
            reports.all_stock()
        elif whichReportFunction == "3":
            reports.user_count()
        elif whichReportFunction == "4":
            reports.vip_users_count()
        elif whichReportFunction == "5":
            reports.count_orders()
        elif whichReportFunction == "6":
            reports.count_unavailable()
        elif whichReportFunction == "7":
            reports.less_than_5()
        elif whichReportFunction == "8":
            reports.average_price()
        elif whichReportFunction == "9":
            reports.count_by_category()
        elif whichReportFunction == "10":
            reports.count_orders_per_user()
        else:
            print("out of range. try again.")
        whichPart = ""
    elif whichPart == "4":
        print("1.add costumer\n2.remove costumer\n3.edit costumer\n4.show costumers\n5.search costumers")
        whichCostumerFunction = input("Please enter which costumer option to use: ")
        if whichCostumerFunction == "1":
            users.add_costumer()
        elif whichCostumerFunction == "2":
            users.remove_costumers()
        elif whichCostumerFunction == "3":
            users.edit_costumers()
        elif whichCostumerFunction == "4":
            users.show_costumers()
        elif whichCostumerFunction == "5":
            users.search_costumers()
        else:
            print("out of range. try again.")
        whichPart = ""
    else:
        print("out of range. try again.")
    exit = input("Do you want to exit?(y/n): ")
    if exit == "y":
        flag = False