import pandas as pd
import tabulate as tab

customers = pd.DataFrame([], columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
orders = pd.DataFrame([], columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

customers_data = pd.DataFrame([
    {'id':1, 'name':'Joe'},
    {'id':2, 'name':'Henry'},
    {'id':3, 'name':'Sam'},
    {'id':4, 'name':'Max'},
])

orders_data = pd.DataFrame([
    {'id':1, 'customerId':3},
    {'id':2, 'customerId':1},
])

customers = pd.concat([customers, customers_data], ignore_index=True)
orders = pd.concat([orders, orders_data], ignore_index=True)
customers.set_index('id', inplace=True)
orders.set_index('id', inplace=True)
 
print(tab.tabulate(customers, headers='keys', tablefmt='psql'))
print(tab.tabulate(orders, headers='keys', tablefmt='psql'))

# Find customers who have not placed orders
# Left outer join
customers_with_order = customers.merge(orders, how='left', left_on='id', right_on='customerId', indicator='customers')
customers_without_order= customers_with_order.loc[customers_with_order['customers'] == 'left_only', ['name']]

customers_without_order.rename(columns={'name': 'customers'}, inplace=True)
print(tab.tabulate(customers_without_order, headers='keys', tablefmt='psql'))