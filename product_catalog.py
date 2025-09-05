from product_data import products
# TODO: Step 1 - Print out the products to see the data that you are working with.
print("Product Catalog Preview:")
for p in products[:3]: #printing jus tthe first 3 products to preview
    print(p)


# TODO: Step 2 - Create a list called customer_preferences and store the user preference in this list.
customer_preferences = []

response = ""
while response != "N":
    print("Input a preference:")
    preference = input().strip().lower()
    # Add the customer preference to the list
    if preference:
        customer_preferences.append(preference)

    response = input("Do you want to add another preference? (Y/N): ").upper()
  

# TODO: Step 3 - Convert customer_preferences list to set to eliminate duplicates.
customer_preferences = set(customer_preferences)


# TODO: Step 4 - Convert the product tags to sets in order to allow for faster comparisons.
converted_products = []
for product in products:
    converted_products.append({
        "name": product["name"],
        "tags": set(product["tags"])
    })



# TODO: Step 5 - Write a function to calculate the number of matching tags
def count_matches(product_tags, customer_tags):
    '''
    Args:
        product_tags (set): A set of tags associated with a product.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        int: The number of matching tags between the product and customer.
    '''
    return len(product_tags.intersection(customer_tags))




# TODO: Step 6 - Write a function that loops over all products and returns a sorted list of matches
def recommend_products(products, customer_tags):
    '''
    Args:
        products (list): A list of product dictionaries.
        customer_tags (set): A set of tags associated with the customer.
    Returns:
        list: A list of products containing product names and their match counts.
    '''
    recommendations = []
    for product in products:
        matches = count_matches(product["tags"], customer_tags)
        if matches > 0:
            recommendations.append((product["name"], matches))
    #sort recommendations by match count
    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations



# TODO: Step 7 - Call your function and print the results
results = recommend_products(converted_products, customer_preferences)

print("\nRecommend Products:")
for name, matches in results:
    print(f"- {name} ({matches} match(es))")




# DESIGN MEMO (write below in a comment):
# 1. What core operations did you use (e.g., intersections, loops)? Why?
#   - I used set intersections to compare product tags with customer preferences. This was to ensure efficient overlap checking (0(1) average per element)
#   - I also used loops to iterate through products and collect match counts. 
#   - Finally, I used sorting to order recommendations by number of matches
# 2. How might this code change if you had 1000+ products?
#   - If I had 1000+ products this approach would still work but it could be optimized by pre-indexing tags into a dictionary, 
#    so that I would only check relevent items
#   - For much larger catalogs, storing products in a database with indexes would imrpove performance, and more advanced techniques like 
#     machine learning could enhance personalization. 