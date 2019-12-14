import sqlite3
def main():
    conn = sqlite3.connect('alphanum.sqlite')
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS writing')
    cur.execute('CREATE TABLE writing (letcode INT, lowerCase TEXT, upperCase TEXT, numbers TEXT)')
    conn.close()
if __name__ == '__main__': main()
