#1. Python Sets Adventure
#Task 1: Flight Route Comparison
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_routes = our_routes.intersection(competitor_routes)
print("Destinations both airlines fly to:", shared_routes)

our_unique_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", our_unique_routes)

unique_routes = our_routes.symmetric_difference(competitor_routes)
print("Destinations that neither airline shares:", unique_routes)

#2. Set Operations in Data Analysis
#Task 1: Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

unique_customer_ids = set(customer_ids)
print("Unique customer IDs:", unique_customer_ids)
