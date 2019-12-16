import sqlite3
def main():
    conn = sqlite3.connect('alphanum.db')
    print("Opened database successfully");

    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS WRITING');

    cur.execute('CREATE TABLE WRITING (charCode INT, lowerCase CHAR, upperCase CHAR, numbers CHAR)')
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(1, 'a', 'A')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(2, 'b', 'B')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(3, 'c', 'C')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(4, 'd', 'D')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(5, 'e', 'E')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(6, 'f', 'F')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(7, 'g', 'G')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(8, 'h', 'H')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(9, 'i', 'I')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(10, 'j', 'J')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(11, 'k', 'K')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(12, 'l', 'L')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(13, 'm', 'M')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(14, 'n', 'N')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(15, 'o', 'O')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(16, 'p', 'P')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(17, 'q', 'Q')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(18, 'r', 'R')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(19, 's', 'S')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(20, 't', 'T')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(21, 'u', 'U')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(22, 'v', 'V')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(23, 'w', 'W')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(24, 'x', 'X')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(25, 'y', 'Y')");
    cur.execute("INSERT INTO WRITING(charCode, lowerCase, upperCase) \ VALUES(26, 'z', 'Z')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(27, '0')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(28, '1')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(29, '2')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(30, '3')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(31, '4')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(32, '5')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(33, '6')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(34, '7')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(35, '8')");
    cur.execute("INSERT INTO WRITING(charCode, numbers) \ VALUES(36, '9')");

    conn.close()
if __name__ == '__main__': main()
