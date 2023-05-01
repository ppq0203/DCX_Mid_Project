package jsp.Recipe;

import java.sql.*;
import java.util.ArrayList;
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

    public void insertIngredient(String id, String i_name, int i_quantity) {
        String sql = "insert into Ingredients(id, i_name, i_quantity)values(?,?,?)";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, id);
            pstmt.setString(2, i_name);
            pstmt.setInt(3, i_quantity);
            

            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }
    
    public void insertImg(String i_name, String color, Float length, Float weight, String image_name, String image_url) {
    
    String sql = "insert into Ingredients_img(i_name, color, length, weight, image_name, image_url)values(?,?,?,?,?,?)";
    try {
    	pstmt = conn.prepareStatement(sql);
    	pstmt.setString(1, i_name);
		pstmt.setString(2, color );
		pstmt.setFloat(3, length);
		pstmt.setFloat(4, weight);
		pstmt.setString(5, image_name);
        pstmt.setString(6, image_url);
        

        pstmt.executeUpdate();
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }
}
    
    public void deleteIngredient(String id, String i_name) {
        String sql = "DELETE FROM ingredients WHERE id=? and i_name=?";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, id);
            pstmt.setString(2, i_name);

            pstmt.executeUpdate();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            close();
        }
    }

    public void updateIngredient(String id, String i_name) {
        String sql = "UPDATE Ingredients SET i_name = ? WHERE id = ?";
        try {
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, i_name);
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

public List<Ingredient> selectAllIngredients() {
    String sql = "SELECT * FROM Ingredients";
    List<Ingredient> ingredients = new ArrayList<>();
    try {
        pstmt = conn.prepareStatement(sql);
        rs = pstmt.executeQuery();

        while (rs.next()) {
            Ingredient ingredient = new Ingredient();
            ingredient.setId(rs.getString("id"));
            ingredient.setI_name(rs.getString("i_name"));
            ingredient.setI_quantity(rs.getInt("i_quantity"));

            ingredients.add(ingredient);
        }
    } catch (SQLException e) {
        e.printStackTrace();
    } finally {
        close();
    }

    return ingredients;
}

public Ingredient selectIngredient(String id) {
    String sql = "SELECT * FROM Ingredients WHERE id=?";
    Ingredient ingredient = null;
    try {
        pstmt = conn.prepareStatement(sql);
        pstmt.setString(1, id);
        rs = pstmt.executeQuery();

        if (rs.next()) {
            ingredient = new Ingredient();
            ingredient.setId(rs.getString("id"));
            ingredient.setI_name(rs.getString("i_name"));
            ingredient.setI_quantity(rs.getInt("i_quantity"));
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





	