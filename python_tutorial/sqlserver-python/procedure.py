
from connect import create_connection
def count_customer_by_email_domain(domain: str) -> int:
    # Connect to the SQL Server
    conn = create_connection()
    if conn is None:
        return 0

    # Call the stored procedure
    with (conn, conn.cursor() as cursor):
        cursor.callproc('CountCustomerByEmailDomain', (domain, 0))
        row = cursor.fetchone()
        return row[0] if row else 0