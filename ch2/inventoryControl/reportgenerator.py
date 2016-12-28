import datastorage

def generate_inventory_report():
	""" generate list of products x locations
		based on returns from datastorage functions for
			products()
			locations()
		and then examining if any inventory is actually there. . .
	"""
	#print(datastorage.products())
	#print(datastorage.locations())
	print("stored")
	print(datastorage.items())
	print("stored")
	product_names = {}
	for product_code, name, desired_number in datastorage.products():
		product_names[product_code] = name

	location_names = {}
	for location_code, name in datastorage.locations():
		location_names[location_code] = name

	grouped_items = {}
	for product_code, location_code in datastorage.items(): #actual inventory
		if product_code not in grouped_items:
			grouped_items[product_code] = {}

		if location_code not in grouped_items[product_code]:
			grouped_items[product_code][location_code] = 1
		else:
			grouped_items[product_code][location_code] += 1

	report = []
	report.append("Inventory Report")
	report.append("")

	for product_code in sorted(grouped_items.keys()):
		product_name = product_names[product_code]
		report.append("inventory: {} - {}".format(product_code, product_name))
		report.append("")

	for location_code in sorted(grouped_items[product_code].keys()):
		location_name = location_names[location_code]
		num_items = grouped_items[product_code][location_code]
		report.append("   {} at {} - {}".format(num_items, location_code, location_name))
		report.append("")
	return report

def generate_reorder_report():
	product_names = {}
	desired_numbers = {}

	for product_code,name,desired_number in datastorage.products():
		product_names[product_code] = name
		desired_numbers[product_code] = desired_number

	num_in_inventory = {}
	for product_code,location_code in datastorage.items():
		if product_code in num_in_inventory:
			num_in_inventory[product_code] += 1
		else:
			num_in_inventory[product_code] = 1

	report = []
	report.append = "Reorder Report"
	report.append("")

	for product_code in sorted(product_names.key()):
		desired_number = desired_numbers[product_code]
		current_number = num_in_inventory.get(product_code,0)
		if current_number < desired_number:
			product_name = product_names[product_code]
			num_to_reorder = desired_number - current_number
			report.append(" Re-order {} of P{ - {}".format(num_to_reorder, product_code, product_name))
	report.append("")
	return report











