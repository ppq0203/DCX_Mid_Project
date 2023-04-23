package jsp.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.sql.DataSource;

// 커넥션을 얻어오는 클래스 - JNDI
public class DBConnection 
{
	public static Connection getConnection() throws ClassNotFoundException, SQLException { 
		Class.forName("oracle.jdbc.driver.OracleDriver");
//		Class.forName("com.mysql.jdbc.Driver");
//		  2. 드라이버 관리자 등록
//		  1번을 할 경우 자동 등록
//		  3. 2번을 통해서 접속
		  String url = "";
		  url = "jdbc:oracle:thin:@localhost:1521:XE";
		  
//		  url = "jdbc:mysql://localhost:3306/DBNAME?characterEncoding=utf8&autoReconnect=true";
		String user = "c##scott";
		String password = "tiger";
		Connection conn = DriverManager.getConnection(url, user, password);
//		  4. 명령문을 생성
		Statement Stmt = conn.createStatement(); //web의 session같은 존재
		return conn;
	}
}	