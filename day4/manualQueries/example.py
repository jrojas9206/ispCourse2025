import sys 
import argparse
import psycopg2

dbURI = "postgresql://juan_pablo:Hiiro9206.23@localhost/isp2025"

# conn = psycopg2.connect(
#     dbname="isp2025",
#     user="juan_pablo",
#     password="Hiiro9206.23",
#     host="localhost"
# )

conn = psycopg2.connect(dbURI)

def main():
    parser = argparse.ArgumentParser('Examples of communication with the database')
    parser.add_argument('action', type=str, help='show, filter, insert, update, delete')
    parser.add_argument('--name', type=str, help='User Name. Default Pablo', default='Rojas')
    parser.add_argument('--lastName', type=str, help='User last name, default Rojas', default='Pablo')
    parser.add_argument('--password', type=str, help='User Password, default 000', default='000')
    parser.add_argument('--avatar', type=str, help='Avatar name', default='None')
    args = parser.parse_args()

    with conn.cursor() as cursor:
        if args.action == 'show':
            query = "SELECT * FROM users;"
        elif args.action == 'filter':
            query = f"SELECT * FROM users WHERE firstname = '{args.name}' AND lastname = '{args.lastName}'"
        elif args.action == 'insert':
            query = f"INSERT INTO users(LastName, FirstName, pass, avatarName)\
                      VALUES ('{args.name}', '{args.lastName}', '{args.password}', '{args.avatar}')"
        elif args.action == 'delete':
            query = f"DELETE FROM users WHERE LastName = '{args.lastName}'"
        elif args.action == 'update':
            query = f"UPDATE users SET LastName = '{args.lastName}' WHERE FirstName = '{args.name}'"

        cursor.execute(query)
        # Get the values from the table 
        if args.action == 'show' or args.action == 'filter':
            answer = cursor.fetchall()
            if isinstance(answer, type(None)):
                print('The exectued query did not return a value')
            else:
                print(answer)
    if args.action != 'show' and args.action != 'filter':
        conn.commit()
        print('Action has been applied on the database')
    conn.close()

if __name__ == '__main__':
    sys.exit(main())