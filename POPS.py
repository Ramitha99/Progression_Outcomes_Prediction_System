
print(" Staff Version With Histogram")
print()


# loop until quit
def continue_or_quit():

    outcomes = 0
    con_tinue = 'y'

    progress_count = 0
    progress_stars = ''
    trailer_count = 0
    trailer_stars = ''
    exclude_count = 0
    exclude_stars = ''
    retriever_count = 0
    retriever_stars = ''

    # continue if yes
    while True:       
        if con_tinue not in ('q', 'Q'):
            outcomes = outcomes + 1  

            # check string type and range
            def valid_number(which="PASS"):
                while True:
                    credit = input('Enter your total {} credits : '.format(which)).strip()
                    if credit.isdigit():
                        credit = int(credit)
                        if 0 <= credit <= 120 and credit % 20 ==0:
                            return credit
                        else:
                            print('Out of range')
                    else:
                        print('Integer required')

        # exit loop    
        else:

            print('-'* 80)
            print('Horizontal Histogram')
            print()
            print ("Progress  ", progress_count, ":", progress_stars)
            print ("Trailer   ", trailer_count, ":", trailer_stars)
            print ("Retriever ", retriever_count, ":", retriever_stars)
            print ("Exclude   ", exclude_count, ":", exclude_stars)
            print()
            print( outcomes,' outcomes in total.')
            print('-'* 80)
            print("Vertical Histogram")
            print()
            print("progress   Trailing   Retriever   Excluded")
            
            while progress_count > 0 or trailer_count > 0 or retriever_count > 0 or exclude_count > 0:
                if progress_count > 0:
                    vp_stars = '*'
                else:
                    vp_stars = ''

                if trailer_count > 0:
                    vt_stars = '*'
                else:
                    vt_stars = '' 

                if retriever_count > 0:
                    vr_stars = '*'
                else:
                    vr_stars =''

                if exclude_count > 0:
                    vx_stars = '*'
                else:
                    vx_stars =''

                progress_count = progress_count - 1
                trailer_count = trailer_count - 1
                retriever_count = retriever_count - 1
                exclude_count = exclude_count -1

                print(f'{vp_stars:^10}{vt_stars:^10}{vr_stars:^10}{vx_stars:^10}')

                print()
               
                

            print()                      
            break
        
            
        # sum must be 120
        while True:
            ca_pass = valid_number("PASS")
            ca_defer = valid_number("DEFER")
            ca_fail = valid_number("FAIL")
            if sum([ca_pass, ca_defer, ca_fail]) == 120:
                break
            print('Total incorrect')


        # volume of credits and progression outcome
        # 1
        if ca_pass == 120 and ca_defer == 0 and ca_fail == 0:
            output = "Progress"
            progress_count = progress_count + 1
            progress_stars = progress_stars + '*'
            print(output)

        # 2 and 3
        elif ca_pass == 100 and 0 <= ca_defer <= 20 and ca_defer % 20 == 0 and 0 <= ca_fail <= 20 and ca_fail % 20 == 0:
            output = "Progress (module trailer)"
            trailer_count  = trailer_count + 1
            trailer_stars = trailer_stars + '*'
            print(output)

        # 4 - 14
        elif 40 <= ca_pass <= 80 and ca_pass % 20 == 0 and 0 <= ca_defer <= 80 and ca_defer % 20 == 0 and 0 <= ca_fail <= 60 and ca_fail % 20 ==0:
            output = "Do not Progress - module retriever"
            retriever_count = retriever_count + 1
            retriever_stars = retriever_stars + '*'
            print(output)

        # 15
        elif ca_pass == 40 and ca_defer == 0 and ca_fail == 80:
            output = "Exclude"
            exclude_count = exclude_count + 1
            exclude_stars = exclude_stars + '*'
            print(output)
            
        # 16 - 19
        elif ca_pass == 20 and 40 <= ca_defer <= 100 and ca_defer % 20 == 0 and 0 <= ca_fail <= 60 and ca_fail % 20 == 0:
            output = "Do not progress - module retriever"
            retriever_count = retriever_count + 1
            retriever_stars = retriever_stars + '*'
            print(output)
            
        # 20 and 21
        elif ca_pass == 20 and 0 <= ca_defer <= 20 and ca_defer % 20 == 0 and 80 <= ca_fail <= 100 and ca_fail % 20 == 0:
            output = "Exclude"
            exclude_count = exclude_count + 1
            exclude_stars = exclude_stars + '*'
            print(output)

        # 22 - 25
        elif ca_pass == 0 and 60 <= ca_defer <= 120 and ca_defer % 20 == 0 and 0 <= ca_fail <= 60 and ca_fail % 20 == 0:
            output = "Do not progress - module retriever"
            retriever_count = retriever_count + 1
            retriever_stars = retriever_stars + '*'
            print(output)

        # 26 - 28
        elif ca_pass == 0 and 0 <= ca_defer <= 40 and ca_defer % 20 == 0 and 80 <= ca_fail <= 120 and ca_fail % 20 == 0:
            output = "Exclude"
            exclude_count = exclude_count + 1
            exclude_stars = exclude_stars + '*'
            print(output)

        print()
   

        # ask for enter again or not
        con_tinue = input ("Would you likr to enter another set of data ?\nEnter 'y' for yes or 'q' to quit and view results : ")
        
        print()
        

        print()

# call the function
continue_or_quit()


print()
