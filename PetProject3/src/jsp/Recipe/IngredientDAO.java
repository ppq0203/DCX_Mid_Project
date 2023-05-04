package jsp.Recipe;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.sql.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class IngredientDAO {
    private Connection conn = null;
    private PreparedStatement pstmt = null;
    private ResultSet rs = null;

    private final String JDBC_DRIVER = "oracle.jdbc.driver.OracleDriver";
    private final String DB_URL = "jdbc:oracle:thin:@localhost:1521:xe";
    private final String USER_NAME = "c##scott";
    private final String PASSWORD = "tiger";

    public IngredientDAO() {
        try {
            Class.forName(JDBC_DRIVER);
            conn = DriverManager.getConnection(DB_URL, USER_NAME, PASSWORD);
        } catch (ClassNotFoundException | SQLException e) {
            e.printStackTrace();
        }
    }

    public void insertIngredient(String id, String ING_NAME, Float ING_AMOUNT,String ING_UNIT ) {
        String sql = "insert into Ingredients(id, ING_NAME, ING_AMOUNT,ING_UNIT)values(?,?,?,?)";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, id);
            pstmt.setString(2, ING_NAME);
            pstmt.setFloat(3, ING_AMOUNT);
            pstmt.setString(4, ING_UNIT);
            
            
            pstmt.executeUpdate();
            System.out.println("1행이 입력되었습니다.");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }
    
    public void insertImg(String ING_NAME , String color, Float length, Float weight, String image_name, String image_url) {
    
    String sql = "insert into Ingredients_img(ING_NAME , color, length, weight, image_name, image_url)values(?,?,?,?,?,?)";
    try {
    	pstmt = conn.prepareStatement(sql);
    	pstmt.setString(1, ING_NAME );
		pstmt.setString(2, color );
		pstmt.setFloat(3, length);
		pstmt.setFloat(4, weight);
		pstmt.setString(5, image_name);
        pstmt.setString(6, image_url);
        

        pstmt.executeUpdate();
        System.out.println("1행이 입력되었습니다.");
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }
}
    public void insertRecipe(String RCP_SNO, String CKG_NM, String CKG_KND_ACTO_NM, String CKG_INBUN_NM, String CKG_DODF_NM, String CKG_TIME_NM, int RCMM_CNT) {
        
        String sql = "insert into Recipe(RCP_SNO, CKG_NM, CKG_KND_ACTO_NM, CKG_INBUN_NM, CKG_DODF_NM,CKG_TIME_NM, RCMM_CNT)values(?,?,?,?,?,?,?)";
        try {
        	pstmt = conn.prepareStatement(sql);
        	pstmt.setString(1, RCP_SNO);
    		pstmt.setString(2, CKG_NM );
    		pstmt.setString(3, CKG_KND_ACTO_NM);
    		pstmt.setString(4, CKG_INBUN_NM);
    		pstmt.setString(5, CKG_DODF_NM);
            pstmt.setString(6, CKG_TIME_NM);
            pstmt.setInt(7, RCMM_CNT);
            pstmt.executeUpdate();
            System.out.println("1행이 입력되었습니다.");
        }	 
        catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }
public void insertContent(String RCP_SNO, String SRAP_CNT , String ING_INFO) {
        
        String sql = "insert into Recipe_content(RCP_SNO, SRAP_CNT, ING_INFO)values(?,?,?)";
        try {
        	pstmt = conn.prepareStatement(sql);
        	pstmt.setString(1, RCP_SNO);
    		pstmt.setString(2, SRAP_CNT );
    		pstmt.setString(3, ING_INFO);

            pstmt.executeUpdate();
            System.out.println("1행이 입력되었습니다.");
        }	 
        catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }
public void insertRIngredient(String RCP_SNO, String ING_NAME, Float ING_AMOUNT,String ING_UNIT) {
    
    String sql = "insert into Recipe_Ingredients(RCP_SNO, ING_NAME, ING_AMOUNT)values(?,?,?,?)";
    try {
    	pstmt = conn.prepareStatement(sql);
    	pstmt.setString(1, RCP_SNO);
		pstmt.setString(2, ING_NAME);
		pstmt.setFloat(3, ING_AMOUNT);
		pstmt.setString(4, ING_UNIT);

        pstmt.executeUpdate();
        System.out.println("1행이 입력되었습니다.");
    }	 
    catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }
}
public void insertPrice(String ING_NAME, int i_price) {
    
    String sql = "insert into Ingredients_Price(ING_NAME, i_price)values(?,?)";
    try {
    	pstmt = conn.prepareStatement(sql);
    	pstmt.setString(1, ING_NAME);
		pstmt.setInt(2, i_price);

        pstmt.executeUpdate();
        System.out.println("1행이 입력되었습니다.");
    }	 
    catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }
}
    public void deleteIngredient(String id, String ING_NAME) {
        String sql = "DELETE FROM ingredients WHERE id=? and ING_NAME=?";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, id);
            pstmt.setString(2, ING_NAME);

            pstmt.executeUpdate();
            System.out.println("1행이 삭제되었습니다.");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }

    public void updateIngredient(String ING_NAME, String id) {
    	String sql = "";
        sql = "UPDATE Ingredients SET ING_NAME = ? WHERE id = ?";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, ING_NAME);
            pstmt.setString(2, id);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected == 0) {
                System.out.println("해당하는 식재료가 없습니다.");
            } else {
                System.out.println(rowsAffected + "개의 행이 수정되었습니다.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
        	
            close();
        }
    }
    
    public void updatePrice(String ING_NAME, int i_price) {
    	String sql = "";
        sql = "UPDATE Ingredients SET i_price = ? WHERE ING_NAME = ?";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, i_price);
            pstmt.setString(2, ING_NAME);
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected == 0) {
                System.out.println("해당하는 식재료가 없습니다.");
            } else {
                System.out.println(rowsAffected + "개의 행이 수정되었습니다.");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
        	
            close();
        }
    }
public RecipeDTO selectIngredient(String id) {
    String sql = "SELECT * FROM Ingredients WHERE id=?";
    RecipeDTO ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, id);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new RecipeDTO();
            ingredient.setId(rs.getString("id"));
            ingredient.setING_NAME(rs.getString("ING_NAME"));
            ingredient.setING_AMOUNT(rs.getFloat("ING_AMOUNT"));
            ingredient.setING_UNIT(rs.getString("ING_UNIT"));
        } else {
            System.out.println("해당하는 식재료가 없습니다.");
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredient;
    
}
public RecipeDTO selectRecipe(String RCP_SNO) {
    String sql = "SELECT * FROM Recipe WHERE RCP_SNO=?";
    RecipeDTO ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, RCP_SNO);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new RecipeDTO();
            ingredient.setRCP_SNO(rs.getString("RCP_SNO"));
            ingredient.setCKG_NM(rs.getString("CKG_NM"));
            ingredient.setCKG_KND_ACTO_NM(rs.getString("CKG_KND_ACTO_NM"));
            ingredient.setCKG_INBUN_NM(rs.getString("CKG_INBUN_NM"));
            ingredient.setCKG_DODF_NM(rs.getString("CKG_DODF_NM"));
            ingredient.setCKG_TIME_NM(rs.getString("CKG_TIME_NM"));
            ingredient.setRCMM_CNT(rs.getInt("RCMM_CNT"));
        } else {
            System.out.println("해당하는 레시피정보가 없습니다.");
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredient;
    
}	
public RecipeDTO selectRecipe_Ingredient(String RCP_SNO) {
    String sql = "SELECT * FROM Recipe_Ingredients WHERE RCP_SNO=?";
    RecipeDTO ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, RCP_SNO);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new RecipeDTO();
            ingredient.setRCP_SNO(rs.getString("RCP_SNO"));
            ingredient.setING_NAME(rs.getString("ING_NAME"));
            ingredient.setING_AMOUNT(rs.getFloat("ING_AMOUNT"));
            ingredient.setING_UNIT(rs.getString("ING_UNIT"));
        } else {
            System.out.println("해당하는 레코드가 없습니다.");
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredient;
    
}
public RecipeDTO select_Content(String RCP_SNO) {
    String sql = "SELECT * FROM Recipe_Content WHERE RCP_SNO=?";
    RecipeDTO ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, RCP_SNO);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new RecipeDTO();
            ingredient.setRCP_SNO(rs.getString("RCP_SNO"));
            ingredient.setSRAP_CNT(rs.getString("SRAP_CNT"));
            ingredient.setING_INFO(rs.getString("ING_INFO"));
        } else {
            System.out.println("해당하는 레코드가 없습니다.");
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredient;
    
}
public RecipeDTO select_Price(String ING_NAME) {
    String sql = "SELECT * FROM Ingredients_Price WHERE ING_NAME=?";
    RecipeDTO ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, ING_NAME);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new RecipeDTO();
            ingredient.setING_NAME(rs.getString("ING_NAME"));
            ingredient.setI_price(rs.getInt("i_price"));
        } else {
            System.out.println("해당하는 레코드가 없습니다.");
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredient;
    
}
public void CSV_Recipe(String csvFilePath) throws SQLException, NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(csvFilePath), "EUC-KR")); 
    
    String line;
    String tableName = "Recipe";
    String insertSql = "INSERT INTO " + tableName + " (RCP_SNO, CKG_NM, CKG_KND_ACTO_NM, CKG_INBUN_NM, CKG_DODF_NM,CKG_TIME_NM, RCMM_CNT) VALUES (?, ?, ?, ?, ?, ?, ?)";
    PreparedStatement pstmt = conn.prepareStatement(insertSql);
    
    // CSV 파일의 첫 번째 줄은 열 이름으로 제외시킴
    br.readLine();
    
    
    while ((line = br.readLine()) != null) {
        String[] values = line.split(",");
        pstmt.setString(1, values[0]);
        pstmt.setString(2, values[1]);
        pstmt.setString(3, values[2]);
        pstmt.setString(4, values[3]);
        pstmt.setString(5, values[4]);
        pstmt.setString(6, values[5]);
        pstmt.setInt(7, Integer.parseInt(values[6]));
        
        pstmt.executeUpdate();
    }
    
    System.out.println("CSV file has been imported into the database.");
    

}
public void CSV_Recipe_Ingredients(String csvFilePath) throws SQLException, NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(csvFilePath), "EUC-KR")); 
    
    String line;
    String tableName = "Recipe_Ingredients";
    String insertSql = "INSERT INTO " + tableName + " (RCP_SNO, ING_NAME, ING_AMOUNT, ING_UNIT) values (?,?,?,?)";
    PreparedStatement pstmt = conn.prepareStatement(insertSql);
    
    // CSV 파일의 첫 번째 줄은 열 이름으로 제외시킴
    br.readLine();
    
    
    while ((line = br.readLine()) != null) {
        String[] values = line.split(",");
        pstmt.setString(1, values[0]);
        pstmt.setString(2, values[1]);
        pstmt.setFloat(3, Float.parseFloat(values[2]));
        pstmt.setString(4, values[3]);
        
        pstmt.executeUpdate();
    }
    
    System.out.println("CSV file has been imported into the database.");
    

}
public void CSV_Recipe_Content(String csvFilePath) throws SQLException, NumberFormatException, IOException {
	BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(csvFilePath), "EUC-KR"));  
    
    String line;
    String tableName = "Recipe_Content";
    String insertSql = "INSERT INTO " + tableName + " (RCP_SNO, SRAP_CNT, ING_INFO) values (?,?,?)";
    PreparedStatement pstmt = conn.prepareStatement(insertSql);
    
    // CSV 파일의 첫 번째 줄은 열 이름으로 제외시킴
    br.readLine();
    
    
    while ((line = br.readLine()) != null) {
    	
        String[] values = line.split(",");
        if(values.length>=3) {
        pstmt.setString(1, values[0]);
        pstmt.setString(2, values[1]);
        pstmt.setString(3, values[2]);
        }else {
        pstmt.setString(3, "");	
        }
        pstmt.executeUpdate();  
    }System.out.println("CSV file has been imported into the database.");
}

public void saveToCsv(String filePath) throws SQLException, IOException {
//    String tableName = "Recipe_Content";
    String sql = "SELECT r.CKG_NM, r.CKG_KND_ACTO_NM, r.CKG_TIME_NM " + 
    		"FROM Recipe r " + 
    		"INNER JOIN Recipe_Ingredients ri ON r.RCP_SNO = ri.RCP_SNO " + 
    		"INNER JOIN Ingredients i ON ri.ING_NAME = i.ING_NAME " + 
    		"WHERE i.ING_NAME IN ('돼지고기', '양파', '대파') " + 
    		"GROUP BY r.CKG_NM, r.CKG_KND_ACTO_NM, r.CKG_TIME_NM " + 
    		"HAVING COUNT(*) >= 3" + 
    		"ORDER BY r.CKG_TIME_NM ASC";
    PreparedStatement pstmt = conn.prepareStatement(sql);
//    pstmt.setString(1, "221094");
    ResultSet rs = pstmt.executeQuery();

    BufferedWriter fw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath), "EUC-KR"));
    fw.append("CKG_NM,CKG_KND_ACTO_NM,CKG_TIME_NM\n");

    while (rs.next()) {
        String CKG_NM = rs.getString("CKG_NM");
        String CKG_KND_ACTO_NM = rs.getString("CKG_KND_ACTO_NM");
        String CKG_TIME_NM = rs.getString("CKG_TIME_NM");

        fw.append(CKG_NM).append(",").append(CKG_KND_ACTO_NM).append(",").append(CKG_TIME_NM).append(",").append("\n");
    }
    
    fw.flush();
    fw.close();

    System.out.println("Data has been saved to CSV file successfully.");
    
}
public void saveToCsv1(String filePath) throws SQLException, IOException {
    String tableName = "Recipe_Content";
    String sql = "SELECT * FROM " + tableName + " where ING_INFO = '마늘' ";
    PreparedStatement pstmt = conn.prepareStatement(sql);

    ResultSet rs = pstmt.executeQuery();

    List<String[]> dataList = new ArrayList<>(); // ArrayList 생성
    
    while (rs.next()) {
        String RCP_SNO = rs.getString("RCP_SNO");
        String SRAP_CNT = rs.getString("SRAP_CNT");
        String ING_INFO = rs.getString("ING_INFO");
        
        String[] rowData = {RCP_SNO, SRAP_CNT, ING_INFO};
        dataList.add(rowData);
        // ArrayList에 데이터 추가
        
    }    
       Arrays.deepToString(dataList.toArray(new String[0][0]));
   
    BufferedWriter fw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath), "EUC-KR"));
    fw.append("RCP_SNO,SRAP_CNT,ING_INFO\n");
    
    for (String[] rowData : dataList) {    	
        fw.append(rowData[0]).append(",").append(rowData[1]).append(",").append(rowData[2]).append(",").append("\n");
        }
    
    fw.flush();
    fw.close();

    System.out.println("Data has been saved to CSV file successfully.");
    
    // ArrayList를 이용하여 데이터 콘솔 출력
//    for (String[] rowData : dataList){
//		for (int i = 0; i < rowData.length; i++){
//			if (rowData[i] == null){
//                rowData[i] = "";
//            } 
//		}System.out.println();
//    }
}
    private void close() {
        try {
            if (rs != null) {
                rs.close();
            }
            if (pstmt != null) {
                pstmt.close();
            }
            if (conn != null) {
                conn.close();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }}





	