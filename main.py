#!/usr/bin/env python3
# -*- coding: utf-8 -*-
      
# Author: Jenny Doan and Mara White
# Program Description: Keep track of and update inventory for a baking supply shop 
#                      to print invoices for customer transactions using classes


# import classes
import inventory
import transactionItem


# function to read file
def process_inventory(file): 
    # open file to read
    inventory_file = open(file, 'r')
    # read the first line
    line = inventory_file.readline()
    # create empty dictionary to store instances
    invDict = {}
    
    # for the length of file do this: 
    while line != '': 
        line = line.rstrip('\n')
        # initialize temporary list for attributes
        att_list= []
        # for loop is what we are doing to each individual line
        for i in range(4): # range is 4 because there are 4 attributes for each item
            att_list.append(line) # adds the line to the list
            line = inventory_file.readline().rstrip('\n')
        # create instances using the attributes
        instance = inventory.Inventory(att_list[0], att_list[1], att_list[2], att_list[3])
        # define key for dictionary
        key = att_list[0]
        
        # assign instances to dictionary keys
        invDict[key] = instance
    
    # close the file
    inventory_file.close()

    # return the dictionary of instances from inventory.txt
    return(invDict)


# function to create and print menu using a dicitionary as a parameter
def print_inventory(dictionary): 
    # print empty line before and headings using field widths to space appropriately
    print()
    print(f'{"ID":<9} {"Item":<27} {"Price":<12} {"Qty Available":<1}')
    # for each item_id in the dictionary print the instance
    for key in dictionary: 
        print(dictionary[key])
    print('Enter 0 when finished.') 



# ask the user for the item id of the item they wish to buy/return
def get_item_id(dictionary): 
    flag = True
    
    # loop to repeat until valid item id is given
    while flag: 
        item_id = input('Please input the item id you wish to purchase/return: ')
        
        # condition for the input being valid (if in the dict or 0)
        if item_id in dictionary or item_id == '0': 
            flag = False
       
        else: 
            print('Input was invalid.')
            flag = True # repeats       
    return item_id


# write the new inventory to a new file ('UpdatedInventory.txt')
def write_updated_inventory(new_inventory, file): 
    # open file to write (w)
    output_file = open(file,'w')
   
    # for each instance in the dictionary (new_inventory) add these values
    for i in new_inventory:
        output_file.write(str(new_inventory[i].get_id()) + ('\n'))
        output_file.write(str(new_inventory[i].get_name()) + ('\n'))
        output_file.write(str(new_inventory[i].get_stock()) + ('\n'))
        output_file.write(str(new_inventory[i].get_price()) + ('\n'))
    
    # close new file
    output_file.close()


# invoice is created using cart- a list of transactions
def print_invoice(cart): 

    # initialize total cost to 0
    total_cost = 0
    
    # print heading for invoice
    print()
    print(f'{"ID":<9} {"Item":<27} {"Price":<18} {"Qty":<8} {"Total":<8}')
    
    # for each item in the cart calculate the total cost
    for i in range(len(cart)): 
        cost = cart[i].calc_cost()
        total_cost = total_cost + cost
    
    # print the items on the receipt part- using instance to get the price
    for i in cart: 
        print(i, format(i.calc_cost(), '.2f'), sep = '')
    
    # print the summary items at the bottom
    print()
    print(f'Price: ${total_cost:.2f}')
    tax = total_cost*.085
    print(f'Tax: ${tax:.2f}')
    total = total_cost + tax
    print(f'Total: ${total:.2f}')



def main(): 
    # initialize item counter as 0
    item_counter = 0
    # create dictionary using process-inventory function
    invDict = process_inventory('Inventory.txt')
    # create menu
    print_inventory(invDict)
    # get item_id
    item_id = get_item_id(invDict)
    # create empty cart to put items in
    cart = []
    purchase = True
    
    # everything that should be done while the item id is not 0
    while item_id != '0':
        
        # empty dictionary that will be used to redisplay menu with changed values
        new_inventory = {}
        # quantity user enters
        qty = int(input('Please enter the desired quantity (negative quantity for return): '))
        
        # create instances of the inventory and transaction class
        quantity = invDict[item_id].get_stock()
        name = invDict[item_id].get_name()
        price = invDict[item_id].get_price()
        inventory_instance = inventory.Inventory(item_id, name, quantity, price)
        transaction_instance = transactionItem.TransactionItem(item_id, name, quantity, price)
        
        # do restock with inputted quantity
        restock = inventory_instance.restock(qty)
        
        # if you are restocking add item to invoice and set new quantity
        if restock == True: 
            old_stock = inventory_instance.get_stock()
            new_stock = transaction_instance.set_qty(old_stock)
            item_counter += 1
            
        else: 
            # if you are not restocking you are purchasing
            purchase = inventory_instance.purchase(qty)
            # if you are purchasing and the asked amt can be met set new stock
            if purchase == True: 
                new_stock = inventory_instance.get_stock()
                item_counter += 1
                
                # if you try to overdraw the inventory print this message
            elif purchase == False:
                print()
                print('Sorry, we do not have enough stock.')
                new_stock = inventory_instance.get_stock()
            
        
        
        # getting info from old dictionary and creating instance for transaction
        name = invDict[item_id].get_name()
        price = invDict[item_id].get_price()
                
                #create dictionary that displays on menu
        instance = transactionItem.TransactionItem(item_id, name, price, new_stock)
                
         
          # creating an instance of the transaction class      
        transaction = transactionItem.TransactionItem(item_id, name, price, qty)
        # add the transaction to the list
        cart.append(transaction)
        # if you overdraft- remove the transaction from the invoice
        if purchase == False: 
            cart.remove(transaction)
            
                
        # copying old dictionary to make new_inventory
        new_inventory = invDict
        new_inventory[item_id] = instance
        

        
        print_inventory(new_inventory)
        item_id = get_item_id(new_inventory)
        write_updated_inventory(new_inventory, 'UpdatedInventory.txt') 

    # if no purchases or returns are made
    if item_counter == 0: 
        print('Thank you for visiting!')
    else: 
        print_invoice(cart)

         
main()

