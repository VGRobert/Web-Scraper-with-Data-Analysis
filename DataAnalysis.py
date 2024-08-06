import pandas as pd  # To handle data
import matplotlib.pyplot as plt  # To create visualizations
import seaborn as sns  # For more advanced visualizations

# Load the scraped data from the CSV file
df = pd.read_csv('amazon_products.csv')

# Clean the data
# Remove any rows with missing prices
df = df.dropna(subset=['Price'])

# Convert prices to float
df['Price'] = df['Price'].astype(float)

# Convert ratings to float (strip 'out of 5 stars')
df['Rating'] = df['Rating'].str.extract(r'(\d+\.\d+)').astype(float)  # Use raw string (r'') to avoid the warning

# Remove commas from reviews and handle NaN values
df['Reviews'] = df['Reviews'].str.replace(',', '')

# Fill NaN values in Reviews with 0 before converting to integer
df['Reviews'] = df['Reviews'].fillna(0).astype(int)

# Perform basic analysis
# Calculate average price
avg_price = df['Price'].mean()
print(f'Average Price: ${avg_price:.2f}')

# Calculate average rating
avg_rating = df['Rating'].mean()
print(f'Average Rating: {avg_rating:.2f}')

# Create visualizations
# Price distribution histogram
plt.figure(figsize=(10, 6))
df['Price'].hist(bins=20)
plt.title('Price Distribution')
plt.xlabel('Price ($)')
plt.ylabel('Number of Products')
plt.grid(False)
plt.show()

# Scatter plot of Price vs. Rating
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Rating', size='Reviews', data=df, sizes=(20, 200))
plt.title('Price vs. Rating')
plt.xlabel('Price ($)')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_amazon_products.csv', index=False)

print("Data analysis completed. Cleaned data saved to 'cleaned_amazon_products.csv'.")
