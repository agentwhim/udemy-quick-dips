import xml.etree.ElementTree as ET


cust_tree = ET.parse('customers.xml')
cust_root = cust_tree.getroot()
for cust in cust_root:
    average_sales = int(cust.find('average_annual_sales_eur').text)
    company_name = cust.find('company').text
    contact_name = cust.find('contact').text
    contact_phone = cust.find('phone').text
    if average_sales < 35000:
        print(f'{contact_name:20s}{contact_phone:20s}({company_name})')
