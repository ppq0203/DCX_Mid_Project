package jsp.util;

//DB를 연결하기위한 클래스
import java.sql.Connection;
import java.sql.DriverManager;
		//DB는 여러 개 연결 가능함.




// 커넥션을 얻어오는 클래스 - JNDI
public class DBConnection 
{
			public static Connection dbConn;					
			//메서드
			public static Connection getConnection(){ 
				
		         //연결할때 try-catch는 반드시 써야함. / NULL일 경우 연결되지않은 상태
				if(dbConn == null) {
					
					try {	
						//type4를 thin으로 표시함 / @뒤에는 자신의ip주소 /오라클 기본포트:1521/내가쓰는오라클버전은 xe
						String url = "jdbc:oracle:thin:@localhost:1521:xe";
						//JDBC방식으로 TYPE4형식, 해당 주소를 가진 1521포트의 TestDB로 연결
						//노트북으로 진행할 때는 서버가 아니므로 IP주소가 아닌 LOCALHOST를 쓴다.
						//동적으로 클래스를 로딩한다. 좀 더 빠른 접근 가능
						String user = "c##scott";
						String pwd = "tiger"; // 여기까지가 접속 정보 
						
						//다른 클래스의 정보를 읽어올 때 사용
		                // oracle.jdbc.driver위치의 OracleDriver클래스를 읽어옴
						Class.forName("oracle.jdbc.driver.OracleDriver"); 
						
						//DriverManager를 통해 내가 지정한 url,user,password로
		                //스트림을 생성해서 dbConn에 담는 것
						dbConn = DriverManager.getConnection(url, user, pwd); //읽어와서 dbConn에 넣는다.
						
						
					} catch (Exception e) {
						System.out.println(e.toString());
					}
				}
				
				return dbConn; //처음부터 여기까지가 DB연결자
			}
			
			
			//DB를 사용하면 끝내는 애가 있어야한다.
			public static void close() {
				
				if(dbConn != null) {
				    try {
				        if(!dbConn.isClosed()) {
				            dbConn.close();
				        }
				    } catch (Exception e) {
				        System.out.println(e.toString());
				    } finally {
				        dbConn = null;
				    }
				}
			}}
			