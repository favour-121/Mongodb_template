```
# MongoDB Connection Template

This project provides a professional template for connecting to a MongoDB database using Python and the `pymongo` library. It includes best practices such as configuration management, error handling, and encapsulation within a class.

## Features

- Secure configuration management
- Robust error handling
- Easy-to-use class for managing MongoDB connections
- Logging for monitoring connection status

## Requirements

- Python 3.6 or higher
- `pymongo` library

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/favour-121/mongodb_template.git
   cd mongodb_template
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```sh
   pip install pymongo
   ```

## Configuration

1. **Update the `config.py` file** with your MongoDB URI and database name:
   ```python
   # Configuration file for MongoDB connection

   # MongoDB URI (replace with your actual URI)
   MONGO_URI = "mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority"

   # Database name
   DATABASE_NAME = "your_database_name"
   ```

## Usage

1. **Import and use the `MongoDBConnection` class** in your project:

   ```python
   from db_connection import MongoDBConnection
   import logging

   # Configure logging
   logging.basicConfig(level=logging.INFO)

   # Initialize and connect to MongoDB
   mongo_conn = MongoDBConnection()
   mongo_conn.connect()

   # Get the database instance
   db = mongo_conn.get_database()

   # Perform database operations...
   # Example: Print the list of collections
   print(db.list_collection_names())

   # Close the connection
   mongo_conn.close()
   ```

2. **Run the example script** to see the connection in action:
   ```sh
   python db_connection.py
   ```

## Example

Here's an example usage of the `MongoDBConnection` class to list collections in the database:

```python
from db_connection import MongoDBConnection
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize and connect to MongoDB
mongo_conn = MongoDBConnection()
mongo_conn.connect()

# Get the database instance
db = mongo_conn.get_database()

# Perform database operations...
# Example: Print the list of collections
print(db.list_collection_names())

# Close the connection
mongo_conn.close()
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or support, please contact [l4utechunlimited@gmial.com](mailto:l4utechunlimited@gmial.com).

```
