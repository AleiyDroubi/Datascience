def main():
    total_sales=float(input("Enter total sales : "))
    print("county tax is:",get_county_tax(total_sales))
    print("state tax is:",get_state_tax(total_sales))
    print("total taxes is:",get_total_tax(total_sales))

def get_county_tax(total_sales):
    global county_tax
    county_tax =total_sales*.2
    return county_tax
   
def get_state_tax(total_sales):
    global state_tax
    state_tax=(total_sales*.4)
    return state_tax

def get_total_tax(total_sales):
    total_tax=(county_tax+state_tax)
    return total_tax
main()
