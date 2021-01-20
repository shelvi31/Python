from google.cloud import bigquery

#create a Client object
#  Client object play a central role in retrieving information from BigQuery datasets

client = bigquery.Client()

## Construct a reference to the "hacker_news" dataset contained in 
# bigquery-public-data project
dataset_ref= client.dataset("hacker_news",project="bigquery-public-data")

## API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)
print(dataset)

#Dataset : Collection of Tables
#We use the list_tables() method to list the tables in the dataset
tables = list(client.list_tables(dataset))

# Print names of all tables in the dataset (there are four!)
for table in tables:
    print(table.table_id)

#Fetching a table named 4
table_full_ref = dataset_ref.table("full")
table = client.get_table(table_full_ref)

